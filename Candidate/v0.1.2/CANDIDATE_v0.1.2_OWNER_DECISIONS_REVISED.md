# Candidate v0.1.2 — Owner Decisions Register

**Register status:** `RECONCILED — ENGINEERING-REVIEW DECISIONS RECORDED; UNDERLYING GOVERNANCE DEPENDENCIES (DEP-01–DEP-10) REMAIN OPEN`
**Reconciliation date:** 19 November 2026 *(new independent reconciliation against committed repository baseline `main` @ `2f81c0f` and `Owner_Engineering_Decision_Register_v0.1.md` @ `85bd488`; uncommitted edits from a previous workstation are not assumed or reconstructed)*
**Companion documents:** [`Owner_Review_Package_Candidate_v0.1.2.md`](../../Governance/Owner%20Review/v0.1.2/Owner_Review_Package_Candidate_v0.1.2.md) · [`Owner_Engineering_Decision_Register_v0.1.md`](../../Governance/Engineering%20Decisions/Owner_Engineering_Decision_Register_v0.1.md) (`CAPE-RPA-GOV-OEDR-001`) · [`CAPE_RPA_Development_Skill_CANDIDATE_v0.1.2_REVISED.md`](CAPE_RPA_Development_Skill_CANDIDATE_v0.1.2_REVISED.md)

**Purpose:** Maintain strict consistency between Candidate v0.1.2 decisions (`D-01`–`D-04`), their agreed project-level engineering interpretations recorded in `CAPE-RPA-GOV-OEDR-001` (3 November 2026), and their unresolved cross-functional governance dependencies (`DEP-01`–`DEP-10`). This register does **not** grant corporate governance approval, amend upstream artifacts, clear the Coverage-Honesty Gate (`NOT CLEARED`), authorize testing, or authorize Active Skill replacement, publication, or deployment.

---

## Status Summary (`D-01` through `D-04`)

| Decision ID | Subject | Engineering-Review Status (`CAPE-RPA-GOV-OEDR-001`, 3 Nov 2026) | Underlying Dependencies (`OPEN`) | Proposed Accountable Role | Formal Approver |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`D-01`** | Provisional Assessment Status semantics and authority | `CLOSED — Engineering Review` (Option B: preserve assigned Permitted Use with concise Provisional caveat) | `DEP-01`, `DEP-02` (`OPEN`) | Policy / Governance Owner (`Owner to be confirmed`) | Policy / Governance Authority (`Owner to be confirmed`) |
| **`D-02`** | Approval and scope of Candidate §6 response rules | `CLOSED — Engineering Review` (preserve inherited Pilot §5 rules & operational clarifications; separate additional behaviors) | `DEP-03` (`OPEN` — `Partial` label not approved) | Project Owner (`Owner to be confirmed`) | Project Owner (`Owner to be confirmed`) |
| **`D-03`** | `KS-003`–`KS-010` Source Role and Assessment Status reconciliation | `CLOSED — Interim Engineering Decision` (Option A interim: retain Trust Matrix v0.1 table with explicit reconciliation disclaimer) | `DEP-04`–`DEP-08` (`OPEN`, incl. `KS-010` canonical identity) | Source Owner & Policy / Governance Owner (`Owner to be confirmed`) | RPA Architecture & Governance Lead (`Owner to be confirmed`) |
| **`D-04`** | `KS-015` Primary / Supporting Role Ambiguity | `CLOSED — Interim Engineering Decision` (Option A interim: retain Supporting ceiling under R13 and open Role Ambiguity flag) | `DEP-09`, `DEP-10` (`OPEN`) | Policy / Governance Owner (`Owner to be confirmed`) | Policy / Governance Authority (`Owner to be confirmed`) |

> **Governance distinction:** `CLOSED — Engineering Review` / `CLOSED — Interim Engineering Decision` means the project-level engineering handling has been agreed by the Project Owner (`CAPE-RPA-GOV-OEDR-001`, commit `85bd488`). It does **not** close `DEP-01` through `DEP-10`, does **not** amend upstream Confluence/Word governance records, and does **not** substitute for Domain-Owner or Formal Governance approval.

---

## D-01 — Provisional Assessment Status Semantics and Authority

- **Engineering-review status:** `CLOSED — Engineering Review` (Option B agreed in `CAPE-RPA-GOV-OEDR-001`, 3 November 2026).
- **Underlying governance status:** **`OPEN`** (`DEP-01`, `DEP-02`).
- **Ownership:** Accountable: Policy / Governance Owner (`Owner to be confirmed`) · Responsible: Governance Analyst / Skill Technical Owner · Consulted: Project Owner, Source Owners · Formal Approver: Policy / Governance Authority (`Owner to be confirmed`).

### D-01 Issue

The governing artifacts do not state a single, unambiguous runtime interpretation for a source whose Assessment Status is `Provisional`:

- Trust Matrix v0.1 §5.6 conditions use on formal validation / resolution of Provisional status, whereas §3.4 and rule R1 permit continued eligibility while assessment dimensions remain unassessed.
- Functional Specification v0.1 Tranche 1 §4.2 describes selection with a light provenance note.
- Pilot Specification v0.1 §5.6 states that a Provisional source retains full Permitted Use confidence and that the flag is a light caveat, not a reason to downgrade or avoid the source. However, Pilot Specification v0.1 is marked `Draft for Review`.

### D-01 Relevant Sources

- RPA Knowledge Source Trust Matrix v0.1, §§3.4–3.5 (rule R1) and §5.6, and source assessment tables.
- RPA Development Skill Functional Specification v0.1 Tranche 1, §§4.1–4.2 and Table 4.1.
- RPA Development Skill Pilot Specification v0.1 (`Draft for Review`), §5.6.
- Candidate v0.1.2, §§4 and 7; `CAPE-RPA-GOV-OEDR-001` §3 (`D-01`).

### D-01 Agreed Interpretation and Open Governance Dependencies

- **Agreed interpretation (`CAPE-RPA-GOV-OEDR-001`):** A `Provisional` source retains its assigned `Permitted Use` unless an independent rule, Source Role ceiling, or governance restriction applies; the Skill must disclose Provisional status via a concise caveat without implying completed assessment. `Pending Validation` remains distinct and ineligible.
- **Open dependencies requiring confirmation:**
  - **`DEP-01`:** Formal governance clarification of Trust Matrix §5.6 wording against §3.4 and rule R1.
  - **`DEP-02`:** Confirmation of Trust Matrix and Pilot Specification document-control / approval status and effective revision.

---

## D-02 — Approval and Scope of Candidate §6 Response Rules

- **Engineering-review status:** `CLOSED — Engineering Review` (`CAPE-RPA-GOV-OEDR-001`, 3 November 2026).
- **Underlying functional status:** **`OPEN`** (`DEP-03` — explicit decision required before treating `Partial` label as mandatory).
- **Ownership:** Accountable: Project Owner (`Owner to be confirmed`) · Responsible: Skill Technical Owner · Consulted: Test Lead, Policy / Governance Owner · Formal Approver: Project Owner (`Owner to be confirmed`).

### D-02 Issue

Candidate §6 consolidates Pilot Specification §5 response behaviors with additional operational detail. Because Pilot Specification v0.1 is `Draft for Review` and detailed grounding/citation work belongs to Functional Specification Tranche 2, Candidate §6 must distinguish:

1. Existing Pilot-contract behaviors inherited from Pilot Specification §5 (grounded answers, KS-ID/title, Source Role, Provisional caveat, conflict/limitation disclosure, `None identified`, coverage-gap refusal, Primary-over-Supporting precedence).
2. Candidate-level operational clarifications (no attribute inference, disclosure of unreconciled metadata/roles, no ungrounded escalation paths, deterministic fallback).
3. Genuinely additional behavior requiring explicit approval — specifically a formal **`Partial`** response label.

### D-02 Relevant Sources

- Candidate v0.1.2, §6.
- RPA Development Skill Pilot Specification v0.1 (`Draft for Review`), §§0.1, 0.3, 5.1–5.6, 6–8.
- RPA Development Skill Functional Specification v0.1 Tranche 1, §§0.1, 0.3, 3–6.
- `Owner_Review_Package_Candidate_v0.1.1.md`, §§1, 5, 6; `CAPE-RPA-GOV-OEDR-001` §3 (`D-02`).

### D-02 Agreed Interpretation and Open Functional Dependency

- **Agreed interpretation (`CAPE-RPA-GOV-OEDR-001`):** Inherited Pilot §5 requirements and justified operational clarifications are preserved without silently expanding the Pilot contract; broader grounding/citation/observability requirements remain deferred to Tranche 2.
- **Open dependency requiring confirmation:**
  - **`DEP-03`:** Explicit Project Owner approval to adopt the `Partial` response label as a mandatory pilot behavior, or direction to defer/remove it.

---

## D-03 — `KS-003`–`KS-010` Source Role and Assessment Status Reconciliation

- **Engineering-review status:** `CLOSED — Interim Engineering Decision` (Option A interim agreed in `CAPE-RPA-GOV-OEDR-001`, 3 November 2026).
- **Underlying governance/source status:** **`OPEN`** (`DEP-04`–`DEP-08`).
- **Ownership:** Accountable: Source Owner & Policy / Governance Owner (`Owner to be confirmed`) · Responsible: Confluence Admin / Knowledge Owner · Consulted: Skill Technical Owner, Project Owner · Formal Approver: RPA Architecture & Governance Lead (`Owner to be confirmed`).

### D-03 Issue

Candidate §7 displays Trust Matrix v0.1 values for `KS-003`–`KS-007` and `KS-010`, whereas Implementation Record §7 retains `UNVERIFIED` values (cross-check status: `PARTIAL / NOT PASSED`). In addition, `KS-008` has `Pending Validation` treatment, `KS-009` is not listed among the seven populated-content entries, and `KS-010` has an unresolved DRPA (`7308640261`, v10) vs. SOLDOC (`8847753943`, v5) duplicate.

### D-03 Relevant Sources

- Candidate v0.1.2, §7; Trust Matrix v0.1 (§26.1); Implementation Record §7 (Confluence v55 / `v0.1-r4`).
- `CAPE_Testing_Results_Follow_Up.md` (§17, §21); `CAPE-RPA-GOV-OEDR-001` §3 (`D-03`).

### D-03 Agreed Interpretation and Open Dependencies

- **Agreed interim interpretation (`CAPE-RPA-GOV-OEDR-001`):** Retain Trust Matrix v0.1 values in Candidate §7 with explicit disclosure that reconciliation against the controlled Implementation Record is pending. Do not alter classifications based on unverified records. Keep `KS-008` ineligible (`Pending Validation`) and do not interpret `KS-009` omission as reclassification.
- **Open dependencies requiring confirmation:**
  - **`DEP-04`:** Obtain and verify the controlled Implementation Record (§7 state and revision).
  - **`DEP-05`:** Establish the authoritative controlling relationship between Trust Matrix and Implementation Record and reconcile `KS-003`–`KS-010` source by source.
  - **`DEP-06`:** Preserve `KS-008` `Pending Validation` until valid reassessment.
  - **`DEP-07`:** Verify `KS-009` representation without inferring reclassification.
  - **`DEP-08`:** Independently resolve `KS-010` canonical identity (DRPA `7308640261` vs. SOLDOC `8847753943`) via controlled source governance (also unblocks Change 04 and Change 07 Pair 2).

---

## D-04 — `KS-015` Primary / Supporting Role Ambiguity

- **Engineering-review status:** `CLOSED — Interim Engineering Decision` (Option A interim agreed in `CAPE-RPA-GOV-OEDR-001`, 3 November 2026; Options B and C reserved for future formal governance).
- **Underlying governance status:** **`OPEN`** (`DEP-09`, `DEP-10`).
- **Ownership:** Accountable: Policy / Governance Owner (`Owner to be confirmed`) · Responsible: Source Owner / Governance Analyst · Consulted: Skill Technical Owner, Security Owner · Formal Approver: Policy / Governance Authority (`Owner to be confirmed`).

### D-04 Issue

`KS-015` (*Critical Incident Playbook*) has declared Source Role `Primary / Supporting`, current Permitted Use `Supporting` (under Trust Matrix rule R13), Assessment Status `Provisional`, and open `Role Ambiguity`.

### D-04 Relevant Sources

- Trust Matrix v0.1 (rule R13, §6); Functional Specification v0.1 Tranche 1 §4.3; Pilot Specification v0.1 §3.1.
- Candidate v0.1.2, §7; `CAPE-RPA-GOV-OEDR-001` §3 (`D-04`).

### D-04 Agreed Interpretation and Open Dependencies

- **Agreed interim interpretation (`CAPE-RPA-GOV-OEDR-001`):** Preserve declared Source Role `Primary / Supporting`, apply the more restrictive `Supporting` ceiling under R13, preserve the open `Role Ambiguity` flag and `Provisional` status, and never present `KS-015` as an official Primary policy.
- **Open dependencies requiring confirmation:**
  - **`DEP-09`:** Formal determination by the appropriate governance authority of whether `KS-015` is governed as `Supporting` (Option B) or `Primary` (Option C), with recorded rationale, approving authority, and effective date.
  - **`DEP-10`:** Independent assessment of `Provisional` Evidence Quality and Ownership completeness (not automatically resolved by a Source Role decision).

---

## Cross-Reference to Broader Cross-Functional Decisions

Additional open project, source, Change 05 (`E-01`–`E-24`, `E-23` open, Requests A/B/C), platform/security, regression, and Change 07 (`DEC-C07-01`) decisions are consolidated in **Section 20 of [`Owner_Review_Package_Candidate_v0.1.2.md`](../../Governance/Owner%20Review/v0.1.2/Owner_Review_Package_Candidate_v0.1.2.md)**.

**Protected state:** This register does not modify the Active Skill, Candidate Skill content, Baseline, historical test results, Coverage-Honesty Gate (`NOT CLEARED`), Change 05 status (`PENDING IMPLEMENTATION`), or Confluence/CAPE state.
