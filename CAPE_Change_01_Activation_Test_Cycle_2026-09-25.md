# CAPE Change 01 — Activation Test Cycle

## 1. Test purpose

This document registers the Iteration 2 test cycle for **Change 01 — Skill activation and contextual activation**.

The purpose of this cycle is narrow:

> Determine whether the revised Skill activates for clearly relevant Inchcape RPA requests, remains inactive for generic technical requests, and activates when the conversation establishes RPA context even if the immediate question is generic.

This cycle evaluates activation behavior only. It does not redesign Change 01, modify Change 02, or close the separate evidence-boundary and claim-level-grounding investigations.

## 2. Test conditions

- **Evaluation date:** 2026-09-25
- **Environment:** CAPE
- **Skill version:** RPA Development Skill — Pilot v0.1
- **Implementation under test:** Change 01
- **Evaluator:** Juan José Restrepo
- **Conversation control:** New CAPE conversation per test where applicable
- **Prompt control:** Exact prompts used; no activation hints added
- **Evidence captured:** Prompt, CAPE response, Skill load indication, and observable behavior
- **Test status:** Partial cycle recorded

## 3. Scope of the results received

The results supplied for this registration contain:

- five negative activation controls: N1-N5;
- two contextual activation controls: C1-C2.

The five positive activation controls for this cycle are recorded as pending because their raw executions were not included in the supplied results:

- Q3
- Q6
- Q10
- Q15
- Q16

This document therefore reports only what the supplied evidence demonstrates.

---

## 4. Control summary

| Test ID | Control type | Skill expected to activate? | Skill observed | Result | Interpretation |
|---|---|---:|---:|---|---|
| N1 | Generic Python | No | No | Pass | Technical terminology alone did not activate the Skill |
| N2 | Generic API | No | No | Pass | Python, API, authentication, and logging did not activate the Skill |
| N3 | Generic architecture | No | No | Pass | Generic architecture terminology did not activate the Skill |
| N4 | Generic security | No | No | Pass | Generic security terminology did not activate the Skill |
| N5 | Generic automation | No | No | Pass | Generic automation terminology did not activate the Skill |
| C1 | Established Inchcape RPA context | Yes | Yes | Pass | Skill activated from established RPA/AutoDrive context |
| C2 | Contextual RPA terminology | Yes | Yes | Pass | Skill activated for an automation/CAB question without requiring the literal term RPA |
| Q3 | Positive RPA control | Yes | Pending | Pending | Raw result not included in this submission |
| Q6 | Positive RPA control | Yes | Pending | Pending | Raw result not included in this submission |
| Q10 | Positive RPA boundary control | Yes | Pending | Pending | Raw result not included in this submission; separate Q10 boundary evidence remains relevant |
| Q15 | Positive RPA control | Yes | Pending | Pending | Raw result not included in this submission |
| Q16 | Positive RPA cross-source control | Yes | Pending | Pending | Raw result not included in this submission |

---

## 5. Negative activation controls

### N1 — Generic Python

**Exact prompt:**

> How should I structure a Python project with modules, type hints, tests, and configuration management?

**Expected behavior:** The RPA Development Skill should not activate.

**Observed behavior:** CAPE treated this as a general Python best-practices request and did not load the RPA Development Skill.

**Result:** Pass.

**Evidence interpretation:** The presence of Python, modules, type hints, tests, and configuration management was not sufficient to establish Inchcape RPA context.

### N2 — Generic API

**Exact prompt:**

> What is a good way to design a Python REST API with authentication, validation, error handling, and logging?

**Expected behavior:** The RPA Development Skill should not activate.

**Observed behavior:** CAPE treated this as a general technical API-design request and did not load the RPA Development Skill.

**Result:** Pass.

**Evidence interpretation:** Python, API, authentication, and logging terminology alone did not trigger the Skill.

### N3 — Generic architecture

**Exact prompt:**

> What factors should I consider when deciding whether a software component should be a monolith or a set of services?

**Expected behavior:** The RPA Development Skill should not activate.

**Observed behavior:** CAPE treated this as a general software architecture question and did not load the RPA Development Skill.

**Result:** Pass.

**Evidence interpretation:** Generic architecture terminology was correctly distinguished from Inchcape RPA architecture context.

### N4 — Generic security

**Exact prompt:**

> What are good practices for securely storing application credentials and secrets in a Python application?

**Expected behavior:** The RPA Development Skill should not activate.

**Observed behavior:** CAPE treated this as general Python security guidance and did not load the RPA Development Skill.

**Result:** Pass.

**Evidence interpretation:** The existence of RPA security knowledge in the Skill did not cause activation without established RPA context.

### N5 — Generic automation

**Exact prompt:**

> How can I automate a repetitive Windows desktop task using Python?

**Expected behavior:** The RPA Development Skill should not activate.

**Observed behavior:** CAPE treated this as general Python desktop automation and did not load the RPA Development Skill.

**Result:** Pass.

**Evidence interpretation:** The ambiguous word automation was correctly insufficient by itself to activate the Skill.

---

## 6. Contextual activation controls

### C1 — RPA context established, generic immediate question

**Context established first:**

> I'm working on an Inchcape RPA automation using AutoDrive.

**Follow-up prompt:**

> How should I structure the Python modules?

**Expected behavior:** The RPA Development Skill should activate because the conversation establishes Inchcape RPA and AutoDrive context, even though the immediate question is generic Python.

**Observed behavior:** CAPE loaded the RPA Development Skill, identified the AutoDrive coding-standard gap, and declined to provide unsupported internal guidance.

**Result:** Pass.

**Boundary observation:** This result is especially important because the response did not use general Python practice as a substitute for missing AutoDrive standards. It reported KG-001 and directed the user to the authoritative RPA or AutoDrive owner.

### C2 — RPA terminology without explicitly saying RPA

**Exact prompt:**

> For the automation we're preparing for CAB, which framework determines whether we need an architecture review?

**Expected behavior:** The RPA Development Skill should activate because the CAB and architecture-review context establishes an Inchcape RPA request without requiring the literal term RPA.

**Observed behavior:** CAPE loaded the RPA Development Skill and correctly identified:

- KS-007 as the Primary source for architecture-review requirements;
- KS-006 as the complementary source for intake and CAB lifecycle requirements;
- the two sources as complementary rather than conflicting.

**Result:** Pass.

---

## 7. Metrics

### Negative activation rate

The negative activation rate is calculated as:

`Incorrectly activated negative controls / negative controls executed`

- Incorrectly activated controls: **0**
- Negative controls executed: **5**
- **Negative activation rate: 0/5 = 0%**

Lower is better for this metric. The observed result is consistent with the intended activation boundary.

### Contextual activation

- C1: **Activated correctly**
- C2: **Activated correctly**
- Contextual activation result: **2/2 = 100%** for the supplied contextual cases

### Positive activation rate

The positive activation rate cannot be calculated for this cycle from the supplied evidence because the raw results for Q3, Q6, Q10, Q15, and Q16 were not included here.

The previously recorded positive results must remain separate from this cycle unless the corresponding raw evidence is attached to this document.

---

## 8. Current assessment of Change 01

### Preliminary result: successful for the tested controls

The supplied evidence demonstrates that Change 01:

- avoids inappropriate activation for five generic technical requests;
- activates correctly in both supplied contextual RPA cases;
- recognizes established RPA context even when the immediate question is generic;
- recognizes RPA context without requiring the literal word RPA;
- preserves the KG-001 boundary in contextual case C1.

This is strong preliminary evidence that Change 01 improved activation precision and contextual activation behavior.

### Limitation

This is not yet a complete activation-cycle verdict because the five positive controls Q3, Q6, Q10, Q15, and Q16 still require their raw execution evidence for this specific cycle.

The results also do not close the separate Q10 evidence-boundary investigation. Correct activation is necessary but does not by itself prove that every subsequent answer remains evidence-bounded.

---

## 9. Decision and next step

- **Change 01:** Keep under test; do not redesign based on these results.
- **Change 02:** Do not modify based on this activation cycle alone.
- **Negative controls:** Preliminary pass, 0/5 inappropriate activations.
- **Contextual controls:** Pass, 2/2 correct activations.
- **Positive controls:** Pending raw evidence for Q3/Q6/Q10/Q15/Q16.
- **Next evidence needed:** Complete the five positive controls under the same test conditions and attach the actual CAPE responses and tool traces.

---

## 10. Evidence preservation rule

For every test, preserve:

1. Exact prompt.
2. Complete CAPE response.
3. Explicit Skill load indication.
4. Relevant tool trace.
5. Screenshot when useful.
6. Pass/fail observation based on the actual execution.

The actual CAPE response and tool trace are the evidence. This document does not treat an expected result as an observed result.
