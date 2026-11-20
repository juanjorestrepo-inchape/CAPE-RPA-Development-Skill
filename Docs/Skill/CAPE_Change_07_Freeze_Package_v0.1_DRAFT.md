# CAPE RPA Development Skill — Change 07 Pre-Freeze Verification & §9 Gate Package

**Document ID:** `CAPE-RPA-C07-FREEZE-001`
**Version:** v0.1 (`DRPA VERIFIED — READY FOR §9 FREEZE SIGN-OFF`)
**Date:** 20 November 2026
**Governing Protocol:** [`CAPE_Change_07_Efficiency_Protocol_v0.1.md`](CAPE_Change_07_Efficiency_Protocol_v0.1.md) (`v0.1-r2`)
**Companion Task Bank:** [`CAPE_Change_07_Task_Bank_v0.2_DRAFT.md`](CAPE_Change_07_Task_Bank_v0.2_DRAFT.md) (`10/10` matched pairs drafted)
**Execution Log Template:** [`Change_07_Execution_Log_TEMPLATE.csv`](Change_07_Execution_Log_TEMPLATE.csv) (`44` columns, validated by `scripts/cape_quality_gate.py score-c07`)

> **Governance Boundary:** This package prepares all nine §9 Execution Gate prerequisites and all twelve §10 open decisions (`C07-D01`–`C07-D12`) for rapid Project Owner (`DEC-C07-01`) and Test Lead sign-off. **Execution remains blocked until §9 is formally signed and frozen. Zero timing measurements have been executed; the ≥ 30% reduction remains an unmeasured target.**

---

## 1. Pre-Freeze Confluence Verification Checklist (`P04`–`P07` + `P01` v3 Check)

Pairs `P01`–`P03` and gap pairs `P08`–`P10` are already aligned to verified contracts (`v0.1` / `Q10`–`Q12` / `Q19`). Complete the five targeted Confluence checks below (~10 minutes total) to promote `CAPE_Change_07_Task_Bank_v0.2_DRAFT.md` to frozen `v0.2`:

| Check ID | Pair(s) | Target Governed Source(s) | Live DRPA Page ID & Version Observed (2026-11-19) | Exact Items to Verify in Confluence | Verified? |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **`CHK-01`** | `P01`, `P04` | `KS-006` (*RPA Project Intake Framework*) | DRPA `8848212048` (**v3**, `2026-10-29 15:46:49 UTC`) | Verified: Phase 3 requires Repository + PSC (DOCX); Phase 4 Scrum Master schedules kickoff, BA runs w/ PMO, developer submits Arch Review Form + presents Repository & PSC, Tier 1 & Tier 2 approvals; all 10 phases + full Phase 10 text (max 2 mo hypercare, KT ≥2 wks, standard/pragmatic closure, CICR) updated in Task Bank v0.2. | `[x]` |
| **`CHK-02`** | `P01`, `P04`, `P05` | `KS-007` (*RPA Architecture Review Framework*) | DRPA `8853815357` (**v8**, `2026-10-29 15:38:42 UTC`) | Verified: New projects + major enhancements scope, exclusions, PSC DOCX prerequisite, Steps 9a/9b + Tier 2 TDM Final Go + Section 9 Automation Summary (MS Forms → Email → MS Teams Approval); confirmed does not govern Phases 7–8 CAB. | `[x]` |
| **`CHK-03`** | `P05` | `KS-003` (*RPA Architecture — Overview*) | DRPA `9025257486` (**v3**, `2026-04-01 06:08:56 UTC`) | Verified: Tiers 1–3 & Cost-First Selection Principle (`Python/VBA → Power Platform → UiPath/C#`); confirmed zero Architecture Review triggers (100% complementary to `KS-007`). | `[x]` |
| **`CHK-04`** | `P06` | `KS-015` (*Critical Incident Playbook — RPA Team*) | DRPA `8219525716` (**v5**, `2025-11-04 05:55:32 UTC`) | Verified: 5 operational stages (Detect/Verify P0–P1, ManageEngine ticket, Mobilize TL IC + inform chain, INTERNAL Teams War Room w/ no stakeholders & 2h huddles, Triage & Contain + RCA in 3–5 business days); Supporting ceiling (`R13`) & Role Ambiguity preserved. | `[x]` |
| **`CHK-05`** | `P07` | `KS-005` (*RPA Architecture — Security*) & `KS-004` (*RPA Architecture — Functional*) | DRPA `9024078121` (**v4**, `2026-04-01 06:09:31 UTC`) & DRPA `9024241974` (**v4**, `2026-04-01 06:09:16 UTC`) | Verified: Both are component-by-component descriptions; `KS-005` Security Notes (PAM360/UiPath Credential Store, TLS 1.2/SFTP SSH, MFA/CAPTCHA P4, Data Policy) recorded; Azure Key Vault mentioned at high level only with zero implementation standards. | `[x]` |

---

## 2. Proposed Dispositions for All §10 Open Decisions (`C07-D01`–`C07-D12`)

Every pending decision from Protocol `v0.1-r2` §10 is pre-populated with a concrete, auditable proposal so the Project Owner and Test Lead can approve or adjust in a single review:

| Decision ID | Protocol Topic | Design Basis (2026-10-20) | Proposed Concrete Disposition for Freeze | Formal Status |
| :---: | :--- | :--- | :--- | :---: |
| **`C07-D01`** | Acceptance threshold | Approved by user | Ratify **≥ 6 / 8** binary rubric score, with **Correctness (Dim 1) = 1** and **Boundary Compliance (Dim 5) = 1** mandatory (§6.2). | `PENDING SIGN-OFF` |
| **`C07-D02`** | Critical-failure veto catalogue | Principle approved; catalogue pending | Ratify all five core veto categories **`C1`–`C5`** plus the five operational veto conditions drafted in Protocol §6.3 verbatim. Any `critical_failure = YES` vetoes acceptance regardless of total score. | `PENDING SIGN-OFF` |
| **`C07-D03`** | Time-limit treatment | Approved by user | Ratify **600-second (10-minute)** hard active-time cap; timeout recorded as `outcome = UNRESOLVED`, `termination_reason = TIME_LIMIT`, `active_time_seconds = 600`, zero imputation (§5.3). | `PENDING SIGN-OFF` |
| **`C07-D04`** | Interruption resumption window | Pending | Fix resumption window at **15 minutes** within the same working session. Interruptions ≤ 15 min pause the timer and are logged in `interruption_seconds`/`interruption_log`; interruptions > 15 min classify the run as `INTERRUPTED` (excluded and reported). | `PENDING SIGN-OFF` |
| **`C07-D05`** | Activation failures in primary analysis | Approved by user | Retain `ACTIVATION_FAILED` runs in the `CAPE` condition as observed (**intention-to-treat**, §5.5); never silently replace or drop failed activations. | `PENDING SIGN-OFF` |
| **`C07-D06`** | Condition order & session isolation | Principle approved; method pending | Adopt **50/50 counterbalanced order**: Odd pairs (`P01, P03, P05, P07, P09`) run `NO_CAPE` (1st) → `CAPE` (2nd); Even pairs (`P02, P04, P06, P08, P10`) run `CAPE` (1st) → `NO_CAPE` (2nd). **Mandatory session control:** All `CAPE` runs execute in clean standalone chats **outside any CAPE Project** to eliminate `PLAT-04` (`Project Memory` carryover). | `PENDING SIGN-OFF` |
| **`C07-D07`** | Permitted Confluence spaces & duplicate rule | Pending | Permitted `NO_CAPE` sources: Inchcape Confluence **`DRPA`** space (operational reference for pilot) and approved internal links referenced directly from governed pages; zero AI tools or SME help. **Duplicate rule:** Where a `DRPA` and `SOLDOC` pair exists (e.g., `KS-010` `7308640261` v11 vs. `8847753943` v5), `DRPA` is scored as the pilot reference copy and any `SOLDOC` citation must be flagged as non-canonical duplicate (preserving `DEP-08` governance caveat until formally closed by Source Owner). | `PENDING SIGN-OFF` |
| **`C07-D08`** | Task-pair equivalence | Approved by user | Adopt equivalent non-identical matched pairs (`CAPE_Change_07_Task_Bank_v0.2_DRAFT.md`, 10/10 pairs) with per-pair `task_difficulty` and `task_matching_rationale` recorded before execution. | `PENDING SIGN-OFF` |
| **`C07-D09`** | Sample size fallback | Pending | Target remains **`n = 10` matched pairs (20 runs)**, reported descriptively with explicit small-sample caveat (no inferential significance claims). Any reduction below 10 pairs requires written Project Owner deviation approval prior to analysis. | `PENDING SIGN-OFF` |
| **`C07-D10`** | Evidence storage, access & retention | Pending | Scored metadata CSV committed to `Docs/Skill/Change_07_Execution_Log_RUN1.csv` using non-sensitive IDs (`DEV-01`, `DEV-02`; zero credentials or confidential text). Raw transcripts/screenshots stored in controlled Inchcape Confluence/SharePoint pilot folder referenced by `evidence_location`, restricted to RPA CoE & Project Owner, retained for 12 months or until Phase 2 handover. | `PENDING SIGN-OFF` |
| **`C07-D11`** | Edge-case scoring rules | Consistent treatment approved; rules pending | Ratify Protocol §6.4 edge-case scoring table verbatim and apply identically across both `NO_CAPE` and `CAPE` conditions. | `PENDING SIGN-OFF` |
| **`C07-D12`** | Participant plan | Same-participant rule approved; plan pending | Same RPA developer completes both tasks within a pair. Target **1–2 Inchcape RPA developers** (`DEV-01` primary; `DEV-02` independent participant on ≥ 3 pairs where available) to mitigate single-author bias; experience band logged non-sensitively. | `PENDING SIGN-OFF` |

---

## 3. Protocol §9 Execution Gate Readiness Tracker (`1`–`9`)

| # | §9 Gate Requirement | Current Readiness | Remaining Action to Close |
| :---: | :--- | :---: | :--- |
| **1** | Ten task pairs and expected outcomes documented and reviewed | `VERIFIED (10/10)` | `CHK-01`–`CHK-05` verified against live DRPA (2026-11-20); ready for `Task Bank v0.2` sign-off. |
| **2** | Per-pair equivalence and matching rationale documented | `DRAFT READY (10/10)` | Approve rationales in `CAPE_Change_07_Task_Bank_v0.2_DRAFT.md`. |
| **3** | Condition order and carryover/familiarity limitations addressed | `PROPOSED READY` | Approve `C07-D06` (50/50 counterbalance + clean sessions outside Projects). |
| **4** | `NO_CAPE` and `CAPE` conditions, allowed spaces, prohibited assistance fixed | `PROPOSED READY` | Approve `C07-D07` permitted space list (`DRPA` pilot reference). |
| **5** | Duplicate/non-canonical/unresolved-identity treatment defined (`KS-010`) | `PROPOSED READY` | Approve `C07-D07` duplicate scoring rule (or record formal `DEP-08` closure). |
| **6** | Rubric dimensions, ≥ 6/8 threshold, `C1`–`C5` vetoes, and edge-case rules approved | `PROPOSED READY` | Ratify `C07-D01`, `C07-D02`, and `C07-D11`. |
| **7** | Data schema, evidence handling, access, retention, and analysis method approved | `PROPOSED READY` | Ratify `C07-D10`; CSV schema (`44` cols) & deterministic CLI (`score-c07`) already verified. |
| **8** | Protocol version frozen (version, commit hash, checksum) | `PENDING FREEZE` | Record frozen commit hash and SHA-256 digests in §4 below immediately after sign-off. |
| **9** | Project Owner / reviewer explicitly approves execution | `PENDING APPROVAL` | Record written sign-off from Nikko Gonzales (TDM / Project Sponsor) in §4 below. |

---

## 4. Formal §9 Freeze & Execution Authorization Record (`NOT YET SIGNED`)

> **Freeze Rule (§9.1):** Complete `CHK-01`–`CHK-05`, record the frozen commit hash and SHA-256 checksums below, and obtain written approval before creating `Docs/Skill/Change_07_Execution_Log_RUN1.csv` or starting the first timer.

| Freeze Field | Value |
| :--- | :--- |
| **Protocol Version Frozen** | `v0.1-r2` *(pending freeze)* |
| **Task Bank Version Frozen** | `v0.2` *(pending `CHK-01`–`CHK-05`)* |
| **Skill Version Under Test** | `[Active v0.1 FA84A451... OR frozen Candidate v0.1.2 — confirm at freeze]` |
| **Frozen Git Commit Hash** | `[Record commit hash at freeze]` |
| **Protocol File LF SHA-256** | `[Run cape_quality_gate / sha256 at freeze]` |
| **Task Bank File LF SHA-256** | `[Run cape_quality_gate / sha256 at freeze]` |
| **Project Owner / Approver** | `Nikko Gonzales (Technical Delivery Manager / Project Sponsor)` |
| **Test Lead / Executor(s)** | `Juan José Restrepo Rosero (DEV-01)` `[+ DEV-02 if available]` |
| **Approval Date & Reference** | `[YYYY-MM-DD — email / Teams / Jira reference]` |
| **Execution Gate State** | **`NOT CLEARED`** *(update to `CLEARED — APPROVED FOR EXECUTION` only when signed)* |
