"""Local Governance & Quality Gate CLI for the CAPE RPA Development Skill.

Library Selection Justification:
    Uses exclusively the Python standard library (``argparse``, ``csv``,
    ``dataclasses``, ``hashlib``, ``json``, ``logging``, ``pathlib``, ``re``,
    ``statistics``, ``sys``, ``urllib.parse``) to maintain zero external
    dependencies, guarantee deterministic execution in air-gapped or corporate
    proxy environments, and comply with the pilot governance constraint against
    installing unnecessary runtime packages.

Capabilities:
    1. ``check-skill``: Measures LF/CRLF character counts, UTF-8 byte lengths,
       headroom against CAPE's 24,000-character limit, and SHA-256 digests.
    2. ``check-docs``: Audits Markdown governance artifacts for balanced code
       fences, heading hierarchy, duplicate headings, GFM table alignment,
       broken or space-unencoded relative links, and trailing whitespace.
    3. ``score-c07``: Validates Change 07 matched-pair execution logs against
       Protocol v0.1-r2 §7.1, enforces the 600-second active-time cap, zero-
       denominator guard, and quality-acceptance gate, and computes both total
       and median active-time reductions alongside separated quality metrics.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import re
import statistics
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence
from urllib.parse import unquote

SKILL_CHAR_LIMIT: int = 24_000
SKILL_SAFETY_BUFFER: int = 500
CHANGE_07_MAX_ACTIVE_SECONDS: int = 600
CHANGE_07_TARGET_REDUCTION_PCT: float = 30.0
CHANGE_07_MIN_QUALITY_SCORE: int = 6

REQUIRED_C07_COLUMNS: frozenset[str] = frozenset(
    {
        "protocol_version",
        "execution_id",
        "pair_id",
        "task_id",
        "task_domain",
        "task_intent",
        "task_difficulty",
        "task_matching_rationale",
        "expected_outcome",
        "condition",
        "condition_order",
        "participant_id",
        "execution_date_time",
        "cape_available",
        "skill_loaded",
        "activation_mode",
        "activation_status",
        "skill_version",
        "start_time",
        "end_time",
        "active_time_seconds",
        "interruption_seconds",
        "interruption_log",
        "termination_reason",
        "outcome",
        "sources_consulted",
        "sources_cited",
        "quality_dim_1",
        "quality_dim_2",
        "quality_dim_3",
        "quality_dim_4",
        "quality_dim_5",
        "quality_dim_6",
        "quality_dim_7",
        "quality_dim_8",
        "quality_total",
        "accepted",
        "critical_failure",
        "critical_failure_reason",
        "rework_indicator",
        "rework_description",
        "reviewer_notes",
        "deviation",
        "evidence_location",
    }
)

VALID_CONDITIONS: frozenset[str] = frozenset({"NO_CAPE", "CAPE"})
COMPARABLE_OUTCOMES: frozenset[str] = frozenset({"RESOLVED", "UNRESOLVED"})
VALID_OUTCOMES: frozenset[str] = frozenset(
    {"RESOLVED", "UNRESOLVED", "INTERRUPTED", "INVALID"}
)
VALID_ACTIVATION_STATUSES: frozenset[str] = frozenset(
    {"ACTIVATED", "ACTIVATION_FAILED", "NOT_APPLICABLE"}
)

_LINK_PATTERN: re.Pattern[str] = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_HEADING_PATTERN: re.Pattern[str] = re.compile(r"^(#{1,6})\s+(.+)$")
_EXTERNAL_URL_PATTERN: re.Pattern[str] = re.compile(r"^(https?://|mailto:|#)")


class QualityGateError(Exception):
    """Base exception for CAPE quality-gate validation failures."""


class SkillValidationError(QualityGateError):
    """Raised when a Skill file cannot be read or validated."""


class Change07LogError(QualityGateError):
    """Raised when a Change 07 execution log violates Protocol v0.1-r2 schema."""


class _JsonLogFormatter(logging.Formatter):
    """Formats log records as single-line structured JSON objects."""

    def format(self, record: logging.LogRecord) -> str:
        """Serialize a log record into JSON with timestamp and metadata.

        Args:
            record: Standard Python logging record.

        Returns:
            JSON-encoded log string.
        """
        payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        context = getattr(record, "context", None)
        if isinstance(context, dict):
            payload["context"] = context
        return json.dumps(payload, ensure_ascii=False)


def configure_logger(name: str = "cape_quality_gate") -> logging.Logger:
    """Create a structured JSON logger writing to stderr.

    Args:
        name: Logger identifier.

    Returns:
        Configured ``logging.Logger`` instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(_JsonLogFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger


@dataclass(frozen=True)
class SkillAuditResult:
    """Audit metrics for a single CAPE Skill Markdown file."""

    path: str
    lf_characters: int
    raw_characters: int
    lf_utf8_bytes: int
    raw_utf8_bytes: int
    lines: int
    sha256: str
    limit: int
    lf_headroom: int
    raw_headroom: int
    within_limit_lf: bool
    within_limit_raw: bool
    low_margin_warning: bool


@dataclass(frozen=True)
class MarkdownAuditResult:
    """Structural quality audit result for a Markdown document."""

    path: str
    lines: int
    code_fences_balanced: bool
    eof_newline: bool
    trailing_whitespace_lines: tuple[int, ...]
    heading_issues: tuple[str, ...]
    table_issues: tuple[str, ...]
    unencoded_space_links: tuple[str, ...]
    broken_relative_links: tuple[str, ...]

    @property
    def passed(self) -> bool:
        """Return True when zero structural, link, or formatting defects exist."""
        return (
            self.code_fences_balanced
            and self.eof_newline
            and not self.trailing_whitespace_lines
            and not self.heading_issues
            and not self.table_issues
            and not self.unencoded_space_links
            and not self.broken_relative_links
        )


@dataclass(frozen=True)
class Change07Summary:
    """Aggregated Change 07 efficiency and separated quality evaluation summary."""

    status: str
    total_rows: int
    valid_comparable_pairs: int
    excluded_rows: int
    baseline_total_active_seconds: int
    cape_total_active_seconds: int
    baseline_median_active_seconds: float | None
    cape_median_active_seconds: float | None
    total_active_time_reduction_pct: float | None
    median_active_time_reduction_pct: float | None
    baseline_quality_acceptance_rate: float | None
    cape_quality_acceptance_rate: float | None
    baseline_critical_failures: int
    cape_critical_failures: int
    cape_activation_failures: int
    baseline_rework_count: int
    cape_rework_count: int
    target_30pct_achieved: bool
    notes: tuple[str, ...]


def audit_skill_file(
    file_path: Path,
    limit: int = SKILL_CHAR_LIMIT,
    safety_buffer: int = SKILL_SAFETY_BUFFER,
) -> SkillAuditResult:
    """Measure character counts, byte lengths, headroom, and SHA-256 of a Skill file.

    Args:
        file_path: Path to the Skill Markdown artifact.
        limit: Maximum permitted character count (must be > 0).
        safety_buffer: Warning threshold below ``limit`` (must be >= 0).

    Returns:
        ``SkillAuditResult`` containing local count and hash measurements.

    Raises:
        SkillValidationError: If ``file_path`` is missing, unreadable, or bounds
            are invalid.
    """
    if limit <= 0:
        raise SkillValidationError(f"Character limit must be positive, got {limit}.")
    if safety_buffer < 0:
        raise SkillValidationError(
            f"Safety buffer must be non-negative, got {safety_buffer}."
        )
    if not file_path.is_file():
        raise SkillValidationError(f"Skill file does not exist: {file_path}")

    raw_bytes = file_path.read_bytes()
    try:
        raw_text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SkillValidationError(
            f"Skill file is not valid UTF-8: {file_path}"
        ) from exc

    lf_text = raw_text.replace("\r\n", "\n")
    lf_bytes = lf_text.encode("utf-8")
    sha256_hex = hashlib.sha256(raw_bytes).hexdigest().upper()
    lf_chars = len(lf_text)
    raw_chars = len(raw_text)

    return SkillAuditResult(
        path=str(file_path),
        lf_characters=lf_chars,
        raw_characters=raw_chars,
        lf_utf8_bytes=len(lf_bytes),
        raw_utf8_bytes=len(raw_bytes),
        lines=len(lf_text.splitlines()),
        sha256=sha256_hex,
        limit=limit,
        lf_headroom=limit - lf_chars,
        raw_headroom=limit - raw_chars,
        within_limit_lf=lf_chars <= limit,
        within_limit_raw=raw_chars <= limit,
        low_margin_warning=(limit - lf_chars) < safety_buffer,
    )


def audit_markdown_file(file_path: Path) -> MarkdownAuditResult:
    """Perform deterministic structural and relative-link validation on a Markdown file.

    Args:
        file_path: Path to the Markdown file to validate.

    Returns:
        ``MarkdownAuditResult`` capturing all detected issues.

    Raises:
        QualityGateError: If ``file_path`` does not exist or cannot be decoded as UTF-8.
    """
    if not file_path.is_file():
        raise QualityGateError(f"Markdown file does not exist: {file_path}")

    try:
        raw_text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise QualityGateError(f"File is not valid UTF-8: {file_path}") from exc

    lines = raw_text.splitlines()
    fence_count = 0
    in_code_block = False
    prev_heading_level = 0
    seen_headings: dict[str, int] = {}
    in_table = False
    expected_cols = 0

    trailing_ws: list[int] = []
    heading_issues: list[str] = []
    table_issues: list[str] = []
    unencoded_links: list[str] = []
    broken_links: list[str] = []

    parent_dir = file_path.resolve().parent

    for idx, line in enumerate(lines, start=1):
        if line.endswith((" ", "\t")):
            trailing_ws.append(idx)

        if line.lstrip().startswith("```"):
            fence_count += 1
            in_code_block = not in_code_block
            in_table = False
            continue

        if in_code_block:
            continue

        heading_match = _HEADING_PATTERN.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            if prev_heading_level > 0 and level > prev_heading_level + 1:
                heading_issues.append(
                    f"L{idx}: skipped heading level {prev_heading_level}->{level} ({title})"
                )
            prev_heading_level = level
            if title in seen_headings:
                heading_issues.append(
                    f"L{idx}: duplicate heading '{title}' (first seen L{seen_headings[title]})"
                )
            else:
                seen_headings[title] = idx

        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            inner = stripped[1:-1]
            col_count = len(re.split(r"(?<!\\)\|", inner))
            if not in_table:
                in_table = True
                expected_cols = col_count
            elif col_count != expected_cols:
                table_issues.append(
                    f"L{idx}: table has {col_count} columns, expected {expected_cols}"
                )
        else:
            in_table = False
            expected_cols = 0

        for match in _LINK_PATTERN.finditer(line):
            target = match.group(2).strip()
            if _EXTERNAL_URL_PATTERN.match(target):
                continue
            if " " in target:
                unencoded_links.append(f"L{idx}: {target}")
            clean_target = unquote(target.split("#", 1)[0])
            if clean_target:
                resolved = (parent_dir / clean_target).resolve()
                if not resolved.exists():
                    broken_links.append(f"L{idx}: {target}")

    return MarkdownAuditResult(
        path=str(file_path),
        lines=len(lines),
        code_fences_balanced=(fence_count % 2 == 0),
        eof_newline=raw_text.endswith("\n"),
        trailing_whitespace_lines=tuple(trailing_ws),
        heading_issues=tuple(heading_issues),
        table_issues=tuple(table_issues),
        unencoded_space_links=tuple(unencoded_links),
        broken_relative_links=tuple(broken_links),
    )


def _parse_int_field(row: dict[str, str], field: str, row_num: int) -> int:
    """Parse a mandatory integer field from a CSV row.

    Args:
        row: CSV row dictionary.
        field: Column name.
        row_num: 1-based data row index for diagnostics.

    Returns:
        Parsed integer value.

    Raises:
        Change07LogError: If the field is missing or not a valid integer.
    """
    raw = (row.get(field) or "").strip()
    try:
        return int(raw)
    except ValueError as exc:
        raise Change07LogError(
            f"Row {row_num}: field '{field}' must be an integer, got '{raw}'."
        ) from exc


def _is_quality_accepted(row: dict[str, str], row_num: int) -> tuple[bool, bool]:
    """Evaluate Change 07 §6 quality-gate acceptance for a single scored row.

    Enforces Protocol v0.1-r2 §6: total score >= 6/8, mandatory Correctness
    (``quality_dim_1 == 1``), mandatory Boundary Compliance
    (``quality_dim_2 == 1``), and ``critical_failure == NO``.

    Args:
        row: CSV row dictionary.
        row_num: 1-based data row index.

    Returns:
        Tuple of ``(is_accepted, is_critical_failure)``.

    Raises:
        Change07LogError: If quality dimension fields contain invalid values.
    """
    crit_raw = (row.get("critical_failure") or "").strip().upper()
    if crit_raw not in {"YES", "NO"}:
        raise Change07LogError(
            f"Row {row_num}: 'critical_failure' must be YES or NO, got '{crit_raw}'."
        )
    is_critical = crit_raw == "YES"

    dims: list[int] = []
    for dim_idx in range(1, 9):
        val = _parse_int_field(row, f"quality_dim_{dim_idx}", row_num)
        if val not in {0, 1}:
            raise Change07LogError(
                f"Row {row_num}: 'quality_dim_{dim_idx}' must be 0 or 1, got {val}."
            )
        dims.append(val)

    total = sum(dims)
    recorded_total = _parse_int_field(row, "quality_total", row_num)
    if recorded_total != total:
        raise Change07LogError(
            f"Row {row_num}: quality_total ({recorded_total}) != sum(quality_dim_1..8) ({total})."
        )

    accepted = (
        not is_critical
        and total >= CHANGE_07_MIN_QUALITY_SCORE
        and dims[0] == 1
        and dims[1] == 1
    )
    return accepted, is_critical


def score_change_07_log(csv_path: Path) -> Change07Summary:
    """Validate and score a Change 07 execution log CSV against Protocol v0.1-r2.

    Args:
        csv_path: Path to the execution log CSV file.

    Returns:
        ``Change07Summary`` separating efficiency metrics, quality acceptance,
        and operational failure counts.

    Raises:
        Change07LogError: If the CSV file is missing, lacks required §7.1
            columns, or contains invalid timing/outcome/quality values.
    """
    if not csv_path.is_file():
        raise Change07LogError(f"Change 07 log file does not exist: {csv_path}")

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise Change07LogError("Change 07 log CSV is empty or missing header row.")
        missing_cols = sorted(REQUIRED_C07_COLUMNS - set(reader.fieldnames))
        if missing_cols:
            raise Change07LogError(
                f"Change 07 log missing required §7.1 columns: {', '.join(missing_cols)}"
            )
        rows = list(reader)

    if not rows:
        return Change07Summary(
            status="NO_DATA",
            total_rows=0,
            valid_comparable_pairs=0,
            excluded_rows=0,
            baseline_total_active_seconds=0,
            cape_total_active_seconds=0,
            baseline_median_active_seconds=None,
            cape_median_active_seconds=None,
            total_active_time_reduction_pct=None,
            median_active_time_reduction_pct=None,
            baseline_quality_acceptance_rate=None,
            cape_quality_acceptance_rate=None,
            baseline_critical_failures=0,
            cape_critical_failures=0,
            cape_activation_failures=0,
            baseline_rework_count=0,
            cape_rework_count=0,
            target_30pct_achieved=False,
            notes=(
                "Zero executions logged. No baseline or CAPE comparison exists; "
                "30% reduction remains an unmeasured target.",
            ),
        )

    pairs: dict[str, dict[str, dict[str, Any]]] = {}
    excluded_rows = 0
    cape_activation_failures = 0
    baseline_rework = 0
    cape_rework = 0
    baseline_crit = 0
    cape_crit = 0
    baseline_scored_total = 0
    baseline_scored_accepted = 0
    cape_scored_total = 0
    cape_scored_accepted = 0

    for row_num, row in enumerate(rows, start=1):
        condition = (row.get("condition") or "").strip().upper()
        if condition not in VALID_CONDITIONS:
            raise Change07LogError(
                f"Row {row_num}: invalid condition '{condition}'; expected NO_CAPE or CAPE."
            )

        outcome = (row.get("outcome") or "").strip().upper()
        if outcome not in VALID_OUTCOMES:
            raise Change07LogError(
                f"Row {row_num}: invalid outcome '{outcome}'; expected one of {sorted(VALID_OUTCOMES)}."
            )

        activation_status = (row.get("activation_status") or "").strip().upper()
        if activation_status not in VALID_ACTIVATION_STATUSES:
            raise Change07LogError(
                f"Row {row_num}: invalid activation_status '{activation_status}'."
            )
        if condition == "CAPE" and activation_status == "ACTIVATION_FAILED":
            cape_activation_failures += 1

        active_sec = _parse_int_field(row, "active_time_seconds", row_num)
        if active_sec < 0 or active_sec > CHANGE_07_MAX_ACTIVE_SECONDS:
            raise Change07LogError(
                f"Row {row_num}: active_time_seconds ({active_sec}) outside [0, {CHANGE_07_MAX_ACTIVE_SECONDS}]."
            )

        rework = (row.get("rework_indicator") or "").strip().upper()
        if rework not in {"YES", "NO"}:
            raise Change07LogError(
                f"Row {row_num}: rework_indicator must be YES or NO, got '{rework}'."
            )

        if outcome not in COMPARABLE_OUTCOMES:
            excluded_rows += 1
            continue

        accepted, is_critical = _is_quality_accepted(row, row_num)
        if condition == "NO_CAPE":
            baseline_scored_total += 1
            baseline_scored_accepted += int(accepted)
            baseline_crit += int(is_critical)
            baseline_rework += int(rework == "YES")
        else:
            cape_scored_total += 1
            cape_scored_accepted += int(accepted)
            cape_crit += int(is_critical)
            cape_rework += int(rework == "YES")

        pair_id = (row.get("pair_id") or "").strip()
        if not pair_id:
            raise Change07LogError(f"Row {row_num}: pair_id must not be empty.")
        pair_bucket = pairs.setdefault(pair_id, {})
        if condition in pair_bucket:
            raise Change07LogError(
                f"Row {row_num}: duplicate comparable entry for pair '{pair_id}', condition '{condition}'."
            )
        pair_bucket[condition] = {"active_time_seconds": active_sec, "accepted": accepted}

    comparable_baseline_times: list[int] = []
    comparable_cape_times: list[int] = []
    for bucket in pairs.values():
        if "NO_CAPE" in bucket and "CAPE" in bucket:
            comparable_baseline_times.append(bucket["NO_CAPE"]["active_time_seconds"])
            comparable_cape_times.append(bucket["CAPE"]["active_time_seconds"])

    valid_pairs = len(comparable_baseline_times)
    base_total = sum(comparable_baseline_times)
    cape_total = sum(comparable_cape_times)
    base_median = (
        float(statistics.median(comparable_baseline_times)) if valid_pairs > 0 else None
    )
    cape_median = (
        float(statistics.median(comparable_cape_times)) if valid_pairs > 0 else None
    )

    notes: list[str] = []
    total_red: float | None = None
    median_red: float | None = None

    if valid_pairs == 0 or base_total == 0:
        status = "NOT_ANALYZABLE"
        notes.append(
            "Zero-denominator guard triggered: no valid comparable pairs with positive baseline time."
        )
    else:
        status = "ANALYZED"
        total_red = round(((base_total - cape_total) / base_total) * 100.0, 2)
        if base_median is not None and base_median > 0 and cape_median is not None:
            median_red = round(((base_median - cape_median) / base_median) * 100.0, 2)
        else:
            notes.append("Median reduction not calculable because baseline median is zero.")

    base_acc_rate = (
        round((baseline_scored_accepted / baseline_scored_total) * 100.0, 2)
        if baseline_scored_total > 0
        else None
    )
    cape_acc_rate = (
        round((cape_scored_accepted / cape_scored_total) * 100.0, 2)
        if cape_scored_total > 0
        else None
    )

    quality_preserved = (
        cape_crit == 0
        and cape_acc_rate is not None
        and base_acc_rate is not None
        and cape_acc_rate >= base_acc_rate
    )
    target_met = bool(
        status == "ANALYZED"
        and total_red is not None
        and total_red >= CHANGE_07_TARGET_REDUCTION_PCT
        and quality_preserved
    )
    if status == "ANALYZED" and not quality_preserved:
        notes.append(
            "Quality gate failed or regressed (CAPE acceptance < baseline or critical failure recorded); "
            "efficiency improvement cannot be claimed."
        )
    if valid_pairs < 10:
        notes.append(
            f"Sample deviation: {valid_pairs}/10 target pairs present; report descriptively with small-sample caveat."
        )

    return Change07Summary(
        status=status,
        total_rows=len(rows),
        valid_comparable_pairs=valid_pairs,
        excluded_rows=excluded_rows,
        baseline_total_active_seconds=base_total,
        cape_total_active_seconds=cape_total,
        baseline_median_active_seconds=base_median,
        cape_median_active_seconds=cape_median,
        total_active_time_reduction_pct=total_red,
        median_active_time_reduction_pct=median_red,
        baseline_quality_acceptance_rate=base_acc_rate,
        cape_quality_acceptance_rate=cape_acc_rate,
        baseline_critical_failures=baseline_crit,
        cape_critical_failures=cape_crit,
        cape_activation_failures=cape_activation_failures,
        baseline_rework_count=baseline_rework,
        cape_rework_count=cape_rework,
        target_30pct_achieved=target_met,
        notes=tuple(notes),
    )


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser for ``cape_quality_gate``.

    Returns:
        Configured ``argparse.ArgumentParser`` instance.
    """
    parser = argparse.ArgumentParser(
        prog="cape_quality_gate",
        description="Local governance, Markdown, Skill budget, and Change 07 scoring checks.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    skill_cmd = sub.add_parser(
        "check-skill",
        help="Verify Skill character count (<24,000), headroom, and SHA-256.",
    )
    skill_cmd.add_argument("files", nargs="+", type=Path, help="Skill Markdown file(s).")
    skill_cmd.add_argument("--limit", type=int, default=SKILL_CHAR_LIMIT)

    docs_cmd = sub.add_parser(
        "check-docs",
        help="Run structural, heading, table, and relative-link checks on Markdown files.",
    )
    docs_cmd.add_argument("files", nargs="+", type=Path, help="Markdown file(s).")

    c07_cmd = sub.add_parser(
        "score-c07",
        help="Validate and score a Change 07 matched-pair execution log CSV.",
    )
    c07_cmd.add_argument("csv_file", type=Path, help="Path to Change 07 execution log CSV.")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint returning process exit status.

    Args:
        argv: Optional command-line argument list.

    Returns:
        ``0`` when all checks pass, ``1`` when a validation failure occurs, or
        ``2`` on input/schema error.
    """
    logger = configure_logger()
    args = build_parser().parse_args(argv)

    try:
        if args.command == "check-skill":
            results = [audit_skill_file(p, limit=args.limit) for p in args.files]
            payload: Any = [asdict(r) for r in results]
            all_ok = all(r.within_limit_lf and r.within_limit_raw for r in results)
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
            logger.info("Skill audit finished", extra={"context": {"all_ok": all_ok}})
            return 0 if all_ok else 1

        if args.command == "check-docs":
            doc_results = [audit_markdown_file(p) for p in args.files]
            payload = [{**asdict(r), "passed": r.passed} for r in doc_results]
            all_ok = all(r.passed for r in doc_results)
            sys.stdout.write(json.dumps(payload, indent=2) + "\n")
            logger.info("Markdown audit finished", extra={"context": {"all_ok": all_ok}})
            return 0 if all_ok else 1

        if args.command == "score-c07":
            summary = score_change_07_log(args.csv_file)
            sys.stdout.write(json.dumps(asdict(summary), indent=2) + "\n")
            logger.info(
                "Change 07 scoring finished",
                extra={"context": {"status": summary.status, "pairs": summary.valid_comparable_pairs}},
            )
            return 0

        raise QualityGateError(f"Unsupported command: {args.command}")
    except QualityGateError as exc:
        logger.error(str(exc), extra={"context": {"command": args.command}})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
