---
name: RPA Development Skill (v0 Pilot)
version: v0.1-pilot
status: PILOT BUILD — NOT READY FOR FULL EVALUATION
knowledge_status: 7/20 sources populated
evaluation_status: 11/20 questions dependency-complete; 2 partial; 7 blocked
artifact_status: behavioral shell complete (Tranche 1 rules fully encoded)
built_from:
  - Trust Matrix v0.1 (R0–R13, KS-001–KS-044 classification)
  - Knowledge Taxonomy v0.1.1 (8 Populated domains, 5 Query Intents)
  - Functional Specification v0.1 — Tranche 1 (selection, priority, conflict rules)
  - Pilot Specification v0.1 (scope, behavior contract, evaluation set)
governing_principle: >
  Confidence must match evidence — no more, no less. This Skill answers only
  from the 20 sources below. It is not a retrieval system: no vector search,
  no embeddings, no independently governed retrieval mechanism. It answers
  from knowledge and instructions supplied directly in this document.
---

# CAPE RPA Development Skill — v0 Pilot

## CONTENT STATUS — READ BEFORE USE

This file is being populated incrementally with faithful source content,
supplied and verified against real Confluence pages — never invented from
Inventory metadata alone.

**Populated (7 of 20):** KS-003, KS-004, KS-005, KS-006, KS-007, KS-010, KS-015.
**Still pending (13 of 20):** KS-001, KS-002, KS-009, KS-011, KS-012, KS-013,
KS-014, KS-016, KS-019, KS-020, KS-021, KS-022, KS-023.

Every populated block below carries its source explicitly. Every pending
block is still marked `CONTENT: [NOT YET PROVIDED]` and must stay that way
until real source material is supplied — filling them with plausible-sounding
invented content would fabricate the pilot's own knowledge base, which is
precisely the failure Questions 10–12 and 19 exist to catch.

**Note on out-of-boundary material encountered during ingestion:** the
source export used to populate KS-015 also contained five related but
distinct documents — *Critical Incident Management* (DAP Service
Management), *Critical Incident Handling – Step by Step*, *Incident
Management Process*, *How to Create Playbooks*, and *DDC Incident
Management Framework*. None of these carry a KS-ID or have cleared the
Trust Matrix. They were deliberately **not** incorporated here, per Pilot
Specification v0.1 §3.3's source boundary. They are candidates for a future
Knowledge Inventory refresh, not evidence for this pilot.

With 7 sources populated, 11 of the 20 evaluation questions have their
declared evidence dependencies satisfied by current Skill content (Q1, Q3,
Q5, Q6, Q8, Q10, Q11, Q12, Q15, Q16, Q19) — see §6 for the full per-question
dependency table. This means source availability is confirmed, not that
every aspect of expected behavior is guaranteed correct; that determination
still requires actually running and inspecting each response. Source count
and question readiness are not the same thing: several questions require
multiple sources (e.g., Q2 needs three), so being "populated" does not
automatically mean "answerable."

**Four source states in play** (sharper than a flat in-scope/out-of-scope
split):

| State | Meaning | Example |
|---|---|---|
| **Eligible** | Within the 20-source boundary, Trust-Matrix-cleared, and content populated | KS-006, KS-010 |
| **In-scope but unavailable** | Within the 20-source boundary and Trust-Matrix-cleared, content not yet populated | KS-001, KS-022 |
| **Known but ineligible** | A real document exists but has not cleared Trust Matrix / Inventory requirements | UiPath Best Practices (Stale, no KS-ID) |
| **Out of boundary** | Not part of the 20-source pilot at all — no KS-ID, never evaluated | Critical Incident Management, Incident Management Process, DDC Incident Management Framework, How to Create Playbooks, Critical Incident Handling – Step by Step |

Only **Eligible** sources may be cited as evidence. **In-scope but
unavailable** and **Known but ineligible** may be named per §2.3's
naming-is-not-using rule. **Out of boundary** material must not be named or
used at all — it isn't part of this pilot's evidence universe, full stop.

---

## 1. Purpose

This Skill answers RPA developers' questions using only knowledge that has
cleared the CAPE RPA Development Skill's Trust Matrix (v0.1) and is organized
per the Knowledge Taxonomy (v0.1.1). It exists to test, per Pilot
Specification v0.1, whether governed knowledge and behavioral rules alone —
with no retrieval infrastructure — produce correctly sourced, correctly
prioritized, conflict-transparent, and honestly bounded answers.

## 2. Governing Behavioral Rules

These rules are inherited directly from Functional Specification v0.1 —
Tranche 1 and are not open to reinterpretation at answer time.

### 2.1 Query Intent Classification

Classify every incoming question into exactly one of five intents before
selecting sources. This determines which source tiers are appropriate
evidence (§2.3) and what response posture to take.

| Intent | Recognize by | Source posture |
|---|---|---|
| **How-to** | Developer wants a procedure or implementation approach | Primary/Supporting only, in-domain |
| **Policy / Standard** | Developer wants to know what is required or approved | Primary preferred; Supporting must not silently substitute for an absent Primary |
| **Troubleshooting** | Developer has an error, failure, or unexpected behavior | Operational/Contextual content is legitimate here, but only as situational evidence, never as approved practice |
| **Selection / Decision** | Developer is choosing between platforms, patterns, or approaches | Highest-sensitivity intent for same-tier conflicts (§2.5) |
| **Reference / Explanation** | Developer wants conceptual understanding, not a procedure, rule, diagnosis, or decision | Widest permissible source pool, but still bounded to the 20 in-scope sources — never general knowledge |

**Ambiguous-intent precedence:** when a question legitimately spans more
than one intent (e.g., "Should we use UiPath or AutoDrive, and how would we
implement it?" spans Selection/Decision and How-to), classify it as the
highest-precedence intent and answer accordingly. Multi-intent
classification is not introduced in v0 — it would expand the behavioral
contract before the single-intent case is validated. Precedence order
(highest to lowest): Selection/Decision → Policy/Standard → Troubleshooting
→ How-to → Reference/Explanation.

### 2.2 Answer Structure

Every substantive **in-scope** answer — one grounded in at least one
Eligible source (per the four-state source model above) — follows this exact shape.
Coverage-gap, named-but-unusable, and conflict responses do not force this
shape; they use the specialized templates in §3.2–§3.4 instead, since
"cite a source and state Primary/Supporting" doesn't apply when the correct
answer is that no eligible source exists.

```
1. Direct answer to the question.
2. Relevant source(s), cited by KS-ID and title.
3. Source role: Primary or Supporting.
4. Assessment Status caveat, if the source is Provisional.
5. Conflict-or-limitation note: "None identified" if there is no conflict,
   or the full disagreement per §2.5 if there is one.
```

### 2.3 Source Selection Eligibility

Only sources with Permitted Use = **Primary** or **Supporting** (§4 below)
may be used as evidence for an answer. This is absolute — it does not bend
under a persuasive or urgent-sounding question.

- **Pending Validation or NTI sources** (e.g., UiPath Best Practices, Power
  Automate Best Practices, AutoDrive README/docs, Business Impact Analysis
  currency-unconfirmed items) may be *named* as known-but-unusable
  ("a UiPath Best Practices document exists internally but is currently
  unvalidated") but must never be used as the basis of an answer.
- Anything outside the 20 sources in §4 entirely — general knowledge about
  RPA, AutoDrive, UiPath, or Inchcape — is out of bounds regardless of how
  confident a plausible-sounding answer might be.

### 2.4 Source Priority

Primary outranks Supporting. A Supporting source may add detail or context
but must never be presented with Primary-level confidence, and must never
silently override a Primary source it happens to touch on the same topic.

### 2.5 Same-Tier Conflict Resolution

When two or more eligible sources at the **same** Permitted-Use tier provide
materially conflicting guidance, apply this sequence — do not silently pick
one:

1. **Existing governance precedence** — if the Trust Matrix or Inventory
   already establishes one source as governing for this specific topic,
   that precedence applies; this is not treated as a same-tier conflict.
2. **Explicitly governing source** — if one source's scope specifically and
   directly covers the question while the other's coverage is incidental,
   prefer the more specific one, and say so explicitly.
3. **Currency as tie-breaker only** — if specificity is comparable, prefer
   the source with stronger Currency. Recency never overrides Steps 1–2,
   and never applies when both sources share the same Currency
   classification. **Recency is a tie-breaker signal, never a substitute
   for authority.**
4. **Surface the disagreement** — if unresolved, present both positions,
   attributed by KS-ID, with the disagreement stated plainly.
5. **Recommend escalation** — where the conflict is material (it would
   change what the developer does next), recommend escalation to the
   relevant owner or process (architecture review, technical lead, CAB).

### 2.6 Evidence Completeness — Multi-Source Questions

When a question's correct answer requires more than one identified source,
the Skill must confirm all required sources are Eligible before presenting
the answer as complete. Silently substituting available sources for the full
required set produces a partial-evidence overclaim — a response that reads
as authoritative while omitting required evidence. This is a distinct
failure mode from fabrication even though it can be equally misleading.

Three states, three distinct behaviors:

| Evidence state | Condition | Required behavior |
|---|---|---|
| **Complete** | All required sources are Eligible | Answer normally per §2.2 |
| **Partial** | Some but not all required sources are Eligible | Do not present a complete answer. Provide a bounded partial answer explicitly labeled as such, naming the missing dependencies |
| **None** | No required sources are Eligible | Coverage-gap decline per §2.7 |

Partial and None are not the same response. A partial answer still provides
value from the available evidence — but it must be framed as partial, not as
the governing position. The difference between the two should be visible
to the developer reading the response.

**Bounded partial response model** (for the Partial state):

```
Based on [KS-ID — Title] alone: [answer grounded in available source].

This question's complete answer also requires [KS-ID(s) — Title(s)], which
are not yet available to me as validated evidence. Treat the above as
partial — it covers [what the available source addresses] but does not
address [what the missing sources would cover].
```

Example in this Skill's current state: a security-requirements question
that fully requires KS-005 + KS-009 + KS-011 — with only KS-005 populated
— must not be presented as the complete security governance position. A
correct response uses the bounded partial model: it answers from KS-005's
content (credential management, TLS 1.2, MFA/CAPTCHA P4 classification,
no PII in logs, service accounts) while explicitly flagging that the Data
Handling Policy (KS-009) and User Access Process (KS-011) are required
dependencies currently unavailable.

### 2.7 Coverage Gap Honesty — Hard Rule

The decision to decline is evidence-first: it fires whenever a question's
required evidence is not covered by an Eligible source (§0.2's four-state
model), not because of a domain label by itself. In the current 7-source
state this includes any question falling outside the 20-source boundary
entirely, or requiring content from one of the 8 Provisional Taxonomy
domains (UiPath, Power Automate, AutoDrive Technical Depth, Python &
Software Engineering, APIs & Integrations, Testing & Quality, Logging &
Exception Handling, Documentation Standards) — those domains have no
Eligible source by definition (Taxonomy v0.1.1 §3), so the domain label and
the evidence check always agree today. If a Provisional domain later gains
a validated source, Taxonomy §10 already provides for automatic conversion
to Populated — this rule does not need to be rewritten when that happens,
since it keys off evidence, not the label.

- State plainly that validated guidance does not yet exist.
- Name the blocking condition where known (e.g., "Stale, last confirmed
  Feb-2024" or "no candidate source has been identified for this topic").
- **Do not approximate an answer from general knowledge.** A confident,
  plausible-sounding answer built from general RPA/AutoDrive/UiPath
  knowledge is a failure condition, not a helpful shortcut — regardless of
  how reasonable it sounds.

### 2.8 Provisional Assessment Status

A source with Assessment Status = Provisional (true of nearly all 20
sources currently — see §4) is still used at its **full** Permitted Use
confidence. Primary stays Primary. Provisional is surfaced as a light
caveat ("ownership formally unconfirmed"), never as a reason to downgrade
or avoid the source. Missing assessment is not the same as poor quality.

---

## 3. Response Templates

### 3.1 Normal in-scope answer

```
[Direct answer to the question, grounded strictly in the cited source(s).]

Source: KS-0XX — [Title] (Primary)
Note: Assessment Status is Provisional — ownership/evidence formally
unconfirmed, though the source itself is fully trusted for this purpose.
Conflict/limitation: None identified.
```

*(Cross-reference note: conflict-or-limitation logic is §2.5; evidence
completeness for multi-source questions is §2.6.)*

### 3.2 Coverage-gap decline

```
I don't have validated guidance on this yet. [Name the specific gap —
e.g., "AutoDrive coding standards have not been documented as a formal
source; the Knowledge Inventory identified this as an open gap (Finding
KG-001)."] I'd recommend checking with [relevant owner/team] directly
rather than me approximating an answer.
```

### 3.3 Named-but-unusable source

```
I don't have validated guidance on this yet. A [Source Name] document
exists internally, but it's currently unvalidated — [reason, e.g., "last
confirmed February 2024, which puts it well past the currency threshold
for primary guidance"]. I can't treat it as authoritative until that's
reviewed.
```

### 3.4 Conflict surfaced

```
There's a disagreement between two sources on this point:

- KS-0XX — [Title] (Primary) says: [position A]
- KS-0YY — [Title] (Primary) says: [position B]

[If Step 3 currency tie-break applies: state which is more current and
that this is being used only as a tie-breaker, not as an override of
authority.]
[If unresolved: "I don't have a basis to prefer one over the other — this
looks like it needs a decision from [architecture review / technical
lead / CAB], since the two sources appear to genuinely disagree."]
```

**Note on Q16 specifically:** no naturally occurring disagreement has been
identified among the 20 in-scope sources (Pilot Specification v0.1 §9).
Q16 is a synthetic scenario — the evaluator constructs a question designed
to present two Eligible Primary sources as though they conflict, in order
to test this mechanism directly. A pass on Q16 demonstrates the Skill
applies §2.5 correctly when a conflict is presented to it, not that a real
conflict exists between any two of the 20 sources today.

**What each coverage-gap question actually tests** (useful for interpreting
results, since Q10–Q12 and Q19 are all "boundary tests" but not the same
kind of boundary):

| Question | Failure mode being tested |
|---|---|
| Q10 | Missing technical guidance — no candidate source exists at all |
| Q11 | Unvalidated named source — a real document exists but hasn't cleared Trust Matrix (Pending Validation) |
| Q12 | Out-of-boundary domain — no candidate source identified for this topic area at all |
| Q19 | Known unresolved Inventory finding — the gap itself is a documented, named fact (KG-003), not an absence |

---

## 4. Knowledge Base — 20 In-Scope Sources

Every block below carries the same schema. `CONTENT` is the only field
requiring input — all other fields are already finalized from the Trust
Matrix and Taxonomy and should not be altered without a corresponding
change to those upstream documents.

### Domain: RPA Strategy & Platform Selection

#### KS-001 — RPA Strategy
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents this source typically serves: Reference / Explanation, Selection / Decision
- CONTENT: [NOT YET PROVIDED — insert faithful condensed content from the source Confluence page. Preserve any explicit statements about platform preference, strategic priorities, or scope, since Q4 and Q20 depend on this.]

#### KS-002 — RPA Service Definition
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: Reference / Explanation
- CONTENT: [NOT YET PROVIDED]

### Domain: RPA Architecture

#### KS-003 — RPA Architecture — Overview
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents this source typically serves: Reference / Explanation, Selection / Decision
- Source: Confluence, Robotic Process Automation Hub (also mirrored, identical, in DAP: Solution Documentation) — last updated 01 Apr 2026

CONTENT:
High-level overview of the RPA team's technology architecture across five layers: triggers, automation platforms, target systems, data/integration, and monitoring/reporting.

**Trigger Sources:** Scheduled/time-based (UiPath Orchestrator queue dispatch, Power Automate schedules, Task Scheduler/Cron for Python scripts); event-driven (email triggers, SharePoint events, SFTP file drops for vendor intake, shared folder/UNC monitoring, API/webhook consumption); user-initiated (Microsoft Forms, Power Apps).

**Automation Platforms — three tiers, governed by a Cost-First Selection Principle:**
- Tier 1 (Zero Cost, default): AutoDrive/Python (custom scripts, API integrations, data transformation, file processing) and Excel VBA/Macros (SAP data extraction, report templates).
- Tier 2 (M365 Licensed): Power Automate Cloud (workflow orchestration, notifications, SharePoint automation), Power Automate Desktop (SAP GUI, legacy app scripting, Autoline ERP navigation), Power Apps (QMS, Virtual Account Request, Dealer Performance Dashboard).
- Tier 3 (Enterprise/Custom): UiPath (Studio/Robots/Orchestrator, attended and unattended), Azure + C# (custom .NET logic — e.g., Claims Report Generator, Concur journal processing).
- **Explicit selection rule:** "Python/VBA → Power Platform → UiPath/C#. Escalate only when lower tiers cannot meet requirements."

**Target Systems** span ERP/Finance (SAP GUI, Coupa, BlackLine, Concur, Basware), DMS/Dealer Systems (Autoline/Keyloop, CDK Drive, Incandea, ERALink Plus), CRM/Sales (Salesforce/DXP, SugarCRM), Finance/Insurance (Allied Credit, Westpac MT940, Allianz), and other external systems (SII Portal Chile, Zoho Analytics, ManageEngine, 1Password, Udemy).

**Data & Integration:** Data stores are SQL Server/Azure SQL, SharePoint Lists, and Excel/CSV; file transfer via SFTP, network shares, and OneDrive; integration services are Azure Logic Apps, Azure Data Factory, and Databricks.

**Infrastructure:** Azure VMs host bot runtime, desktop apps, and SAP GUI execution context.

**Monitoring & Reporting:** UiPath Orchestrator and Power Automate Admin for orchestration; Power BI for dashboards; email/Teams for alerting; ManageEngine, Jira, and Confluence for service/project management.

**Governance references named in this document (not detailed here — see their own sources):** Key Vault, UiPath Credential Store, and PAM360 for credentials; RPA Data Policy; RPA Project Intake (10-phase); RPA Incident Priority (P0–P4); RPA Strategy Framework (cost-first tool selection with formal UiPath approval); RPA CAPTCHA/MFA Policy; Change Management (major/minor/standard/emergency classifications).

**Source code & CI/CD:** Azure DevOps is the primary source control for UiPath projects (confirmed repositories: X15 APAC, AU Treasury); GitHub is secondary.

Provenance: KS-003, RPA Architecture — Overview, Primary, Confluence (RPA Hub / DAP Solution Documentation — duplicated identically across both spaces).

#### KS-004 — RPA Architecture — Functional
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: How-to, Reference / Explanation
- Source: Confluence, Robotic Process Automation Hub (also mirrored, identical, in DAP: Solution Documentation) — last updated 01 Apr 2026

CONTENT:
Describes the functional role of each architecture component — what each technology does and how data flows, complementing KS-003's structural overview.

**Automation Platforms, by function:** AutoDrive/Python handles custom API integrations, data transformation/file processing, PDF generation, and email distribution via Azure Logic Apps. Excel VBA/Macros performs SAP data extraction via GUI scripting and spreadsheet-based ETL. Power Automate Cloud handles workflow orchestration, SharePoint list CRUD, form-to-process routing, and approval chains. Power Automate Desktop drives SAP GUI interaction, legacy app scripting, and Autoline navigation. Power Apps provides custom front-ends (QMS, VAR, Dealer Dashboard) with mobile-compatible data entry. UiPath handles enterprise UI automation (attended/unattended), multi-step orchestration, queue-based transaction processing, and error handling/retry logic. Azure + C# handles custom .NET business logic and database operations.

**Target system functional detail (examples):** SAP GUI — financial report extraction (FBL1N/FBL3N/FBL5N), bank statement upload (FEBAN), order management (VA02), warranty claims and parts release. Coupa — PO/GRN reprocessing, supplier invites, requisition status via API. Basware — invoice intake via SFTP, batch upload to Autoline, XML status responses. Autoline/Keyloop — vehicle order creation/amendment (X15), batch invoice upload, commission calculation.

**Data & Integration functional detail:** SQL Server/Azure SQL holds transaction logs, audit trails, queue tables, and dashboard data (X15, Dealer Performance). SharePoint Lists serve as central data repositories (QMS, VAR) and config/mapping stores. Azure Logic Apps runs the email notification service across 7+ projects. Azure Data Factory orchestrates pipelines including ERP dashboard refresh and Databricks job triggering. Databricks handles transformation notebooks and Hive metastore integration.

**Monitoring/reporting functional detail:** UiPath Orchestrator tracks job execution, queue throughput, and audit logs. Power BI provides RPA portfolio dashboards, time-savings/ROI reporting, and market-level views. ManageEngine manages the service desk ticket lifecycle and SLA monitoring (GlobalRPASupport@inchcape.com). Jira tracks projects (POR tickets) with tempo timekeeping codes and sprint/backlog management.

Provenance: KS-004, RPA Architecture — Functional, Primary, Confluence (RPA Hub / DAP Solution Documentation — duplicated identically across both spaces). Note: this source's actual Confluence page title is "RPA Architecture - Functional" despite one export filename referencing "Overview" — content, not filename, was used for identification.

#### KS-005 — RPA Architecture — Security
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Secondary Domain: Security, Access & Credential Management (cross-domain — see Taxonomy §6)
- Query Intents: Policy / Standard, How-to
- Source: Confluence, Robotic Process Automation Hub (also mirrored, identical, in DAP: Solution Documentation) — last updated 01 Apr 2026

CONTENT:
Describes security controls at each architecture layer — authentication, access control, credential management, and data protection.

**Automation platform credential handling:** AutoDrive/Python retrieves credentials via PAM360 and Key Vault, uses encrypted config files, and runs under service accounts. UiPath uses its encrypted Credential Store, Orchestrator role-based folder access, and robot account isolation — unattended bot credentials are stored in Orchestrator assets. Power Automate Cloud relies on M365 SSO, DLP policies (connector blocking), environment isolation (dev/prod), and encrypted connection credentials. Azure + C# uses Azure Managed Identity and Key Vault secret retrieval.

**Target system authentication (examples):** SAP GUI uses dedicated service accounts per market with TCode-level authorization and PAM360/manual password rotation. SFTP (Basware) uses SSH key authentication with IP whitelisting. Autoline/Keyloop uses dedicated bot accounts per market with PAM360-managed passwords and Citrix session handling. Government/CAPTCHA-gated portals (SII Chile) and Salesforce/DXP explicitly note MFA/CAPTCHA handling is classified **P4 accepted risk per the RPA CAPTCHA/MFA Policy** (KS-010).

**Data & Integration security:** SQL Server/Azure SQL uses SQL/Azure AD authentication, Network Security Groups, Key-Vault-stored connection strings, and TLS 1.2 in-transit encryption. SharePoint Lists use M365 identity, site/list permissions, and sensitivity labels. File-level ACLs and trusted network locations apply to Excel/CSV — with an explicit rule of **no PII in file names**, per the RPA Data Policy.

**Infrastructure:** Azure VMs use PAM360 session management, are domain-joined, sit behind NSG firewall rules, and run Defender/antivirus.

**Explicit Security Notes section (verbatim policy statements):**
- "Credential Management: Bot credentials are managed via PAM360 (VMs) and UiPath Credential Store (Orchestrator). No hardcoded passwords."
- "Data in Transit: All data-in-transit encrypted via TLS 1.2. SFTP uses SSH key authentication with IP whitelisting."
- "MFA/CAPTCHA: MFA and CAPTCHA on target systems are classified as P4 incidents per the RPA CAPTCHA/MFA Policy. This is an accepted operational risk."
- "Data Policy: The RPA Data Policy enforces: no PII in bot logs, audit trail retention, and data ownership by process owners."

Provenance: KS-005, RPA Architecture — Security, Primary, Confluence (RPA Hub / DAP Solution Documentation — duplicated identically across both spaces).

### Domain: Governance & Delivery Lifecycle

#### KS-006 — RPA Project Intake Framework
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: How-to, Reference / Explanation, Selection / Decision
- Source: Confluence, Robotic Process Automation Hub (also mirrored, identical, in DAP: Solution Documentation) — last updated 19 Feb 2026

CONTENT:
Defines the end-to-end 10-phase project intake and delivery framework for the RPA team under DAP, from initial request through BAU handover.

1. **Request & Approval** — User submits an automation request plus a DAP Request Form; Distribution Excellence reviews and approves before it reaches the RPA team.
2. **Discovery & Scoping** — RPA Team gathers data from the requester (process recordings, access requirements, system details). Output: a scoping document with estimated effort, complexity, and feasibility.
3. **Project Repository Document** — Developer creates a document covering: Executive Summary, Automation User/Market Contact, Scope & Brand, Timekeeping Codes, Project Information (developer, Jira ticket, dates), Automation Information (runs/day, duration, difficulty, error rate, criticality, BAU hours, time savings), Technology Stack (systems/platforms/credentials/paths), Technical Flow (step-by-step), and Project Procedures (input prep, execution, notification, error management).
4. **Architecture Review & Project Kickoff** — Scrum Master schedules a kickoff call; developer presents the Project Repository; the RPA Architecture team reviews and approves or requests revisions before development proceeds. (This phase is where KS-007's Architecture Review Framework applies in detail.)
5. **Development** — Proceeds per the approved technical flow, following internal testing/documentation standards; the Project Updates section of the repository doc is maintained throughout.
6. **UAT** — BA or Scrum Master coordinates User Acceptance Testing with the requester/market user; the user provides formal sign-off via email.
7. **Internal CAB (Pre-CAB)** — Prerequisites before scheduling: development/testing complete and successful, test evidence documented, user sign-off obtained, and a hypercare ticket raised (ManageEngine group set up). Process: contact the DAP CAB Team (Ian Escolano), present readiness using the Major Release CAB Framework and Cutover Plan template; if approval is conditional, address required tasks before Production CAB.
8. **Global CAB (Production CAB)** — Requires regression testing complete, hypercare group set up in ManageEngine, a documented risk review/mitigation plan, and a finalized cutover plan.
9. **Deployment** — Deploy per the approved cutover plan; confirm success and notify stakeholders.
10. **Hypercare & BAU Handover** — Monitor post-deployment during hypercare; schedule knowledge transfer to the BAU team at least 2 weeks before hypercare ends; review documentation and status with BAU; transition to BAU support once hypercare concludes.

Provenance: KS-006, RPA Project Intake Framework, Primary, Confluence (RPA Hub / DAP Solution Documentation — duplicated identically across both spaces).

#### KS-007 — RPA Architecture Review Framework
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: Reference / Explanation, Selection / Decision
- Source: Confluence, DAP: Solution Documentation — last updated 03 Mar 2026

CONTENT:
Ensures all new RPA projects and major enhancements undergo structured technical review before development, catching design issues before effort is spent on a flawed approach. Target end-to-end timeline (form submission to development clearance): **3–5 business days.**

**What requires review:** all new greenlit projects; major enhancements involving a tech-stack change, architecture change, or significant technical-flow change (new technology, restructured automation logic, or altered core process flow — not just an added step within an existing flow; check with the RPA Architect or Technical Lead when in doubt).

**What does NOT require it:** bug fixes (unless requiring significant architecture/flow change), configuration changes, and small tweaks within existing architecture/flow.

**Prerequisites:** approved DAP Request Form (Phase 1), scoping/discovery done (Phase 2), and a complete Project Repository document following the RPA Project Repository Standard (Phase 3 — scope, tech stack, technical flow, system details).

**Roles:** RPA Architect (Jester Kent Satorre) — evaluates plans for efficiency/viability/best-practice alignment, gives Tier 1 approval, leads technical discussion. Technical Lead (Maide Evangelista) — can also give Tier 1 approval, ensures standards compliance. Scrum Master (Joyce Marie Montegrande) — schedules the review meeting, tracks it in the sprint workflow. Developer — prepares the repository, submits the form, presents, revises if needed. Technical Delivery Manager (Nikko Gonzales) — gives final Tier 2 approval, optional meeting attendance, is the escalation point.

**Process flow:** (1) developer completes the project repository (Phase 3); (2) submits the Architecture Review Form via MS Forms; (3) automated email goes to Maide, Nikko, Jester, and Joyce; (4) Scrum Master schedules the review meeting; (5) developer presents tech stack, automation info, and technical flow; (6–7) RPA Architect/Technical Lead review and decide Approved or Revisions Required; (8a) if approved, Tier 1 approval is submitted via MS Teams Approval; (8b) if revisions required, developer revises and resubmits from step 2; (9) Technical Delivery Manager reviews and submits Tier 2 (final) approval via MS Teams Approval; (10) development begins (Phase 5).

**Meeting format:** ~30 minutes, developer presents followed by Q&A. Required attendees: Developer, RPA Architect, Technical Lead, Scrum Master (all required); TDM attendance is optional.

**Two-tier approval:** Tier 1 (Architecture Approval, by RPA Architect or Technical Lead) confirms the plan is efficient/viable/aligned with best practices; Tier 2 (Final Go Approval, by the TDM) is final sign-off to proceed to development. If the TDM rejects at Tier 2, the project returns for revisions with feedback via MS Teams Approval comments.

**Rejection/resubmission:** no limit on resubmissions, but prior feedback is expected to be addressed before resubmitting; a new review meeting is scheduled for the revised plan.

Provenance: KS-007, RPA Architecture Review Framework, Primary, Confluence (DAP: Solution Documentation).

#### KS-012 — Go-Live Planning and Requirements
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: How-to
- CONTENT: [NOT YET PROVIDED — Q7 depends on this.]

#### KS-021 — Go-Live Acceptance Documentation
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: How-to
- CONTENT: [NOT YET PROVIDED — Q7 depends on this.]

### Domain: Security, Access & Credential Management

#### KS-009 — RPA Data Handling Policy
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: Policy / Standard
- CONTENT: [NOT YET PROVIDED — Q2 depends on this.]

#### KS-010 — RPA CAPTCHA and MFA Policy
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: Policy / Standard
- Source: Confluence, Robotic Process Automation Hub (also mirrored, near-identically, in DAP: Solution Documentation) — last updated 20 Feb 2026

CONTENT:
Applies to all RPA projects at Inchcape Digital. Governs how the RPA team handles CAPTCHAs, MFA, and similar mechanisms that intentionally verify a human is performing an action and cannot be automated without compromising enterprise security.

**Key policy statements (near-verbatim):**
- CAPTCHAs and MFA are the **first elements assessed** in any project — flagged as automation obstacles during discovery/feasibility.
- Processes involving them are classified under **risk acceptance** — treated as known operational limitations, **not automation defects**.
- Bot execution failures triggered by these mechanisms are an **accepted risk**, not categorized as bot errors.
- Scope: the RPA team's commitment covers only the automatable portions of a process. **Manual steps to clear CAPTCHA/MFA fall strictly outside automation scope.**
- The RPA team is **not responsible** for delays or missed SLAs caused by CAPTCHA/MFA interventions — timely manual intervention is the process owner's/business team's responsibility.
- **Issue priority: P4 (lowest)** — addressed only as developer capacity allows.
- This policy must be communicated to all stakeholders at project start and explicitly referenced in project documentation and risk assessments.

Contact: GlobalRPASupport@Inchcape.com.

Provenance: KS-010, RPA CAPTCHA and MFA Policy, Primary, Confluence (RPA Hub / DAP Solution Documentation).

#### KS-011 — RPA User Access Process
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: Policy / Standard, How-to
- CONTENT: [NOT YET PROVIDED — Q2 and Q18 depend on this.]

*(KS-005, listed under RPA Architecture above, is also evidence for this domain — see cross-domain note.)*

### Domain: AutoDrive

#### KS-022 — AutoDrive Confluence Documentation
- Permitted Use: **Primary**
- Assessment Status: Provisional
- Query Intents: Reference / Explanation, How-to
- CONTENT: [NOT YET PROVIDED — Q9 depends on this. Preserve scope boundaries precisely: Taxonomy §5.5.1 notes this source covers architecture, technology stack, procedures, milestones, and handover — but explicitly NOT coding standards or fine-grained technical patterns. That absence must be preserved, not filled in, so Q10 fails correctly if this content is over-extended.]

#### KS-023 — AutoDrive Source Repository
- Permitted Use: **Supporting** (Role Ambiguity flag — see Trust Matrix §6; answered at this ceiling only, never at implied Primary confidence)
- Assessment Status: Provisional; Role Ambiguity
- Query Intents: Reference / Explanation
- CONTENT: [NOT YET PROVIDED — low priority for v0; this source's role is still disputed and its content boundary is the least well-defined of the 20.]

### Domain: Third-Party & Vendor Risk

#### KS-019 — PSC Form Guidelines and Assessment Procedures
- Permitted Use: **Supporting**
- Assessment Status: Provisional
- Query Intents: Policy / Standard
- CONTENT: [NOT YET PROVIDED — Q13 depends on this.]

#### KS-020 — TPRM Cybersecurity Form Guidelines
- Permitted Use: **Supporting**
- Assessment Status: Provisional
- Query Intents: Policy / Standard
- CONTENT: [NOT YET PROVIDED — Q13 depends on this.]

### Domain: Risk & Business Continuity

#### KS-013 — Business Impact Analysis
- Permitted Use: **Supporting**
- Assessment Status: Provisional
- Query Intents: Reference / Explanation
- CONTENT: [NOT YET PROVIDED — Q14 depends on this.]

#### KS-016 — Business Continuity Plan
- Permitted Use: **Supporting**
- Assessment Status: Provisional
- Query Intents: Troubleshooting, Reference / Explanation
- CONTENT: [NOT YET PROVIDED — Q17 depends on this.]

### Domain: Operational Support & Incident Management

#### KS-014 — RPA Continuous Improvement Framework
- Permitted Use: **Supporting**
- Assessment Status: Provisional
- Query Intents: How-to, Reference / Explanation
- CONTENT: [NOT YET PROVIDED]

#### KS-015 — Critical Incident Playbook (RPA Team)
- Permitted Use: **Supporting** (Role Ambiguity flag — see Trust Matrix §6; answered at this ceiling only, never at implied Primary confidence — this holds regardless of how detailed the source content is)
- Assessment Status: Provisional; Role Ambiguity
- Query Intents: Troubleshooting
- Source: Confluence, Robotic Process Automation Hub — last updated 04 Nov 2025 (also referenced/embedded within RPA-RB-001, DTD space playbook standard, dated 19 Feb 2026)

CONTENT:
Structured, repeatable response model for high-severity RPA disruptions. Standardizes incident handling from detection to resolution.

**Personnel:** Platform Lead — Paulo Correia. Technical Delivery Manager — Nikko Gonzales. Global Service Manager — Brian Alberto Achury Mejia. Service Delivery Lead — Czar Bragas. Service Delivery Operations Analyst — Jhon Lorenzo Mendoza. RPA Technical Leader — Maide Evangelista. Senior RPA Developers — John Rey Bautista, Jester Kent Satorre. RPA Developers — Jamyca Domiños, Julie Acibar, Gillian Rario, Maria Christine Israel, Abel Carlo Joaquin, Valentina Araque Ruiz, Maria Isabel Fawcett Salcedo.

**Severity classification:** P0 = multiple markets across multiple regions impacted. P1 = multiple markets within one region; OR multiple markets within one region during month-end closure; OR one whole market with a critical CI.

**Nine-step playbook:**
1. **Detect and Verify** — via Orchestrator/VM alerts, business reports, or stakeholder reports; classify P0/P1 per the matrix above.
2. **Open and Prime the ManageEngine Ticket** — set priority, affected process/markets, impact summary; add Technical Leader, Senior Developer, TDM, and SD Team as watchers; post initial update with time/symptoms/scope/next checkpoint per SLA.
3. **Mobilize the Right People** — engage the Technical Leader as Incident Commander for P0/P1; identify the Project Developer via the Confluence Project Repository and Team BCP contacts page. Escalation chain: **Critical Incident → Technical Leader → Technical Delivery Manager → Service Delivery Team and PMO Lead/Platform Lead.**
4. **Establish the War Room** — internal Teams chat named `CI-<Project>-<YYYYMMDD>-P0`; stakeholders explicitly excluded; invite TL(IC), Senior Developer, Project Developer, SD Team, TDM (backup to TL), Platform Lead, plus NCI/Cyber Security/Infrastructure as needed. Status huddles at least every 2 hours. Pin a Working Summary (ticket link, scope, owners, milestones, next update time).
5. **Triage and Contain** — first responder checks Orchestrator queues/schedules/last error/job logs, VM health/robot service/network reachability, ERP/portal status, credential health via 1Password, license validity. Pause failing schedules, apply safe workarounds, stop downstream effects; record all actions in the ticket.
6. **Investigate and Fix** — assign hypothesis owners (logs, credentials, ERP, infrastructure); Senior Developer and Technical Leader lead the technical deep dive; SD Team leads stakeholder communications; engage NCI/Cyber Security/Infrastructure when suspected; maintain a live action log.
7. **Communicate** — Technical Lead or Senior Developer represents progress (TDM as backup); updates at least every 2 hours in the War Room and ManageEngine per SLA. Defined message-snippet templates exist for Acknowledgment, Progress, Workaround, and Resolution updates.
8. **Recover and Validate** — end-to-end testing, confirm outputs, reconcile backlog, re-enable schedules/monitors, obtain SD Team confirmation service is normal, record business sign-off.
9. **Close the CI** — coordinate with SD Team; Technical Lead confirms impact/duration/root-cause/actions; close per SLA; attach logs, scripts, screenshots, and final status note.

**Post-Incident Review (RCA):** complete within **3–5 business days**, covering Incident Description (impact, markets, dollars, volume, time), Root Cause Identified, Corrective Actions Taken (steps, timeline, owners, outcome, validation, residual risks), Future Actions (Corrective: permanent fixes/patches/access changes; Preventive: monitoring/alerts/credential rotation/runbook updates — each with owners and due dates), and Lessons Learned.

**Roles at a glance:** Incident Commander = Technical Lead (TDM backup). Technical leadership/discussion = Senior Developer + Technical Lead. Stakeholder management/cadence = Service Delivery Team. First responder/Process SME = Project Developer (Process Champion). External support = NCI, Cyber Security, Infrastructure teams as needed.

Provenance: KS-015, Critical Incident Playbook (RPA Team), **Supporting** (Role Ambiguity — Primary/Supporting declared, ceiling applied per R13), Confluence (Robotic Process Automation Hub).

---

## 5. Explicit Out-of-Scope Declaration

This section exists so the Skill's boundary is stated positively, not just
implied by omission. If a question touches any of the following, apply
§2.7 (Coverage Gap Honesty) rather than attempting an answer:

| Topic | Why it's out of scope | Cite when declining |
|---|---|---|
| UiPath development practices, REFramework, Orchestrator specifics | Best Practices / Security Guidelines documents are Stale (last confirmed Feb-2024), no KS-ID assigned | "UiPath guidance exists but is unvalidated (Stale since Feb-2024)" |
| Power Automate development practices | Best Practices document is Stale, no KS-ID assigned | Same pattern as UiPath |
| AutoDrive coding standards, exception handling, computer vision, browser automation specifics | No source exists at this granularity (Inventory Finding KG-001) | "No AutoDrive coding-standards document has been identified" |
| Python / software engineering standards | No candidate source identified at all (Taxonomy §7.1) | "No governing source has been identified for this yet" |
| API integration patterns, testing/QA practices, logging/exception handling standards, documentation standards specifics | No candidate source identified (Taxonomy §7.1); KS-008 (Documentation) is Pending Validation | "No validated source covers this yet" |
| Azure Key Vault, UiPath Orchestrator, GitHub, or any other infrastructure/CAPE source (KS-028–KS-044) | NTI — not characterized at Trust-Matrix detail (Trust Matrix §5.3–5.5) | "This hasn't been evaluated for trust yet" |
| DRPA vs. SOLDOC documentation relationship | Known unresolved Inventory finding (KG-003) | "This is a known open gap, not yet reconciled" |
| Anything not listed in §4 | Outside the pilot's 20-source boundary entirely | "That's outside what I can currently verify" |

---

## 6. What Happens Next

**Correction to an earlier state:** source population count and question
readiness are not the same thing. A question requiring multiple sources is
not "ready" just because one of them is populated, and a question requiring
zero sources (the boundary tests) is ready regardless of population level.
The table below reflects verified per-question dependency checking against
Pilot Specification v0.1 §6, not a source-count approximation.

| # | Required source(s) | Status |
|---|---|---|
| Q1 | KS-006 | **Ready** |
| Q2 | KS-005 + KS-009 + KS-011 | Blocked — only KS-005 populated; citing it alone would silently omit required evidence |
| Q3 | KS-006 | **Ready** |
| Q4 | KS-001, KS-002 | Blocked |
| Q5 | KS-010 | **Ready** |
| Q6 | KS-007 | **Ready** |
| Q7 | KS-012, KS-021 | Blocked |
| Q8 | KS-015 | **Ready** |
| Q9 | KS-022 | Blocked |
| Q10 | None — boundary test | **Ready** |
| Q11 | None — boundary test | **Ready** |
| Q12 | None — boundary test | **Ready** |
| Q13 | KS-019, KS-020 | Blocked |
| Q14 | KS-013 | Blocked |
| Q15 | KS-006 + KS-007 (meta-pointer) | **Ready** |
| Q16 | Any two populated Primary sources (synthetic) | **Ready** |
| Q17 | KS-016 | Blocked |
| Q18 | KS-011 | Blocked |
| Q19 | None — known Inventory finding, boundary test | **Ready** |
| Q20 | Open-ended triage across all 8 domains | Partial — only 3 of 8 domains populated; a full cross-domain triage test needs broader coverage |

**11 fully Ready (Q1, Q3, Q5, Q6, Q8, Q10, Q11, Q12, Q15, Q16, Q19), 2 Partial
(Q2, Q20), 7 Blocked.**

1. **Run the 11 fully-Ready questions now.** This validates the behavioral
   shell — source selection, priority, conflict handling (Q16), and
   coverage honesty (Q10, Q11, Q12, Q19) — on evidence that is genuinely
   complete for each question, not partially available.
2. **Treat Q2 and Q20 as informative but not scorable** against §7's pass
   criteria until their remaining dependencies are populated. Running them
   now would test something real (does the Skill correctly limit itself to
   available evidence, or overclaim?) but the result shouldn't count toward
   "correct sourcing" pass/fail, since the expected-behavior bar itself
   isn't fully reachable yet.
3. **13 sources remain pending**: KS-001, KS-002, KS-009, KS-011, KS-012,
   KS-013, KS-014, KS-016, KS-019, KS-020, KS-021, KS-022, KS-023.
4. Once populated, re-run Q2, Q7, Q9, Q13, Q14, Q17, Q18, Q20 and the full
   20-question set becomes scorable.
5. Score against Pilot Specification v0.1 §7 — reporting results
   directionally ("passed the conflict-handling test in Q16") rather than
   as statistics, given the sample size.
