# CAPE RPA Development Skill — Change 07 Task Bank v0.2 (Expanded 10-Pair Draft)

**Draft date:** 19 November 2026 *(DRPA Confluence verification completed 20 November 2026)*
**Status:** `VERIFIED DRAFT — READY FOR OWNER & TEST LEAD §9 FREEZE SIGN-OFF (NOT YET FROZEN)`
**Supersedes (upon approval only):** [`CAPE_Change_07_Task_Bank_v0.1.md`](CAPE_Change_07_Task_Bank_v0.1.md) *(retained unchanged as prior 3-pair baseline)*
**Governing protocol:** [`CAPE_Change_07_Efficiency_Protocol_v0.1.md`](CAPE_Change_07_Efficiency_Protocol_v0.1.md) (`v0.1-r2`)
**Execution log template:** [`Change_07_Execution_Log_TEMPLATE.csv`](Change_07_Execution_Log_TEMPLATE.csv)

> **Governance & Verification Notice:** This draft completes the target **10 matched pairs / 20 executions** and adds the mandatory `task_difficulty` and `task_matching_rationale` fields required by Protocol `v0.1-r2` §2.2, §7.1, and §9 (Checklist items 1–2). **Zero measurements have been executed.** Pairs `P01`–`P03` preserve the validated key points from `v0.1` (`P02` remains gated by `KS-010` canonical identity `DEP-08`). Pairs `P04`–`P10` are grounded strictly in the pilot's 7 populated sources and 4 boundary gaps, and require Confluence source-point verification and formal approval before protocol freeze.

---

## 1. Ten-Pair Design Summary & Coverage Matrix

| Pair ID | Domain | Primary Intent | Governed Source / Boundary | Difficulty | Condition A (`NO_CAPE`) | Condition B (`CAPE`) | Verification Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| **`P01`** | Delivery Lifecycle | How-to | `KS-006` / `KS-007` | Medium | Pre-development preparation & kickoff review | Post-discovery remaining steps & gate | Verified vs `KS-006` v3 & `KS-007` v8 (2026-11-20) |
| **`P02`** | Security / Policy | Policy / Standard | `KS-010` | Medium | Priority, SLA, manual handoff & comms on CAPTCHA/MFA | Business request to bypass MFA / log defect | Confirmed vs `KS-010` DRPA (`v0.1`); **gated by `DEP-08`** |
| **`P03`** | Coding Standards (Gap) | How-to / Boundary | `KG-001` (AutoDrive gap) | Low-Medium | Find & summarize Inchcape AutoDrive coding standards | Ask what validated AutoDrive standards apply | Confirmed boundary gap (`v0.1`) |
| **`P04`** | Delivery Lifecycle | Reference / Explanation | `KS-006` / `KS-007` | Medium | Full 10-phase sequence & Internal vs Global CAB | Post-development progression through BAU handover | Verified vs `KS-006` v3 (`8848212048`) & `KS-007` v8 (2026-11-20) |
| **`P05`** | Architecture & Precedence | Selection / Decision | `KS-003` / `KS-007` | High | Resolve apparent conflict: platform choice vs review gate | Which source governs platform tier vs review prerequisite | Verified vs `KS-003` v3 (`9025257486`) & `KS-007` v8 (2026-11-20) |
| **`P06`** | Operations / Incident | Troubleshooting / Authority | `KS-015` (Supporting; Role Ambiguity) | High | Critical bot incident playbook & policy authority check | Escalating critical bot outage using KS-015 boundaries | Verified vs `KS-015` v5 (`8219525716`, 2026-11-20) |
| **`P07`** | Architecture — Security & Functional | Policy / Reference | `KS-005` / `KS-004` | Medium | Documented RPA security controls & functional roles | Security vs functional scope & Azure Key Vault gap | Verified vs `KS-005` v4 (`9024078121`) & `KS-004` v4 (`9024241974`, 2026-11-20) |
| **`P08`** | Platform Practices (Stale Gap) | How-to / Boundary | `UiPath Best Practices` (Stale, Feb 2024, no KS-ID) | Medium | Find validated Inchcape UiPath REFramework practices | Ask for governed UiPath REFramework standards | `DRAFT — Boundary gap (confirm against Q11 contract)` |
| **`P09`** | Engineering Standards (Gap) | How-to / Boundary | Uncovered Logging/Exception domain (`Q12`) | Low-Medium | Locate Inchcape bot logging & exception structure standard | Ask how to structure bot logging per Inchcape standard | `DRAFT — Boundary gap (confirm against Q12 contract)` |
| **`P10`** | Governance Taxonomy (Gap) | Reference / Boundary | `KG-003` (`DRPA` vs `SOLDOC`) | Medium | Determine governed distinction between DRPA and SOLDOC | Ask where to publish docs: DRPA vs SOLDOC boundary | `DRAFT — Boundary gap (confirm against Q19 contract)` |

**Balanced Coverage Verification:**
- **6 Populated-Source Pairs** (`P01`, `P02`, `P04`, `P05`, `P06`, `P07`) spanning all 7 populated pilot sources (`KS-003`, `KS-004`, `KS-005`, `KS-006`, `KS-007`, `KS-010`, `KS-015`).
- **4 Coverage-Gap / Boundary Pairs** (`P03`, `P08`, `P09`, `P10`) covering all 4 mandatory Coverage-Honesty Gate domains (`Q10`/`KG-001`, `Q11`/Stale UiPath, `Q12`/Logging gap, `Q19`/`KG-003`).
- **Recommended Condition-Order Counterbalancing (for §9 approval):** Pairs `P01, P03, P05, P07, P09` execute `NO_CAPE` first → `CAPE` second; Pairs `P02, P04, P06, P08, P10` execute `CAPE` first → `NO_CAPE` second (50/50 split controlling within-participant learning/carryover bias).

---

## 2. Detailed Pair Specifications (`P01`–`P10`)

### Pair `P01` — Lifecycle and Pre-Development Gate (`KS-006` / `KS-007`)

- **`task_difficulty`:** `Medium`
- **`task_matching_rationale`:** Both tasks belong to the *Delivery Lifecycle* domain with *How-to* intent, require consulting `KS-006` Phases 3–4 (and complementary `KS-007` review scope), and expect identical key points (Project Repository creation, Scrum Master kickoff scheduling, Architecture Review presentation, approval/revision loop before Phase 5 Development). Non-identical prompts prevent verbatim memory carryover while maintaining equivalent search complexity.
- **Task A (`NO_CAPE`):** *"What does a developer need to prepare and present before an RPA project can move into the Development phase at Inchcape? Who schedules the review, and what happens if the review does not pass?"*
- **Task B (`CAPE`):** *"An Inchcape RPA project has completed Discovery and Scoping. What are the remaining steps before development can begin, and which governance gate must be cleared?"*
- **Expected key points (verified 20 Nov 2026 against DRPA `KS-006` `8848212048` v3 & `KS-007` `8853815357` v8):** Phase 3 outputs are the Project Repository Document and a completed Project Security Checklist (**PSC**, DOCX format — required input; review does not go ahead without it); Phase 4 Scrum Master schedules kickoff call (BA runs it with PMO); developer submits Architecture Review Form (MS Forms) and presents Repository + PSC to RPA Architect / Technical Lead; two-tier approval follows (Tier 1 Architecture approval by RPA Architect or Technical Lead; Tier 2 Final Go by TDM); if revisions are required, developer revises Repository & PSC and resubmits (back to Step 3) before Phase 5 Development.

---

### Pair `P02` — CAPTCHA and MFA Policy (`KS-010`)

- **`task_difficulty`:** `Medium`
- **`task_matching_rationale`:** Both tasks address *Security / Policy* (*Policy / Standard* intent) governed exclusively by `KS-010`, testing retrieval of the same non-negotiable policy constraints (cannot bypass, feasibility-first evaluation, accepted risk not bot defect, manual steps owned by business/process owner, RPA team not responsible for SLA delays, P4 lowest priority as capacity allows, upfront stakeholder communication). *(Source-authority scoring gated by `DEP-08` canonical ID confirmation.)*
- **Task A (`NO_CAPE`):** *"An RPA automation encounters CAPTCHA or MFA during execution. What should the developer conclude about priority, SLA responsibility, manual intervention, and stakeholder communication?"*
- **Task B (`CAPE`):** *"A business team asks whether the RPA team can bypass MFA or treat a CAPTCHA-related delay as a bot defect. What should CAPE answer according to the RPA CAPTCHA and MFA Policy?"*
- **Expected key points (verified 16 Oct 2026 against `KS-010` DRPA):** Intentional security barriers (no bypass); evaluated first during feasibility; classified as accepted risk (not defect/bot error); only automatable portions in scope; manual intervention belongs to business/process owner; RPA team not responsible for SLA delays; P4 priority addressed as capacity allows; communicated at project start and documented in risk assessments.

---

### Pair `P03` — Knowledge Gap: AutoDrive Coding Standards (`KG-001`)

- **`task_difficulty`:** `Low-Medium`
- **`task_matching_rationale`:** Both tasks test *Boundary Honesty* on `KG-001` (*How-to / Boundary* intent), measuring time required to confirm that no validated AutoDrive coding standards document exists without fabricating Python/AutoDrive conventions. Both require explicit refusal and zero synthetic standards.
- **Task A (`NO_CAPE`):** *"Find the validated Inchcape AutoDrive coding standards document and summarize the required standards a developer must follow."*
- **Task B (`CAPE`):** *"What validated Inchcape AutoDrive coding standards should an RPA developer follow?"*
- **Expected key points (verified gap):** Confirm no validated AutoDrive coding standards source exists (`KG-001`); stop without inventing organizational coding standards from general Python/AutoDrive knowledge or informal repositories; preserve visibility of the unresolved gap.

---

### Pair `P04` — End-to-End 10-Phase Lifecycle & CAB Separation (`KS-006` / `KS-007`)

- **`task_difficulty`:** `Medium`
- **`task_matching_rationale`:** Both tasks address *Delivery Lifecycle* (*Reference / Explanation* intent) governed by `KS-006` (with `KS-007` restricted strictly to Phase 4 Architecture Review), testing complete phase-order fidelity (specifically preventing the historical merger of UAT, Internal CAB, Global CAB, Deployment, and Hypercare & BAU Handover, and preventing CAB-before-Development sequence errors).
- **Task A (`NO_CAPE`):** *"List all formal phases of the Inchcape RPA delivery lifecycle in exact order from initial request through BAU handover, and clarify how Internal CAB, Global CAB, and Architecture Review relate to each other."*
- **Task B (`CAPE`):** *"After an Inchcape RPA bot finishes Phase 5 Development, what exact remaining lifecycle phases must it pass through until BAU handover, and which governing document defines CAB vs. Architecture Review?"*
- **Expected key points (verified 20 Nov 2026 against DRPA `KS-006` `8848212048` v3 & `KS-007` `8853815357` v8):** `KS-006` (Primary, Provisional) governs all 10 ordered phases (`1. Request & Approval`, `2. Discovery & Scoping`, `3. Project Repository Document`, `4. Architecture Review & Project Kickoff`, `5. Development`, `6. UAT`, `7. Internal CAB (Pre-CAB)`, `8. Global CAB (Production CAB)`, `9. Deployment`, `10. Hypercare & BAU Handover`); Internal CAB (Pre-CAB Approval) and Global CAB (Production CAB Approval) remain separate phases (conditional Pre-CAB tasks must be completed before Production CAB); Phase 10 hypercare lasts max 2 months, KT scheduled ≥2 weeks prior, supports standard vs. pragmatic closure, and enhancements during hypercare are CICRs; `KS-007` governs Phase 4 Architecture Review only and does not govern CAB phases.

---

### Pair `P05` — Platform Selection vs. Architecture Review Complementarity (`KS-003` / `KS-007`)

- **`task_difficulty`:** `High`
- **`task_matching_rationale`:** Both tasks belong to *Architecture & Governance Precedence* (*Selection / Decision* intent), requiring synthesis of two Primary sources (`KS-003` and `KS-007`) and scope-based analysis to establish that they are complementary (technology selection vs. review gate) rather than conflicting. High cognitive load makes manual multi-page verification directly comparable to CAPE cross-source reasoning.
- **Task A (`NO_CAPE`):** *"A developer thinks the RPA Architecture Overview and the RPA Architecture Review Framework conflict on how platform selection and architecture review work together. Determine which document governs which decision and whether one overrides the other."*
- **Task B (`CAPE`):** *"When choosing an automation platform and checking whether an architecture review is required at Inchcape, how do KS-003 and KS-007 divide responsibility, and which takes precedence if they seem to overlap?"*
- **Expected key points (verified 20 Nov 2026 against DRPA `KS-003` `9025257486` v3 & `KS-007` `8853815357` v8):** Both `KS-003` and `KS-007` are Primary (Provisional); `KS-003` governs platform/technology architecture and tiers (Tier 1 Zero Cost Default: AutoDrive/Python, Excel VBA; Tier 2 M365 Licensed: Power Automate Cloud/Desktop, Power Apps; Tier 3 Enterprise/Custom: UiPath, Azure + C#) under the Cost-First Selection Principle (`Python/VBA → Power Platform → UiPath/C#`) and contains **zero** Architecture Review triggers; `KS-007` governs when an Architecture Review is required (all new projects + major enhancements changing tech stack, architecture, or core technical flow; excludes standard bug fixes/config/small tweaks) and its PSC + 2-tier approval gate; they are complementary by scope, not conflicting.

---

### Pair `P06` — Critical Incident Handling & Supporting Authority Ceiling (`KS-015`)

- **`task_difficulty`:** `High`
- **`task_matching_rationale`:** Both tasks address *Operations / Incident Troubleshooting* (*Troubleshooting* intent) governed only by `KS-015` (*Critical Incident Playbook — RPA Team*). Both test identical governance difficulty: locating operational playbook steps while strictly preserving `KS-015`'s **Supporting** ceiling (Trust Matrix rule R13) and open **Role Ambiguity** flag without inflating it into "official Inchcape primary policy" or pulling non-governed incident pages.
- **Task A (`NO_CAPE`):** *"A production RPA bot is involved in a critical incident. Identify the governed RPA playbook to consult, summarize its key guidance, and state its exact governance authority status and limitations."*
- **Task B (`CAPE`):** *"My production automation just triggered a critical incident — what playbook governs my response, and is it considered official Primary Inchcape policy?"*
- **Expected key points (verified 20 Nov 2026 against DRPA `KS-015` `8219525716` v5):** Cites `KS-015` (*Critical Incident Playbook — RPA Team*); explicitly classifies it as **Supporting** (not Primary) with open **Role Ambiguity** and **Provisional** status; covers core playbook stages (1. Detect & Verify `P0`/`P1` severity; 2. Open & Prime ManageEngine ticket with watchers & initial update; 3. Mobilize Technical Leader as Incident Commander, Project Dev via Repository/BCP, inform TDM → SD Team & PMO/Platform Lead; 4. Establish **INTERNAL** Teams War Room `CI-<Project>-<YYYYMMDD>-P0` with **no stakeholders**, 2-hour huddle cadence & pinned Working Summary; 5. Triage & Contain via Orchestrator/VM/ERP/1Password/licence checks + pause failing schedules, followed by Investigate/Fix, Communicate, Recover/Validate, Close CI, and Post-Incident RCA in 3–5 business days); excludes unvalidated CI pages (`8218509380`, `8152777079`); avoids authority-inflation phrases.

---

### Pair `P07` — RPA Architecture: Security & Functional Scope (`KS-005` / `KS-004`)

- **`task_difficulty`:** `Medium`
- **`task_matching_rationale`:** Both tasks address *Architecture — Security & Functional Design* (*Policy / Reference* intent) drawing on the two remaining populated Primary architecture sources (`KS-005` and `KS-004`), ensuring the 10-pair bank covers 100% of the 7 populated pilot sources while enforcing strict refusal on unpopulated security/vault topics (e.g., Azure Key Vault implementation specifics outside `KS-005`).
- **Task A (`NO_CAPE`):** *"Consult Inchcape's governed RPA Architecture — Security and Functional documents to summarize the documented security controls and functional component roles, and note whether Azure Key Vault implementation standards are covered."*
- **Task B (`CAPE`):** *"What security controls and functional component roles are documented in Inchcape's RPA Architecture pages, and does the validated knowledge base cover Azure Key Vault implementation standards?"*
- **Expected key points (verified 20 Nov 2026 against DRPA `KS-005` `9024078121` v4 & `KS-004` `9024241974` v4):** Both pages are component-by-component architecture descriptions (not formal bot requirement specs); `KS-005` (*RPA Architecture — Security*, Primary, Provisional) documents layer controls (UiPath Credential Store/RBAC, Power Automate DLP/env isolation, PAM360 for VMs/SAP/Autoline) and 4 Security Notes (credentials via PAM360 & UiPath Credential Store with no hardcoded passwords; TLS 1.2 in-transit & SFTP SSH keys + IP whitelisting; MFA/CAPTCHA as P4 accepted risk; RPA Data Policy: no PII in logs/file names, no sensitive data in emails, audit trail retention); `KS-004` (*RPA Architecture — Functional*, Primary, Provisional) describes each component's functional role only; **Azure Key Vault** is mentioned at high level only (*Key Vault integration / secret retrieval / connection strings*) with **zero implementation standards** (no vault names, RBAC/access policies, rotation, or retrieval patterns) and omitted from Security Notes.

---

### Pair `P08` — Known-but-Ineligible Stale Source: UiPath Best Practices (`KG-002` / `Q11`)

- **`task_difficulty`:** `Medium`
- **`task_matching_rationale`:** Both tasks test *Stale-Source Boundary Discipline* (*How-to / Boundary* intent), directly assessing whether the developer/CAPE correctly identifies the existing `UiPath Best Practices` document (v1, Feb 2024, no KS-ID, `Pending Validation (Stale)`) as known-but-ineligible and refuses to extract REFramework guidance from it. Naming is permitted; using as evidence is a critical failure.
- **Task A (`NO_CAPE`):** *"Search approved Inchcape documentation for validated UiPath REFramework best practices and determine whether any existing UiPath Best Practices page can be used as authoritative guidance."*
- **Task B (`CAPE`):** *"Can I rely on Inchcape's UiPath Best Practices documentation for REFramework development standards on a new bot?"*
- **Expected key points (aligned with `Q11` contract §26.9):** Declines to provide UiPath REFramework standards; may name *UiPath Best Practices* (Version 1, Feb 2024, no KS-ID) solely to disclose its blocking condition (`Pending Validation (Stale)` / ineligible); does **not** use its content or generic UiPath knowledge as governed Inchcape guidance.

---

### Pair `P09` — Uncovered Engineering Standards: Logging & Exception Structure (`Q12`)

- **`task_difficulty`:** `Low-Medium`
- **`task_matching_rationale`:** Both tasks test *Uncovered-Domain Boundary Honesty* (*How-to / Boundary* intent) in the Logging & Exception Handling domain (zero candidate sources identified). Both require confirming absence of a validated standard without synthesizing structured-logging templates or inventing an unverified escalation owner/document (such as pointing to `KS-007` for logging rules).
- **Task A (`NO_CAPE`):** *"Check Inchcape's governed RPA documentation for the required logging and exception-handling structure for a new bot, and report what authoritative standard applies."*
- **Task B (`CAPE`):** *"What validated logging format and exception-handling structure must I follow in my Inchcape RPA bot?"*
- **Expected key points (aligned with `Q12` contract §26):** Explicitly declines — no validated candidate source exists for bot logging or exception-handling standards; provides zero synthetic logging schemas; applies deterministic follow-up rule without inventing unverified owners or attributing logging rules to `KS-007`.

---

### Pair `P10` — Unresolved Taxonomy Boundary: `DRPA` vs. `SOLDOC` (`KG-003` / `Q19`)

- **`task_difficulty`:** `Medium`
- **`task_matching_rationale`:** Both tasks test *Known-Unresolved-Gap Discipline* (*Reference / Boundary* intent) on `KG-003`. Even though Confluence pages exist in both `DRPA` and `SOLDOC` spaces, neither developer nor CAPE may infer an organizational rule defining their formal distinction or canonical precedence from page titles or search snippets.
- **Task A (`NO_CAPE`):** *"Determine from governed Inchcape RPA documentation what official rule separates the DRPA and SOLDOC Confluence spaces and which space is canonical for publishing a new RPA guide."*
- **Task B (`CAPE`):** *"Where should an RPA developer publish documentation — DRPA or SOLDOC — and what is the governed difference between the two spaces?"*
- **Expected key points (aligned with `Q19` / `KG-003`):** Explicitly identifies this as a known unresolved knowledge gap (`KG-003`), not merely an unknown topic; declines to define `DRPA` vs. `SOLDOC` or declare canonical precedence from general knowledge or non-eligible Confluence pages; applies deterministic follow-up rule without inventing space-owner governance.

---

## 3. Pre-Freeze Verification Checklist (Required Before Protocol §9 Closure)

- [x] Verify exact Confluence source-backed key points for Pairs `P01`, `P04`, `P05`, `P06`, and `P07` against live DRPA pages (`8848212048` v3, `8853815357` v8, `9025257486` v3, `8219525716` v5, `9024078121` v4, `9024241974` v4 — completed 2026-11-20).
- [ ] Resolve `KS-010` canonical identity (`DEP-08`) to unblock `P02` source-authority scoring.
- [ ] Confirm counterbalanced condition-order table (e.g., odd pairs `NO_CAPE → CAPE`, even pairs `CAPE → NO_CAPE`) with Test Lead & Project Owner.
- [ ] Approve final `v0.2` Task Bank together with Protocol `v0.1-r2` §9 freeze before recording any execution in [`Change_07_Execution_Log_TEMPLATE.csv`](Change_07_Execution_Log_TEMPLATE.csv).
