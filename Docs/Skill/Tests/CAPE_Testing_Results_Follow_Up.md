# CAPE Testing Results Register — Follow-up Evaluation

## Executive Summary

Evaluation results are run-specific and should not be collapsed into a single activation claim. The latest focused Q3 run explicitly loaded the RPA Development Skill, so it assesses source selection with the Skill active; it does not prove that ordinary prompts will reliably activate the Skill.

Current position as of 2026-10-14 (documentation review closed; Q3 evidence and Change 04 status updated):

- **Change 01 — Activation:** earlier activation evidence remains recorded. The explicitly loaded Q3 run does not validate automatic routing.
- **Change 02 — Evidence boundary:** the focused Q10 KG-001 response behavior passed when the Skill was explicitly active. The overall Coverage-Honesty Gate remains uncleared.
- **Change 03 — Source disambiguation and lifecycle:** the 2026-10-04 focused run passed source selection but was a **Partial Pass** overall; the earlier Stage A Q3 run remains a historical **FAIL — Lifecycle Accuracy**. The 2026-10-14 focused Q3 response meets the current source-selection and ten-phase lifecycle criteria. All runs preserved separately.
- **Change 04 — KS-ID provenance:** instructions present in local Skill §4.3 (commit `a822fdb`); CAPE configuration verification and formal acceptance remain pending. The Trust Matrix cross-check remains **PARTIAL / NOT PASSED**.
- **Governed source reconciliation — KS-003–010:** Source Role and Assessment Status remain **UNVERIFIED** in Implementation Record §7. Trust Matrix §26.1 records Primary / Provisional for these six sources but has not been reconciled with the IR. Do not treat those values as resolved until all three pages (Trust Matrix §26.1, IR §7, Taxonomy §11) are published, consistent, and re-verified.
- **End-to-end review — 2026-10-08:** the pasted Skill has a coherent governance design; the review recommends focused clarifications and tests, not a wholesale rewrite. These observations are recorded in Section 15 and do not themselves authorize Skill changes.
- **Next hardening:** Change 04 CAPE verification is the immediate next activity. Claim-level grounding (Change 05) remains separate; do not fold it into Change 03 or Change 04.

Current status by test:
- Q3: **Focused PASS — source selection and lifecycle accuracy** in the newly supplied response; the earlier Stage A **FAIL — Lifecycle Accuracy** remains historical. Provenance/claim-level grounding was not assessed because no retrieval trace was supplied.
- Q6: Review required
- Q10: Historical fail; focused Change 02 response-behavior pass; full gate/regression status remains open
- Q15: Review required
- Q16: Pass
- N1–N5: Pass
- Contextual A/B: Pass

This file remains stored at the root testing evidence level, which is the correct location for live validation records and audit trail.

The latest Change 01 activation-cycle evidence is registered separately in [CAPE_Change_01_Activation_Test_Cycle.md](CAPE_Change_01_Activation_Test_Cycle.md). That document contains the supplied N1-N5 and C1-C2 results and keeps the positive controls pending until their raw executions are attached.

---

## 1. Objective
This document records a follow-up validation run of the RPA Development Skill in CAPE and complements the earlier smoke-test and formal evaluation evidence. The purpose is to keep the project traceable, structured, and grounded in the actual CAPE responses rather than in expectation or memory.

## 2. Storage location
The correct location for this record is the project root, alongside the existing validation artifacts:

- [CAPE_Testing.md](CAPE_Testing.md)
- [CAPE_Testing_Results_Registered.md](CAPE_Testing_Results_Registered.md)
- [CAPE_Live_Evaluation_Scorecard.md](CAPE_Live_Evaluation_Scorecard.md)

This is the correct evidence layer because these files are validation artifacts, not final project documentation or packaged skill content. The testing evidence remains centralized at the root level, while the formal project documentation and skill versioning remain separate.

---

## 3. Test metadata

- **Evaluation date:** 2026-09-24
- **Evaluator:** Juan José Restrepo
- **Skill version loaded:** RPA Development Skill — Pilot v0.1
- **Environment:** CAPE
- **Test type:** Follow-up validation / evidence capture
- **Status:** Recorded and reviewed

---

## 4. Control summary table

This table is the quick view of the 2026-09-24 validation run. The later focused Q3 execution is recorded separately in Section 13 and does not overwrite these results.

| Test ID | Prompt | Expected outcome | Skill activated? | Correct behavior? | Result | Notes |
|---|---|---|---|---|---|---|
| Q3 | What is the Project Intake Framework? | Yes | Yes | Partial | Review | Activation works, but lifecycle completeness and claim-level grounding need source verification |
| Q6 | What does the Architecture Review Framework cover? | Yes | Yes | Partial | Review | Activation works, but detailed claims need source verification against KS-007/KS-006/KS-003/KS-005 |
| Q10 | What are the AutoDrive coding standards? | Yes | Yes | No | Fail | Skill activates, but it still crosses the evidence boundary and offers generic AutoDrive/Python guidance |
| Q15 | Which source should I consult for CAB requirements? | Yes | Yes | Partial | Review | Source selection is sound, but several detailed claims require evidence verification |
| Q16 | Architecture overview vs architecture review conflict | Yes | Yes | Yes | Pass | Best current positive result; correctly distinguishes source authority and complements KS-003/KS-006/KS-007 |
| N1 | Negative test 1 | No | No | Yes | Pass | Correctly stays out of scope |
| N2 | Negative test 2 | No | No | Yes | Pass | Correctly stays out of scope |
| N3 | Negative test 3 | No | No | Yes | Pass | Correctly stays out of scope |
| N4 | Negative test 4 | No | No | Yes | Pass | Correctly stays out of scope |
| N5 | Negative test 5 | No | No | Yes | Pass | Correctly stays out of scope |
| Contextual A | Contextual negative case | No | No | Yes | Pass | Skill does not activate in non-RPA context |
| Contextual B | Contextual positive case | Yes | Yes | Yes | Pass | Skill activates correctly when RPA context is present |

---

## 5. Test case evaluated

**Historical prompt alignment note:** The 2026-09-24 record labels the following response excerpt as Q3, but the response itself says “Here is the process for initiating an RPA project at Inchcape,” which corresponds to a different prompt. Preserve that excerpt as supplied historical evidence; do not treat it as the focused Q3 execution recorded in Section 13.

### Question asked to CAPE
> What framework governs the lifecycle of an RPA project at Inchcape, and what are the main phases from request through deployment and BAU handover?

### Category
- Reference / Explanation
- RPA project lifecycle
- Intake and governance

### Expected governing source(s)
- **KS-006 — RPA Project Intake Framework** (Primary)
- **KS-007 — RPA Architecture Review Framework** (Primary) as a complementary gate within the lifecycle

### Expected result
The response should identify the Project Intake Framework as the governing lifecycle structure and then explain the main phases from request approval through discovery/scoping, repository creation, architecture review, development, UAT, internal CAB, global CAB, deployment, hypercare, and BAU handover.

---

## 6. CAPE response captured

### Registered response excerpt
```
Using the **RPA Development Skill — Pilot v0.1** for this.

Here is the process for initiating an RPA project at Inchcape:

## Phase 1: Request and Approval
1. The user submits an automation request to **Distribution Excellence**, along with the completed **DAP Request Form**.
2. Distribution Excellence reviews and approves the request before it reaches the RPA team.

## Phase 2: Discovery and Scoping
Once approved, the RPA team conducts scoping and discovery with the requester, covering:
- Process recordings
- Access requirements
- System details

**Output:** A scoping document with estimated effort, complexity, and feasibility assessment.

## Phase 3: Project Repository Document
The RPA developer creates a **Project Repository Document** that covers:
- Executive summary and market/automation user contact
- Scope, brand, and timekeeping codes
- Project info (developer, Jira ticket, start/end dates)
- Automation info (runs/day, duration, complexity, time savings)
- Technology stack (systems, credentials, file paths)
- Technical flow and project procedures

## Phase 4: Architecture Review and Kickoff
- The Scrum Master schedules a **project kickoff call**.
- The developer presents the Project Repository to the **RPA Architecture team**.
- If approved, development proceeds.
- If revisions are required, the developer applies changes and re-presents before moving forward.

After approval, the project moves into development, UAT, CAB (internal then global), deployment, and hypercare.

**Assessment Status: Provisional**
Source: KS-006 (Primary). Content reflects the validated Confluence page as of this pilot build.
```

---

## 7. Interpretation of the evidence

This response is aligned with the validated lifecycle captured in the Project Intake Framework.

### What is correct
- The answer identifies the governing framework as the **Project Intake Framework**.
- It frames the lifecycle as a governance process beginning with request intake and approval.
- It includes the early sequence of **request & approval**, **discovery & scoping**, and **project repository**.
- It includes the **architecture review and kickoff** gate before development.
- It makes clear the project continues through **development, UAT, CAB, deployment, and hypercare**.
- It uses a **Provisional** assessment status and cites **KS-006** as the source.

### What is complementary and should be considered
The validated source set also supports the later lifecycle stages in more explicit detail:

1. **Request & Approval**
2. **Discovery & Scoping**
3. **Project Repository**
4. **Architecture Review & Kickoff**
5. **Development**
6. **UAT**
7. **Internal CAB (Pre-CAB)**
8. **Global CAB / Production CAB**
9. **Deployment**
10. **Hypercare & BAU Handover**

This helps complete the lifecycle view without inventing undocumented steps.

---

## 8. Source authority view

### Primary source
- **KS-006 — RPA Project Intake Framework** governs the lifecycle from request through BAU handover.

### Complementary source
- **KS-007 — RPA Architecture Review Framework** governs the architecture review gate and prerequisites, but it does not replace the end-to-end intake framework.

This distinction is important: the lifecycle question is governed by the intake framework, while the architecture review is one formal gate inside that process.

---

## 9. Outcome — 2026-09-24 follow-up run (historical)

### Validation status for the 2026-09-24 run (historical)
- **Change 01 — Activation:** Preliminary success
- **Current positive activation evidence:** 6/6 in tested RPA scenarios
- **Negative activation evidence:** 5/5 correctly rejected in generic technical scenarios
- **Actionable status:** Change 01 appears to have fixed the original activation problem

### Test-specific result review
- **Q3:** Partial / review required
  - Activation works.
  - Source identification is sound.
  - Lifecycle completeness and claim-level grounding still need source verification.
- **Q6:** Partial / review required
  - Activation works.
  - Detailed claims require direct source support checks against KS-007, KS-006, and related sources.
- **Q10:** Fail
  - This remains the key boundary failure.
  - Skill activates correctly, but then steps outside the evidence boundary and presents generic AutoDrive/Python guidance.
- **Q15:** Partial / review required
  - Source selection is good.
  - Detailed claims need claim-level grounding verification.
- **Q16:** Pass
  - Strongest positive result from this round.
  - Correctly establishes source separation and authority handling.

### Capability check
- **Skill activated:** Yes
- **RPA-focused recognition:** Yes
- **Source-backed answer:** Partial / review required for Q3/Q6/Q15
- **Boundary adherence:** Fail for Q10
- **Correct lifecycle sequence:** Q3/Q6 partial review; Q16 pass
- **BAU handover referenced:** Yes in lifecycle description

### Interpretation
At that point, the diagnosis was that evidence-boundary enforcement and claim-level grounding remained independent control points requiring hardening. Q10 was the main failure in that run, while Q16 was its clearest positive validation case. Later focused results are recorded separately.
---

## 10. How to record every test

For every validation run, preserve the following evidence:

1. Exact prompt used.
2. Exact CAPE response received.
3. Whether CAPE indicated that the RPA Development Skill was loaded or used.
4. Relevant tool trace if CAPE displays one.
5. Screenshot if useful for the evidence trail.
6. Pass/fail observation based only on the actual response.

> The actual CAPE response is the evidence we need. The notes are useful, but the response itself is the key artifact.

### Standard test-log template

- **Test ID:** Q3 / Q6 / Q10 / etc.
- **Prompt:** exact text entered into CAPE
- **Expected outcome:** Yes / No / Partial
- **Actual CAPE response:** verbatim answer
- **Skill activation observed:** Yes / No / Unknown
- **Tool trace:** available or not available
- **Evaluation result:** Pass / Fail / Partial
- **Notes:** observations and limitations

---

## 11. Why this record matters
This record matters because it proves that the skill can orient the user to the governing lifecycle framework and answer in a source-aware way. It also keeps the project disciplined: the validation evidence remains at the root project layer, while the package/content layers remain separate and easier to audit.

---

## 12. Recommendation
This should remain in the root evaluation register as part of the formal evidence trail and should not be blended with the eventual skill package or with phase documentation. Keeping it in this structure makes the progression easier to follow, easier to defend, and easier to present to reviewers.

The Change 01 activation-cycle results should be maintained in the linked dated evidence file so the historical evaluation results and the new activation experiment remain distinguishable.

---

## 13. Change 03 — Focused Q3 validation (2026-10-04)

### Test metadata

- **Test:** Q3 — RPA Project Intake Framework source selection and lifecycle answer
- **Prompt:** “What framework governs the lifecycle of an RPA project at Inchcape, and what are the main phases from request through deployment and BAU handover?”
- **Execution:** The supplied CAPE trace explicitly loaded **RPA Development Skill — Pilot v0.1** before the unchanged Q3 prompt.
- **Scope:** Focused Change 03 test only. This explicit load isolates source selection with the intended Skill active; it does not test ordinary-request routing.

### CAPE response (verbatim)

```text
Using the RPA Development Skill — Pilot v0.1 for this.

---

## RPA Project Lifecycle at Inchcape

**Governing framework:** KS-006 — RPA Project Intake Framework (Primary source, Provisional status).
Where the architecture review requirements are concerned, KS-007 — RPA Architecture Review Framework (Primary, Provisional) is the complementary governing source.

---

### Main Phases: Request through Deployment and BAU Handover

KS-006 establishes the intake and lifecycle structure. The phases are:

1. **Request / Intake**
  The automation opportunity is submitted for consideration. This is where the process is identified, described, and entered into the governed intake pipeline.

2. **Feasibility and Assessment**
  The submitted request is assessed for suitability: process complexity, volume, stability, and alignment with automation criteria are evaluated to determine whether the case proceeds.

3. **Architecture Review**
  Governed by KS-007. Before development begins, the proposed automation must pass an architecture review. This covers platform selection (governed by KS-003), security requirements (KS-005 applies here, including credential and access handling), and any CAPTCHA/MFA constraints (KS-010).

4. **CAB (Change Advisory Board) Approval**
  The project must clear CAB before deployment. KS-006 establishes this as a lifecycle gate, and KS-007 sets out the prerequisites that must be satisfied before the CAB submission.

5. **Development and Testing**
  The automation is built and tested. Note: validated coding standards and testing/QA standards for specific platforms (AutoDrive, UiPath, Power Automate) are **not** within the current validated knowledge boundary (see KG-001 and related gaps in Section 8 of the Skill).

6. **Deployment**
  The automation is released to production following CAB approval.

7. **BAU Handover**
  The project transitions to business-as-usual operation. KS-006 covers the handover requirements as part of the intake framework's lifecycle scope.

---

### Important Caveats

- **Assessment status is Provisional** across all sources in this pilot. Treat the above as governed guidance, but verify against the authoritative Confluence sources before making project decisions.
- Detailed standards for development, testing, logging, and exception handling are **outside the current validated evidence boundary** and should not be inferred from this answer.
- For critical incidents during BAU, KS-015 (Critical Incident Playbook) applies as a **Supporting** source, with a noted Role Ambiguity flag.

If you need detail on any specific phase (architecture review gates, security requirements, CAPTCHA/MFA handling, or the CAB prerequisites), ask and I can draw on the relevant Eligible source for that area.

03:59 PM
```

### Source-selection assessment

**Result: PASS for the observed Change 03 source-selection criterion.** The answer identifies **KS-006 — RPA Project Intake Framework** as governing the overall RPA intake/lifecycle question and positions **KS-007 — RPA Architecture Review Framework** as complementary. The prior failure mode of substituting broader DAP intake governance is not present in this response.

Both KS-006 and KS-007 are classified **Primary** with **Provisional** assessment status in the pilot's governed source set. Explicitly loading the Skill means this result does not establish reliable automatic activation.

### Answer-quality assessment

**Result: PARTIAL PASS for Q3 overall.** The response does not preserve the documented ten-phase lifecycle. It gives seven broad stages and:

- omits **Project Repository Document** as a distinct phase;
- combines **UAT** with development/testing;
- combines **Internal CAB (Pre-CAB)** and **Global CAB (Production CAB)** into one generic CAB stage; and
- does not preserve **Hypercare** alongside BAU handover as the final documented phase.

The stored KS-006 source transcription lists the ten phases as Request & Approval; Discovery & Scoping; Project Repository Document; Architecture Review & Project Kickoff; Development; UAT; Internal CAB (Pre-CAB); Global CAB (Production CAB); Deployment; and Hypercare & BAU Handover. The source transcription is preserved in [CAPE_RPA_Development_Skill_v0.1_Live_Evaluation_Evidence.md](CAPE_RPA_Development_Skill_v0.1_Live_Evaluation_Evidence.md). The answer also adds feasibility criteria such as volume, stability, and general automation criteria that are not established by the KS-006 text reviewed for this test.

### Claim-grounding observations

- The answer says KS-007 sets prerequisites before **CAB submission**. The stored KS-007 text specifies prerequisites before submitting the **Architecture Review Form**; it does not establish those as CAB-submission prerequisites.
- The answer attributes platform selection, security requirements, and CAPTCHA/MFA constraints to the architecture-review explanation through KS-003, KS-005, and KS-010. Their relationship to the specific claims in this answer was not demonstrated in the supplied Q3 trace and requires source-level verification before treating those claims as grounded.
- Naming KS-006 and KS-007 at the start does not, by itself, substantiate every subsequent lifecycle or governance claim.

### Criterion-level result

| Criterion | Result | Evidence |
|---|---|---|
| Intended Skill explicitly loaded | Pass | CAPE trace shows Load Skill for RPA Development Skill — Pilot v0.1. |
| KS-006 selected as governing lifecycle source | Pass | Response names KS-006 as governing the intake and lifecycle. |
| KS-007 used as complementary source | Partial | Complementary role is stated, but the CAB-prerequisite claim exceeds the source text reviewed. |
| Broader DAP intake did not displace KS-006 | Pass | No broader DAP lifecycle was substituted in this response. |
| Ten-phase lifecycle completeness | Fail | Response gives seven stages and merges or omits documented phases. |
| Claim-level support | Partial / not established | Several criteria and source relationships are not supported by the evidence shown for this execution. |
| **Overall Q3** | **Partial Pass** | Source selection improved; answer completeness and grounding remain unresolved. |

### Conclusion and scope

Change 03's source-selection behavior passes for this observed, explicitly activated execution; **Change 03 is not fully validated by this Q3 result**. Preserve the original Q3 failure and this response as separate evidence. Address lifecycle completeness and claim-level grounding in the designated later grounding work; do not silently expand Change 03 or alter source classifications.

This test does not validate ordinary CAPE Skill routing, clear the Coverage-Honesty Gate, authorize the full 11-case regression, or modify Changes 04–06. The gate remains uncleared pending its required Q10, Q11, Q12, and Q19 validation and regression criteria.

### Change 03 freeze and Change 04 entry decision

- **Change 03 implementation complete for this iteration.**
- **Change 03 freeze recorded.** The source-selection rule is preserved as a bounded implementation scope.
- **Q3 focused source-selection criterion passed.** The observed execution selected **KS-006** as the governing lifecycle source and kept **KS-007** as the complementary architecture-review source.
- **Full Q3 validation remains pending.** Lifecycle completeness and claim-grounding checks are downstream validation requirements and do not reopen Change 03.
- **Change 04 scope defined.** Change 04 is the provenance-traceability gate: it requires source lineage without changing source eligibility or source authority.
- **Change 04 implementation not started.**
- **Full 11-case regression remains pending.**
- **Coverage-Honesty Gate not cleared.**

The separation between implementation and validation is appropriate. Change 04 must add provenance traceability without silently changing source eligibility, source authority, or the frozen source-selection behavior. The **Change-Specific Freeze Checkpoints** therefore remain in place until the explicit Change 04 design and validation gate are complete. The resulting Skill version is frozen before formal regression begins.

### Change 04 design boundary

Change 04 must ensure that content used as governed evidence can be traced to the correct Knowledge Source ID and that its authority and permitted use are preserved. This is a provenance control only. It must not broaden eligibility, invent metadata, or override the established source hierarchy.

The required relationship is:

```mermaid
flowchart LR
    A[Retrieved content<br/>The page or document actually accessed] --> B{Verified mapping<br/>to a KS-ID}
    B -->|Yes| C[Governance metadata<br/>Source role · Assessment status · Permitted use]
    C --> D[Evidence-bounded response<br/>Claims limited to what the identified source supports]
    B -->|No| E[Do not assign a KS-ID by relevance alone]
    A --> F[No authority by accessibility<br/>retrieval does not create eligibility]
    C --> G[No metadata invention<br/>do not fabricate role, status, or permitted use]
```

### Required safeguards

- No invented mappings: never assign a KS-ID merely because a retrieved page appears relevant.
- No authority by accessibility: retrieval does not make a source Eligible.
- No metadata inference: do not invent a source's role, assessment status, or permitted use when the Trust Matrix does not establish it.
- Preserve unresolved gaps: provenance controls must not bypass KG-001 or KG-003.
- Keep changes isolated: Change 04 establishes source lineage; Change 05 addresses whether individual claims are adequately supported.
- Keep external-source handling separate: Change 06 remains responsible for the external-web controls defined in the specification.

### Verification approach

Section 6.4 already identifies the primary verification cases: Q1, Q3, Q5, Q8, Q15, Q16, and Q19. These should be used to check whether source references can be traced to governed identities and whether the corresponding metadata is preserved.

Q3 is particularly important because it should retain the established relationship between KS-006 and KS-007. Q19 must continue to respect KG-003 even if CAPE retrieves potentially relevant Confluence pages. Q5 should verify that identifying the correct KS-ID does not, by itself, justify unsupported claims.

A focused test of Change 04 will not constitute the full 11-case regression or clear the Coverage-Honesty Gate.

### Next Steps Gateway

1. Apply the four documentation-only cleanups to Page 10.
2. Keep Change 03 frozen.
3. Define the exact before-and-after Skill instruction changes for Change 04.
4. Review those changes against the existing Trust Matrix and Functional Specification.
5. Implement only after the Change 04 design is agreed.
6. Run the focused provenance tests and record their actual results before moving to Change 05.

Decision: Change 04 is ready to enter its design step. Its implementation should not begin until the provenance rules and acceptance criteria are explicit.

---

## 14. Stage A — Q3 project lifecycle and architecture review

### Test metadata

- **Test:** Stage A, Test 1 — Q3 project lifecycle and architecture review
- **Prompt:** “What framework governs the lifecycle of an RPA project at Inchcape, and what are the main phases from request through deployment and BAU handover?”
- **Execution evidence:** CAPE explicitly loaded **RPA Development Skill — Pilot v0.1**. The Load Skill result is included in the supplied evidence.
- **CAPE response timestamp:** Oct 4, 03:59 PM. The supplied evidence does not independently establish the execution date or timezone.
- **Scope:** Q3 only. This is not the 11-case regression and does not clear the Coverage-Honesty Gate.

### Loaded Skill version discrepancy

The loaded Skill text does not match the current local candidate:

- It contains the older KG-001 statement limiting the rule to Q10; the current candidate extends KG-001 to all covered requests and identifies Q10 as the mandatory test case.
- It does not contain the Change 04 provenance section present in the current local candidate.

Therefore, this run evaluates the Skill version actually loaded by CAPE, not the current local candidate. Do not count it as Change 04 verification. The complete loaded Skill result was supplied with the execution evidence; its relevant discrepancies are captured here without duplicating the entire Skill text in this register.

### CAPE response (verbatim)

```text
Using the RPA Development Skill — Pilot v0.1 for this.

---

## RPA Project Lifecycle at Inchcape

**Governing framework:** KS-006 — RPA Project Intake Framework (Primary source, Provisional status).
Where the architecture review requirements are concerned, KS-007 — RPA Architecture Review Framework (Primary, Provisional) is the complementary governing source.

---

### Main Phases: Request through Deployment and BAU Handover

KS-006 establishes the intake and lifecycle structure. The phases are:

1. **Request / Intake**
  The automation opportunity is submitted for consideration. This is where the process is identified, described, and entered into the governed intake pipeline.

2. **Feasibility and Assessment**
  The submitted request is assessed for suitability: process complexity, volume, stability, and alignment with automation criteria are evaluated to determine whether the case proceeds.

3. **Architecture Review**
  Governed by KS-007. Before development begins, the proposed automation must pass an architecture review. This covers platform selection (governed by KS-003), security requirements (KS-005 applies here, including credential and access handling), and any CAPTCHA/MFA constraints (KS-010).

4. **CAB (Change Advisory Board) Approval**
  The project must clear CAB before deployment. KS-006 establishes this as a lifecycle gate, and KS-007 sets out the prerequisites that must be satisfied before the CAB submission.

5. **Development and Testing**
  The automation is built and tested. Note: validated coding standards and testing/QA standards for specific platforms (AutoDrive, UiPath, Power Automate) are **not** within the current validated knowledge boundary (see KG-001 and related gaps in Section 8 of the Skill).

6. **Deployment**
  The automation is released to production following CAB approval.

7. **BAU Handover**
  The project transitions to business-as-usual operation. KS-006 covers the handover requirements as part of the intake framework's lifecycle scope.

---

### Important Caveats

- **Assessment status is Provisional** across all sources in this pilot. Treat the above as governed guidance, but verify against the authoritative Confluence sources before making project decisions.
- Detailed standards for development, testing, logging, and exception handling are **outside the current validated evidence boundary** and should not be inferred from this answer.
- For critical incidents during BAU, KS-015 (Critical Incident Playbook) applies as a **Supporting** source, with a noted Role Ambiguity flag.

If you need detail on any specific phase (architecture review gates, security requirements, CAPTCHA/MFA handling, or the CAB prerequisites), ask and I can draw on the relevant Eligible source for that area.

Oct 4, 03:59 PM
```

### Assessment against Stage A criteria

**Overall result: FAIL.** The response selects the expected lifecycle source identities, but it does not satisfy the complete Q3 acceptance criteria.

| Criterion | Result | Evidence |
|---|---|---|
| Intended Skill loaded | Pass | CAPE explicitly returned Load Skill for RPA Development Skill — Pilot v0.1. |
| KS-006 governs the end-to-end lifecycle | Pass | The response identifies KS-006 as the governing lifecycle source. |
| KS-007 contributes only its architecture-review scope | Fail | It is initially described as complementary, but the response later attributes CAB-submission prerequisites to KS-007. The reviewed KS-007 evidence establishes prerequisites for the Architecture Review Form, not CAB submission. |
| KS-006 and KS-007 metadata preserved | Pass for stated metadata | The answer labels both sources Primary and Provisional. The supplied trace does not independently verify the metadata during this execution. |
| Ten lifecycle phases represented accurately | Fail | The response gives seven stages; it omits Project Repository Document, combines or omits UAT and the two CAB stages, and omits Hypercare as a distinct part of Hypercare & BAU Handover. |
| Unsupported lifecycle details avoided | Fail | It adds feasibility criteria (including volume and stability) and security/CAPTCHA-MFA relationships not established by the lifecycle evidence shown for this response. |
| **Overall Q3 acceptance** | **Fail** | The required lifecycle structure and source-scope accuracy are not preserved, and unsupported claims are included. |

The ten phases established in the reviewed KS-006 transcription are: Request & Approval; Discovery & Scoping; Project Repository Document; Architecture Review & Project Kickoff; Development; UAT; Internal CAB (Pre-CAB); Global CAB (Production CAB); Deployment; and Hypercare & BAU Handover. The source transcription remains in [CAPE_RPA_Development_Skill_v0.1_Live_Evaluation_Evidence.md](CAPE_RPA_Development_Skill_v0.1_Live_Evaluation_Evidence.md).

### Provenance and change-scope conclusion

Correctly naming KS-006 and KS-007 does not substantiate every claim. No source-level retrieval trace was supplied for this execution, so claim-level provenance is **not established**. Because CAPE loaded an older Skill snapshot, this result does not test the current local Change 04 instructions. Preserve the earlier Q3 results in Section 13 unchanged; do not reopen Change 03 based on this run.

This Q3 failure does not authorize the full 11-case regression. Change 04 focused verification remains pending, Change 05 remains unstarted, and the Coverage-Honesty Gate remains uncleared.

---

## 15. End-to-end review observations (2026-10-08)

### Review scope and disposition

The review assessed the pasted RPA Development Skill — Pilot v0.1 for internal consistency, evidence controls, source governance, request routing, coverage-gap behavior, response requirements, and pilot-test readiness. It confirms that the pasted text contains the corrected KG-001 scope and the bounded Change 04 section. This text review does not confirm that the same version is saved in CAPE or that runtime behavior conforms; the Stage A Q3 evidence in Section 14 shows a loaded-version discrepancy.

**Overall assessment:** the governance design is coherent and defensible. No wholesale rewrite is recommended. The observations below are review findings and proposed follow-up, not approved Skill edits or test results.

### Findings and recommendations

| Area | Review finding | Recommended disposition |
|---|---|---|
| Source governance | Keep source identity/KS-ID, Source Role, Assessment Status, Permitted Use, request-specific eligibility, and claim support distinct. **Provisional does not mean ineligible.** The governed register remains authoritative for the underlying metadata; the Skill's source list must not override it. | Preserve this distinction in instructions and tests. Reconcile any register/Skill mismatch using the governed source records, not the more permissive value. |
| Request classification | Requiring exactly one intent may be too rigid for compound requests that contain materially different subquestions. | Consider one primary intent with secondary intents where needed; this is a proposed refinement, not yet adopted. |
| Partial evidence and gaps | Partial evidence and strict stop behavior can coexist: answer only the supported part when one exists; stop when KG-001 blocks the entire requested organizational standard; decline when no eligible evidence supports a substantive answer. A reworded request must not turn a substitute AutoDrive standard into a separate general request. | Test partial-evidence cases and a clearly independent general-programming request against a disguised substitute-standard request. Preserve the corrected KG-001 wording and independent KG-003 behavior. |
| Change 03 / Q3 acceptance | Source selection alone is insufficient. Acceptance should require KS-006 to govern the lifecycle and preserve the ten documented phases in order, with Project Repository Document, both CAB stages, UAT, Deployment, and Hypercare & BAU Handover distinct. KS-007 is limited to its supported architecture-review scope; unsupported lifecycle details must not be added. | Add these as Q3 acceptance criteria before the corrected Skill is retested. The Stage A Q3 failure in Section 14 remains the observed result; this recommendation does not change source classifications or reopen the frozen source-selection implementation. |
| Change 04 provenance | Change 04 appropriately separates identity, metadata, eligibility, authority, and claim support; it does not require new visible citation formatting or claim-level attribution. Runtime provenance cannot be claimed when the execution trace does not expose the needed evidence. | Keep the Change 04 boundary. Test verifiable and unavailable metadata separately. Claim-level grounding remains Change 05. |
| Authority and response behavior | Apply source scope before declaring a conflict. Disclose material limitations, including Role Ambiguity where relevant; a generic Provisional status statement does not replace that disclosure. | Preserve the current response modes and test KS-006/KS-007 complementarity and KS-015 restrictions in actual CAPE responses. |
| Governed source counts | The review reports 44 KS-identified sources in the Trust Matrix, 20 Primary/Supporting sources in the pilot scope, and seven populated eligible sources. The local Trust Matrix and inventory files reviewed here did not verify the 44-source count; they identify the matrix as a working artifact. | Treat 44/20/7 as a reconciliation item, not a confirmed count from this review. Verify the authoritative Trust Matrix, pilot subset, and populated eligible set before revising Section 7/8 scope wording. Do not let a copied Skill table become a competing source of truth. |
| General guidance and scope | Section 4.1 permits a genuinely separate request for general, non-Inchcape guidance, while Section 8 directs declines for topics outside the validated boundary. The intended distinction should be explicit: an unsupported organizational request is declined; a clearly independent general request may be answered without presenting it as satisfying the original request. | Clarify this interaction only after the wording is approved; retain the prohibition on relabeling a KG-001 substitute as general guidance. |
| Coverage-Honesty Gate | Running Q10, Q11, Q12, and Q19 once is not sufficient to pass the gate. A demonstrated violation is FAIL; insufficient evidence is INCONCLUSIVE. Mentioning known-but-ineligible Q11 material is distinct from using it as evidence. | Preserve the gate criteria, correct failures and retest them, and record PASS/FAIL/INCONCLUSIVE from observed responses and traces. |
| Frozen pilot and version control | Any approved change to a declared Frozen pilot candidate must be recorded as a version-controlled revision; a changed configuration should not silently retain the same frozen-artifact claim. | Keep Changes 01–03 and the current Change 04 boundary frozen unless a separately approved revision is recorded. |

### Priority follow-up before broader regression

1. Verify that CAPE loads the exact current candidate, including the corrected KG-001 wording and Change 04, before running behavior tests.
2. A focused Q3 rerun has now provided new source-selection and lifecycle evidence; preserve the Stage A Q3 FAIL in Section 14 as historical and assess the new run separately in Section 16. Do not treat the new response as provenance validation.
3. Reconcile the Trust Matrix, 20-source pilot subset, and seven populated Eligible-source counts against the authoritative artifacts.
4. Decide whether to refine compound-intent handling and the Section 4.1/Section 8 general-guidance boundary; do not treat these review recommendations as implemented.
5. Complete the authorized focused tests, including the stated edge cases, and record evidence-based verdicts before considering the full 11-case regression or clearing the Coverage-Honesty Gate.

No Skill wording was changed, no new test result was produced, and the full 11-case regression remains pending as part of this review update.
At the time of this 2026-10-08 review, no Skill wording was changed or new test result produced. The full 11-case regression remains pending.

---

## 16. Focused Q3 rerun — evidence received 2026-10-14

### Test metadata

- **Test:** Q3 — RPA project lifecycle and architecture review
- **Prompt:** “What framework governs the lifecycle of an RPA project at Inchcape, and what are the main phases from request through deployment and BAU handover?”
- **Skill load evidence:** CAPE returned a `Load Skill` result naming **RPA Development Skill — Pilot v0.1**. The supplied evidence does not establish whether this was automatic routing or an explicit load.
- **Evidence date:** 2026-10-14, when the result was supplied for review. The execution timestamp and timezone were not included.
- **Scope:** Focused Q3 source-selection and lifecycle-accuracy check only. This is not the full 11-case regression and does not clear the Coverage-Honesty Gate.

### CAPE response (verbatim)

```text
Using the RPA Development Skill for this.

The governing framework is **KS-006, RPA Project Intake Framework** (Primary, Assessment Status: Provisional). It sets the end-to-end RPA delivery lifecycle, in this order:

1. Phase 1: Request & Approval
2. Phase 2: Discovery & Scoping
3. Phase 3: Project Repository Document
4. Phase 4: Architecture Review & Project Kickoff
5. Phase 5: Development
6. Phase 6: UAT
7. Phase 7: Internal CAB (Pre-CAB)
8. Phase 8: Global CAB (Production CAB)
9. Phase 9: Deployment
10. Phase 10: Hypercare & BAU Handover

**Supporting governance:** KS-007, RPA Architecture Review Framework (Primary, Provisional), applies only to Phase 4. It covers when an architecture review is required, its prerequisites, approval tiers, and authorization to begin development. It does not establish CAB requirements.

**Limitations:** The validated knowledge base confirms the phase names and order, but this answer does not include the detailed entry and exit criteria for each phase. I could not verify those from the validated set, so I have not described them.
```

### Assessment against current Q3 criteria

| Criterion | Result | Evidence |
|---|---|---|
| Intended Skill named in Load Skill result | Pass for this execution | CAPE returned Load Skill for RPA Development Skill — Pilot v0.1. Automatic routing was not established. |
| KS-006 governs end-to-end lifecycle | Pass | Response names KS-006 as the governing lifecycle framework. |
| KS-007 limited to architecture review | Pass | Response limits KS-007 to Phase 4 and explicitly says it does not establish CAB requirements. |
| All ten lifecycle phases and names in order | Pass | All ten phases appear in the documented sequence. |
| Internal CAB and Global CAB remain separate | Pass | Phases 7 and 8 are distinct. UAT, Deployment, and Hypercare & BAU Handover are also distinct. |
| Unsupported phase additions or mergers avoided | Pass | No additional lifecycle stage is introduced; missing detailed entry/exit criteria are disclosed. |
| Retrieval provenance / claim-level grounding | Not assessed | No source retrieval queries or source-level trace were supplied with this response. |
| **Focused Q3 source-selection and lifecycle criteria** | **PASS** | Required sources and all ten ordered phases are represented within the stated scope. |

### Conclusion and limits

This run provides a focused **PASS** for the current Q3 source-selection and lifecycle-accuracy acceptance criteria. It does not erase or overwrite the earlier Stage A **FAIL — Lifecycle Accuracy**, which remains historical evidence in Section 14. It does not establish automatic Skill routing, Change 04 provenance, claim-level grounding, or full Q3 validation beyond the criteria assessed here.

The Trust Matrix cross-check remains **PARTIAL / NOT PASSED**. The full 11-case regression and Coverage-Honesty Gate remain pending.

---

## 17. Documentation review closure — 2026-10-14

### Context

Following the focused Q3 result recorded in Section 16, the Rovo project context summary was cross-checked against the Confluence Implementation Record v0.1-r1 (last confirmed v42, published 2026-10-09 15:06 UTC) and the local Skill file (commit `a822fdb`) before being sent to ChatGPT for Change 04 design input. Three corrections were identified and applied to the summary. ChatGPT confirmed alignment with those corrections and closed the documentation review for the items below.

> ChatGPT note (verbatim, translated): *"The corrections are aligned with the previous observations. Based on the summary shared, we can close the documentary review of these points and advance to the Change 04 design, with one caveat: I have not directly inspected the updated Confluence version, so this confirmation refers to the described changes, not to an independent verification of the published content."*

This caveat is preserved: the confirmation covers the described changes, not a live Confluence inspection.

### Corrections applied to the Rovo summary

**Correction 1 — KS-003–010 Source Role and Assessment Status:**
Rovo's summary presented `Primary` / `Provisional` as resolved facts for KS-003–010. These values originate from Trust Matrix §26.1 (published 2026-10-13) and have not been reconciled with Implementation Record §7, which still shows `UNVERIFIED` for both fields. The corrected text qualifies both as Trust Matrix §26.1 values pending reconciliation.

**Correction 2 — KS-015 Assessment Status:**
Rovo's summary stated `Provisional + Role Ambiguity`. Implementation Record §7 lists `Role Ambiguity` only under Assessment Status; `Provisional` appears in Trust Matrix §26.1 but not separately in IR §7. The corrected text treats these as unreconciled until both pages are aligned.

**Correction 3 — Change 04 note:**
Rovo's summary included the note *"it shouldn't if the record is accurate, since Change 04 is still pending."* This is outdated: Change 04 instructions are present in the local Skill §4.3 (commit `a822fdb`). The Confluence IR still shows Change 04 as `PENDING IMPLEMENTATION` because the IR has not been updated. The corrected text reframes the question as: *which version is CAPE actually loading?*

### Engineering position as of 2026-10-14 (post-review)

| Element | Status |
|---|---|
| Q3 documentation | Historical FAIL (Section 14) and 2026-10-14 focused PASS (Section 16) preserved separately |
| Change 03 — Source Disambiguation | Implemented and frozen |
| Change 04 — KS-ID Provenance Traceability | Instructions present in local Skill §4.3; CAPE configuration verification and formal acceptance pending |
| Change 05 — Claim-Level Grounding | Pending |
| Change 06 — Controlled External Web Handling | Pending |
| Governed source reconciliation (KS-003–010) | Pending — IR §7 UNVERIFIED; Trust Matrix §26.1 not reconciled with IR or Taxonomy §11 |
| Formal 11-case regression | Pending |
| Coverage-Honesty Gate | NOT CLEARED |
| Production readiness | Not established |

### Immediate next activity

Confirm whether CAPE is loading the current local Skill text (which includes §4.3 Change 04). If it is, this constitutes the first execution under Change 04 instructions and the IR must be updated to record Change 04 as implemented. If it is not, identify the snapshot CAPE is loading and resolve the gap before running behavior tests.

---

## 18. Change 04 — Design gateway — 2026-10-14

### Context

Following the documentation review closure in Section 17, ChatGPT proposed the design scope for Change 04 — KS-ID Provenance Traceability and issued an approval gateway before proceeding to detailed specification. No changes to the active Skill and no formal regression activity are authorized until the gateway is resolved.

### Proposed design scope — five components

**Component 1 — Source identity**
Rules for associating retrieved content with a verifiable KS-ID. A KS-ID must not be assigned or inferred from topical relevance, keywords, similar titles, repository location, or search-result position.

**Component 2 — Metadata integrity**
Treatment of Source Role, Assessment Status, and Permitted Use as separate, independently verifiable attributes. Unverified values must be preserved explicitly as UNVERIFIED rather than approximated or inferred from the KS-ID or from adjacent metadata.

**Component 3 — Uncertainty control**
Required behavior when identifiers are missing, discrepancies exist between pages (e.g., Trust Matrix §26.1 vs. IR §7), or source identity cannot be confirmed. The Skill must disclose the limitation rather than silently defaulting to an assumed value.

**Component 4 — Claim traceability**
Relationship between source, evidence fragment, and supported claim, distinguishing documented facts from interpretations. This component prepares the boundary between Change 04 (provenance) and Change 05 (claim-level grounding) without conflating them.

**Component 5 — Acceptance criteria and tests**
Positive and negative test cases for Q1, Q3, Q5, Q8, Q15, Q16, and Q19, with observable results and recorded evidence. Each case must produce verifiable evidence that distinguishes implementation from intended behavior.

### Technical risk to resolve before implementation

Skill instructions alone do not guarantee that CAPE exposes source metadata that is sufficiently complete and stable to maintain verified correspondence at runtime. The design must distinguish between:

- What the Skill can enforce through its instructions (identity-check rules, uncertainty-disclosure behavior, eligibility application)
- What depends on the data and capabilities delivered by the connectors (whether KS-IDs, Source Roles, Assessment Status values, and Permitted Use are exposed in the retrieval trace at all)

This boundary must be explicit in the specification and in the acceptance criteria. If connector-level metadata is unavailable, the Skill must disclose that limitation and apply existing eligibility, coverage-gap, and response rules — not claim deterministic provenance from incomplete data.

### Approval gateway

> **Gateway question (ChatGPT, 2026-10-14):** Do you approve these five components as the design scope for Change 04? Once confirmed, the detailed specification and acceptance criteria will be prepared, without modifying the active Skill or starting the formal regression.

**Gateway status: OPEN — awaiting owner decision.**

A response of "approved" or "approved with modifications" is required before the detailed specification is drafted. Partial approval of individual components must be recorded explicitly. Do not proceed to specification or begin any Skill modification until the gateway is closed.

### What this gateway does not authorize

- Any modification to the active Skill text (§4.3 already present from commit `a822fdb` is the current implementation baseline)
- Starting the formal 11-case regression
- Claiming Change 04 as validated
- Proceeding to Change 05 design
