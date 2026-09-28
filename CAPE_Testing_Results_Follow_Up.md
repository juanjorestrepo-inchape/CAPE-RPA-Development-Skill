# CAPE Testing Results Register — Follow-up Evaluation

## Executive Summary

The latest CAPE validation run shows a clear improvement in activation behavior compared with the original pilot. The RPA Development Skill now activates correctly for the tested RPA scenarios and stays inactive for generic technical requests, which confirms that Change 01 materially improved the activation path.

The main remaining issue is not activation itself. The key failure is in Q10, where the skill still crosses the evidence boundary and offers generic AutoDrive/Python guidance despite the absence of a validated AutoDrive coding-standard source. This means the next hardening focus is evidence-boundary enforcement and claim-level grounding.

Current status by test:

- Q3: Review required
- Q6: Review required
- Q10: Fail
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

This table is the quick view of the validation run.

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

## 9. Outcome

### Current validation status
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
This result moves the diagnosis forward: activation is no longer the primary problem, but evidence-boundary enforcement and claim-level grounding remain independent control points that still need hardening. The most important failing test remains Q10, while Q16 is the clearest positive validation case from this round.
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
