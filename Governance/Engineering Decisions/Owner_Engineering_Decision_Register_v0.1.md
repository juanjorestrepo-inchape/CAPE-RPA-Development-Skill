# CAPE RPA Development Skill

# Owner Engineering Decision Register

**Document ID:** CAPE-RPA-GOV-OEDR-001\
**Version:** 0.1\
**Status:** Owner-approved draft for repository incorporation\
**Decision scope:** D-01 to D-04\
**Decision authority:** Project Owner\
**Prepared:** 03 November 2026

------------------------------------------------------------------------

## 1. Purpose

This register consolidates the four engineering decisions made during
the review of Candidate v0.1.2 and its supporting governance artifacts.

Its purpose is to preserve the decision rationale and establish a
traceable record of:

-   The issue and decision question.
-   The applicable source evidence.
-   The ambiguity or conflict identified.
-   The alternatives considered.
-   The selected engineering decision and rationale.
-   The consequences for the Candidate and Pilot.
-   Outstanding governance dependencies and restrictions.

This register records project-level engineering decisions. It does not
independently amend upstream governance artifacts, grant corporate
governance approval, or authorize changes to the Active Skill or
Baseline.

## 2. Decision Status Summary

  ---------------------------------------------------------------------------
  Decision          Subject           Engineering-review   Underlying
                                      status               dependency
  ----------------- ----------------- -------------------- ------------------
  D-01              Provisional       Closed               Trust Matrix §5.6
                    Assessment Status                      clarification and
                    and Permitted Use                      document-control
                                                           alignment

  D-02              Candidate §6      Closed               Explicit approval
                    response                               of genuinely
                    behaviors                              additional pilot
                                                           requirements;
                                                           broader
                                                           requirements
                                                           deferred to
                                                           Tranche 2

  D-03              KS-003--KS-010    Closed --- interim   Controlled
                    source-level      decision             Implementation
                    reconciliation                         Record and final
                                                           reconciliation

  D-04              KS-015 Primary /  Closed --- interim   Formal Source Role
                    Supporting Role   decision             determination by
                    Ambiguity                              the appropriate
                                                           governance
                                                           authority
  ---------------------------------------------------------------------------

**Interpretation of status:** Closed means the project-level engineering
interpretation has been agreed. It does not mean that every underlying
source, governance, or document-control dependency has been resolved.

------------------------------------------------------------------------

# 3. Decision Records

## D-01 --- Provisional Assessment Status and Permitted Use

**Status:** CLOSED --- Engineering Review\
**Selected approach:** Option B\
**Scope:** Interpretation of Provisional Assessment Status in relation
to Permitted Use.

### 3.1 Decision question

Should a source with Assessment Status `Provisional` retain its assigned
Permitted Use, or should its eligibility or use be automatically
downgraded until its outstanding assessment dimensions have been
formally resolved?

### 3.2 Evidence and interpretation

The Trust Matrix distinguishes between:

-   **Permitted Use:** the governance decision that determines how a
    source may be used.
-   **Assessment Status:** the completeness of the source assessment.
-   **Source Role:** the standardized role assigned to the source.

Trust Matrix §3.4 defines Provisional status in relation to outstanding
assessment dimensions, including Evidence Quality and Ownership. R1
permits certain sources to retain eligibility while those dimensions
remain unassessed, subject to applicable restrictions and Source Role
ceilings.

Functional Specification §4.2 establishes source-selection behavior. The
Pilot Specification §5.6 explicitly states that Provisional status
should not automatically reduce the source's assigned Permitted Use and
should instead be disclosed as a caveat.

However, Trust Matrix §5.6 contains wording concerning formal validation
of Provisional sources that requires clarification against §3.4 and R1.

### 3.3 Alternatives considered

  -----------------------------------------------------------------------
  Alternative                         Assessment
  ----------------------------------- -----------------------------------
  Automatically downgrade or exclude  Rejected. It conflates assessment
  all Provisional sources             completeness with the independently
                                      assigned Permitted Use.

  Preserve the assigned Permitted Use Selected. It maintains the
  and disclose Provisional status     distinction between source
                                      eligibility and assessment
                                      completeness while preserving
                                      transparency.
  -----------------------------------------------------------------------

### 3.4 Owner decision

A source with Assessment Status `Provisional` remains eligible for
selection according to its assigned `Permitted Use`, provided that no
applicable decision rule, Source Role ceiling, or other governance
restriction prevents its use.

Its Permitted Use must not be automatically downgraded or revoked solely
because its assessment is incomplete.

The Skill must disclose the Provisional status through a concise
provenance caveat, without representing the source as fully assessed or
implying that outstanding assessment dimensions have been formally
resolved.

### 3.5 Consequences

1.  Candidate source-selection behavior must preserve the distinction
    between Permitted Use and Assessment Status.
2.  A Provisional Primary source may retain Primary eligibility where
    the applicable rules permit it.
3.  Independent restrictions, including Role Ambiguity and Source Role
    ceilings, remain enforceable.
4.  Pending Validation remains distinct from Provisional and must not be
    treated as an eligible evidence status merely because a source is
    known or relevant.
5.  The distinction between a Provisional source and a Provisional
    domain must be preserved.

### 3.6 Outstanding dependencies

-   Clarify the wording in Trust Matrix §5.6 against §3.4 and R1.
-   Reconcile the Trust Matrix document-control status with the upstream
    status described in the Functional Specification.
-   Establish the appropriate governance approval and effective revision
    for any required upstream clarification.

### 3.7 Decision boundaries

This decision:

-   Does not mark outstanding Evidence Quality or Ownership dimensions
    as assessed.
-   Does not change individual source classifications.
-   Does not promote sources beyond their applicable Source Role
    ceilings.
-   Does not amend the Trust Matrix or Functional Specification.
-   Does not change the Active Skill, Baseline, or Coverage-Honesty
    Gate.

------------------------------------------------------------------------

## D-02 --- Candidate §6 Response Behaviors and Approval Scope

**Status:** CLOSED --- Engineering Review\
**Selected approach:** Preserve inherited Pilot requirements;
distinguish operational clarifications from genuinely additional
requirements.\
**Scope:** Candidate v0.1.2 §6.

### 3.8 Decision question

Which response behaviors in Candidate §6 are already mandatory through
the Pilot Specification, which are operational clarifications, and which
would introduce additional pilot requirements requiring explicit
approval?

### 3.9 Evidence and interpretation

Pilot Specification §5 establishes the mandatory response behaviors
inherited from Functional Specification v0.1 Tranche 1.

These include:

-   Direct answers grounded in eligible sources.
-   Source identification using KS-ID and title.
-   Disclosure of Source Role.
-   Provisional-status caveats.
-   Conflict and limitation transparency.
-   Explicit `None identified` when no conflict or limitation exists.
-   Coverage-gap honesty.
-   Correct precedence between Primary and Supporting sources.

Candidate §6 consolidates these behaviors and adds operational detail in
some areas.

The review distinguished inherited requirements from additional
conventions that must not be presented as if they were already part of
the Pilot contract.

### 3.10 Alternatives considered

  -----------------------------------------------------------------------
  Alternative                         Assessment
  ----------------------------------- -----------------------------------
  Treat every Candidate §6 statement  Rejected. This would misrepresent
  as an existing Pilot requirement    the origin and approval status of
                                      additional behaviors.

  Remove all Candidate-level          Rejected. Some clarifications
  operational clarifications          improve deterministic handling of
                                      existing governance boundaries.

  Preserve inherited requirements,    Selected. This preserves
  retain justified operational        traceability and prevents
  clarifications, and explicitly      uncontrolled scope expansion.
  identify additional requirements
  -----------------------------------------------------------------------

### 3.11 Owner decision

Candidate §6 is a consolidated response-behavior section.

Requirements already defined in Pilot Specification §5 remain inherited
Pilot requirements.

Candidate-level clarifications may be retained as operational
expressions of existing governance and evidence-boundary rules.

Any genuinely additional behavior must be explicitly identified and
approved as a project-level Pilot requirement before being treated as
mandatory.

Broader response-generation, grounding, citation, failure-mode,
evaluation, security, and observability requirements remain subject to
Functional Specification Tranche 2 and subsequent technical design.

### 3.12 Classification of reviewed behaviors

**A. Existing Pilot-contract behaviors**

-   Direct answers grounded in eligible sources.
-   Source identification by KS-ID and title.
-   Source Role disclosure.
-   Provisional-status disclosure.
-   Conflict attribution and transparency.
-   Explicit `None identified` where applicable.
-   Coverage-gap disclosure and refusal to fabricate unsupported
    guidance.
-   Primary-over-Supporting precedence.

**B. Candidate-level operational clarifications**

-   Do not infer unverified source attributes.
-   Disclose unresolved metadata or Source Role reconciliation.
-   Do not recommend an owner, repository, or escalation path without
    eligible supporting evidence.
-   Use a deterministic fallback when authoritative follow-up evidence
    is unavailable.

These clarifications must remain consistent with the existing governance
and evidence-boundary rules.

**C. Additional behavior requiring explicit approval**

-   A formal `Partial` response label.

The `Partial` label is not explicitly established as a mandatory
behavior in Pilot Specification §5. It must not be attributed to that
specification or treated as mandatory without explicit project-level
approval.

### 3.13 Consequences

1.  Candidate §6 must preserve the distinction between inherited
    requirements and additional behavior.
2.  The Candidate must not silently expand the Pilot contract.
3.  Any additional mandatory behavior must have an explicit approval
    record.
4.  Broader technical and operational requirements remain deferred to
    their designated specification and design phases.
5.  Candidate §§4, 5 and 6 must remain internally consistent and avoid
    duplicating or contradicting requirements.

### 3.14 Outstanding dependencies

-   Preserve explicit traceability between Pilot requirements and
    Candidate operational wording.
-   Record any future approval of additional response conventions.
-   Address broader requirements through Functional Specification
    Tranche 2 and subsequent technical design.

### 3.15 Decision boundaries

This decision does not:

-   Approve the `Partial` label as a mandatory Pilot behavior.
-   Approve Functional Specification Tranche 2.
-   Introduce new retrieval, citation, security, observability, or
    evaluation architecture.
-   Change the Pilot's source boundary or evaluation dataset.
-   Change the Active Skill, Baseline, or Coverage-Honesty Gate.

------------------------------------------------------------------------

## D-03 --- KS-003--KS-010 Source-Level Reconciliation

**Status:** CLOSED --- Interim Engineering Decision\
**Selected approach:** Option A now, followed by final reconciliation
when the controlled Implementation Record is available.\
**Scope:** Source Role and Assessment Status representation for KS-003
through KS-010.

### 3.16 Decision question

How should Candidate §7 represent KS-003--KS-010 while the values in the
Trust Matrix and the controlled Implementation Record have not yet been
reconciled?

### 3.17 Evidence and interpretation

Candidate §7 currently reflects the Trust Matrix v0.1 representation and
identifies reconciliation with the Implementation Record as pending.

The available review record identifies the controlled Implementation
Record as the required evidence for final source-level reconciliation.
Its relevant controlled copy was not available for this review.

The review also identified three distinctions that must be preserved:

-   KS-008 has Pending Validation treatment and must not be treated as
    eligible evidence.
-   KS-009's absence from the populated-content table must not be
    interpreted as a change to its Trust Matrix classification.
-   KS-010 has a separate canonical identity dependency that must not be
    conflated with the broader reconciliation.

The available evidence does not establish that the Trust Matrix and
Implementation Record have been formally reconciled or establish the
final controlling relationship between those records.

### 3.18 Alternatives considered

  -----------------------------------------------------------------------
  Alternative                         Assessment
  ----------------------------------- -----------------------------------
  Preserve the current Trust Matrix   Selected as the interim approach.
  representation and disclose the     It avoids unsupported
  reconciliation dependency           classification changes.

  Change Candidate values based on    Rejected. The controlled source
  unverified Implementation Record    evidence is unavailable for
  values                              verification.

  Treat the reconciliation as         Rejected. The existence of
  complete based on the current       displayed values does not establish
  Candidate representation            reconciliation.
  -----------------------------------------------------------------------

### 3.19 Owner decision

The values currently displayed in Candidate §7 shall remain as recorded
in Trust Matrix v0.1, with the reconciliation dependency explicitly
disclosed.

This is an interim representation of the currently available governance
record, not confirmation that the Trust Matrix and Implementation Record
are reconciled.

No Source Role, Permitted Use, or Assessment Status shall be changed
based on unverified Implementation Record values.

KS-008 shall retain its existing Pending Validation treatment and shall
not be treated as eligible evidence.

KS-009's absence from the populated-content table shall not be
interpreted as a change to its Trust Matrix classification.

KS-010's canonical identity dependency remains separately open.

Final reconciliation requires comparison with the controlled
Implementation Record and determination of the authoritative values and
effective revision.

### 3.20 Consequences

1.  Candidate §7 retains its current Trust Matrix-based representation.
2.  The reconciliation dependency must remain explicit.
3.  No source-level classifications may be changed without verified
    evidence.
4.  KS-008 remains Pending Validation and ineligible as evidence.
5.  KS-009's omission from the populated-content table does not imply a
    classification change.
6.  KS-010's canonical identity dependency remains independently
    tracked.
7.  Final reconciliation must be based on controlled records, not
    inferred from the Candidate's displayed values.

### 3.21 Outstanding dependencies

-   Obtain the controlled Implementation Record, including the relevant
    §7 state and document-control revision.
-   Retrieve and review the referenced Follow-Up material where
    applicable.
-   Establish the authoritative relationship between the Trust Matrix
    and Implementation Record.
-   Compare the records source by source for KS-003--KS-010.
-   Determine the authoritative values, rationale, and effective
    revision.
-   Resolve KS-010's canonical identity dependency separately.

### 3.22 Decision boundaries

This decision:

-   Does not amend the Trust Matrix.
-   Does not establish that the Implementation Record has been
    reconciled.
-   Does not promote, demote, or reclassify any source.
-   Does not change KS-008's Pending Validation treatment.
-   Does not interpret KS-009's omission as a classification change.
-   Does not resolve KS-010's canonical identity dependency.
-   Does not change the Active Skill, Baseline, or Coverage-Honesty
    Gate.

------------------------------------------------------------------------

## D-04 --- KS-015 Primary / Supporting Role Ambiguity

**Status:** CLOSED --- Interim Engineering Decision\
**Selected approach:** Option A\
**Reserved future governance options:** Option B or Option C\
**Scope:** KS-015 --- Critical Incident Playbook.

### 3.23 Decision question

How should the Skill handle KS-015 while its declared Source Role
remains Primary / Supporting and its current Permitted Use is Supporting
under Trust Matrix R13?

### 3.24 Evidence and interpretation

The Trust Matrix records KS-015 with:

-   Declared Source Role: Primary / Supporting.
-   Permitted Use: Supporting.
-   Assessment Status: Provisional.
-   Role Ambiguity: Open.

Trust Matrix R13 applies the more restrictive Supporting ceiling to the
compound role.

Trust Matrix §6 establishes that the provisional ceiling is a governance
safeguard rather than a final determination of source quality or
intended role.

Functional Specification §4.3 requires sources with open Role Ambiguity
to remain at their provisional lower ceiling. The Pilot Specification
§3.1 also identifies KS-015 as Supporting and requires the Role
Ambiguity note to be preserved when answering the relevant pilot
question.

The available evidence does not establish a final governance
determination of whether KS-015 should be governed as Primary or
Supporting.

### 3.25 Alternatives considered

  -----------------------------------------------------------------------
  Alternative                         Assessment
  ----------------------------------- -----------------------------------
  Option A --- Preserve Supporting    Selected. It maintains the existing
  ceiling and keep Role Ambiguity     governance safeguard without
  open                                asserting an unsupported final role
                                      determination.

  Option B --- Formally resolve       Reserved for a subsequent
  KS-015 as Supporting                governance decision supported by an
                                      explicit authority determination
                                      and controlled record update.

  Option C --- Formally resolve       Reserved for a subsequent
  KS-015 as Primary                   governance decision requiring
                                      explicit confirmation of Primary
                                      authority and consideration of
                                      applicable assessment and
                                      governance requirements.
  -----------------------------------------------------------------------

### 3.26 Owner decision

KS-015 shall retain its declared Source Role of Primary / Supporting,
current Permitted Use of Supporting, and Assessment Status of
Provisional, with the Role Ambiguity flag remaining open.

In accordance with Trust Matrix R13 and §6, the Skill shall continue to
apply the more restrictive Supporting ceiling and must not present
KS-015 as an official Primary policy.

The current Supporting ceiling is an interim governance safeguard, not a
final determination of the source's intended role.

Final resolution requires the appropriate owner or governance authority
to determine whether KS-015 should be governed as Primary or Supporting,
document the supporting rationale, identify the approving authority and
effective date, and update the controlled governance artifact
accordingly.

Any decision to promote KS-015 to Primary must also address the
applicable assessment and governance requirements.

Provisional Assessment Status shall remain independently controlled and
must not be changed solely because the Source Role ambiguity is
resolved.

### 3.27 Consequences

1.  KS-015 remains usable only at the Supporting ceiling.
2.  The Skill must not present KS-015 as an official Primary policy.
3.  The Role Ambiguity flag remains open.
4.  Provisional Assessment Status remains unchanged.
5.  Options B and C remain available only through subsequent formal
    governance resolution.
6.  Any future role change must be reflected in the controlled
    governance artifact with its rationale, approving authority, and
    effective date.
7.  A future Source Role resolution does not automatically resolve
    Assessment Status.

### 3.28 Outstanding dependencies

-   Identify the appropriate owner or governance authority.
-   Obtain an explicit determination of the intended Source Role.
-   Record the supporting rationale.
-   Record the approving authority and effective date.
-   Update the controlled Trust Matrix or applicable governance
    artifact.
-   Independently assess whether outstanding Evidence Quality and
    Ownership dimensions have been resolved.

### 3.29 Decision boundaries

This decision:

-   Does not resolve the underlying Source Role ambiguity.
-   Does not promote KS-015 to Primary.
-   Does not establish Supporting as its permanent governed role.
-   Does not remove the Role Ambiguity flag.
-   Does not change Provisional Assessment Status.
-   Does not amend the Trust Matrix.
-   Does not change the Active Skill, Baseline, or Coverage-Honesty
    Gate.

------------------------------------------------------------------------

# 4. Cross-Decision Dependencies and Controls

The four decisions are related but must remain independently controlled.

  -----------------------------------------------------------------------
  Control area                        Required treatment
  ----------------------------------- -----------------------------------
  Assessment Status                   Must remain distinct from Permitted
                                      Use and Source Role.

  Source Role                         Must remain distinct from the
                                      current Permitted Use ceiling.

  Provisional status                  Must not automatically trigger a
                                      downgrade where the applicable
                                      rules permit the existing use.

  Pending Validation                  Must not be treated as equivalent
                                      to Provisional.

  Role Ambiguity                      Must preserve the more restrictive
                                      applicable ceiling until formally
                                      resolved.

  Source reconciliation               Must rely on controlled records and
                                      verified revisions.

  Candidate response behavior         Must distinguish inherited Pilot
                                      requirements from additional
                                      project-level requirements.

  Governance authority                Engineering decisions must not be
                                      represented as corporate governance
                                      approval.

  Coverage honesty                    No decision may be used to justify
                                      unsupported answers or bypass an
                                      unresolved evidence boundary.
  -----------------------------------------------------------------------

## 5. Consolidated Outstanding Dependency Register

  -------------------------------------------------------------------------
  ID                Dependency         Related decision  Required
                                                         resolution
  ----------------- ------------------ ----------------- ------------------
  DEP-01            Trust Matrix §5.6  D-01              Governance
                    interpretation                       clarification
                                                         against §3.4 and
                                                         R1

  DEP-02            Trust Matrix       D-01              Confirm
                    document-control                     authoritative
                    alignment                            status and
                                                         approval record

  DEP-03            Candidate §6       D-02              Explicit decision
                    additional                           before treating
                    behavior approval                    `Partial` as
                                                         mandatory

  DEP-04            Controlled         D-03              Obtain and verify
                    Implementation                       the controlled
                    Record                               record
                    availability

  DEP-05            Trust Matrix /     D-03              Establish
                    Implementation                       controlling
                    Record authority                     relationship and
                    relationship                         effective revision

  DEP-06            KS-008 treatment   D-03              Preserve Pending
                                                         Validation until
                                                         valid reassessment

  DEP-07            KS-009 table       D-03              Verify
                    omission                             representation
                                                         without inferring
                                                         reclassification

  DEP-08            KS-010 canonical   D-03              Resolve
                    identity                             independently
                                                         through controlled
                                                         source evidence

  DEP-09            KS-015 final       D-04              Formal
                    Source Role                          owner/governance
                    determination                        decision

  DEP-10            KS-015 assessment  D-04              Resolve
                    completeness                         independently of
                                                         Source Role
  -------------------------------------------------------------------------

## 6. Project-Level Effects and Non-Effects

The closure of D-01 through D-04 establishes the agreed engineering
interpretation for the reviewed issues.

It does not constitute:

-   Formal corporate governance approval.
-   Approval or amendment of upstream governance artifacts.
-   Completion of all source-level reconciliation.
-   Closure of KS-015's underlying Role Ambiguity.
-   Approval of additional Candidate response requirements not
    explicitly accepted.
-   Approval of Functional Specification Tranche 2.
-   Publication, activation, or deployment of an Active Skill.
-   A change to the established Baseline.
-   Formal Q11/Q12 evaluation results.
-   Clearance of the Coverage-Honesty Gate.

**Coverage-Honesty Gate:** NOT CLEARED.

**Active Skill:** Unchanged.

**Baseline:** Unchanged.

## 7. Change Control and Record Maintenance

Any subsequent modification arising from these decisions must preserve
the following traceability chain:

**Source evidence → Identified ambiguity → Alternatives → Owner decision
→ Rationale → Consequences → Remaining dependencies.**

The following controls apply:

1.  Each decision must retain its D-01 through D-04 identifier.
2.  Any future governance resolution must be recorded separately from
    the engineering decision that established interim handling.
3.  Changes to upstream artifacts must be supported by the applicable
    approval and document-control process.
4.  Candidate changes must be traceable to the relevant decision and
    approved scope.
5.  The register must be revised when an outstanding dependency is
    formally resolved or when new controlled evidence changes the
    decision basis.
6.  Historical decisions must not be silently overwritten; revisions
    must preserve the prior decision and its superseding record.

## 8. Owner Review and Acceptance

  Review item                         Status
  ----------------------------------- ------------------------
  D-01 engineering decision           Agreed
  D-02 engineering decision           Agreed
  D-03 interim engineering decision   Agreed
  D-04 interim engineering decision   Agreed
  Consolidated register               Owner-approved content
  Repository incorporation            Pending
  Upstream governance amendments      Not performed
  Active Skill / Baseline changes     Not performed

**Owner acceptance of this consolidated register**

-   Project Owner: Approved in project conversation
-   Acceptance date: 03 November 2026
-   Register version accepted: 0.1
-   Repository commit / revision: Pending

------------------------------------------------------------------------

**End of Register**
