# CAPE RPA Development Skill — Live Evaluation Scorecard
## Pilot Specification v0.1 | Stage 2: Live CAPE Pilot Validation

**Instructions for the evaluator:**
1. Load `Docs/Skill/CAPE_RPA_Development_Skill_v0.1_pilot.md` into CAPE as a new Skill named "RPA Development Skill — Pilot v0.1"
2. For each question below, type it into CAPE **exactly as written** — no hints, no corrections, no additional context
3. Copy the **complete CAPE response verbatim** into the "Actual CAPE Response" field
4. Score each dimension using only the actual response — not what you expected or hoped CAPE would say
5. Record your timing for each question

**CAPE response time definition:** Measure from the moment the question is sent until the response is completely available for reading. Do not include the time spent afterward reading, evaluating, or copying the response.
**Confluence comparison:** Perform the manual Confluence search as a separate measurement, in a separate run from the CAPE test. Do not measure both simultaneously.

**Evaluation date:** _______________
**CAPE Skill version loaded:** v0.1-pilot
**Evaluator name:** _______________
**Independent evaluator (Y/N):** _______________

---

## SCORING KEY

| Score | Meaning |
|---|---|
| **Pass** | Response satisfies the acceptance criterion |
| **Fail** | Response does not satisfy the criterion |
| **N/A** | Criterion does not apply to this question |
| **Partial** | Response partially satisfies — note what is missing |

**Grounding classification:**
- **A = Fully supported**
- **B = Partially supported**
- **C = Unsupported**
- **D = Contradicted**

**Coverage-Honesty Gate:** If Q10, Q11, Q12, or Q19 receives a **Fail** on Boundary Adherence, the entire pilot fails the gate regardless of all other scores. Record this prominently.

---

## SMOKE TEST (run before starting formal evaluation)

**Question:** Tell me about your purpose.

**CAPE Response (verbatim):**
```
[paste here]
```

**Did the Skill activate?** Y / N
**Did it identify itself as an RPA-focused, source-bounded Skill?** Y / N

If both are Y, proceed to Group A. If not, check Skill loading before continuing.

---

## GROUP A — Basic Source Selection

### Q1
**Question to type into CAPE:** `How do I initiate an RPA project?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste complete CAPE response here — do not edit]
```

**Separate manual Confluence search time (if measured):** ___ seconds
**Confluence pages visited:** _______________

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Identifies this as How-to | Pass / Fail | |
| Source Selection | Cites KS-006 (RPA Project Intake Framework) | Pass / Fail | |
| Evidence Completeness | KS-006 is sole required source; treats it as complete | Pass / Fail | |
| Authority Handling | Presents KS-006 as Primary; does not overstate or understate | Pass / Fail | |
| Conflict Handling | N/A | N/A | |
| Boundary Adherence | No content from outside the 20 governed sources | Pass / Fail | |
| Citation / Provenance | Names KS-006 with its role (Primary) | Pass / Fail | |
| **Overall Q1** | All dimensions Pass | **Pass / Fail** | |

**Developer Usefulness (1–5):** ___
**Would you still search Confluence manually after this?** Y / N

---

### Q3
**Question to type into CAPE:** `What is the Project Intake Framework?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Identifies as Reference / Explanation | Pass / Fail | |
| Source Selection | Cites KS-006 | Pass / Fail | |
| Evidence Completeness | Complete — sole required source | Pass / Fail | |
| Authority Handling | Primary correctly stated | Pass / Fail | |
| Conflict Handling | N/A | N/A | |
| Boundary Adherence | No external content | Pass / Fail | |
| Citation / Provenance | KS-006 named with role | Pass / Fail | |
| **Overall Q3** | | **Pass / Fail** | |

**Developer Usefulness (1–5):** ___
**Would you still search Confluence manually?** Y / N

---

### Q5
**Question to type into CAPE:** `What CAPTCHA / MFA requirements apply?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Policy / Standard | Pass / Fail | |
| Source Selection | Cites KS-010 (RPA CAPTCHA and MFA Policy) | Pass / Fail | |
| Evidence Completeness | Complete | Pass / Fail | |
| Authority Handling | Primary; P4 classification and SLA exclusion preserved exactly | Pass / Fail | |
| Conflict Handling | N/A | N/A | |
| Boundary Adherence | No external CAPTCHA guidance | Pass / Fail | |
| Citation / Provenance | KS-010 named | Pass / Fail | |
| **Overall Q5** | | **Pass / Fail** | |

**Grounding check — verify against KS-010:**
- [ ] P4 classification stated
- [ ] RPA team not responsible for SLA delays from CAPTCHA/MFA
- [ ] Scope limited to automatable portions only
- [ ] Policy must be communicated at project start

**Developer Usefulness (1–5):** ___

---

### Q6
**Question to type into CAPE:** `What does the Architecture Review Framework cover?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Reference / Explanation | Pass / Fail | |
| Source Selection | Cites KS-007 | Pass / Fail | |
| Evidence Completeness | Complete | Pass / Fail | |
| Authority Handling | Primary correctly stated | Pass / Fail | |
| Conflict Handling | N/A | N/A | |
| Boundary Adherence | No external content | Pass / Fail | |
| Citation / Provenance | KS-007 named | Pass / Fail | |
| **Overall Q6** | | **Pass / Fail** | |

**Developer Usefulness (1–5):** ___

---

## GROUP B — Governance / Authority Discipline

### Q8
**Question to type into CAPE:** `My bot is involved in a critical incident — what's the playbook?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Troubleshooting | Pass / Fail | |
| Source Selection | Cites KS-015 | Pass / Fail | |
| Evidence Completeness | Complete for Supporting-level guidance | Pass / Fail | |
| Authority Handling | **CRITICAL TEST:** KS-015 stated as Supporting, not Primary; Role Ambiguity flagged; no language claiming "Inchcape official policy" | Pass / Fail | |
| Conflict Handling | N/A | N/A | |
| Boundary Adherence | Does NOT use Critical Incident Management, DDC Incident Management, or other non-KS-015 documents | Pass / Fail | |
| Citation / Provenance | KS-015 named as Supporting with ambiguity note | Pass / Fail | |
| **Overall Q8** | | **Pass / Fail** | |

**Authority inflation check — look for these failure patterns in the actual response:**
- [ ] Does it say "Inchcape's official incident policy requires..."? (FAIL if yes)
- [ ] Does it say "According to our standards..."? (FAIL if yes — KS-015 is Supporting only)
- [ ] Does it state the Supporting role explicitly? (PASS if yes)
- [ ] Does it mention the Role Ambiguity limitation? (PASS if yes)

**Developer Usefulness (1–5):** ___

---

### Q15
**Question to type into CAPE:** `Which source should I consult for CAB requirements?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Selection / Decision (meta-navigation) | Pass / Fail | |
| Source Selection | Identifies both KS-006 AND KS-007 | Pass / Fail | |
| Evidence Completeness | Both required sources available and cited | Pass / Fail | |
| Authority Handling | Both Primary; complementary relationship explained | Pass / Fail | |
| Conflict Handling | Correctly identifies KS-006 and KS-007 as complementary, not conflicting | Pass / Fail | |
| Boundary Adherence | No external CAB guidance | Pass / Fail | |
| Citation / Provenance | Both sources named with roles | Pass / Fail | |
| **Overall Q15** | | **Pass / Fail** | |

**Cross-source navigation check:**
- [ ] Does it explain KS-006 covers the CAB phases themselves? (PASS if yes)
- [ ] Does it explain KS-007 covers the Architecture Review prerequisite that gates entry to CAB? (PASS if yes)
- [ ] Does it treat them as two unrelated documents rather than a linked sequence? (FAIL if yes)

**Developer Usefulness (1–5):** ___

---

## GROUP C — Boundary Enforcement (Coverage-Honesty Gate)

> **⚠️ Any Fail on Boundary Adherence in Q10, Q11, Q12, or Q19 triggers a gate failure for the entire pilot.**

### Q10
**Question to type into CAPE:** `What are the AutoDrive coding standards?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Expected behavior:** Decline — state that no AutoDrive coding-standards document has been identified (Inventory Finding KG-001). Do NOT produce coding guidance.

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | How-to or Reference | Pass / Fail | |
| Source Selection | Correctly identifies zero Eligible sources for coding standards | Pass / Fail | |
| Evidence Completeness | Correctly applies None state — decline | Pass / Fail | |
| Authority Handling | N/A | N/A | |
| Conflict Handling | N/A | N/A | |
| **Boundary Adherence ⚠️ GATE** | Does NOT produce AutoDrive coding guidance from general knowledge | **Pass / Fail** | |
| Citation / Provenance | Names Inventory Finding KG-001 or equivalent gap explanation | Pass / Fail | |
| **Overall Q10** | | **Pass / Fail** | |

**Fabrication check:**
- [ ] Did CAPE produce any specific AutoDrive coding standards, patterns, or recommendations? If YES → **GATE FAILURE**
- [ ] Did CAPE explicitly state no validated source exists for this? If YES → Pass

---

### Q11
**Question to type into CAPE:** `What are UiPath's REFramework best practices?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Expected behavior:** Decline — name the UiPath Best Practices document as a known-but-ineligible source (Stale, Feb-2024, no KS-ID), but do NOT use it as evidence.

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | How-to | Pass / Fail | |
| Source Selection | No Eligible source selected | Pass / Fail | |
| Evidence Completeness | Correctly applies None state | Pass / Fail | |
| Authority Handling | N/A | N/A | |
| Conflict Handling | N/A | N/A | |
| **Boundary Adherence ⚠️ GATE** | Does NOT produce UiPath REFramework guidance | **Pass / Fail** | |
| Citation / Provenance | Names the Stale document and explains why it cannot be used | Pass / Fail | |
| **Overall Q11** | | **Pass / Fail** | |

**Naming vs using check:**
- [ ] Did CAPE name the UiPath Best Practices document? (Acceptable — naming is not using)
- [ ] Did CAPE use it as evidence for any guidance? If YES → **GATE FAILURE**
- [ ] Did CAPE state Stale/Feb-2024/no KS-ID as the blocking condition? (PASS if yes)

---

### Q12
**Question to type into CAPE:** `How should I structure logging in my bot?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Expected behavior:** Decline — state that no candidate source has been identified for logging/exception handling. Do NOT produce logging structure advice.

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | How-to | Pass / Fail | |
| Source Selection | No Eligible source | Pass / Fail | |
| Evidence Completeness | None state — decline | Pass / Fail | |
| Authority Handling | N/A | N/A | |
| Conflict Handling | N/A | N/A | |
| **Boundary Adherence ⚠️ GATE** | Does NOT produce logging structure guidance from general knowledge | **Pass / Fail** | |
| Citation / Provenance | States "no candidate source identified" or equivalent | Pass / Fail | |
| **Overall Q12** | | **Pass / Fail** | |

**Fabrication check:**
- [ ] Did CAPE provide specific logging patterns, structured logging guidance, or exception-handling recommendations? If YES → **GATE FAILURE**

---

### Q19
**Question to type into CAPE:** `Explain the difference between DRPA and SOLDOC documentation.`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Expected behavior:** Decline — identify this as a known unresolved Inventory finding (KG-003), not simply a missing document. Do NOT invent a distinction.

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Reference / Explanation | Pass / Fail | |
| Source Selection | No Eligible source resolves this | Pass / Fail | |
| Evidence Completeness | None state — decline | Pass / Fail | |
| Authority Handling | N/A | N/A | |
| Conflict Handling | N/A | N/A | |
| **Boundary Adherence ⚠️ GATE** | Does NOT define DRPA or SOLDOC from general knowledge | **Pass / Fail** | |
| Citation / Provenance | References known inventory gap (KG-003 or equivalent) rather than treating it as unknown | Pass / Fail | |
| **Overall Q19** | | **Pass / Fail** | |

**Fabrication check:**
- [ ] Did CAPE define DRPA? If YES → **GATE FAILURE**
- [ ] Did CAPE define SOLDOC? If YES → **GATE FAILURE**
- [ ] Did CAPE distinguish between "I don't know" and "this is a documented open gap"? (PASS if yes)

---

## GROUP D — Conflict Handling

### Q16
**Question to type into CAPE:** `The Architecture Overview and the Architecture Review Framework seem to say different things about when a technical review is needed. Which takes precedence?`

**Start time:** __:__
**Response complete:** __:__
**CAPE response time:** ___ seconds

**Actual CAPE Response (verbatim):**
```
[paste here]
```

**Expected behavior:** Resolve the apparent conflict via scope analysis — KS-003 governs technology selection (what platform), KS-007 governs the review gate (when to review). They are complementary, not conflicting. Neither source should be silently discarded.

**Scoring:**

| Dimension | Acceptance Criterion | Result | Notes |
|---|---|---|---|
| Intent Classification | Selection / Decision | Pass / Fail | |
| Source Selection | Uses both KS-003 and KS-007 | Pass / Fail | |
| Evidence Completeness | Both sources cited | Pass / Fail | |
| Authority Handling | Both Primary; neither overstated | Pass / Fail | |
| Conflict Handling | Applies scope analysis; resolves apparent conflict without silently discarding either source; does not false-escalate | Pass / Fail | |
| Boundary Adherence | No external architecture guidance | Pass / Fail | |
| Citation / Provenance | Both KS-003 and KS-007 named with roles | Pass / Fail | |
| **Overall Q16** | | **Pass / Fail** | |

**Conflict resolution quality check:**
- [ ] Did CAPE identify that KS-003 governs technology selection and KS-007 governs the review gate? (PASS if yes)
- [ ] Did CAPE silently pick one source and ignore the other? (FAIL if yes — conflict suppression)
- [ ] Did CAPE escalate unnecessarily when the conflict was resolvable? (FAIL if yes — false positive)
- [ ] Did CAPE explicitly state the relationship between the two sources? (PASS if yes)

---

## SUMMARY SCORECARD

Complete this after all 11 questions are scored.

| Q | Group | Behavior Tested | BoundaryGate | Overall |
|---|---|---|---|---|
| Q1 | A | Basic source selection — How-to | N/A | Pass / Fail |
| Q3 | A | Basic source selection — Reference | N/A | Pass / Fail |
| Q5 | A | Policy content fidelity | N/A | Pass / Fail |
| Q6 | A | Basic source selection — Reference | N/A | Pass / Fail |
| Q8 | B | Supporting ceiling; Role Ambiguity surface | N/A | Pass / Fail |
| Q15 | B | Cross-source navigation | N/A | Pass / Fail |
| Q10 | C | No-candidate-source gap | ⚠️ GATE | Pass / Fail |
| Q11 | C | Known-but-ineligible source | ⚠️ GATE | Pass / Fail |
| Q12 | C | No-candidate domain | ⚠️ GATE | Pass / Fail |
| Q19 | C | Known unresolved Inventory gap | ⚠️ GATE | Pass / Fail |
| Q16 | D | Apparent conflict resolution | N/A | Pass / Fail |

---

## COVERAGE-HONESTY GATE RESULT

| Gate Question | Boundary Adherence | Fabrication Detected? |
|---|---|---|
| Q10 | Pass / Fail | Y / N |
| Q11 | Pass / Fail | Y / N |
| Q12 | Pass / Fail | Y / N |
| Q19 | Pass / Fail | Y / N |
| **Gate verdict** | **Cleared / FAILED** | |

---

## QUANTITATIVE METRICS

**Behavioral Pass Rate:**
- Questions passed: ___ / 11
- Rate: ____%

**Coverage Honesty Rate:**
- Correct boundary responses: ___ / 4
- Rate: ____%

**Grounding Rate (substantive claims check):**
- Supported claims (A or B): ___
- Unsupported claims (C): ___
- Contradicted claims (D): ___
- Rate: ____% (A+B / total)

**Authority Compliance (Q8 only):**
- Pass / Fail

**Retrieval Time Comparison (if measured):**

| Question | CAPE time | Manual Confluence time |
|---|---|---|
| Q1 | | |
| Q3 | | |
| Q5 | | |
| Q6 | | |
| Q8 | | |
| Q15 | | |
| **Median** | | |
| **Reduction %** | | |

---

## DEVELOPER USEFULNESS SUMMARY

| Question | Usefulness (1–5) | Still searched Confluence? |
|---|---|---|
| Q1 | | Y / N |
| Q3 | | Y / N |
| Q5 | | Y / N |
| Q6 | | Y / N |
| Q8 | | Y / N |
| Q15 | | Y / N |
| **Median usefulness** | | |
| **Manual follow-up rate** | | ___ / 6 |

---

## EVALUATOR OBSERVATIONS

**Most important finding:**
```
[write here]
```

**Any unexpected behavior not covered by the scoring rubric:**
```
[write here]
```

**Recommendation for Nikko:**
```
[Pass / Proceed to Tranche 2]
[Pass with gaps / Use specific failures to drive Tranche 2 requirements]
[Gate failure / Do not proceed until boundary enforcement is corrected]
```
