# CAPE Platform Defect, Connector & Telemetry RFC (RPA Pilot Findings)

**Document ID:** `CAPE-RPA-PLT-RFC-001`
**Version:** v0.1 (`DRAFT — FOR CAPE PLATFORM TEAM & PROJECT OWNER REVIEW`)
**Date:** 20 November 2026
**Author:** Juan José Restrepo Rosero (RPA Development Skill Pilot)
**Target Audience:** CAPE Platform Engineering (`dappy` / Azure Databricks Apps), CAPE Platform Owner (`DEC-PLT-01`), Project Sponsor (Nikko Gonzales)
**Evidence Basis:** Live 11-case regression ([`CAPE_Regression_Run_2026-11-19.md`](../../Docs/Skill/Tests/CAPE_Regression_Run_2026-11-19.md)), clean-session negative controls `N1`–`N5` (2026-11-20), and preliminary qualitative user feedback ([`02_User_Feedback_Summary.md`](../../04_User_Feedback/02_User_Feedback_Summary.md))

> **Governance Boundary:** This RFC isolates **CAPE host-platform behaviors** from **RPA Development Skill instructions** so platform defects are never misattributed to Skill quality or masked by prompt workarounds. No production platform change is authorized by this document.

---

## 1. Executive Summary

During controlled live pilot validation of the **RPA Development Skill (`Pilot v0.1`, SHA-256 `FA84A451...`)** on CAPE (`dappy`), the Skill achieved **`4/4 PASS`** on Coverage-Honesty boundary cases (`Q10, Q11, Q12, Q19`) and **`0 FAIL`** across the 11-question subset. However, live execution exposed **five reproducible or recurring host-platform limitations (`PLAT-01`–`PLAT-05`)** and **three platform-contract gaps** (character-counting criterion, native Confluence metadata, and audit telemetry export) that directly affect developer UX, latency, token consumption, and benchmark auditability.

---

## 2. Observed Platform Defects & Reproducible Evidence (`PLAT-01`–`PLAT-05`)

| Platform ID | Severity | Symptom Observed | Reproducibility / Evidence | Operational & Benchmark Impact | Recommended Platform Fix |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **`PLAT-01`** | Medium | Session/sign-in expiration and intermittent context errors requiring page refresh or re-prompt | Preliminary qualitative feedback (Maide — `02_User_Feedback_Summary.md`) | Causes `INTERRUPTED` runs during Change 07 and erodes developer trust | Improve token refresh / session recovery without dropping active conversation state. |
| **`PLAT-02`** | Medium | Failure to ingest tabular data (empty tables) during document conversion | Preliminary qualitative feedback (Isa — `02_User_Feedback_Summary.md`) | Blocks future Skill/document workflows relying on Confluence or Word tables | Upgrade document-to-Markdown table parser with regression tests on complex tables. |
| **`PLAT-03`** | **High** | False internal *"empty reply"* retry producing **concatenated duplicate responses** in chat UI | **Observed in `8 / 11` (72.7%)** multi-tool Confluence runs on 2026-11-19 (`Q1, Q5, Q6, Q11, Q12, Q15, Q16, Q19`); **`0 / 5`** in zero-tool clean runs (`N1`–`N5`, 2026-11-20) | Doubles reading time (hurting Change 07), inflates token consumption, and confuses users | Fix streaming/retry completion detection when tool-call turns precede the final assistant message. |
| **`PLAT-04`** | **High** | `Add To Project Memory` persists cross-session notes inside CAPE Projects (`Ticket Tracker`), leaking prior page IDs and gap verdicts into new chats | Observed across `Q3, Q5, Q12, Q15, Q16, Q19` inside `Ticket Tracker`; **`0 / 5`** in standalone chats outside Projects (`N1`–`N5`) | Violates Clean Session Isolation for regression testing and Change 07 benchmarking; risks stale-memory contamination | Provide an explicit per-chat *"Stateless / Disable Project Memory"* toggle and clear UI indicator when memory is injected. |
| **`PLAT-05`** | Medium | `Confluence Get Page` silently truncates long Confluence pages mid-section (`KS-006` Phase 10; `KS-007` step 9a) | Reproducible on `Q1, Q6, Q15, Q16` (2026-11-19) | Forces the Skill to disclose partial reads instead of answering end-of-page rules (e.g., Phase 10 BAU Handover) | Expose structured pagination (`offset`/`cursor`) or a clear `truncated: true` metadata field in `Confluence Get Page`. |

---

## 3. Platform Contract & Auditability Requests (`DEC-PLT-01` & Change 04/05)

1. **Confirm Official 24,000-Character Counting Rule:**
   - Local measurement of Candidate v0.1.2 is `23,435` LF chars (`23,726` CRLF chars / `23,786` UTF-8 bytes).
   - *Request:* Confirm whether CAPE enforces the 24,000 limit on LF characters, CRLF characters, UTF-8 bytes, or Markdown-rendered length so Skill CI (`.github/workflows/cape-quality-gate.yml`) can enforce the exact platform ceiling.
2. **Native Confluence Provenance Fields in Search & Get Page Outputs:**
   - Currently, Change 04 requires extra `Confluence Page Info` round-trips per page (adding latency and duplicate tool calls — e.g., `Q6` issued 12 calls / 62s) to capture `page_id`, `space_key`, `version`, and `last_modified`.
   - *Request:* Include `{page_id, space_key, version_number, last_modified, canonical_url}` directly in `Confluence Search` and `Confluence Get Page` tool responses. Expected impact: **30–50% fewer tool calls** per governed RPA query.
3. **Exportable Conversation Telemetry & Stable Conversation IDs (Requests B & C):**
   - Historical audit findings `E-10` and `E-14` remain open because CAPE lacks an exportable audit bundle (stable `conversation_id`, UTC timestamps, loaded Skill SHA-256/version, tool trace).
   - *Request:* Expose a read-only JSON transcript/trace export button per conversation for pilot QA and Change 07 evidence retention (`C07-D10`).

---

## 4. Pilot Workarounds Active Until Platform Fixes Land

- **For `PLAT-04`:** All formal regression runs and Change 07 executions run strictly in **standalone CAPE sessions outside Projects** (`C07-D06`).
- **For `PLAT-03`:** Duplicate concatenated blocks are logged as platform friction (`M-C5`) and excluded from Skill behavioral penalties.
- **For `PLAT-05`:** Skill instructions preserve honest truncation disclosure; Change 07 key points are verified directly in Confluence (`CHK-01`–`CHK-05`).
