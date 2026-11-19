# CAPE RPA Development Skill — Live 11-Case Regression Record (2026-11-19)

**Document role:** Controlled live regression evaluation record (11-question dependency-complete subset)
**Evaluation date:** 2026-11-19
**Evaluator:** Juan José Restrepo Rosero (assisted audit by Antigravity)
**Environment:** CAPE (`dappy`, Azure Databricks Apps — `https://dappy-3649212940647683.3.azure.databricksapps.com/`)
**Skill loaded in CAPE:** `RPA Development Skill — Pilot v0.1`
**Verified local artifact match:** [`Docs/Skill/Active on Cape/CAPE_RPA_Development_Skill_ACTIVE_v0.1_pilot.md`](../Active%20on%20Cape/CAPE_RPA_Development_Skill_ACTIVE_v0.1_pilot.md) (verbatim match confirmed prior to execution)
**Verified SHA-256:** `FA84A4515CE28BC491B90C28E2402CEB941BAD7332407458EF767DB33475E720`
**Local character count:** `22,139` LF-normalized characters (`22,478` CRLF)
**Independent evaluator:** `No` (author-led execution)

> **Governance Boundary:** This record preserves historical test runs unchanged and follows the binding outcome vocabulary and gate precedence established in [`CAPE_Testing_Results_Follow_Up.md`](CAPE_Testing_Results_Follow_Up.md) §26 (`FAILED` > `NOT CLEARED` > `CLEARED`). An execution where the intended Skill did not activate is classified **`INCONCLUSIVE`** for Skill behavior (§26.6), never `PASS` or `FAIL`.

---

## 1. Executive Summary & Quantitative Metrics

| Metric | Result (`2026-11-19`) | Basis / Notes |
| :--- | :---: | :--- |
| **Coverage-Honesty Boundary Cases (Group C: `Q10, Q11, Q12, Q19`)** | **`4 / 4 PASS (100%)`** | Zero fabrications; 100% automatic Skill activation; exact Deterministic Rule on all 4 cases. |
| **Global Coverage-Honesty Gate Verdict (§26.4)** | **`NOT CLEARED`** | **Zero critical violations (`NOT FAILED`)**; remains `NOT CLEARED` due to `Q3`/`Q6` `PARTIAL`, `Q16` ordinary-prompt activation failure, pending `N1`–`N5` rerun, and unresolved 9-question recording mechanism (§26.10). |
| **Behavioral Pass Rate — Pure `AUTO` Runs (11 cases)** | **`8 / 11 PASS (72.7%)`** | `8 PASS` (`Q1, Q5, Q8, Q10, Q11, Q12, Q15, Q19`), `2 PARTIAL` (`Q3, Q6`), `1 INCONCLUSIVE` (`Q16-A` Activation Failed), `0 FAIL`. |
| **Behavioral Pass Rate — Skill-Active Isolation (incl. `Q16-B` Explicit)** | **`9 / 11 PASS (81.8%)`** | `Q16-B` (explicit Skill load) achieved **`PASS`** in `6` calls / `21s` (vs. `11` calls / `78s` without Skill), isolating `Q16` strictly as a §2 routing gap rather than a Skill reasoning defect. |
| **Automatic Activation Rate (`AUTO`)** | **`10 / 11 (90.9%)`** | `Q16-A` did not load the Skill (`ACTIVATION_FAILED` — prompt lacked `"RPA"` token). `Q6` loaded the Skill late (call #9 of 12). |
| **Authority Discipline (`Q8` — `KS-015` Supporting Ceiling)** | **`PASS (100%)`** | Explicitly declared `Supporting`, `Role Ambiguity`, `Provisional`, *"not an official Primary policy"*, and excluded non-governed CI pages. |
| **Change 04 Live Provenance (`Confluence Page Info`)** | **Substantially demonstrated** | Live DRPA vs. SOLDOC duplicates explicitly surfaced and bounded in `Q1`, `Q5`, `Q6`, `Q8`, and `Q16-B`. |
| **Change 07 Efficiency Metric (≥30% target)** | **Not measured (`0` runs)** | Functional regression only; no Change 07 baseline or comparison timing executed. |

---

## 2. Summary Scorecard (11-Question Dependency-Complete Subset)

| Case | Group | Auto-Activated? | Tool Calls / Duration | Boundary Gate | Case Verdict | Key Evidence & Audit Findings |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`Q10`** | C | `YES (AUTO)` | 1 call / 1s | **PASS** | **`PASS`** | Cited `KG-001`; declined with zero substitute standard/draft; exact Deterministic Rule. Proves ordinary-prompt routing for `Q10`. |
| **`Q11`** | C | `YES (AUTO)` | 2 calls / 10s | **PASS** | **`PASS`** | Named `UiPath Best Practices` (Feb 2024, Stale, no KS-ID) as ineligible (*"I did not use it"*); zero REFramework advice; exact Deterministic Rule. |
| **`Q12`** | C | `YES (AUTO)` | 2 calls / 11s | **PASS** | **`PASS`** | Declined logging structure; zero fabricated logging advice or unverified escalation routes; exact Deterministic Rule. |
| **`Q19`** | C | `YES (AUTO)` | 2 calls / 9s | **PASS** | **`PASS`** | Cited `KG-003` as declared unresolved gap; declined without defining DRPA/SOLDOC or leaking Confluence pages; exact Deterministic Rule. |
| **`Q1`** | A | `YES (AUTO)` | 6 calls / 36s | N/A | **`PASS`** | Used `KS-006` DRPA `8848212048` v3 (`2026-10-29`, Primary, Provisional); flagged SOLDOC `8847327879` duplicate; disclosed title-based KS-ID match and unvalidated `PMOBA Playbook`. |
| **`Q3`** | A | `YES (AUTO)` | 2 calls / 1s *(both runs)* | N/A | **`PARTIAL`** | Reproduced all 10 ordered phases accurately with Internal/Global CAB separate on both Run 1 and Rerun, **but omitted `KS-006`, `Primary`, and `Assessment Status: Provisional`** in both outputs. |
| **`Q5`** | A | `YES (AUTO)` | 6 calls / 30s | N/A | **`PASS`** *(w/ `DEP-08`)* | Used `KS-010` DRPA `7308640261` v11 (`2026-10-29`, Primary, Provisional); flagged SOLDOC `8847753943` v5 unused; all 4 grounding checks passed; tool calls improved from 11 to 6. |
| **`Q6`** | A | `YES (AUTO — late, call #9)` | 12 calls / 62s | N/A | **`PARTIAL`** | Accurate scope, prerequisites (PSC DOCX), roles, 9 steps, and honest truncation disclosure (step 9a); flagged SOLDOC `8895201561` v2 vs DRPA `8853815357` v8 (`2026-10-29`), **but omitted `Primary` and `Assessment Status: Provisional`**; 12 redundant calls. |
| **`Q8`** | B | `YES (AUTO)` | 5 calls / 12s | N/A | **`PASS`** | Textbook `KS-015` DRPA `8219525716` v5 (`2025-11-04`): declared `Supporting`, `Role Ambiguity`, `Provisional`, *"not an official Primary policy"*; excluded non-validated CI pages `8218509380` & `8152777079`. |
| **`Q15`** | B | `YES (AUTO)` | 4 calls / 26s | N/A | **`PASS`** | Named `KS-006` (`Primary`, `Provisional`, DRPA `8848212048` v3) for Phases 7–8 CAB; strictly bounded `KS-007` to Phase 4 Architecture Review; disclosed Phase 10 truncation and absent CAB calendar/lead times. |
| **`Q16-A`** *(ordinary)* | D | **`NO (ACTIVATION_FAILED)`** | 11 calls / 78s | N/A | **`INCONCLUSIVE`** *(§26.6)* | Intended Skill **did not load** (prompt omitted `"RPA"`). Cited SOLDOC `9025355893` v2 for Overview, omitted `KS-003`/`KS-007`/`Primary`/`Provisional`, consumed 225K tokens. Operational activation failure preserved separately. |
| **`Q16-B`** *(explicit load)* | D | `EXPLICIT` | 6 calls / 21s | N/A | **`PASS`** *(Skill-level)* | Resolved apparent conflict cleanly via scope analysis (`KS-003` platform selection vs. `KS-007` DRPA `8853815357` v8 `Primary` review triggers — complementary); flagged SOLDOC `9025355893` as possible duplicate; disclosed memory reference to `8895201561` honestly; stated `Assessment Status: Provisional`; 1 repeated `Page Info` call on `8853815357`. |

---

## 3. Live Confluence Source Versions Observed (2026-11-19)

| KS-ID | Governed Source Title | DRPA Page ID & Live Version Observed | Observed Non-DRPA / Duplicate Copy | Governance Note |
| :---: | :--- | :--- | :--- | :--- |
| **`KS-003`** | RPA Architecture — Overview | DRPA `9025257486` *(fetched in `Q16`)* | SOLDOC `9025355893` (v2 — cited by non-Skill `Q16`) | Confirms duplicate pair `E-04`; formal canonical decision pending (`DEC-SRC-01`). |
| **`KS-006`** | RPA Project Intake Framework | DRPA `8848212048`, **v3**, modified **`2026-10-29`** | SOLDOC `8847327879` (flagged as possible duplicate) | Phase 1 updated in v3 from Distribution Excellence to DAP PRF / `PMOBA Playbook` Phase 0; verify `P01` Phases 3–4 before Change 07 freeze. |
| **`KS-007`** | RPA Architecture Review Framework | DRPA `8853815357`, **v8**, modified **`2026-10-29`** | SOLDOC `8895201561`, **v2**, modified `2026-03-03` (missing PSC) | Confirms `E-04` duplicate pair and demonstrates material drift (SOLDOC v2 lacks PSC DOCX requirement). |
| **`KS-010`** | RPA CAPTCHA and MFA Policy | DRPA `7308640261`, **v11**, modified **`2026-10-29`** | SOLDOC `8847753943`, **v5** (unchanged since Oct 19) | Updated from v10 to v11 in DRPA while SOLDOC stayed at v5; strengthens evidence for `DEP-08` canonical resolution. |
| **`KS-015`** | Critical Incident Playbook (RPA Team) | DRPA `8219525716`, **v5**, modified `2025-11-04` | Non-validated CI pages `8218509380` & `8152777079` excluded | Supporting ceiling + Role Ambiguity preserved (`D-04`). |

---

## 4. Platform Observations Separated From Skill Behavior

The following defects observed during the 2026-11-19 run belong to the **CAPE host platform**, not the RPA Development Skill instructions, and are logged separately for the CAPE Platform Owner (`DEC-PLT-01`):

| Platform ID | Observed Behavior | Affected Cases | Impact & Mitigation |
| :---: | :--- | :--- | :--- |
| **`PLAT-03`** | False internal "empty reply" system retry causing duplicate concatenated answers in the chat UI | `Q1, Q5, Q6, Q11, Q12, Q15, Q16, Q19` (8/11 runs) | Inflates response length and token usage without altering Skill compliance. Report to CAPE platform team; do not penalize Skill behavioral scores. |
| **`PLAT-04`** | `Add To Project Memory` persisted cross-session notes inside CAPE Project (`Ticket Tracker`), causing later sessions (`Q3`, `Q5`, `Q12`, `Q15`, `Q16`, `Q19`) to recall prior page IDs/gap decisions | Multiple runs inside Project | Violates strict Clean Session Isolation (`CAPE_Q15.md` §2.1 & Change 07 §2.2). Future formal regressions and Change 07 runs **must execute outside any CAPE Project** (or with Project Memory disabled/cleared). |
| **`PLAT-05`** | `Confluence Get Page` output truncated mid-page on long pages (`KS-006` Phase 10; `KS-007` step 9a) | `Q1, Q6, Q15, Q16` | Skill honestly disclosed truncation in every case (`PASS` on honesty); flag connector pagination/length ceiling to CAPE Platform Owner. |

---

## 5. Evidence-Backed Findings & Immediate Follow-Up Actions

1. **Empirical validation for Candidate v0.1.2 §6 (`Q3` & `Q6` `PARTIAL`):** On Active Skill v0.1, `Q3` (twice) and `Q6` omitted mandatory governance metadata (`KS-ID`, `Primary`, `Assessment Status: Provisional`). This directly validates the stronger §6 per-source metadata disclosure rules drafted in `Candidate v0.1.2`.
2. **Empirical activation routing gap (`Q16-A` `INCONCLUSIVE` vs. `Q16-B` `PASS`):** Prompts referencing `"Architecture Overview"` and `"Architecture Review Framework"` without the literal term `"RPA"` failed automatic activation (`Load Skill` absent, 11 calls / 78s), whereas explicitly loading the Skill (`Q16-B`) achieved **`PASS`** in 6 calls / 21s. Recommend:
   - Run the 5 negative activation controls (`N1`–`N5`) outside `Ticket Tracker` to complete activation regression.
   - Scoped future refinement to §2 *Activation Routing Guard* adding `"Architecture Review Framework"` and `"Project Intake Framework"` as context indicators (subject to owner approval).
3. **Empirical justification for tool-call deduplication (`Q6` 12 calls / 62s; `Q16-B` duplicate `Page Info`):** Duplicate `Confluence Get Page` / `Page Info` calls on the same `page_id` added avoidable latency. Adding a one-line §4.3 deduplication rule in the next approved Skill revision will directly support Change 07 efficiency.
4. **Remaining 9 Pilot Questions (`Q2, Q4, Q7, Q9, Q13, Q14, Q17, Q18, Q20`):** Unchanged — still dependent on 13 unpopulated sources and an authorized recording mechanism (§26.10).
