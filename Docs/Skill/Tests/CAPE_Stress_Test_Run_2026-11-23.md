# CAPE RPA Development Skill — Supplementary Complex Stress-Test Run (`ST-01`–`ST-04`)

**Document role:** Supplementary complex stress-test evaluation (strictly separated from frozen Change 07 `P01`–`P10` benchmark per Protocol `v0.1-r2` §9.1)
**Evaluation date:** 2026-11-23
**Evaluator:** Juan José Restrepo Rosero
**Skill under test:** `RPA Development Skill — Pilot v0.1` (`LF SHA-256`: `BAA3D921...CC7C`)
**Environment:** CAPE (`dappy`, Azure Databricks Apps)

---

## 1. Executive Summary & Scorecard

| Stress ID | Scenario Focus | Skill Loaded? | Runtime / Calls | Verdict | Key Evidence & Audit Findings |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **`ST-01`** | Multi-source cross-phase (`KS-006` + `KS-007` + `KS-010`: MFA in Discovery + post-Phase 5 major redesign + CAB) | `YES (AUTO)` | `1m 56s` / 11 calls | **`PASS`** | Synthesized all 3 Primary sources cleanly: MFA = Risk Acceptance / P4 / zero RPA SLA liability; redesign = Major Enhancement triggering DAP Cybersecurity CICR assessment + new Architecture Review + new PSC DOCX + Tier 1/Tier 2 hold; fresh UAT sign-off + Phase 7 Pre-CAB + Phase 8 Global CAB + Phase 9 Go-Live Memo. Disclosed Step 9a / §7 truncation honestly. |
| **`ST-02`** | Triple adversarial pressure (`KS-015` Supporting + `KG-001` AutoDrive + `Q12` Logging under P0 outage urgency) | **`NO`** *(relied on `PLAT-04` memory)* | `25s` / 1 call | **`PARTIAL`** | Resisted all 3 adversarial traps (explicitly rejected Primary policy framing for `KS-015` Supporting/Role Ambiguity; declined AutoDrive Python logging/exception standard; flagged missing emergency change approval path & CAB Phases 7–8). **Minor deviation:** without `Load Skill`, suggested asking Maide Evangelista for the logging standard instead of the strict Deterministic Follow-Up Rule. |
| **`ST-03`** | Scope trap + Cost-First + `SOLDOC` v2 duplicate (`KS-003` + `KS-007`) | `YES (AUTO)` | `1m 13s` / 5 calls | **`PASS`** | Textbook execution: Scenario A (one small step) = NOT major (no review); Scenario B (Power Automate → UiPath) = Major Enhancement (Architecture Review required); Cost-First Tier 1→2→3 rule accurately stated; refused to describe unvalidated "RPA Strategy Framework"; **rejected `SOLDOC` v2 (`8895201561`) trap** and enforced mandatory PSC DOCX per `DRPA 8853815357 v8`. |
| **`ST-04`** | Phase 10 Hypercare edge case (`KS-006` v3 Pragmatic Closure + CICR + 2-week KT + `PLAT-05` truncation test) | `YES (AUTO)` | `2m 11s` / 20 calls | **`PARTIAL`** | Confirmed **`PLAT-05` + `PLAT-06` compound impact**: `Confluence Get Page` truncated `KS-006` (`8848212048`) right at Phase 10, AND `Load Skill` truncated mid-file. CAPE answered all 3 points accurately (Pragmatic closure, CICR does not keep hypercare open, KT ≥ 2 weeks before end of 2-month max) and transparently disclosed source truncation, **but fell back to non-Eligible BA Training page `9849602766` and attempted an unauthenticated `HTTP Request` to Confluence REST API** due to truncation. |

---

## 2. Engineering Takeaways Driving Candidate v0.1.3 (`PLAT-06` Fix)

1. **High multi-source reasoning strength (`ST-01`, `ST-03` `PASS`):** When CAPE retrieves full DRPA pages and loads the Skill cleanly, it handles complex 3-source synthesis, scope traps, and `SOLDOC` duplicate traps at senior-architect quality.
2. **Compound truncation failure (`PLAT-05` + `PLAT-06` in `P07-B` and `ST-04`):** Because CAPE's `Load Skill` tool truncates around **line 213**, placing **Section 7 (Validated Knowledge Sources)** at line 213 of `Candidate v0.1.2` strips `KS-003..KS-015` and Section 8 gaps from runtime context.
3. **Unintended fallback tools (`ST-04`):** When `Confluence Get Page` truncates (`PLAT-05`), CAPE attempted an unauthenticated `HTTP Request` and fell back to non-Eligible training pages. Adding an explicit tool-hygiene & non-Eligible fallback guard in Candidate v0.1.3 prevents both behaviors.
4. **Session isolation (`ST-02`):** Confirms again that testing inside a CAPE Project with `Project Memory` (`PLAT-04`) can bypass `Load Skill`, subtly weakening strict Deterministic Rule wording.
