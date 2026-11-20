"""Unit tests for ``scripts/cape_quality_gate.py``.

Validates Skill budget auditing, Markdown structural checks, and Change 07
Protocol v0.1-r2 scoring logic (including zero-denominator guard, 600s cap,
critical-failure veto override, and separated quality acceptance vs. speed).
"""

from __future__ import annotations

import csv
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "scripts"))

import cape_quality_gate as cqg  # noqa: E402

C07_HEADERS: list[str] = [
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
]


def _make_c07_row(**overrides: str) -> dict[str, str]:
    """Build a valid Change 07 CSV row with optional field overrides."""
    base: dict[str, str] = {
        "protocol_version": "v0.1-r2",
        "execution_id": "C07-P01-NO_CAPE-1",
        "pair_id": "P01",
        "task_id": "P01-A",
        "task_domain": "lifecycle",
        "task_intent": "how-to",
        "task_difficulty": "Medium",
        "task_matching_rationale": "Equivalent lifecycle pair",
        "expected_outcome": "KS-006 Phase 3-4",
        "condition": "NO_CAPE",
        "condition_order": "1",
        "participant_id": "DEV-01",
        "execution_date_time": "2026-11-20T10:00:00Z",
        "cape_available": "NO",
        "skill_loaded": "NO",
        "activation_mode": "NOT_APPLICABLE",
        "activation_status": "NOT_APPLICABLE",
        "skill_version": "",
        "start_time": "2026-11-20T10:00:00Z",
        "end_time": "2026-11-20T10:05:00Z",
        "active_time_seconds": "300",
        "interruption_seconds": "0",
        "interruption_log": "",
        "termination_reason": "ANSWERED",
        "outcome": "RESOLVED",
        "sources_consulted": "KS-006",
        "sources_cited": "KS-006",
        "quality_dim_1": "1",
        "quality_dim_2": "1",
        "quality_dim_3": "1",
        "quality_dim_4": "1",
        "quality_dim_5": "1",
        "quality_dim_6": "1",
        "quality_dim_7": "1",
        "quality_dim_8": "1",
        "quality_total": "8",
        "accepted": "YES",
        "critical_failure": "NO",
        "critical_failure_reason": "",
        "rework_indicator": "NO",
        "rework_description": "",
        "reviewer_notes": "Clean run",
        "deviation": "NONE",
        "evidence_location": "local://evidence/1",
    }
    base.update(overrides)
    return base


class TestSkillAudit(unittest.TestCase):
    """Tests for ``audit_skill_file``."""

    def test_counts_lf_crlf_and_headroom(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            skill_path = Path(tmp) / "skill.md"
            skill_path.write_bytes(b"line1\r\nline2\r\n")
            result = cqg.audit_skill_file(skill_path, limit=20, safety_buffer=5)
            self.assertEqual(result.lf_characters, 12)
            self.assertEqual(result.raw_characters, 14)
            self.assertTrue(result.within_limit_lf)
            self.assertTrue(result.within_limit_raw)
            self.assertFalse(result.low_margin_warning)
            self.assertEqual(len(result.sha256), 64)

    def test_detects_over_limit_and_invalid_args(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            skill_path = Path(tmp) / "big.md"
            skill_path.write_text("x" * 25, encoding="utf-8")
            result = cqg.audit_skill_file(skill_path, limit=20, safety_buffer=5)
            self.assertFalse(result.within_limit_lf)
            self.assertTrue(result.low_margin_warning)
            with self.assertRaises(cqg.SkillValidationError):
                cqg.audit_skill_file(skill_path, limit=0)
            with self.assertRaises(cqg.SkillValidationError):
                cqg.audit_skill_file(Path(tmp) / "missing.md")


class TestMarkdownAudit(unittest.TestCase):
    """Tests for ``audit_markdown_file``."""

    def test_valid_markdown_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            doc = root / "doc.md"
            doc.write_text(
                "# Title\n\n## Section 1\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n[ok](target.md)\n",
                encoding="utf-8",
            )
            result = cqg.audit_markdown_file(doc)
            self.assertTrue(result.passed)

    def test_detects_defects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "bad.md"
            doc.write_text(
                "# Title  \n\n### Skipped\n\n### Skipped\n\n| A | B |\n|---|\n\n[bad](missing file.md)\n```\nunclosed",
                encoding="utf-8",
            )
            result = cqg.audit_markdown_file(doc)
            self.assertFalse(result.passed)
            self.assertFalse(result.code_fences_balanced)
            self.assertFalse(result.eof_newline)
            self.assertTrue(result.trailing_whitespace_lines)
            self.assertEqual(len(result.heading_issues), 2)
            self.assertEqual(len(result.table_issues), 1)
            self.assertEqual(len(result.unencoded_space_links), 1)
            self.assertEqual(len(result.broken_relative_links), 1)


class TestChange07Scoring(unittest.TestCase):
    """Tests for ``score_change_07_log``."""

    def _write_csv(self, path: Path, rows: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=C07_HEADERS)
            writer.writeheader()
            writer.writerows(rows)

    def test_empty_log_returns_no_data(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "empty.csv"
            self._write_csv(csv_path, [])
            summary = cqg.score_change_07_log(csv_path)
            self.assertEqual(summary.status, "NO_DATA")
            self.assertFalse(summary.target_30pct_achieved)
            self.assertIsNone(summary.total_active_time_reduction_pct)

    def test_valid_pairs_compute_total_and_median_reduction(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "valid.csv"
            rows = [
                _make_c07_row(pair_id="P01", condition="NO_CAPE", active_time_seconds="400"),
                _make_c07_row(
                    pair_id="P01",
                    execution_id="C07-P01-CAPE-2",
                    condition="CAPE",
                    cape_available="YES",
                    skill_loaded="YES",
                    activation_mode="AUTO",
                    activation_status="ACTIVATED",
                    active_time_seconds="200",
                ),
                _make_c07_row(pair_id="P02", condition="NO_CAPE", active_time_seconds="200"),
                _make_c07_row(
                    pair_id="P02",
                    execution_id="C07-P02-CAPE-2",
                    condition="CAPE",
                    cape_available="YES",
                    skill_loaded="YES",
                    activation_mode="AUTO",
                    activation_status="ACTIVATED",
                    active_time_seconds="100",
                ),
            ]
            self._write_csv(csv_path, rows)
            summary = cqg.score_change_07_log(csv_path)
            self.assertEqual(summary.status, "ANALYZED")
            self.assertEqual(summary.valid_comparable_pairs, 2)
            self.assertEqual(summary.total_active_time_reduction_pct, 50.0)
            self.assertEqual(summary.median_active_time_reduction_pct, 50.0)
            self.assertTrue(summary.target_30pct_achieved)

    def test_critical_failure_blocks_30pct_claim_despite_speed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "veto.csv"
            rows = [
                _make_c07_row(pair_id="P01", condition="NO_CAPE", active_time_seconds="500"),
                _make_c07_row(
                    pair_id="P01",
                    condition="CAPE",
                    activation_status="ACTIVATED",
                    active_time_seconds="50",
                    critical_failure="YES",
                    critical_failure_reason="C1-fabricated-standard",
                ),
            ]
            self._write_csv(csv_path, rows)
            summary = cqg.score_change_07_log(csv_path)
            self.assertEqual(summary.total_active_time_reduction_pct, 90.0)
            self.assertEqual(summary.cape_critical_failures, 1)
            self.assertEqual(summary.cape_quality_acceptance_rate, 0.0)
            self.assertFalse(summary.target_30pct_achieved)

    def test_rejects_active_time_over_600s(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "overcap.csv"
            self._write_csv(csv_path, [_make_c07_row(active_time_seconds="601")])
            with self.assertRaises(cqg.Change07LogError):
                cqg.score_change_07_log(csv_path)

    def test_cli_score_template_exits_zero(self) -> None:
        template_path = REPO_ROOT / "Docs" / "Skill" / "Change_07_Execution_Log_TEMPLATE.csv"
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cqg.main(["score-c07", str(template_path)])
        self.assertEqual(code, 0)
        parsed = json.loads(buf.getvalue())
        self.assertEqual(parsed["status"], "NO_DATA")
        self.assertFalse(parsed["target_30pct_achieved"])

    def test_report_c07_generates_self_contained_html(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            csv_path = root / "run.csv"
            out_html = root / "report.html"
            rows = [
                _make_c07_row(
                    pair_id="P01",
                    task_domain="lifecycle <script>",
                    condition="NO_CAPE",
                    active_time_seconds="400",
                ),
                _make_c07_row(
                    pair_id="P01",
                    execution_id="C07-P01-CAPE-2",
                    task_domain="lifecycle <script>",
                    condition="CAPE",
                    activation_status="ACTIVATED",
                    active_time_seconds="200",
                ),
            ]
            self._write_csv(csv_path, rows)
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = cqg.main(["report-c07", str(csv_path), "--output", str(out_html)])
            self.assertEqual(code, 0)
            self.assertTrue(out_html.is_file())
            content = out_html.read_text(encoding="utf-8")
            self.assertIn("TARGET ACHIEVED", content)
            self.assertIn("50.0%", content)
            self.assertIn("lifecycle &lt;script&gt;", content)
            self.assertNotIn("<script>", content)

    def test_report_c07_handles_empty_template_safely(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            template_path = REPO_ROOT / "Docs" / "Skill" / "Change_07_Execution_Log_TEMPLATE.csv"
            out_html = Path(tmp) / "empty.html"
            summary = cqg.generate_change_07_html_report(template_path, out_html)
            self.assertEqual(summary.status, "NO_DATA")
            content = out_html.read_text(encoding="utf-8")
            self.assertIn("NO DATA — 0 EXECUTIONS LOGGED", content)
            self.assertIn("No valid comparable pairs logged yet.", content)


if __name__ == "__main__":
    unittest.main()
