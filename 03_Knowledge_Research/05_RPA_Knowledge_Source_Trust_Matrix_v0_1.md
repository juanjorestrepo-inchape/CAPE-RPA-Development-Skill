# RPA Knowledge Source Trust Matrix v0.1

**Status:** Phase 2 active workstream
**Started after:** RPA Knowledge Inventory v0.2.0 baseline completion
**Next review gate:** Complete initial scoring and source disposition

## Purpose

This document defines the evaluation framework for determining whether a knowledge source is suitable for the RPA Development Skill, how strongly it should be trusted, how it should be used, and under what conditions it should be treated as authoritative, contextual, or excluded.

The inventory baseline is complete for Phase 1. This matrix is now the working Phase 2 artifact; it should be populated from the v0.2.0 inventory rather than used to reopen the completed baseline.

This is the governance layer between:

- the knowledge inventory; and
- the final skill knowledge base / source selection logic.

The matrix is intentionally a working artifact. It is not a final approval document, but it is the mechanism that turns inventory findings into decision-ready source trust rules.

---

## Objective

The purpose of this matrix is to answer the following question:

> Given a source of RPA knowledge, how does the Skill decide whether it is trustworthy, relevant, current, authoritative, and appropriate for a specific use case?

---

## Evaluation Principles

1. Authority is not the same as relevance.
2. Currentness is not the same as appropriateness.
3. Operational evidence is not automatically normative guidance.
4. Internal documentation can be authoritative in some contexts and contextual in others.
5. Conflicting sources must be resolved through a documented precedence model.
6. A source should never be treated as definitive without being assessed for ownership, validity, and currency.
7. The Skill should distinguish between:
   - authoritative guidance,
   - contextual knowledge,
   - supporting evidence,
   - deprecated or outdated references,
   - and excluded sources.

---

## Decision Model

Each source should be evaluated on the following dimensions.

### 1. Authority

How strong is the source as an authoritative reference?

Suggested scale:

- 5 = Formal governance / policy / enterprise standard / maintained by accountable owner
- 4 = Strong documented team or product guidance
- 3 = Relevant technical or operational documentation with known owner
- 2 = Useful but secondary or partially validated content
- 1 = Weak or informal reference
- 0 = Untrusted or unsuitable

### 2. Relevance

How directly does this source address an RPA development need?

Suggested scale:

- 5 = Directly supports routine RPA build, deployment, governance, or support decisions
- 4 = Strongly relevant to a major capability area
- 3 = Relevant but needs interpretation
- 2 = Related or contextual only
- 1 = Limited relevance
- 0 = Not relevant

### 3. Currency

How current is the information?

Suggested scale:

- 5 = Updated and clearly current
- 4 = Recent and likely still valid
- 3 = Somewhat current but needs validation
- 2 = Potentially stale or uncertain
- 1 = Outdated or aging
- 0 = Obsolete or no longer trusted

### 4. Ownership

Is there a clear accountable owner for the content?

Suggested scale:

- 5 = Named owner, reviewed and maintained
- 4 = Known team or process owner
- 3 = Some ownership known but incomplete
- 2 = Informal or shared ownership
- 1 = Unclear ownership
- 0 = No accountable owner

### 5. Evidence Quality

How strong is the evidence or basis behind the guidance?

Suggested scale:

- 5 = Strong evidence, clear rationale, explicit examples or standards
- 4 = Good documentation and reasonable evidence
- 3 = Acceptable but limited evidence
- 2 = Minimal or indirect evidence
- 1 = Weak evidence
- 0 = No evidence

### 6. Normative vs. Contextual Status

Is the source intended as a mandatory standard, a recommended practice, or merely contextual background?

Values:

- Normative
- Recommended
- Contextual
- Historical
- Operational evidence
- Exclude

### 7. Source Tier

How should the source be categorized in the source hierarchy?

Suggested tiers:

- Tier 1 — Enterprise authority / formal governance / approved standard
- Tier 2 — High-value operational or product guidance
- Tier 3 — Technical reference or vendor guidance
- Tier 4 — Contextual or secondary source
- Tier 5 — Weak or temporary source

### 8. Skill Role

What role should the source play in the RPA Development Skill?

Suggested values:

- Primary authoritative source
- Supporting authority
- Operational evidence source
- Contextual knowledge source
- Validation / escalation source
- Excluded source

### 9. Conflict Precedence

If multiple sources conflict, which one takes precedence?

Suggested ordering:

1. Enterprise-approved governance documents
2. Official platform/vendor documentation
3. Internal architecture and security standards
4. Current operational evidence
5. Team guidance or historical documentation
6. Informal or secondary sources

### 10. Validation Requirement

What must be confirmed before the source is treated as a trusted input?

Examples:

- confirm owner
- confirm currentness
- confirm internal vs. external precedence
- confirm whether it is normative or contextual
- confirm whether it applies to this technology / process / scope
- confirm whether it is still operationally used

---

## Scoring Template

A simple scoring model can be used for initial prioritization.

Recommended formula:

Weighted Trust Score =

(A authority x weight) +
(B relevance x weight) +
(C currency x weight) +
(D ownership x weight) +
(E evidence x weight)

where weights can be adjusted over time.

Suggested initial weighting:

- Authority: 25%
- Relevance: 25%
- Currency: 20%
- Ownership: 15%
- Evidence: 15%

Interpretation:

- 4.5–5.0 = Strong trust; primary source candidate
- 3.5–4.4 = Valid supporting source; use with validation
- 2.5–3.4 = Contextual or conditional use
- 1.5–2.4 = Investigate before use
- 0.0–1.4 = Do not trust for final guidance

---

## Status Labels

Each source should receive one of the following labels:

| Status | Meaning |
|--------|---------|
| Candidate | Promising source that requires validation before trusted use |
| Validate | Useful but needs explicit review of authority, currency, or ownership |
| Investigate | Source exists but additional discovery is required |
| Contextual | Useful background, not primary guidance |
| Use with caution | Relevant but should be treated as secondary or conditional |
| Exclude | Not appropriate for this project's skill use |

---

## Trust Matrix Template

Use the following table to assess each source.

| Source ID | Source Name | Source Type | Domain | Owner | Authority (1-5) | Relevance (1-5) | Currency (1-5) | Ownership (1-5) | Evidence (1-5) | Normative / Contextual | Source Tier | Skill Role | Conflict Precedence | Validation Required | Current Status | Decision | Notes |
|----------|-------------|------------|--------|-------|----------------|----------------|----------------|----------------|----------------|---------------------|------------|-----------|---------------------|--------------------|----------------|---------|-------|
| KS-001 | Example source | Confluence / policy / vendor / ticket / repo | RPA governance | Owner name |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Initial Sources Requiring Assessment

Phase 2 assessment queue:

- [ ] Verify source owner and accountable reviewer.
- [ ] Record exact page, repository, or record identifier.
- [ ] Confirm currency and revision metadata.
- [ ] Assess authority, relevance, ownership, currency, and evidence scores.
- [ ] Classify normative, recommended, contextual, historical, operational, or excluded use.
- [ ] Record conflicts and apply precedence.
- [ ] Confirm CAPE connector availability and authorization where relevant.
- [ ] Assign a decision and review cadence.

The following source has been identified since the original inventory and should be formally assessed during Phase 2:

| Source ID | Source Name | Source Type | Domain | Owner | Authority (1-5) | Relevance (1-5) | Currency (1-5) | Ownership (1-5) | Evidence (1-5) | Normative / Contextual | Source Tier | Skill Role | Conflict Precedence | Validation Required | Current Status | Decision | Notes |
|----------|-------------|------------|--------|-------|----------------|----------------|----------------|----------------|----------------|---------------------|------------|-----------|---------------------|--------------------|----------------|---------|-------|
| CAPE-001 | CAPE first-party product and architecture documentation | Internal Confluence product documentation | CAPE platform and Skill architecture | To be confirmed |  |  |  |  |  | Contextual platform evidence |  | Parent evidence set only; do not score or use as an authoritative source | To be defined | Confirm owner, page identifiers, currency, current connector availability, and per-user authorization | Candidate | Pending assessment | Aggregate record only; assess KS-CAPE-001 through KS-CAPE-010 separately. |

The CAPE evidence sources identified for the revised Phase 1 baseline should be assessed as separate records during Phase 2:

| Source ID | Source Name | Initial Role | Initial Status |
| --- | --- | --- | --- |
| KS-CAPE-001 | CAPE — Overview and Features | Primary platform / Skill context | Candidate |
| KS-CAPE-002 | CAPE — Architecture | Primary architecture and deployment context | Candidate |
| KS-CAPE-003 | CAPE — Tools and Connectors | Primary / supporting integrations and security context | Candidate |
| KS-CAPE-004 | CAPE — Projects, Agents, and Workflows | Primary Skill, agent, and workflow context | Candidate |
| KS-CAPE-005 | CAPE — Artifacts, Decks, Dashboards, and Forms | Contextual artifacts and output context | Candidate |
| KS-CAPE-006 | CAPE — Admin, Metrics, and Deployment | Supporting administration and deployment context | Candidate |
| KS-CAPE-007 | CAPE — Data Policy | Supporting security and data-governance context | Candidate |
| KS-CAPE-008 | CAPE Feedback | Contextual platform limitation and user evidence | Candidate |
| KS-CAPE-009 | CAPE — Discovery and Definition | Project governance context | Candidate |
| KS-CAPE-010 | CAPE RPA Development Skill — Phase 1 and 2 evidence | Project execution context | Candidate |

---

## Source Assessment Guidance

For each source, capture the following before deciding its final role:

1. What is the source exactly?
2. Who owns it or maintains it?
3. Is it operational, normative, or contextual?
4. Is it current enough for current practice?
5. Does it conflict with a more authoritative source?
6. Is it suitable for direct CAPE use, or only for contextual interpretation?
7. What type of question should it support?
8. What type of answer should it never be used for?

---

## Recommended Review Questions

Use the following questions for each source during the trust assessment:

- Is this source official, maintained, and owned by an accountable party?
- Is it still actively used today?
- Is it intended to direct behavior or merely describe context?
- Does it reflect the current policy and process?
- Is it relevant to the RPA Development Skill's intended use cases?
- Does it conflict with other sources and, if so, which source ranks higher?
- Is the source suitable for direct automation guidance, or is it only supporting context?
- Should it be included as a primary source, a supporting source, or excluded?

---

## Initial Trust Decision Rules

The following decision rules should be used as a starting point:

- Formal enterprise governance documents are default Tier 1 candidates.
- Current platform/vendor documentation can be high-trust for technical standards and implementation details.
- Service Desk and incident history can support contextual and operational learning, but not automatically normative guidance.
- Historical documentation should be treated as context unless it is still confirmed as current.
- Sources with unclear ownership should not be treated as final authority.
- Unverified sources may be retained as candidate sources but must not be used as authoritative guidance.

---

## Example Fill-In Section

This section is intentionally blank for initial population.

### Source assessment examples

| Source ID | Source Name | Decision | Rationale |
|-----------|-------------|----------|-----------|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

## Next Action

This template should now be populated with the sources identified in the knowledge inventory. The output should produce a practical trust classification for each source before the team proceeds to skill design and implementation.

The transition should be:

> Inventory -> Trust Matrix -> Use-Case Catalog -> Skill Specification
