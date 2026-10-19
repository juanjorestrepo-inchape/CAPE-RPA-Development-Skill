# CAPE RPA Development Skill — Change 07 Task Bank v0.1

**Original draft date:** October 16, 2026  
**Revision date:** October 19, 2026  
**Status:** Draft — pending governance gateway approval  
**Author:** Juan José Restrepo Rosero  
**Source-validation note:** Pair 2 (KS-010) remains subject to confirmation of the canonical governed page ID against the Knowledge Source Trust Matrix. Do not freeze the protocol or begin baseline measurement until that identity is reconciled.

---

## Evaluation Design

Three matched pairs of questions for the developer efficiency measurement protocol. Within each pair, Task A goes to the no-CAPE condition (developer searches manually) and Task B goes to the CAPE condition. Questions within a pair cover the same knowledge domain but are not identical.

| Field | Value |
|---|---|
| **Pairs** | 3 |
| **Tasks per pair** | 2 (Task A = no-CAPE, Task B = CAPE) |
| **Total task executions** | 6 |
| **Time limit per task** | 10 minutes |
| **Unresolved threshold** | Task not completed within 10 minutes = recorded as UNRESOLVED |
| **Unresolved treatment** | Kept in the data; not excluded from the calculation |
| **Author** | Juan José Restrepo Rosero |

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

## Quality Rubric — 8 Binary Dimensions (Pass/Fail)

Score each dimension as Pass (1) or Fail (0). Maximum score: 8. Do not award partial credit.

| # | Dimension | Pass condition | Mandatory / critical |
|---:|---|---|---|
| 1 | Correctness | The answer reaches the correct source-backed conclusion and contains no false or invented Inchcape policy. | Yes — failure is a critical failure. |
| 2 | Completeness | The answer covers at least 75% of the task's expected key points. | No |
| 3 | Source identification | The answer identifies the correct governed Confluence source or, for KG-001, identifies the declared knowledge gap. | No |
| 4 | Source authority | The answer applies the correct source role and scope; Primary sources are not displaced by Supporting sources, and a gap is not treated as a source. | No |
| 5 | Boundary compliance | The answer stays within documented evidence and does not assert requirements beyond the source or fill a declared gap. | Yes — failure is a critical failure. |
| 6 | No invented guidance | The answer does not synthesize Inchcape requirements from general knowledge, informal practice, or ineligible content. | No; any material invention is also a critical failure under dimensions 1 and/or 5. |
| 7 | Rework status | The answer is usable as-is and requires no material correction before it can be used for the task. | No |
| 8 | Time compliance | The task reaches an acceptable answer within the 10-minute limit. | No; if the limit expires without an acceptable answer, record UNRESOLVED and fail the task. |

**Task acceptance rule:** At least **6 of 8 dimensions must pass**, and both mandatory dimensions (1 — Correctness and 5 — Boundary compliance) must pass. Failure of either mandatory dimension means the task fails regardless of the total score. A score of 6/8 does not override any critical failure.

**Critical failures — task fails regardless of score:**
- Inventing an Inchcape policy, standard, approval path, or source that is not documented.
- Treating a declared knowledge gap as resolved.
- Using CAPE during a no-CAPE task.
- Bypassing the documented source boundary or presenting general practices as Inchcape-approved requirements.
- Ignoring the 10-minute limit or treating an unresolved task as successfully completed.
- Presenting a faster but incorrect answer as successful completion.

---

## Time Limit Rule

Each task has a hard 10-minute limit. If the participant has not produced an acceptable answer within 10 minutes, the task is recorded as UNRESOLVED. Unresolved tasks remain in the dataset and are not excluded from the calculation.

---

## Governance Note

This task bank is a draft preparation artifact. Sponsor approval is required before any measurement begins. The task bank is not frozen, and no efficiency result may be claimed until the approved protocol is executed and reviewed.
