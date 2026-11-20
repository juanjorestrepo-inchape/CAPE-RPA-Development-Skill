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
import html
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


def _read_comparable_pairs(csv_path: Path) -> list[dict[str, Any]]:
    """Extract sorted comparable pair rows for visual Change 07 reporting.

    Args:
        csv_path: Path to a validated Change 07 execution log CSV.

    Returns:
        Sorted list of per-pair comparison dictionaries containing baseline and
        CAPE active times, domain, difficulty, and delta percentage.
    """
    pairs: dict[str, dict[str, dict[str, Any]]] = {}
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            outcome = (row.get("outcome") or "").strip().upper()
            cond = (row.get("condition") or "").strip().upper()
            pair_id = (row.get("pair_id") or "").strip()
            if outcome not in COMPARABLE_OUTCOMES or cond not in VALID_CONDITIONS:
                continue
            try:
                active = int((row.get("active_time_seconds") or "0").strip())
            except ValueError:
                continue
            pairs.setdefault(pair_id, {})[cond] = {
                "active_time_seconds": active,
                "domain": (row.get("task_domain") or "").strip(),
                "difficulty": (row.get("task_difficulty") or "").strip(),
                "accepted": (row.get("accepted") or "").strip().upper(),
                "critical_failure": (row.get("critical_failure") or "NO").strip().upper(),
                "activation_status": (row.get("activation_status") or "").strip().upper(),
            }

    output: list[dict[str, Any]] = []
    for pair_id in sorted(pairs.keys()):
        bucket = pairs[pair_id]
        if "NO_CAPE" in bucket and "CAPE" in bucket:
            base_s = bucket["NO_CAPE"]["active_time_seconds"]
            cape_s = bucket["CAPE"]["active_time_seconds"]
            delta_pct = round(((base_s - cape_s) / base_s) * 100.0, 1) if base_s > 0 else None
            output.append(
                {
                    "pair_id": pair_id,
                    "domain": bucket["NO_CAPE"]["domain"] or bucket["CAPE"]["domain"],
                    "difficulty": bucket["NO_CAPE"]["difficulty"] or bucket["CAPE"]["difficulty"],
                    "no_cape_seconds": base_s,
                    "cape_seconds": cape_s,
                    "delta_pct": delta_pct,
                    "no_cape_accepted": bucket["NO_CAPE"]["accepted"],
                    "cape_accepted": bucket["CAPE"]["accepted"],
                    "cape_activation": bucket["CAPE"]["activation_status"],
                }
            )
    return output


def generate_change_07_html_report(csv_path: Path, output_path: Path) -> Change07Summary:
    """Generate a self-contained HTML executive dashboard from a Change 07 CSV log.

    Renders KPI cards, separated Answer-Quality vs. Operational Performance
    panels (Protocol v0.1-r2 §6.5), and per-pair ``NO_CAPE`` vs. ``CAPE``
    horizontal bar comparisons using pure HTML/CSS with zero external assets.

    Args:
        csv_path: Path to the Change 07 execution log CSV file.
        output_path: Destination path for the generated HTML report.

    Returns:
        ``Change07Summary`` computed from ``csv_path``.

    Raises:
        Change07LogError: If ``csv_path`` fails Protocol v0.1-r2 validation.
    """
    summary = score_change_07_log(csv_path)
    pair_rows = _read_comparable_pairs(csv_path)
    max_time = max(
        [max(r["no_cape_seconds"], r["cape_seconds"]) for r in pair_rows] or [600]
    )

    def _fmt_pct(val: float | None) -> str:
        return f"{val:.1f}%" if val is not None else "N/A"

    def _fmt_sec(val: float | int | None) -> str:
        return f"{val:.1f}s" if isinstance(val, float) else (f"{val}s" if val is not None else "N/A")

    if summary.status == "NO_DATA":
        badge_cls, badge_txt = "badge-neutral", "NO DATA — 0 EXECUTIONS LOGGED"
    elif summary.target_30pct_achieved:
        badge_cls, badge_txt = "badge-pass", "TARGET ACHIEVED (≥30% & QUALITY PRESERVED)"
    else:
        badge_cls, badge_txt = "badge-warn", "TARGET NOT YET ACHIEVED / QUALITY GATED"

    rows_html_parts: list[str] = []
    for row in pair_rows:
        base_w = round((row["no_cape_seconds"] / max_time) * 100, 1) if max_time > 0 else 0
        cape_w = round((row["cape_seconds"] / max_time) * 100, 1) if max_time > 0 else 0
        delta_txt = _fmt_pct(row["delta_pct"])
        rows_html_parts.append(
            "<tr>"
            f"<td><strong>{html.escape(row['pair_id'])}</strong></td>"
            f"<td>{html.escape(row['domain'])}<br><small>{html.escape(row['difficulty'])}</small></td>"
            f"<td><div class='bar-wrap'><div class='bar bar-base' style='width:{base_w}%'>{row['no_cape_seconds']}s</div></div>"
            f"<div class='bar-wrap'><div class='bar bar-cape' style='width:{cape_w}%'>{row['cape_seconds']}s</div></div></td>"
            f"<td class='num'>{delta_txt}</td>"
            f"<td class='num'>{html.escape(row['no_cape_accepted'])} / {html.escape(row['cape_accepted'])}</td>"
            f"<td class='num'>{html.escape(row['cape_activation'])}</td>"
            "</tr>"
        )
    table_body = (
        "\n".join(rows_html_parts)
        if rows_html_parts
        else "<tr><td colspan='6' class='empty'>No valid comparable pairs logged yet.</td></tr>"
    )
    notes_html = "".join(f"<li>{html.escape(n)}</li>" for n in summary.notes) or "<li>None.</li>"
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    document = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CAPE RPA Skill — Change 07 Efficiency Report</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 24px; color: #1e293b; background: #f8fafc; }}
  .container {{ max-width: 1080px; margin: 0 auto; background: #ffffff; padding: 28px; border-radius: 12px; box-shadow: 0 2px 12px rgba(15,23,42,0.08); }}
  h1 {{ margin: 0 0 6px 0; font-size: 22px; }}
  .subtitle {{ color: #475569; margin: 0 0 18px 0; font-size: 13px; }}
  .badge {{ display: inline-block; padding: 6px 12px; border-radius: 999px; font-size: 12px; font-weight: 700; margin-bottom: 18px; }}
  .badge-pass {{ background: #dcfce7; color: #166534; }}
  .badge-warn {{ background: #fef3c7; color: #92400e; }}
  .badge-neutral {{ background: #e2e8f0; color: #334155; }}
  .grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 22px; }}
  .card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; }}
  .card-label {{ font-size: 11px; text-transform: uppercase; color: #64748b; letter-spacing: 0.04em; }}
  .card-value {{ font-size: 22px; font-weight: 700; margin-top: 4px; color: #0f172a; }}
  .split {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 22px; }}
  .panel {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; }}
  .panel h2 {{ font-size: 14px; margin: 0 0 10px 0; color: #0f172a; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th, td {{ border-bottom: 1px solid #e2e8f0; padding: 10px 8px; text-align: left; vertical-align: middle; }}
  th {{ background: #f1f5f9; font-size: 12px; color: #334155; }}
  .num {{ text-align: right; white-space: nowrap; }}
  .bar-wrap {{ background: #e2e8f0; border-radius: 4px; margin: 3px 0; overflow: hidden; }}
  .bar {{ color: #ffffff; font-size: 11px; font-weight: 600; padding: 2px 6px; white-space: nowrap; }}
  .bar-base {{ background: #64748b; }}
  .bar-cape {{ background: #2563eb; }}
  .legend {{ font-size: 12px; color: #475569; margin-bottom: 8px; }}
  .dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 4px; }}
  .empty {{ text-align: center; color: #64748b; padding: 24px; }}
  .notes {{ font-size: 12px; color: #475569; margin-top: 18px; }}
</style>
</head>
<body>
<div class="container">
  <h1>CAPE RPA Development Skill — Change 07 Efficiency Report</h1>
  <p class="subtitle">Source CSV: <code>{html.escape(csv_path.name)}</code> · Protocol v0.1-r2 · Generated {generated_at} · Principle: <strong>Trust Before Breadth</strong></p>
  <span class="badge {badge_cls}">{badge_txt}</span>

  <div class="grid">
    <div class="card"><div class="card-label">Valid Comparable Pairs</div><div class="card-value">{summary.valid_comparable_pairs} / 10</div></div>
    <div class="card"><div class="card-label">Total Time Reduction (M-C1)</div><div class="card-value">{_fmt_pct(summary.total_active_time_reduction_pct)}</div></div>
    <div class="card"><div class="card-label">Median Time Reduction (M-C2)</div><div class="card-value">{_fmt_pct(summary.median_active_time_reduction_pct)}</div></div>
    <div class="card"><div class="card-label">CAPE Critical Failures</div><div class="card-value">{summary.cape_critical_failures}</div></div>
  </div>

  <div class="split">
    <div class="panel">
      <h2>Answer-Quality Acceptance (§6.5 — Separated from Speed)</h2>
      <p><strong>NO_CAPE Acceptance Rate:</strong> {_fmt_pct(summary.baseline_quality_acceptance_rate)} (Critical Failures: {summary.baseline_critical_failures})</p>
      <p><strong>CAPE Acceptance Rate:</strong> {_fmt_pct(summary.cape_quality_acceptance_rate)} (Critical Failures: {summary.cape_critical_failures})</p>
    </div>
    <div class="panel">
      <h2>Operational Performance (§6.5)</h2>
      <p><strong>Total Active Time:</strong> NO_CAPE {_fmt_sec(summary.baseline_total_active_seconds)} vs. CAPE {_fmt_sec(summary.cape_total_active_seconds)}</p>
      <p><strong>Median Active Time:</strong> NO_CAPE {_fmt_sec(summary.baseline_median_active_seconds)} vs. CAPE {_fmt_sec(summary.cape_median_active_seconds)}</p>
      <p><strong>Rework (NO_CAPE / CAPE):</strong> {summary.baseline_rework_count} / {summary.cape_rework_count} · <strong>Activation Failures:</strong> {summary.cape_activation_failures} · <strong>Excluded Rows:</strong> {summary.excluded_rows}</p>
    </div>
  </div>

  <div class="legend"><span class="dot" style="background:#64748b"></span>NO_CAPE (Manual Baseline) &nbsp;&nbsp; <span class="dot" style="background:#2563eb"></span>CAPE (RPA Skill)</div>
  <table>
    <thead>
      <tr><th>Pair</th><th>Domain &amp; Difficulty</th><th>Active Time Comparison (s)</th><th class="num">Delta</th><th class="num">Accepted (Base/CAPE)</th><th class="num">CAPE Activation</th></tr>
    </thead>
    <tbody>
      {table_body}
    </tbody>
  </table>

  <div class="notes">
    <strong>Protocol Guardrails &amp; Notes:</strong>
    <ul>{notes_html}</ul>
  </div>
</div>
</body>
</html>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding="utf-8")
    return summary


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

    report_cmd = sub.add_parser(
        "report-c07",
        help="Generate a self-contained HTML executive dashboard from a Change 07 CSV.",
    )
    report_cmd.add_argument("csv_file", type=Path, help="Path to Change 07 execution log CSV.")
    report_cmd.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output path for the generated HTML report.",
    )

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

        if args.command == "report-c07":
            summary = generate_change_07_html_report(args.csv_file, args.output)
            sys.stdout.write(json.dumps(asdict(summary), indent=2) + "\n")
            logger.info(
                "Change 07 HTML report generated",
                extra={"context": {"output": str(args.output), "status": summary.status}},
            )
            return 0

        raise QualityGateError(f"Unsupported command: {args.command}")
    except QualityGateError as exc:
        logger.error(str(exc), extra={"context": {"command": args.command}})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
