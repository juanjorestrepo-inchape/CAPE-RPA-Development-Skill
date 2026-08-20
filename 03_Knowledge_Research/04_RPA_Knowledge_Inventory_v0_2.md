---
## Definition
A structured baseline inventory derived from the currently available RPA Confluence, project documentation, AutoDrive documentation, technology landscape, and Service Desk information. It is not yet the final authoritative knowledge register; sources whose ownership, currency, authority, or applicability remain uncertain will be explicitly marked for validation.
---

## Newly verified CAPE platform evidence

First-party CAPE product and architecture documentation is now available and should be treated as a new source category in the inventory. The documentation confirms that CAPE is deployed on Databricks Apps with a FastAPI runtime and uses Lakebase Postgres in the deployed environment. It also confirms that Skills are packaged domain knowledge loaded on demand when relevant, rather than a static repository containing all RPA documentation.

This evidence changes the project framing in two ways:

1. CAPE platform architecture should be documented from first-party evidence rather than architectural inference.
2. The RPA Development Skill should be designed as an on-demand domain knowledge and instruction module grounded in validated sources.

The full technical reference is maintained in [06_CAPE_First_Party_Technical_Reference_v0_1.md](06_CAPE_First_Party_Technical_Reference_v0_1.md). Its source owner, exact Confluence identifiers, current connector availability, and currency still require assessment in the Trust Matrix.

This CAPE platform evidence must remain distinct from RPA knowledge sources. CAPE explains the host platform and Skill mechanism; it does not automatically provide normative RPA development guidance.

---

The next artifact should contain four sections:

1. Internal RPA Knowledge Sources

Confluence/DRPA/SOLDOC governance, architecture, policies, standards, etc.

2. Development & Technology Knowledge Sources

AutoDrive, UiPath, Power Automate, Python, Azure, integrations, libraries, etc.

3. Operational Knowledge Sources

Service Desk, incident reports, monitoring, operational procedures, etc.

4. Knowledge Quality & Gaps

Stale documents, duplicate sources, fragmented documentation, missing AutoDrive developer guide, ownership gaps, conflicting sources, etc.


# 14. Inventory Status
**RPA Knowledge Inventory v0.2 — Status: Phase 1 Closure Amendment Pending Freeze**

The original v0.1 inventory remains valid as the knowledge landscape baseline. It is being amended, not replaced, with first-party CAPE platform and Skill architecture sources before Phase 2 begins.

The v0.2 amendment is documented in [07_Phase_1_Closure_Amendment_v0_2.md](07_Phase_1_Closure_Amendment_v0_2.md).

The revised inventory must be frozen before proceeding to the RPA Knowledge Source Trust Matrix.

The remaining validation activities are:

1. Validate ownership of high-authority sources.
2. Confirm DRPA versus SOLDOC source precedence.
3. Validate the current status of the three 2024 best-practice documents.
4. Review the AutoDrive GitHub documentation with the appropriate owner.
5. Determine which Service Desk information can legitimately be used as contextual knowledge.
6. Identify missing RPA developer documentation.
7. Record explicit source URLs/page identifiers where available.
8. Establish the review cadence for sources that will eventually support the Skill.

## CAPE Platform / Skill Architecture Sources

These sources represent CAPE platform knowledge and must remain distinct from RPA development knowledge and RPA operational knowledge.

| ID | Knowledge Source | Repository | Domain | Authority | Relevance | Currency | Skill Role | Evidence Status | Initial Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KS-CAPE-001 | CAPE — Overview and Features | Confluence / CAPE | CAPE platform / Skills | High pending owner verification | Very High | Pending metadata verification | Primary | Documented | Candidate |
| KS-CAPE-002 | CAPE — Architecture | Confluence / CAPE | Architecture / Deployment | High pending owner verification | Very High | Pending metadata verification | Primary | Documented | Candidate |
| KS-CAPE-003 | CAPE — Tools and Connectors | Confluence / CAPE | Integrations / Security | High pending owner verification | Very High | Pending metadata verification | Primary / Supporting | Documented | Candidate |
| KS-CAPE-004 | CAPE — Projects, Agents, and Workflows | Confluence / CAPE | Skills / Agents / Workflows | High pending owner verification | High | Pending metadata verification | Supporting | Documented | Candidate |
| KS-CAPE-005 | CAPE — Artifacts, Decks, Dashboards, and Forms | Confluence / CAPE | Artifacts / Output | High pending owner verification | Medium | Pending metadata verification | Contextual | Documented | Review |
| KS-CAPE-006 | CAPE — Admin, Metrics, and Deployment | Confluence / CAPE | Administration / Deployment / Metrics | High pending owner verification | High | Pending metadata verification | Supporting | Documented | Candidate |
| KS-CAPE-007 | CAPE — Data Policy | Confluence / CAPE | Security / Data Governance | High pending owner verification | Very High | Pending metadata verification | Primary / Supporting | Documented | Candidate |
| KS-CAPE-008 | CAPE Feedback | Confluence / CAPE | Platform limitations / User evidence | Medium/High pending owner verification | High | Pending metadata verification | Supporting | Observational | Candidate |
| KS-CAPE-009 | CAPE — Discovery and Definition | Kanban / Project records | Project governance | High pending owner verification | Very High | Current subject to record verification | Project context | Documented | Candidate |
| KS-CAPE-010 | CAPE RPA Development Skill — Phase 1 and 2 evidence | Project repository | Project execution | High pending owner verification | Very High | Current subject to record verification | Project context | Documented | Candidate |

Authority and currency labels are provisional until exact page or record identifiers, accountable owners, revision metadata, source currency, connector availability, and per-user authorization are verified in the Trust Matrix.


# SECTION 3 Internal RPA Knowledge Source

## Column: Initial Disposition

| Initial Disposition | Meaning in this project                                                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Candidate**       | The source appears potentially relevant to the RPA Development Skill, but its suitability has not yet been assessed in sufficient detail.                                    |
| **Validate**        | The source is potentially valuable, but its authority, ownership, currency, scope, or applicability requires explicit validation before it can be relied upon.               |
| **Investigate**     | The source or knowledge area has been identified, but additional discovery is required to determine what actually exists, where it is maintained, or whether it is relevant. |
| **Contextual**      | The source provides useful background or contextual information but should not be treated as a primary authoritative source for the Skill.                                   |
| **Exclude**         | The source is currently considered unsuitable for the Skill, either because it is irrelevant, redundant, inaccessible, unreliable, or outside the project's scope.           |


**Why I changed the existing values this way**

The most important change is that Include should disappear from Section 3.
For example:
> KS-001 — RPA Strategy — Include

becomes:

> KS-001 — RPA Strategy — Candidate

**Why?** Because we have established that the RPA Strategy is a very high-authority, highly relevant, documented source, but we have not yet performed the validation required to determine exactly how it should be incorporated into the Skill.

***"Candidate"*** therefore means:
> This source is sufficiently relevant and promising to proceed to the next validation stage.

It does not mean:

> This source has already been approved for CAPE.

That distinction is critical.

```text
                         IDENTIFIED SOURCE
                                │
                ┌───────────────┼───────────────┐
                │               │               │
            Candidate        Investigate      Contextual
                │               │
                ▼               ▼
             Validate ◄────────┘
                │
                ▼
        Future Trust Matrix
                │
        ┌───────┴────────┐
        ▼                ▼
   Suitable          Unsuitable
        │                │
        ▼                ▼
   Skill Candidate      Exclude
```

**Important:** `Exclude` is intentionally not used in this table yet. That is not a problem. We should not exclude a source merely because its role is unclear; if we have insufficient evidence, **Investigate** or **Validate** is more appropriate.

Likewise, `Contextual` is useful for sources such as **RPA Job Descriptions** or **Business Continuity Plan** where the information can help CAPE understand organizational context but is unlikely to be a primary source for day-to-day development guidance.