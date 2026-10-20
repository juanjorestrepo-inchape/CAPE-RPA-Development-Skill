# Change 07 — Developer Efficiency Measurement and Pilot Value Validation

**CAPE RPA Development Skill · Pilot Value Validation · Measurement Protocol v0.1 · 20 October 2026**

**Status:** `PROPOSED — PENDING APPROVAL`
**Author:** Juan José Restrepo Rosero
**Document role:** Canonical protocol for Change 07. Task Bank: [`CAPE_Change_07_Task_Bank_v0.1.md`](CAPE_Change_07_Task_Bank_v0.1.md). Project register: [`Tests/CAPE_Testing_Results_Follow_Up.md`](Tests/CAPE_Testing_Results_Follow_Up.md) §20 and §22.

This document defines the measurement protocol only. It does not execute the pilot, does not record measurements, does not assert an efficiency improvement, and does not modify the active Skill, source classifications, Trust Matrix, Knowledge Taxonomy, Knowledge Inventory, or the Coverage-Honesty Gate.

---

## 0. Document control and starting position

| Field | Value |
|---|---|
| **Protocol version** | v0.1 (draft, not frozen) |
| **Protocol status** | `PROPOSED — PENDING APPROVAL` |
| **Measurement status** | Not started |
| **Baseline status** | Not measured |
| **Total executions to date** | 0 |
| **Target sample** | 10 matched pairs / 20 executions |
| **Prepared task bank** | 3 proposed pairs / 6 executions |
| **Acceptance threshold** | Proposed, not approved |
| **Coverage-Honesty Gate** | `NOT CLEARED` (unchanged by this document) |
| **Implementation Record** | Latest verified state v55; Document Control `v0.1 / Revision v0.1-r4` |
| **Confluence impact** | None — no Confluence page or version is changed by this document |

### 0.1 Project status at the time of writing

These are recorded facts about the project, not results of this protocol:

- Change 07 concerns **Developer Efficiency Measurement and Pilot Value Validation**.
- The pilot target remains **10 matched pairs / 20 total executions**.
- **No efficiency baseline has been measured.**
- **No CAPE-versus-no-CAPE comparison has been executed** under this protocol.
- The proposed **30% reduction in active resolution time is a target, not a demonstrated result.**
- The acceptance threshold and several experimental controls **remain pending review and approval**.
- Measurements **must not start** until the protocol is approved and frozen.
- The existing Task Bank contains **three proposed pairs / six executions**, not ten pairs. The additional seven pairs must be prepared and reviewed before execution, unless an explicit documented decision changes the sample size.
- The Coverage-Honesty Gate remains **`NOT CLEARED`**.
- The Implementation Record's latest verified state is **v55**, with Document Control `v0.1 / Revision v0.1-r4`. This task does not change Confluence and does not advance that revision.

### 0.2 Separation of status classes

The protocol keeps four classes of statement separate. No statement may be promoted from one class to another without the approval gate in §9.

| Class | Meaning | Location in this document |
|---|---|---|
| **Project status** | Verified facts about the project at a point in time | §0.1, §0.2, §11 |
| **Proposed decisions** | Rules drafted for review; not binding | §2–§9, marked *Proposed* |
| **Approved decisions** | Rules explicitly approved and frozen | §9 gate; currently empty |
| **Measured results** | Observations produced by executed, approved runs | None exist; §8 defines how they would be reported |

### 0.3 Explicit non-claims

This document does **not** claim that:

- the CAPE Skill reduces resolution time by 30% or by any other amount;
- a baseline or a comparison run has been performed;
- the Task Bank is complete, approved, or frozen;
- the eight-dimension rubric or its acceptance threshold has been approved;
- the Coverage-Honesty Gate is cleared, or that Change 07 clears it;
- any Confluence page, Implementation Record revision, Trust Matrix entry, or source classification has been updated;
- the pilot is production-ready or that results generalize beyond the sampled tasks.

---

## 1. Objective and evaluation question

**Objective:** Evaluate whether use of the CAPE RPA Development Skill reduces RPA developers' **active time** to resolve eligible knowledge tasks, **without** reducing answer quality or violating source, security, or governance boundaries.

**Primary evaluation question:**

> For matched knowledge tasks drawn from the pilot's governed source scope, does resolving the task with CAPE and the RPA Development Skill active require less developer active time than resolving the same task through the developer's normal authorized knowledge-retrieval workflow, while maintaining equivalent or better answer quality and boundary compliance?

**Secondary questions (reported separately, never merged into the primary metric):**

1. Does the quality acceptance rate differ between conditions?
2. How often does CAPE/Skill activation fail, and what is the effect on the recorded outcome?
3. What rework is required after submission in each condition?
4. Which task domains show the largest or smallest time difference?

The 30% reduction figure is the **sponsor-aligned target threshold** for this pilot. It is a hypothesis to be tested, not an assumption built into the measurement.

---

## 2. Experimental design

### 2.1 Design summary

| Element | Design |
|---|---|
| **Design type** | Matched-pair comparison, within-participant |
| **Conditions** | `NO_CAPE` (baseline) and `CAPE` |
| **Target pairs** | 10 |
| **Executions per pair** | 2 (one per condition) |
| **Target total executions** | 20 |
| **Task pairing** | Same task definition and expected outcome in both conditions within a pair, unless an explicitly approved methodology specifies equivalent task variants |
| **Participant** | Same participant for both executions of a pair during the initial pilot |
| **Order** | Recorded for every pair; randomized or counterbalanced where practical |
| **Time limit** | 10 minutes active time per execution |
| **Primary metric** | Total active time per condition, valid comparable set only |

### 2.2 Rules

1. **Ten pairs, twenty executions.** The sample target is fixed at 10 pairs unless an explicit, documented decision by the approving owner changes it. A smaller sample must be reported as a deviation, not presented as the planned design.
2. **Comparable task definition.** Within a pair, both conditions use the same task definition and the same expected outcome. If variant tasks are used, the variants must be approved as equivalent before execution, and the equivalence rationale must be recorded. Unapproved variants make the pair non-comparable.
3. **Condition order.** The order in which the two conditions are executed is recorded for every pair. Order is randomized or counterbalanced where practical. Because the same participant performs both executions, task familiarity and carryover are recognized limitations and must be disclosed in the analysis; they are not eliminated by this design.
4. **Same participant.** The initial pilot uses one participant per matched pair. Introducing a different participant for one condition requires a formal protocol revision, because it changes the comparison from within-participant to between-participant.
5. **Activation failure is data.** A CAPE activation failure is recorded as an observed outcome. It is not a reason to discard the execution, repeat it silently, or replace it with a successful run.
6. **No execution before approval.** Execution does not start until the ten pairs, experimental controls, scoring rubric, data schema, and analysis method have been approved and the protocol is frozen (§9).
7. **No protocol changes during execution.** Scoring rules, critical-failure definitions, and exclusion rules are fixed before the first execution. Retrospective changes after viewing results are prohibited; any necessary change forces a new protocol version and invalidates prior runs under the old version.
8. **One task, one condition.** A task instance is executed once per condition. Repeating an execution to obtain a better time is prohibited; a repeat is only permissible as a replacement for an execution formally classified `INVALID`, and both the invalid run and the replacement are retained in the log.

### 2.3 Known design limitations

| Limitation | Effect | Treatment |
|---|---|---|
| Small sample (10 pairs) | Low statistical power | Report descriptively; no broad organizational claims |
| Within-participant order effects | Familiarity may favor the second condition | Record order; counterbalance; disclose |
| Single participant per pair | Participant skill dominates | Disclose; do not generalize to the developer population |
| Task selection bias | Tasks may favor CAPE's indexed scope | Approved task bank; document source coverage per task |
| Source volatility | Confluence content may change between conditions | Record page IDs and versions per execution |
| Measurement reactivity | Timing may alter normal behavior | Fixed 10-minute limit; same evidence rules in both conditions |

---

## 3. No-CAPE baseline conditions

The baseline must be reproducible by another reviewer using the same task definition and the same allowed sources.

### 3.1 Permitted workflow

The participant uses their **normal authorized knowledge-retrieval workflow**:

1. Start at the **agreed Confluence search entry point**.
2. Use only **approved internal documentation** and **authorized linked pages**.
3. Use the **read-only Service Desk** only when the task makes it relevant and the participant is authorized to view it.
4. Record every source consulted or cited, with page ID, version, and URL where available.

### 3.2 Prohibited assistance

During a `NO_CAPE` execution the participant must not use:

- CAPE;
- the RPA Development Skill;
- any other generative AI system;
- prepared answers, prior written solutions, or cached results;
- colleague or SME assistance;
- any source outside the approved internal documentation set.

If prohibited assistance is used, the execution is classified `INVALID` and retained in the log with the reason recorded.

### 3.3 Source scope rules

- Permitted Confluence spaces must be **defined and approved before execution**. Until that list is approved, the baseline cannot be executed.
- Duplicate and non-canonical pages are handled by the approved rule. Accessibility does **not** establish canonical status: a page used in the pilot must not be assumed canonical merely because it was reachable. Where canonical identity is unreconciled (for example KS-010, DRPA page `7308640261` versus SOLDOC page `8847753943`), the pair cannot be scored for source authority until the approval owner records the treatment.
- The same task definition, expected outcome, time limit, and evidence requirements apply in both conditions. The baseline is not permitted a looser evidentiary standard.

### 3.4 Baseline validity conditions

A baseline execution is valid only if:

- no prohibited assistance was used;
- the start and end times and interruptions are recorded;
- the outcome is one of the defined outcome statuses (§5);
- sources consulted are recorded at the metadata level required by §7.

---

## 4. CAPE condition

### 4.1 Activation recording

For every `CAPE` execution, record:

- whether CAPE was available;
- whether the **RPA Development Skill** was loaded;
- whether the Skill was auto-routed or explicitly invoked;
- the Skill version or file reference in use;
- the activation result: `ACTIVATED`, `ACTIVATION_FAILED`, or `NOT_APPLICABLE`.

If activation fails, record the failure, the observed behavior, and the resulting outcome. Follow the approved classification rule (§5.5). Do not quietly replace the run with a successful one, and do not report the failure only in narrative notes.

### 4.2 What counts as active time

Active time includes:

- time spent formulating the query or search;
- time spent searching and opening sources;
- time spent reading and interpreting content;
- time spent verifying source identity, authority, and version;
- time spent correcting or reworking the answer before submission;
- time spent deciding that the correct behavior is to refuse, escalate, or declare a knowledge gap.

Active time excludes:

- interruptions (recorded separately, §5.3);
- scheduled breaks;
- time waiting on an unrelated system outage, recorded as an interruption with its cause.

### 4.3 Quality protection

- A fast answer is not a successful answer. An unsupported or invented answer fails the rubric regardless of elapsed time.
- Time spent verifying sources is part of the measured workload, not overhead to be omitted.
- If CAPE produces an answer the participant must correct, the correction time counts toward active time and the rework indicator is set.

---

## 5. Timing and execution outcomes

### 5.1 Timing rules

| Field | Rule |
|---|---|
| **Maximum active time** | 10 minutes (600 seconds) per execution |
| **Start time** | When the participant begins the task after reading the prompt |
| **End time** | When the participant declares the answer complete, or when the limit is reached |
| **Active time** | End − start − recorded interruption time |
| **Interruptions** | Recorded with start, end, duration, and cause; excluded from active time |
| **Evidence** | Times recorded to the second from a single clock source per execution |

### 5.2 Outcome taxonomy

| Outcome | Definition |
|---|---|
| `RESOLVED` | The participant submitted a complete answer to the task, including a correct evidence-based conclusion that the knowledge does not exist or must be escalated |
| `UNRESOLVED` | No complete answer was submitted within the limit, or the participant concluded the task could not be answered and that conclusion was not the task's correct expected outcome |
| `INTERRUPTED` | The execution was stopped and not resumed within the approved resumption window (§5.4) |
| `INVALID` | The execution violated the protocol (prohibited assistance, wrong condition, unapproved source, unrecorded timing) |

`RESOLVED` and `UNRESOLVED` are the only outcomes used in the primary time analysis. `INTERRUPTED` and `INVALID` are recorded, reported as exclusions, and never silently deleted.

### 5.3 Time-limit rule

When an execution reaches 600 seconds without a complete answer:

- outcome = `UNRESOLVED`;
- termination reason = `TIME_LIMIT`;
- recorded active time = exactly **600 seconds**;
- no resolution time beyond the limit is invented, estimated, or extrapolated.

A partial answer produced at the limit is retained as evidence and scored, but the execution remains `UNRESOLVED` and the time-compliance dimension fails.

### 5.4 Interruption rule

- The timer stops for the duration of the interruption.
- If the participant resumes and completes the task, the execution remains a single execution with recorded interruption time.
- If the participant does not resume within the approved resumption window, the execution is classified `INTERRUPTED` and excluded from the primary analysis, with the exclusion reported.
- The resumption window is an experimental control that must be approved before execution; it is not defined by this draft.

### 5.5 Invalid and activation-failure classification

| Case | Classification | Primary analysis treatment (proposed) |
|---|---|---|
| CAPE unavailable or Skill not loaded, participant still answers from authorized sources | `RESOLVED` or `UNRESOLVED`, flagged `ACTIVATION_FAILED` | Retained in the CAPE condition as observed (intention-to-treat); no replacement |
| CAPE unavailable and participant falls back to the no-CAPE workflow | `INVALID` | Excluded from the primary analysis; reported as a protocol violation |
| Prohibited assistance used in either condition | `INVALID` | Excluded; reported |
| Wrong task, wrong order not matching the log, or unrecorded timing | `INVALID` | Excluded; reported |
| Execution interrupted and not resumed | `INTERRUPTED` | Excluded; reported |
| Execution cancelled before any work began | Not counted as an execution | Recorded as a non-start with reason |

These treatments are **proposed**, must be approved before execution, and must be applied identically to both conditions.

### 5.6 Unresolved versus failure

`UNRESOLVED` is not automatically a quality failure. For a task whose correct expected outcome is a documented knowledge gap (for example KG-001), a correct evidence-based refusal or escalation is recorded as `RESOLVED`, because the participant reached the task's expected conclusion. Conversely, an inability to answer a task that has an available authoritative source is `UNRESOLVED` and is a quality-relevant outcome. The distinction is scored in §6.1 dimensions 1, 3, and 5.

---

## 6. Proposed eight-dimension quality rubric

Scoring is **binary**: pass = 1, fail = 0. No partial credit. Maximum score = 8.

### 6.1 Dimensions and operational definitions

| # | Dimension | Pass condition | Observable pass example | Observable fail example |
|---:|---|---|---|---|
| 1 | **Correctness** | The answer reaches the correct, source-backed conclusion for the task and contains no false or invented Inchcape policy | States that the Scrum Master schedules the kickoff call, matching KS-006 | States that the developer schedules the kickoff call |
| 2 | **Completeness** | The answer covers at least 75% of the task's approved expected key points | Covers 5 of 5 key points for Pair 1 | Covers 2 of 5 key points |
| 3 | **Source identification** | The answer identifies the correct governed source (KS-ID and/or page), or for a declared gap identifies the gap itself | Cites KS-006 and the corresponding Confluence page | Answers without identifying any source, or cites an unrelated page |
| 4 | **Source authority** | The answer applies the correct source role and scope; Primary sources are not displaced by Supporting sources, and a declared gap is not treated as a source | Uses KS-010 policy text for policy requirements | Uses a general Python style guide as the authority for an Inchcape requirement |
| 5 | **Boundary compliance** | The answer stays within documented evidence and does not assert requirements beyond the source or fill a declared gap | Says the validated source does not define MFA technical controls | Invents an exception-approval route not present in any governed source |
| 6 | **No invented guidance** | The answer does not synthesize Inchcape requirements from general knowledge, informal practice, or ineligible content | Declines to state AutoDrive coding standards because none are validated | Drafts "recommended" Inchcape AutoDrive standards from general practice |
| 7 | **Rework status** | The answer is usable as submitted and requires no material correction before use | Answer could be used in the project without edits | Answer requires factual correction before it can be used |
| 8 | **Time compliance** | An acceptable answer is reached within the 10-minute limit | Complete answer submitted at 7:12 | Limit reached with no complete answer |

### 6.2 Proposed acceptance rule

A task execution is **accepted** only if:

1. the total score is **at least 6 of 8**;
2. **Correctness (1)** and **Boundary compliance (5)** both pass;
3. no predefined **critical failure** occurred (§6.3).

A score of 6/8 never overrides a critical failure, and a mandatory dimension failure fails the execution regardless of the total. **This threshold is proposed, not approved.** It must be confirmed by the approval owner before the protocol is frozen.

### 6.3 Critical failures (proposed veto list)

A critical failure vetoes acceptance regardless of total score:

- inventing an Inchcape policy, standard, approval path, or source that is not documented;
- treating a declared knowledge gap as resolved;
- using CAPE during a `NO_CAPE` execution;
- bypassing the documented source boundary, or presenting general practice as an Inchcape-approved requirement;
- ignoring the 10-minute limit, or recording an unresolved task as successfully completed;
- presenting a faster but incorrect or unsupported answer as successful completion;
- presenting an unsupported Inchcape-specific requirement as fact;
- materially violating source-authority or knowledge-boundary rules.

This list must be ratified, and any additional veto conditions must be added, **before** execution begins. It may not be extended after results are known.

### 6.4 Edge-case scoring (must be fixed before freeze)

| Case | Proposed scoring rule |
|---|---|
| Correct, evidence-based refusal or escalation (documented gap) | `RESOLVED`; dimensions scored normally; no automatic fail |
| Incorrect inability to answer an available task | `UNRESOLVED`; Correctness = 0; Time compliance = 0; accepted = no |
| Timed out with partial answer | `UNRESOLVED`; Time compliance = 0; content dimensions scored on the partial answer; accepted = no |
| Timed out with no answer | `UNRESOLVED`; all dimensions = 0 |
| Interrupted and not resumed | Not scored for acceptance; excluded and reported |
| Activation failure with an answer | Scored normally as produced; activation failure reported separately |
| Activation failure with no answer | `UNRESOLVED`; all dimensions = 0 |
| `INVALID` execution | Not scored for acceptance; excluded and reported with reason |

These rules are proposed and must be approved before the protocol is frozen. They must not be changed retroactively after results are visible.

---

## 7. Data log and evidence

The log must allow an independent reviewer to reproduce the comparison without access to the participant's machine.

### 7.1 Required schema

| Field | Type / allowed values | Required |
|---|---|---|
| `protocol_version` | e.g. `v0.1`; frozen runs use the frozen version and commit hash | Yes |
| `execution_id` | `C07-P<nn>-<NO_CAPE\|CAPE>-<seq>` | Yes |
| `pair_id` | `P01`–`P10` | Yes |
| `task_id` | Identifier from the approved Task Bank | Yes |
| `task_domain` | Approved domain label (e.g. lifecycle, security, knowledge gap) | Yes |
| `task_intent` | Short description of what the task asks | Yes |
| `expected_outcome` | Approved expected key points reference | Yes |
| `condition` | `NO_CAPE` \| `CAPE` | Yes |
| `condition_order` | `1` or `2` (position within the pair) | Yes |
| `participant_id` | Approved non-sensitive label (e.g. `DEV-01`) | Yes |
| `execution_date_time` | ISO 8601 with timezone | Yes |
| `cape_available` | `YES` \| `NO` | CAPE only |
| `skill_loaded` | `YES` \| `NO` \| `UNKNOWN` | CAPE only |
| `activation_mode` | `AUTO` \| `EXPLICIT` \| `NOT_APPLICABLE` | CAPE only |
| `activation_status` | `ACTIVATED` \| `ACTIVATION_FAILED` \| `NOT_APPLICABLE` | Yes |
| `skill_version` | Version or file reference in use | CAPE only |
| `start_time` / `end_time` | ISO 8601 | Yes |
| `active_time_seconds` | Integer; 600 maximum | Yes |
| `interruption_seconds` | Integer; 0 if none | Yes |
| `interruption_log` | List of start, end, duration, cause | If any |
| `termination_reason` | `ANSWERED` \| `TIME_LIMIT` \| `INTERRUPTED` \| `PROTOCOL_VIOLATION` \| `TOOL_FAILURE` | Yes |
| `outcome` | `RESOLVED` \| `UNRESOLVED` \| `INTERRUPTED` \| `INVALID` | Yes |
| `sources_consulted` | List with page ID, version, URL, KS-ID where known | Yes |
| `sources_cited` | List with page ID, version, URL, KS-ID where known | Yes |
| `quality_dim_1..8` | `0` \| `1` each | Yes, if scored |
| `quality_total` | Integer 0–8 | Yes, if scored |
| `accepted` | `YES` \| `NO` | Yes, if scored |
| `critical_failure` | `YES` \| `NO` | Yes |
| `critical_failure_reason` | Controlled reason code plus note | If `YES` |
| `rework_indicator` | `YES` \| `NO` | Yes |
| `rework_description` | Short note | If `YES` |
| `reviewer_notes` | Free text, factual only | Yes |
| `deviation` | Protocol deviation reference or `NONE` | Yes |
| `evidence_location` | Reference to the approved evidence store | Yes |

### 7.2 Data-handling rules

- Do **not** commit credentials, access tokens, personal or sensitive data, production records, or confidential source content to this repository.
- Store only **approved metadata and evidence references**; keep raw evidence in the approved controlled location referenced by `evidence_location`.
- Participant identity is represented only by an approved non-sensitive label.
- Retention period and destruction method are **pending approval** and must be recorded before execution.
- Quoting governed source text is limited to the minimum needed to justify a score.

---

## 8. Analysis method

### 8.1 Primary efficiency formula

```
Efficiency reduction (%) =
    (Total baseline active time − Total CAPE active time)
    ------------------------------------------------------ × 100
                Total baseline active time
```

Where:

- totals are computed over the **approved comparable task set** only;
- the same inclusion and exclusion rules are applied to both conditions;
- `UNRESOLVED` and timed-out executions contribute their recorded active time, capped at 600 seconds, in both conditions;
- `INTERRUPTED` and `INVALID` executions are excluded from both conditions' totals and reported as exclusions.

### 8.2 Mandatory reporting alongside the result

Every reported figure must be accompanied by:

1. the number of valid pairs included;
2. the number of excluded or deviating executions, with reasons;
3. per-pair active times for both conditions;
4. the **quality acceptance result**, reported separately from the time reduction;
5. the activation-failure count and its treatment;
6. the sample size and the limitations in §2.3;
7. the protocol version and freeze reference.

### 8.3 Guards and prohibitions

- **No calculation if total baseline active time is zero.** Report the condition as not analyzable.
- Do not claim an efficiency improvement if quality or boundary requirements fail, even where the time reduction is large.
- Do not report a single aggregate percentage without the pair-level data and exclusion count.
- Do not impute missing times, exclude inconvenient slow runs, or treat a timed-out execution as zero.
- Do not make broad statistical or organizational claims from this small initial pilot. No significance testing is planned at n = 10; any inferential statement must be explicitly labeled as exploratory and unpowered.
- The **30% target is treated as achieved only if** the approved analysis supports it **and** the quality acceptance criteria are met. Meeting the time threshold alone does not establish value.

### 8.4 Proposed supplementary views (not the primary metric)

- Median per-pair time difference.
- Quality acceptance rate by condition.
- Rework rate by condition.
- Time difference by task domain, reported as descriptive only.

These are secondary and must not substitute for the primary formula.

---

## 9. Approval and execution gate

Execution is blocked until **all** of the following are satisfied and recorded. Each item is currently **OPEN**.

| # | Requirement | State | Evidence required |
|---:|---|---|---|
| 1 | Ten task pairs and their expected outcomes are documented and reviewed | **OPEN** — 3 of 10 pairs drafted | Approved Task Bank version |
| 2 | `NO_CAPE` and `CAPE` conditions, allowed sources, and prohibited assistance are fixed | **OPEN** | Approved §3–§4 text; approved space list |
| 3 | Condition order and carryover limitations are addressed | **OPEN** | Approved randomization/counterbalancing decision |
| 4 | The eight scoring dimensions, critical-failure vetoes, and edge-case rules are approved | **OPEN** | Signed-off §6 |
| 5 | Data schema, evidence handling, retention, and analysis method are approved | **OPEN** | Approved §7–§8, retention decision |
| 6 | The protocol is versioned and frozen | **OPEN** | Frozen version, commit hash, checksum |
| 7 | The appropriate project owner/reviewer has explicitly approved execution | **OPEN** | Recorded written approval |

Until all seven are satisfied:

- status remains **`PROPOSED — PENDING APPROVAL`**;
- **measurements must not start**;
- no efficiency figure, baseline, or comparison may be published;
- no intermediate "preliminary" result may be treated as a finding.

### 9.1 Freeze procedure

1. Resolve every open decision in §10.
2. Obtain explicit written approval for items 1–7.
3. Record the protocol version, commit hash, and file checksum in this document and in the project register.
4. Change status to `APPROVED — FROZEN` with the approval date and approver.
5. Only then begin the first execution.

Any change after freeze requires a new protocol version; executions under the previous version remain reported under that version and are not re-scored.

---

## 10. Decisions pending approval

| ID | Decision needed | Current draft position |
|---|---|---|
| `C07-D01` | Acceptance threshold | ≥ 6/8, with Correctness and Boundary compliance mandatory |
| `C07-D02` | Final critical-failure veto list | §6.3 list, pending ratification |
| `C07-D03` | Time-limit treatment | 600 s cap, `UNRESOLVED`, no imputation |
| `C07-D04` | Interruption resumption window | Not defined |
| `C07-D05` | Treatment of activation failures in the primary analysis | Retain as observed (intention-to-treat) |
| `C07-D06` | Condition order method | Randomized or counterbalanced; method not fixed |
| `C07-D07` | Permitted Confluence spaces and duplicate/non-canonical page rule | Not defined |
| `C07-D08` | Task-pair equivalence: identical tasks versus approved variants | Identical tasks required absent an approved variant methodology |
| `C07-D09` | Sample size if the ten-pair target is not met | Target unchanged at 10 pairs |
| `C07-D10` | Evidence retention, storage location, and destruction | Not defined |
| `C07-D11` | Scoring of unresolved, timed-out, interrupted, and activation-failure cases | §6.4 draft |
| `C07-D12` | Participant selection and skill level | Not defined |

No decision in this table may be treated as approved merely because it appears in this document.

---

## 11. Known gaps and deviations at draft stage

These gaps must be closed or explicitly accepted before the gate in §9 can pass.

1. **Task Bank coverage.** The Task Bank contains three pairs / six executions. Seven pairs / fourteen executions are not yet prepared or reviewed. The sample target remains ten pairs; the Task Bank is not to be represented as complete.
2. **Task-pair equivalence.** Task Bank v0.1 uses different prompts for the two conditions within each pair ("same knowledge domain but not identical"). The protocol requires the same task definition and expected outcome unless an approved methodology establishes equivalent variants. This is an unresolved methodology question (`C07-D08`); it must be resolved before execution.
3. **KS-010 canonical identity.** Pair 2 depends on KS-010, where the DRPA page (`7308640261`) and SOLDOC page (`8847753943`) remain unreconciled. Behavioral handling of the duplicate was observed in the Change 04 Q5 test, but governance resolution is outstanding. Source-authority scoring for this pair is blocked until the treatment is recorded.
4. **Permitted source spaces.** The approved Confluence space list and the duplicate/non-canonical rule are undefined.
5. **Retention and evidence storage.** No approved retention period, storage location, or destruction method exists.
6. **Condition order.** No randomization or counterbalancing method has been selected or recorded.
7. **Participant plan.** Participant selection, availability, and skill level are undefined; the initial pilot assumes one developer per matched pair.
8. **Acceptance threshold approval.** The 6/8 threshold and the critical-failure list are proposals.
9. **No baseline.** No baseline execution has occurred, so no time data exists for any pair.
10. **Gate status.** The Coverage-Honesty Gate remains `NOT CLEARED`; Change 07 does not alter it.

---

## 12. What this document does not authorize

- Executing any pilot task, baseline, or comparison run.
- Collecting, recording, or publishing timing data.
- Claiming any efficiency improvement, including the 30% target.
- Modifying the active Skill, its baseline, or its archive.
- Changing source classifications, the Trust Matrix, the Knowledge Taxonomy, the Knowledge Inventory, or the Coverage-Honesty Gate.
- Updating, or claiming an update to, any Confluence page or the Implementation Record.
- Treating Task Bank v0.1 as approved, complete, or frozen.

---

## 13. Version history

| Version | Date | Change | Status |
|---|---|---|---|
| v0.1 | 2026-10-20 | Initial protocol definition for Change 07: objective, experimental design, baseline and CAPE conditions, timing and outcome taxonomy, eight-dimension rubric, data schema, analysis method, approval gate, open decisions, known gaps | `PROPOSED — PENDING APPROVAL` |

**Related documents**

- Task Bank: [`CAPE_Change_07_Task_Bank_v0.1.md`](CAPE_Change_07_Task_Bank_v0.1.md)
- Change 04 design specification: [`CAPE_Change_04_Design_Specification_v0.1.md`](CAPE_Change_04_Design_Specification_v0.1.md)
- Project evaluation register: [`Tests/CAPE_Testing_Results_Follow_Up.md`](Tests/CAPE_Testing_Results_Follow_Up.md)
- Active Skill: [`CAPE_RPA_Development_Skill_ACTIVE_v0.1_pilot.md`](CAPE_RPA_Development_Skill_ACTIVE_v0.1_pilot.md)
