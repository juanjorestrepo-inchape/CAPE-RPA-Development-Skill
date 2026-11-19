# CAPE RPA Development Skill — Execution Blueprint, Metrics Framework, Reporting Cadence & Optimization Playbook

**Document ID:** `CAPE-RPA-DEL-PLAYBOOK-001`
**Version:** v0.1 (`DRAFT — FOR OWNER & TECHNICAL REVIEW`)
**Date:** 19 November 2026
**Repository Baseline:** Branch `main` @ `2f81c0f` (with reconciled working-tree Owner Review Package v0.1.2)
**Governing Principle:** **Trust Before Breadth** — confidence must match evidence; speed never overrides accuracy or boundary honesty.

> **Governance Boundary:** This playbook consolidates engineering execution phases, KPIs, traceability, reporting templates, and optimization levers aligned with `engineering-lifecycle` (7-Stage Protocol), `rpa-development` CoE governance standards, and Q4 2026 objectives. It does **not** alter protected Skill files, clear the Coverage-Honesty Gate (`NOT CLEARED`), approve Change 05 (`PENDING IMPLEMENTATION`), approve Change 07 (`PROPOSED — PENDING APPROVAL`), or record measured efficiency results (`0` executions to date).

---

## 1. End-to-End Execution Phases (Mapped to 7-Stage Engineering Lifecycle & Q4 2026)

To close Q4 2026 without restarting Discovery or diluting governance rigor, remaining work is structured into **five incremental execution phases** anchored to the 7-Stage Engineering Lifecycle (`Discovery → Planning/ADR → Interface Design → Diátaxis Documentation → Clean Execution → Testing Pyramid → Deployment & Observability`):

```text
[Phase 1: Governance & Continuity Closure]  (Gates: Block A/B decisions, KS-010, E-23, E-20)
                    │
                    ▼
[Phase 2: Platform & Traceability Pre-Check] (Gates: CAPE 24k counter, SHA-256, connector schema)
                    │
                    ▼
[Phase 3: Frozen Regression & Meets Gate]   (Gates: Q11/Q12, Q10 routing, 11-case regression, Gate CLEARED)
                    │
                    ▼
[Phase 4: Change 07 Efficiency Benchmark]   (Gates: 10/10 Task Bank, §9 freeze, NO_CAPE vs CAPE runs)
                    │
                    ▼
[Phase 5: Q4 Closure & Phase 2 Handover]    (Gates: Meets/Exceeds Report, Change 05/06 scoped backlog)
```

| Execution Phase | Lifecycle Stage Alignment | Concrete Work Package | Primary Owners | Hard Exit Gate (Definition of Done) | Target Q4 Contribution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1 — Governance & Continuity Closure** | Stages 1–2 (Discovery Closure & ADRs) | Transfer missing files (`WORK PLAN NOV 9 2026.md`, `siete casos de regresión restantes.md`); close Block A (`DEC-PO-01`, `D-02`/`DEP-03`) & Block B (`KS-010` canonical ID `DEP-08`, `E-23` Page 7 §5.4 verification, `E-20` Hardening Spec §11, Request A `KS-007` V5). | Project Owner, Source Owners, Policy/Governance Owner | `DEP-08` resolved; `DEC-PO-01` signed; `E-23` verified or formally ratified; `G6` path unblocked. | Unblocks Meets & Exceeds scoring |
| **Phase 2 — Platform & Traceability Pre-Check** | Stage 3 (Contracts & Interface Verification) | Verify CAPE platform character-counting criterion against 24,000 limit; confirm deployed SHA-256 vs local repo; verify Confluence connector metadata fields for Change 04 (`P04-01`–`P04-08`); execute Requests B & C; run local `scripts/cape_quality_gate.py`. | CAPE Platform Owner, Skill Technical Owner, Security Owner | Verified CAPE character-count rule; runtime SHA-256 matched; security boundaries confirmed (`DEC-PLT-01`). | Prevents deployment rejection & untraceable runs |
| **Phase 3 — Frozen Regression & Coverage-Honesty Gate** | Stage 6 (Testing Pyramid — Functional & Boundary) | Execute controlled `Q11` & `Q12` runs and ordinary-prompt `Q10` routing check; freeze Candidate v0.1.2 (reconciled post-Block B); execute full 11-case regression + negative controls (`N1`–`N5`, `C1`–`C2`); agree authorized handling for 9 unpopulated questions. | Test Lead, Skill Technical Owner, RPA Developers | `4/4` Boundary Adherence PASS (`Q10, Q11, Q12, Q19`); zero critical fabrications; regression report signed; **Coverage-Honesty Gate `CLEARED`**. | **Delivers Q4 Meets (100%) & Exceeds #1 traceability** |
| **Phase 4 — Change 07 Efficiency Pilot** | Stage 6 (Benchmarking & Value Validation) | Review and verify Pairs 4–10 in [`CAPE_Change_07_Task_Bank_v0.2_DRAFT.md`](../../Docs/Skill/CAPE_Change_07_Task_Bank_v0.2_DRAFT.md); close Protocol `v0.1-r2` §9 checklist (permitted spaces, `C1`–`C5` vetoes, retention, condition order); freeze protocol; execute 10 matched pairs (20 runs: `NO_CAPE` vs `CAPE`); score via `scripts/cape_quality_gate.py score-c07`. | Test Lead, RPA Developers, Project Owner | Protocol §9 formally frozen; 20 executions logged in `Change_07_Execution_Log_TEMPLATE.csv`; quality-gated efficiency report generated. | **Evaluates Q4 Exceeds #2 (≥30% target)** |
| **Phase 5 — Q4 Pilot Closure & Tranche 2 Handover** | Stages 4 & 7 (Diátaxis Docs & Observability) | Compile Q4 Executive Closure Report & Sponsor Write-Up; separate Change 05 implementation (post-`G6`) and Change 06 into controlled post-pilot backlog; escalate `PLAT-01`/`PLAT-02` to CAPE platform backlog. | Project Owner, Skill Technical Owner, Authorized Change Owner | Signed Pilot Closure Report; explicit continuation/deployment disposition (`DEC-ACC-01`). | **Closes Q4 2026 Goal cleanly** |

---

## 2. Three-Layer KPI & Metrics Architecture

Every metric is anchored to the project's **Three-Layer Architecture** (`Capa A → Capa B → Capa C`) so operational speed never masks behavioral failure or platform defects.

### 2.1 Capa A — Behavioral & Governance Controls (Skill Quality)

| Metric ID | Metric Name | Formula / Definition | Target / Threshold | Data Source | Anti-Gaming Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`M-A1`** | **Coverage-Honesty Gate Verdict** | Categorical precedence: `FAILED` (any critical fabrication in `Q10/Q11/Q12/Q19`) > `NOT CLEARED` (incomplete, `PARTIAL`, `INCONCLUSIVE`, or non-critical `FAIL`) > `CLEARED` | **`CLEARED`** (4/4 Boundary Adherence PASS; 0 fabrications) | Formal Regression Scorecard + verbatim transcripts | Never average gate cases; a single fabrication fails the entire pilot. |
| **`M-A2`** | **Activation Precision & Recall** | Negative Rejection Rate = `Passed N1–N5 / 5`; Positive/Contextual Activation Rate = `Activated on RPA prompts / Total RPA prompts` | **100%** negative rejection; **≥90%** ordinary-prompt positive activation | Change 01 Activation Cycle + regression traces | Explicit `Load Skill` prompts cannot be counted as automatic routing proof. |
| **`M-A3`** | **Source Selection & Authority Compliance** | `% of test cases citing exact governed Primary/Supporting source without authority inflation` (esp. `KS-015` Supporting ceiling + Role Ambiguity; `KS-006` 10-phase exact order) | **100%** on `Q3`, `Q5`, `Q8`, `Q15`, `Q16` | Live Evaluation Scorecard & tool traces | Presenting `KS-015` as official Primary policy is an automatic Authority FAIL. |
| **`M-A4`** | **Claim-Level Grounding Rate** | `(Claims rated A [Fully Supported] + B [Partially Supported]) / Total substantive claims` (reported alongside `C` Unsupported and `D` Contradicted counts) | **≥95%** `(A+B)` and **0** `D` (Contradicted) claims | Claim-level audit matrix (Change 05 format) | Never hide a `D` contradiction (e.g., CAB before Dev) inside an aggregate score. |
| **`M-A5`** | **Provenance Metadata Completeness** | `% of Confluence-backed runs invoking Page Info and capturing verifiable Page ID, URL/space, Version, and Last-Modified without inference` | **100%** of Change 04 verification cases (`P04-01`–`P04-08`) | CAPE tool traces (`Confluence Page Info`) | Missing connector data = `NOT VERIFIABLE`, never `PASS`. |
| **`M-A6`** | **Skill Character-Budget Compliance** | Local LF/CRLF character count vs. 24,000-char CAPE ceiling + verified SHA-256 | **< 24,000** chars (recommended safety buffer: **≤ 23,500** chars) | `scripts/cape_quality_gate.py check-skill` + CAPE verification | Local count is provisional until CAPE's own counter is confirmed (`DEC-PLT-01`). |

### 2.2 Capa B — Pilot Validation & Coverage Completeness (Q4 Meets)

| Metric ID | Metric Name | Formula / Definition | Target / Threshold | Reporting Rule |
| :--- | :--- | :--- | :--- | :--- |
| **`M-B1`** | **Dependency-Complete Behavioral Pass Rate** | `Cases Passing all mandatory criteria / 11` (`Q1, Q3, Q5, Q6, Q8, Q10, Q11, Q12, Q15, Q16, Q19`) | **≥ 90%** (≥10/11) with **100%** on Group C gate (`Q10, Q11, Q12, Q19`) | Report exact pass/partial/fail/inconclusive breakdown per question. |
| **`M-B2`** | **20-Question Scope Transparency** | Explicit accounting of `11` evaluated + `9` unpopulated-source cases (`Q2, Q4, Q7, Q9, Q13, Q14, Q17, Q18, Q20`) | **100% documented disposition** (no silent omissions) | Never extrapolate 11-question pass rate as 20-question completion. |
| **`M-B3`** | **Verified Evidence-Based Improvements Count** | Count of Skill-level changes linked end-to-end: `Pilot Finding → Scoped Instruction Change → Regression Verification` | **≥ 3** verified improvements (Q4 Exceeds #1) | Documentary typos, commit-hash fixes, and README edits **do not count**. |
| **`M-B4`** | **Developer Perceived Utility & Manual Follow-Up Rate** | Median usefulness (`1–5` Likert scale) and `% of valid answers where developer still had to manually search Confluence` | Median **≥ 4.0 / 5.0**; Manual follow-up **≤ 25%** | Qualitative/operational indicator; reported separately from accuracy. |

### 2.3 Capa C — Developer Efficiency & Value Quantification (Q4 Exceeds — Change 07)

| Metric ID | Metric Name | Exact Formula | Target / Threshold | Mandatory Guardrails (`Protocol v0.1-r2`) |
| :--- | :--- | :--- | :--- | :--- |
| **`M-C1`** | **Primary Efficiency Reduction (Total Active Time)** | `((Total NO_CAPE active time − Total CAPE active time) / Total NO_CAPE active time) × 100` | **≥ 30%** target *(currently 0 runs — NOT MEASURED)* | Valid comparable pairs only; 600s cap (`UNRESOLVED` kept at 600s); zero-denominator guard; **invalid unless quality gate passes**. |
| **`M-C2`** | **Median Resolution-Time Reduction** | `((Median NO_CAPE active time − Median CAPE active time) / Median NO_CAPE active time) × 100` | Reported side-by-side with `M-C1` (robust against outliers) | Computed over identical valid comparable pair set via `scripts/cape_quality_gate.py score-c07`. |
| **`M-C3`** | **Change 07 Answer-Quality Acceptance Rate** | `Executions scoring ≥ 6/8 with Correctness=1, Boundary=1, and Critical_Failure=NO / Total scored executions` | CAPE acceptance rate **≥ NO_CAPE** acceptance rate (zero quality regression) | Reported **separately** from speed (`Protocol v0.1-r2 §6.5`). |
| **`M-C4`** | **Rework & Activation-Failure Rate** | `Rework executions / Total valid CAPE runs` and `ACTIVATION_FAILED / Total CAPE attempts` | Tracked & disclosed transparently (**0** silent exclusions) | Rework time is **included** in `active_time_seconds`; activation failures are data. |
| **`M-C5`** | **Platform Friction Rate (Non-Skill)** | Count of `INTERRUPTED` / `TOOL_FAILURE` events caused by CAPE session timeout, context errors, or table parsing (`PLAT-01`, `PLAT-02`) | Logged separately from Skill performance | Escalated to CAPE Platform Owner; never blamed on or masked by Skill edits. |

---

## 3. Finding → Improvement → Verification Traceability Matrix

Closes the traceability gap identified in [`02_Hardening_Consolidation_Review_v0.1.md`](../../05_Next_Steps/02_Hardening_Consolidation_Review_v0.1.md) §5 (*Meets 3* & *Exceeds 1*):

| Trace ID | Pilot Finding / Failure Mode | Root-Cause Artifact | Scoped Skill Intervention | Before Evidence | After Evidence | Counts Toward Exceeds #1 (≥3)? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`TR-01`** | Skill failed to distinguish generic technical prompts from contextual Inchcape RPA prompts | Initial Pilot Testing | **Change 01:** Contextual activation rules & Activation Routing Guard (§2) | Early activation misses / ambiguity | `N1`–`N5` PASS, `C1`–`C2` PASS (`CAPE_Change_01_Activation_Test_Cycle.md`) | **Candidate #1** *(pending positive ordinary-prompt regression)* |
| **`TR-02`** | Skill fabricated AutoDrive Python standards on `Q10` (`KG-001`) and invented ungrounded follow-up paths on `Q12`/`Q19` | `CAPE_Testing_Results_Follow_Up.md` §4 & `Change 02` | **Change 02 & 02.1:** Strict Evidence-Boundary Enforcement §4.1 & Deterministic Follow-Up Rule | Historical `Q10` FAIL; `Q12`/`Q19` PARTIAL | `Q10` (2026-10-02) Skill-level PASS; `Q19` Focused PASS | **Candidate #2** *(pending `Q11`/`Q12` & Gate `CLEARED`)* |
| **`TR-03`** | `Q3` merged/omitted KS-006 phases (7 generic stages instead of 10) and misattributed CAB prerequisites to KS-007 | Stage A `Q3` FAIL (`CAPE_Testing_Results_Follow_Up.md` §14) | **Change 03:** Explicit 10-phase KS-006 acceptance criteria & KS-007 scope boundary (§4.2) | Stage A `Q3` FAIL — Lifecycle Accuracy | Focused `Q3` PASS (2026-10-14): all 10 phases ordered, Internal/Global CAB separate | **Candidate #3** *(strongest verified before/after; pending frozen regression)* |
| **`TR-04`** | Retrieved Confluence pages lacked page ID/version/space provenance and risked collapsing DRPA/SOLDOC duplicates | Step 2 tool-trace audit (`P04-01`/`P04-02`) | **Change 04:** `Confluence Page Info` instruction & non-DRPA duplicate detection (§4.3, `b22d09c`) | No Page Info metadata capture | `Q5` (KS-010, 2026-10-19) Focused PASS (`P04-01`–`P04-08`) exposing DRPA vs SOLDOC copies | **Candidate #4** *(pending remaining 6 Change 04 cases & `KS-010` reconciliation)* |
| **`TR-05`** | `Q1 V2` reversed lifecycle order (CAB before Dev) and blended supported facts with unsupported timing | `Change_05_Evidence_Annex_Q1_Q1V2_v0.1.1.md` (`2f81c0f`) | **Change 05 (Proposed):** Temporal grounding, claim decomposition & version provenance (`C05-01`–`C05-04`) | `Q1 V2` retrospective FAIL (`Q1V2-04b`, `Q1V2-05b`) | None — `PENDING IMPLEMENTATION` (blocked by `G6`/`E-23`) | **Not yet countable** |
| **`TR-DOC`** | Editorial/documentation repairs (`b22d09c` hash fix, `F-01`–`F-05`, `R1`–`R8`, Owner Review reconciliation) | Audit passes | Documentation-only corrections | N/A | Verified via local checks | **EXPLICITLY EXCLUDED** *(never counted as Skill improvements)* |

---

## 4. Reporting Architecture & Cadence (Diátaxis + RACI)

To eliminate ad-hoc status summaries and prevent conflating drafts with formal approvals, reporting follows four standardized outputs:

| Report Artifact | Audience | Cadence / Trigger | Governing Template / Contents | Mandatory Disclaimer |
| :--- | :--- | :--- | :--- | :--- |
| **1. Hardening & Blocker Standup Digest** | Skill Technical Owner, Test Lead, RPA CoE | Weekly during Iteration 2 | Delta on `BLK-01`–`BLK-07`, `DEP-01`–`DEP-10`, SHA-256 of active/candidate Skill, open domain-owner requests (`Requests A/B/C`). | Explicitly separates `Verified` vs `Pending owner confirmation`. |
| **2. Formal Regression & Coverage-Honesty Gate Report** | Project Owner, RPA CoE, Governance | At completion of Phase 3 frozen regression | Skill SHA-256, `M-A1`–`M-A6`, `M-B1`–`M-B4`, verbatim transcripts, `FAILED`/`NOT CLEARED`/`CLEARED` gate verdict, 9-question dependency disclosure. | Preserves prior historical FAILs alongside new PASS runs. |
| **3. Change 07 Efficiency & Value Report** | Project Sponsor (Nikko), Project Owner, RPA Developers | At completion of Phase 4 (`20` runs) | Output JSON/table from `scripts/cape_quality_gate.py score-c07`: `M-C1` (total %), `M-C2` (median %), pair-by-pair times, `M-C3` quality acceptance, `M-C4` rework/activation failures, `M-C5` platform interruptions, `n=10` sample limits. | Never claims ≥30% without quality-gated empirical logs. |
| **4. Q4 2026 Goal Closure & Executive Write-Up** | Leadership / Performance Review (Nikko Gonzales & Juan José Restrepo) | Q4 2026 Close (Phase 5) | Structured directly around **Meets (1–3)** and **Exceeds (1–2)** with verifiable artifact links, exact measured numbers, honest limits, and Phase 2 recommendations. | Distinguishes achieved results from deferred Phase 2 items. |

### 4.1 Q4 2026 Executive Write-Up Template (Ready for Evidence Population)

```markdown
### Q4 2026 Goal Outcome — Develop and Validate the CAPE RPA Development Skill

- **Approach:** Applied "Trust Before Breadth" across a governed 20-source pilot scope (7 populated Eligible sources, 8 domains, 5 intents, 4 load-bearing boundary tests).
- **Meets — Live Pilot Validation & Honesty:**
  - Frozen Skill artifact: `[File + SHA-256 + verified char count]`
  - Behavioral pass rate (11-case dependency-complete subset): `[X / 11 (Y%)]`
  - Coverage-Honesty Gate (`Q10, Q11, Q12, Q19`): `[CLEARED / NOT CLEARED — exact counts]`
  - Documented findings & Phase 2 recommendations: `[Links to Closure Report & Owner Review Package]`
- **Exceeds — Evidence-Based Improvements (Target: ≥ 3):**
  - `[List only verified TR-01..TR-04 improvements with before/after regression evidence]`
- **Exceeds — Knowledge-Retrieval Efficiency (Target: ≥ 30% reduction):**
  - Protocol: Change 07 `v0.1-r2` (`[N]` valid matched pairs / `[2N]` executions)
  - Total active-time reduction (`M-C1`): `[X.X%]` | Median active-time reduction (`M-C2`): `[Y.Y%]`
  - Quality acceptance (`M-C3`): `CAPE [A%] vs NO_CAPE [B%]` | Activation failures (`M-C4`): `[k]`
  - Sample & platform caveats: `[n=10 descriptive scope; CAPE platform issues tracked separately]`
```

---

## 5. Engineering Optimizations & Future Architectural Roadmap

### 5.1 Permitted Pilot Optimizations (Strictly Within Context-Based Skill Scope)

These optimizations respect the **24,000-character limit** and require **zero external infrastructure**:

1. **Character-Budget & Token Economy Engineering (Target: ≤ 22,500 LF chars):**
   - Current Candidate v0.1.2 sits at **`23,435` LF chars** (`565` chars of margin under 24,000 — high risk if CAPE counts UTF-8 bytes or CRLF, which is `23,726` chars).
   - *Optimization (post-Block B approval):* Consolidate repeated caveat prose across §§4–6 into a single canonical rule block (saving an estimated 800–1,200 characters), creating safe headroom for future Change 05 instructions without truncating mandatory governance rules.
2. **Tool-Call Efficiency Hygiene (Closing `Q5` Redundancy):**
   - In the `Q5` trace (`CAPE_Testing_Results_Follow_Up.md` §21), CAPE issued **11 tool calls** including a redundant `Confluence Page Info` call on the same SOLDOC page (`8847753943`), adding avoidable latency that will directly hurt Change 07 active time.
   - *Optimization (post-regression candidate):* Add a one-line deterministic tool-call hygiene rule in §4.3: *"Call `Confluence Page Info` at most once per unique `page_id` per turn; reuse captured metadata."*
3. **Automated Local CI / Quality Gate (`scripts/cape_quality_gate.py`):**
   - Eliminates manual counting mistakes (such as the earlier byte-vs-character audit error) and enforces automated SHA-256 tracking, Markdown structural integrity (`G9`), and deterministic Change 07 scoring (`M-C1`–`M-C5`) with zero external dependencies.
4. **Structured Response Skeleton for Fast Developer Scanning:**
   - Align Skill output format with Diátaxis (concise *Direct Answer* → *Governed Source & Role* → *Provisional / Limitation Caveat*), reducing developer reading and verification time during Change 07 without sacrificing provenance rigor.

### 5.2 Quarantined Phase 2 / Tranche 2 Architectural Evolution *(Explicitly Out of Pilot Scope)*

Recorded strictly as **recommendations for post-pilot Phase 2** (never implemented during the current context-based pilot):

- **Populate Remaining 13 Pilot Sources + Resolve `KG-001`/`KG-002`/`KG-003`:** Author or revalidate AutoDrive coding standards (`KG-001`), UiPath REFramework/Best Practices (`KG-002`), Logging/Exception standards (`Q12`), and DRPA vs. SOLDOC governance (`KG-003`) before expanding Skill breadth.
- **Modular Multi-Skill Decomposition in CAPE:** Because CAPE loads Skills on demand from a budgeted index (`06_CAPE_First_Party_Technical_Reference_v0_1.md`), once governed sources exceed the 24,000-character ceiling, split into bounded sub-skills (e.g., *RPA Governance & Intake Skill*, *RPA Security & Architecture Skill*, *RPA Platform Standards Skill*) rather than bloating a single prompt.
- **CAPE Platform Co-Engineering (Databricks Apps / Lakebase):** Partner with the CAPE platform team to expose structured connector metadata (page ID, space key, version) natively in tool outputs (reducing Change 04 round-trips), stabilize session persistence (`PLAT-01`), improve table parsing (`PLAT-02`), and expose native telemetry exports (resolving `E-10`/`E-14` auditability gaps).
