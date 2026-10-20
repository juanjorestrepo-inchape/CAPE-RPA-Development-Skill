# CAPE RPA Development Skill — Change 07 Task Bank v0.1

**Original draft date:** October 16, 2026  
**Revision date:** October 20, 2026  
**Status:** Draft — pending governance gateway approval (`PROPOSED — PENDING APPROVAL`)  
**Author:** Juan José Restrepo Rosero  
**Governing protocol:** [`CAPE_Change_07_Efficiency_Protocol_v0.1.md`](CAPE_Change_07_Efficiency_Protocol_v0.1.md) — this Task Bank supplies the task set; the protocol is canonical for design, rubric, data schema, analysis, and approval gates.  
**Source-validation note:** Pair 2 (KS-010) remains subject to confirmation of the canonical governed page ID against the Knowledge Source Trust Matrix. Do not freeze the protocol or begin baseline measurement until that identity is reconciled.

---

## Evaluation Design

Three matched pairs of questions prepared to date, against a pilot target of ten matched pairs. Task A goes to the no-CAPE condition (developer searches manually) and Task B goes to the CAPE condition. Under the protocol's approved design basis (`C07-D08`, 2026-10-20), questions within a pair must be **equivalent** — matched by domain, intent, expected outcome, and approximate difficulty; identical wording is not required and may be avoided where familiarity could bias the second execution. Per-pair equivalence rationales are not yet documented (protocol checklist item 2).

| Field | Value |
|---|---|
| **Pilot target pairs** | 10 |
| **Pairs prepared in this draft** | 3 |
| **Tasks per pair** | 2 (Task A = no-CAPE, Task B = CAPE) |
| **Target total task executions** | 20 |
| **Executions prepared in this draft** | 6 |
| **Time limit per task** | 10 minutes |
| **Unresolved threshold** | Task not completed within 10 minutes = recorded as UNRESOLVED |
| **Unresolved treatment** | Kept in the data; not excluded from the calculation |
| **Author** | Juan José Restrepo Rosero |

> **Coverage status:** this draft does not yet contain all ten pairs. Seven additional pairs / fourteen executions must be prepared and reviewed before execution, unless an explicit documented decision changes the sample size (protocol §2.2 and §11).

> **Pair-equivalence status — `C07-D08` resolved as design basis; documentation still required:** the protocol's approved design basis (2026-10-20) requires **equivalent** tasks within a pair, matched by domain, intent, expected outcome, and approximate difficulty; identical wording is **not** required. The Task A / Task B prompt pairs below are non-identical by design, but **no per-pair equivalence rationale has been documented yet**. Each pair must have its documented and reviewed matching rationale (protocol §2.2, checklist item 2) before it may be executed. This is a documentation gap, not a methodology gap.

---

## Pair 1 — Lifecycle and Governance (KS-006 / KS-007)

### Task A — no-CAPE condition

**Prompt:**
> What does a developer need to prepare and present before an RPA project can move into the Development phase at Inchcape? Who schedules the review, and what happens if the review does not pass?

**Expected key points (from developer's own research):**
- Developer creates the Project Repository Document (Phase 3 — KS-006).
- The Scrum Master schedules the project kickoff call — not the developer.
- Developer presents the Project Repository to the RPA Architecture team.
- The RPA Architecture team reviews and provides approval or revision feedback.
- If approved — development proceeds. If revisions required — developer applies changes and re-presents before proceeding.

**Governing sources:** KS-006 (RPA Project Intake Framework) for the lifecycle; KS-007 (RPA Architecture Review Framework) for architecture review scope.

### Task B — CAPE condition

**Prompt:**
> An Inchcape RPA project has completed Discovery and Scoping. What are the remaining steps before development can begin, and which governance gate must be cleared?

**Expected key points:**
- Phase 3: developer creates the Project Repository Document.
- Phase 4: Scrum Master schedules the kickoff call.
- Developer presents the Project Repository to the RPA Architecture team.
- Architecture team reviews and provides approval or revision feedback.
- If revisions are required, developer applies them and re-presents before proceeding.
- Architecture review approval is the gate before Phase 5 Development begins.

**Governing sources:** KS-006 for the lifecycle; KS-007 for the architecture review gate details.

**Source validation status:** All key points confirmed against KS-006 Confluence page (16 Oct 2026). Scrum Master scheduling and re-presentation step verified from source text.

---

## Pair 2 — CAPTCHA and MFA Policy (KS-010)

### Task A — no-CAPE condition

**Prompt:**
> An RPA automation encounters CAPTCHA or MFA during execution. What should the developer conclude about priority, SLA responsibility, manual intervention, and stakeholder communication?

**Expected key points:**
- CAPTCHA and MFA are the first elements evaluated in any RPA project.
- If present, they are flagged during the feasibility phase as obstacles to full end-to-end automation.
- They are classified as risk acceptance: known limitations, not defects.
- If a bot fails because of CAPTCHA or MFA, that is an accepted risk, not a bot error.
- Only the automatable parts of the process are in scope; manual steps remain outside automation scope.
- The RPA team is not responsible for delays or missed SLAs caused by CAPTCHA or MFA interventions.
- Manual intervention is the responsibility of the process owner or business team.
- CAPTCHA and MFA-related issues are categorized as P4 (lowest priority).
- P4 issues are addressed as developer capacity allows.
- The policy must be communicated to stakeholders at the start of each RPA project.

### Task B — CAPE condition

**Prompt:**
> A business team asks whether the RPA team can bypass MFA or treat a CAPTCHA-related delay as a bot defect. What should CAPE answer according to the RPA CAPTCHA and MFA Policy?

**Expected key points:**
- The policy applies to all RPA projects at Inchcape Digital.
- CAPTCHA and MFA are intentional barriers to automation and cannot be bypassed without compromising security.
- CAPTCHA and MFA are evaluated first in any RPA project and flagged during feasibility if present.
- They are known limitations handled as risk acceptance, not defects.
- A bot failure caused by CAPTCHA or MFA is an accepted risk, not a bot error.
- Manual steps remain outside automation scope.
- Manual intervention belongs to the process owner or business team.
- The RPA team is not responsible for delays or missed SLAs caused by CAPTCHA or MFA interventions.
- CAPTCHA/MFA-related issues are P4 (lowest priority) and handled as developer capacity allows.
- The policy must be communicated at project start and referenced in project documentation / risk assessments.

**Source validation status:** All key points confirmed against KS-010 DRPA Confluence page (16 Oct 2026). P4 priority is in the Issue Handling and Priority bullet, separate from RPA Team Responsibility. “Addressed as developer capacity allows” is included.

---

## Pair 3 — Knowledge Gap / AutoDrive Coding Standards (KG-001)

### Explanation

There is nothing to open in Confluence because the correct answer to Pair 3 is that nothing exists. The gap is the point.

- **Task A (no-CAPE):** The developer searches for the answer themselves — Confluence, GitHub, or wherever they normally look. The correct outcome is that they search, find nothing authoritative, and write: “No validated AutoDrive coding standards document found.” The test measures how long it takes to reach that conclusion without CAPE.
- **Task B (CAPE):** CAPE should activate the Skill, identify KG-001, say no validated source exists, and stop. That is the correct CAPE behavior.

There is no Confluence page to validate because the gap is the point. Pair 3 is confirmed as-is.

### Task A — no-CAPE condition

**Prompt:**
> Find the validated Inchcape AutoDrive coding standards document and summarize the required standards a developer must follow.

**Expected key points:**
- Developer searches normal approved working sources.
- No validated AutoDrive coding standards document is found.
- Correct answer: No validated AutoDrive coding standards document found.
- The response must not invent standards from general Python, AutoDrive experience, GitHub examples, or informal practice.
- The unresolved knowledge gap must remain visible.

### Task B — CAPE condition

**Prompt:**
> What validated Inchcape AutoDrive coding standards should an RPA developer follow?

**Expected key points:**
- CAPE activates the RPA Development Skill.
- CAPE identifies KG-001.
- CAPE states that no validated source exists for AutoDrive coding standards.
- CAPE stops rather than generating or drafting organization-specific standards.
- CAPE does not rely on general coding knowledge as Inchcape policy.

**Source validation status:** No Confluence page exists to validate because the expected answer is the documented absence of a validated source. Pair 3 is confirmed as a knowledge-gap task.

---

## Protocol Alignment

The following components are defined in the governing protocol and are **not duplicated here**:

- **Eight-dimension quality rubric, acceptance threshold, and critical-failure vetoes:** protocol §6. The rubric and the ≥ 6/8 threshold are part of the user-approved **design basis**; formal approval is still pending, and the critical-failure catalogue remains a proposed candidate list.
- **Timing, outcome taxonomy, and time-limit rule:** protocol §5. Each task has a hard 10-minute limit; a task not completed within 10 minutes is recorded as `UNRESOLVED` with active time exactly 600 seconds. Unresolved tasks remain in the dataset and are not excluded from the calculation.
- **Data log and evidence schema:** protocol §7.
- **Analysis method and reporting rules:** protocol §8.
- **Approval and execution gate:** protocol §9.

## Governance Note

This task bank is a draft preparation artifact. It does not contain the full ten-pair sample, is not frozen, and has not been approved for execution. Sponsor/owner approval of the protocol is required before any measurement begins. No efficiency result may be claimed until the approved protocol is executed and reviewed.

No execution has occurred: baseline measurements = 0, CAPE measurements = 0. The 30% reduction remains a target, not a result. No Confluence page, Implementation Record revision, source classification, Trust Matrix entry, or Coverage-Honesty Gate status is changed by this document.
