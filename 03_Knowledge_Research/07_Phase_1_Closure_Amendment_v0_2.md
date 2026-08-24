# Phase 1 Closure Amendment v0.2

## Purpose

This amendment enriches the existing Phase 1 baseline with newly verified first-party CAPE product and architecture documentation. It does not restart Phase 1 or replace the existing RPA Knowledge Inventory. It corrects and strengthens the baseline before Phase 2 source-trust assessment begins.

## What changed

The original CAPE understanding was based primarily on UI observations, the CAPE Manual, platform interaction, the RPA Confluence inventory, information exposed by dappy, and architectural inference.

The project now also has CAPE's own internal product and architecture documentation. This allows the project to replace previous assumptions with documented evidence where available.

The confirmed platform facts include:

- CAPE is deployed as a Databricks App on the FastAPI runtime.
- The deployed application uses Lakebase Postgres.
- CAPE Skills are packaged domain knowledge loaded on demand when relevant.
- Skills are auto-pooled and progressively disclosed rather than manually equipped per conversation.
- CAPE provides tools, connectors, agents, workflows, projects, artifacts, feedback, and administrative capabilities.
- CAPE is currently documented as a proof-of-concept platform.

## CAPE Platform Context

CAPE (Capability Accelerator Productivity Engine) is Inchcape's internal AI productivity platform, developed by the Digital Delivery Centers. It provides a conversational AI interface through which users can access models, tools, connectors, skills, agents, workflows, projects, and generated artifacts.

CAPE is currently documented as a proof-of-concept platform and is deployed as a Databricks App using a FastAPI backend and a Vite/React frontend. The deployed application uses Lakebase Postgres as its persistent data store. Model access is implemented through the OpenAI SDK and an OpenAI-compatible server; the specific underlying model providers are configurable and are not disclosed in the available documentation.

CAPE's Skills architecture provides domain-specific knowledge modules that are loaded on demand when relevant to a user request. Skills are progressively disclosed rather than manually activated per conversation.

## Corrected Skill abstraction

The RPA Development Skill is not the model and is not a repository containing all RPA documentation. It is:

> A domain-specific knowledge and instruction module that CAPE can load when an RPA-development-related request requires it, providing grounded guidance based on validated RPA knowledge sources.

This distinction must guide the future Skill architecture, knowledge structure, testing methodology, and evaluation criteria.

## New CAPE knowledge-source category

CAPE platform and Skill architecture sources must be tracked separately from RPA operational and development sources.

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

These authority and currency labels are provisional until exact page or record identifiers, accountable owners, revision metadata, and operational availability are confirmed in Phase 2.

These sources support understanding of the host platform and operating environment. They do not automatically become normative RPA development guidance.

## Confirmed architecture versus potential Databricks context

### Confirmed by CAPE documentation

- Databricks Apps deployment
- FastAPI backend
- Vite/React frontend
- Lakebase Postgres in deployment
- Databricks identity/proxy information through `X-Forwarded-Email`
- Databricks secret mechanism for secrets and encryption keys
- Separate executor application for Python execution
- OpenAI SDK against an OpenAI-compatible server
- CAPE-administered model tiers

### Not established as CAPE architecture

The following Databricks concepts must not be presented as components of CAPE unless separate evidence is found:

- Unity Catalog
- AI Gateway
- Genie
- Agent Bricks
- Lakeflow
- Lakehouse
- Genie Ontology
- Genie Code
- MCP through Genie
- Lakewatch
- CustomerLake

These may be documented later under a separate **Potential Databricks Platform Context** section, clearly distinguished from the documented CAPE architecture.

## CAPE feedback and user-validation evidence

CAPE provides an existing feedback mechanism for bugs, ideas, and general feedback, including messages, up to three screenshots, automatically captured origin, encrypted content, an administrator inbox, and CSV export.

This can complement the project-specific RPA user-discovery workstream. The project should use two evidence streams:

1. Existing CAPE platform feedback
2. Project-specific validation of RPA developer needs and Skill usefulness

The existing observations from Maide and Isa remain preliminary platform observations:

| Observation | Category | Relevance to RPA Skill |
| --- | --- | --- |
| Sign-in expires | Platform / Authentication | Indirect |
| Context error after execution | Platform / Reliability | Indirect |
| Table data is not ingested | File / Data handling | Potentially relevant |
| Table conversion fails | Artifact / Data processing | Potentially relevant |

These observations must not be treated automatically as defects in the RPA Development Skill. They may affect adoption and perceived usefulness while remaining broader CAPE platform issues.

## Phase 1 closure sequence

```text
RPA Knowledge Inventory v0.1
        |
        v
Newly verified CAPE documentation
        |
        v
CAPE Platform Context and architecture clarification
        |
        v
Skill operating-model clarification
        |
        v
CAPE feedback observations classified
        |
        v
RPA Knowledge Inventory v0.2.0 [complete]
        |
        v
Phase 1 baseline [complete]
        |
        v
Phase 2 - RPA Knowledge Source Trust Matrix v0.1 [active]
```

## What this amendment does not authorize

This amendment does not authorize:

- restarting the project;
- discarding the existing inventory;
- implementing the Skill;
- building an ML or AI model;
- implementing Databricks components;
- creating the user survey before the knowledge baseline is frozen;
- treating unverified Databricks platform concepts as CAPE architecture;
- moving into full Phase 2 scoring before the v0.2 baseline is frozen.

## Phase 2 handoff actions

1. Record the exact CAPE Confluence page identifiers and accountable owner in the Trust Matrix.
2. Assess the ten CAPE source candidates as separate Trust Matrix records.
3. Confirm current connector availability and per-user authorization in the CAPE user interface.
4. Score authority, relevance, currency, ownership, and evidence for each source.
5. Record source conflicts, precedence, decisions, and review cadence.
