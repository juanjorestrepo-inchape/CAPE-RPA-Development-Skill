1. DOCUMENTS UPDATE CORRECTIONS

The new CAPE documentation is not merely additional background. It changes several factual assumptions about CAPE's architecture, Skill mechanism, tool/connector model, security boundaries, data handling, and current limitations. Those changes affect:

1. CAPE — RPA Development Skill | Project & Technical Specification
> This is the project-level governing document. It needs a controlled amendment so that its CAPE description, technical assumptions, requirements, scope, and references accurately reflect the actual platform.

2. RPA Knowledge Inventory v0.1
> This is the Phase 1 deliverable. It needs the new CAPE documentation added as knowledge sources and, more importantly, classified appropriately rather than simply appended to the source list.

---

# 1. What the new CAPE documentation changes
I would treat the documentation you just provided as a new evidence set discovered after the original inventory, not as something that should automatically override the existing RPA documentation.

That distinction is important.

The new material establishes several things that were either missing or less precise in v0.1.

## 1.1 CAPE is more clearly defined as a Skill platform
The existing specification already says that CAPE provides reusable domain-specific Skills.

The new documentation gives us a much more precise description:
> Skills are packaged domain knowledge that CAPE loads on demand when relevant.

That matters for the project because our proposed RPA Development Skill is not a conventional standalone application, chatbot, RAG system, or autonomous agent.

It is a CAPE Skill operating inside an existing agentic platform.

That should become an explicit architectural constraint in the Project Specification.

### Correction needed
We should change the conceptual framing from:

> "build an AI assistant that consolidates RPA knowledge"

toward:

> "design and validate a domain-specific CAPE Skill that provides structured RPA development knowledge and behavioral guidance within CAPE's existing agentic architecture."

That is much more technically accurate.

---

2. The Skill architecture is now much clearer

The new documentation tells us:

- Skills are loaded on demand.
- Skills are progressively disclosed rather than manually equipped.
- There is a `load_skill` mechanism.
- CAPE has a skill index.
- A meta-skill can create/save new Skills.
- Skills are different from agents, workflows, and tools.
- Agents have `before_message` and `on_finish`.
- Tools can be MCP, text, or connectors.
- Projects can inject instructions and memory.
- The user's EquipBar controls models, agents, workflows, tools, and projects, but not Skills.

This distinction is important.

Our project specification currently talks about the Skill somewhat generically.

We can now specify the architectural model much more accurately:

```text
                         CAPE
                          │
              ┌───────────┴───────────┐
              │                       │
        Agentic Chat Loop        Skill System
                                      │
                              On-demand loading
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                 RPA Development Skill      Other Skills
                          │
              ┌───────────┼───────────┐
              │           │           │
           RPA Docs     Standards   Guidance
              │           │           │
          Confluence   GitHub/etc.  External
```

The Skill therefore does not need to recreate CAPE's chat, agent, tool, storage, or connector infrastructure.

That should be explicitly stated.

---

# 3. CAPE's actual architecture should be corrected in the Project Specification

The existing specification says CAPE has access to:
> Confluence and read-only Service Desk information, together with additional tools for code execution, HTTP requests, user chat history, reusable Skills, files, and rich generated artifacts.

That is directionally correct, but the new documentation is considerably more precise.

We now know:

| Component          | Confirmed CAPE implementation                                                               |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Frontend           | Vite + React 19 + TypeScript + Tailwind 3                                                   |
| Backend            | FastAPI                                                                                     |
| Model access       | OpenAI SDK / OpenAI-compatible server                                                       |
| Primary transport  | WebSocket                                                                                   |
| Fallback transport | SSE                                                                                         |
| Deployment         | Databricks Apps                                                                             |
| Database           | Lakebase Postgres in deployment                                                             |
| Local database     | SQLite                                                                                      |
| Code execution     | Separate capability-stripped executor                                                       |
| Skills             | On-demand, progressively disclosed                                                          |
| Connectors         | Atlassian, Zoho ServiceDesk Plus, Confluence API-token; Outlook apparently still developing |
| Tools              | MCP, text, connector                                                                        |
| Identity           | Databricks Apps `X-Forwarded-Email`                                                         |
| Artifacts          | Markdown/HTML + specialized forms/decks/dashboards/diagrams                                 |
| Projects           | Conversations + instructions + persistent memory                                            |
| Agents             | System prompt + `before_message` + `on_finish`                                              |

This is sufficiently important that I would update Section 1.2 and probably Section 10 of the Project Specification.

---

# 4. The new documentation also changes how we should think about connectors

This is particularly important for the Skill.

The new documentation says that CAPE has per-user authenticated connectors.

For example:

- Atlassian → Jira + Confluence
- Zoho ServiceDesk Plus → read-only named tools
- Confluence API-token connector
- Outlook → Microsoft Graph, but apparently still under development

This gives us an important architectural principle:

> The RPA Development Skill should not assume that every knowledge source is directly available to it merely because CAPE supports the corresponding connector.

Instead

```text
Knowledge Source
      │
      ▼
Is it accessible through CAPE?
      │
      ├── No ──► Inventory / Trust Matrix only
      │
      └── Yes
           │
           ▼
     Is the source authorized?
           │
           ├── No ──► Do not use
           │
           └── Yes
                │
                ▼
        Is it trustworthy enough?
                │
                ├── No ──► contextual / restricted use
                │
                └── Yes ──► eligible Skill knowledge
```

This actually strengthens the logic behind the Trust Matrix.

---

# 5. The Data Policy gives us an important distinction

The new documentation says:
> Administrators cannot read user chats or private artifacts.

But it also says administrators can see:

- email
- request counts
- token counts
- model tier
- usage information.

And importantly, CAPE stores:

- chats
- attachments
- extracted attachment text
- code execution history
- generated files
- tool credentials
- project memory
- presenter notes
- shared chat snapshots.

That means the RPA Skill project should explicitly distinguish between:

## Platform data governance

What CAPE itself stores, encrypts, retains, and exposes.

## Skill knowledge governance

What information the RPA Development Skill is permitted to use as knowledge.

These are different concerns.

I recommend adding this distinction to the Project Specification.

---

# 6. The new documentation confirms an important security boundary

The CAPE architecture includes:

- encrypted storage
- AES-SIV for identity fields
- Fernet for opaque content
- SSRF validation
- upstream response redaction
- scoped/named tools
- no generic raw-request escape hatch
- sandboxed HTML artifacts
- capability-stripped code executor.

This is useful, but we should not accidentally turn the RPA Skill specification into a CAPE security specification.

The correct relationship is:
> CAPE provides platform-level security controls; the RPA Development Skill must operate within those controls and must not instruct users to bypass them.

That aligns with the existing requirement:
> The Skill must not encourage insecure credential handling, unauthorized access, or bypassing organizational controls.

So I would strengthen that requirement rather than duplicate CAPE's entire security architecture.

---

# 7. The new CAPE Feedback is especially valuable

This is probably the most important addition from a Skill design perspective.

The feedback identifies actual CAPE failure modes:

## Output quality
- poor contrast
- weak branding
- hidden navigation
- overly casual emoji usage
- subtle progress indicators

## Model behavior
- long output truncation
- overengineering simple requests
- incorrect handling of ties
- unsupported inference
- incorrect classifications

These aren't necessarily RPA Skill knowledge sources.

Instead, they are platform behavioral constraints / known CAPE limitations.

They should therefore influence the project specification's:
- assumptions
- risks
- evaluation design
- acceptance criteria.

For example:

## New evaluation concern

We should explicitly test that the RPA Skill:
- does not invent stakeholders;
- does not invent deadlines;
- does not infer undocumented organizational requirements;
- handles ambiguity explicitly;
- handles tied recommendations correctly;
- avoids unnecessarily complex solutions;
- does not exceed practical output limits unnecessarily.

That is directly supported by the CAPE testing evidence you supplied.


---

# 8. The biggest impact on RPA Knowledge Inventory v0.1

This is where I would make the larger correction.

Your existing Inventory correctly concludes that knowledge is fragmented across:

- Confluence
- GitHub
- Service Desk
- project repositories
- technology-specific documentation.

That conclusion remains valid.

However, we now have an additional knowledge domain:

> CAPE platform knowledge

And that knowledge is relevant because the deliverable being built is itself a CAPE Skill.

I would therefore add a dedicated section:

## CAPE Platform and Skill Architecture Knowledge

Something along these lines:

| ID          | Knowledge Source                               | Repository       | Domain                     | Authority   | Relevance | Currency | Initial Skill Role      | Evidence      | Action  |
| ----------- | ---------------------------------------------- | ---------------- | -------------------------- | ----------- | --------- | -------- | ----------------------- | ------------- | ------- |
| KS-CAPE-001 | CAPE — Overview and Features                   | Confluence / DTD | CAPE / Skills              | High        | Very High | Current* | Primary                 | Documented    | Include |
| KS-CAPE-002 | CAPE — Architecture                            | Confluence / DTD | Architecture               | High        | Very High | Current* | Primary                 | Documented    | Include |
| KS-CAPE-003 | CAPE — Tools and Connectors                    | Confluence / DTD | Tools / Integrations       | High        | Very High | Current* | Primary                 | Documented    | Include |
| KS-CAPE-004 | CAPE — Projects, Agents, and Workflows         | Confluence / DTD | Agent architecture         | High        | High      | Current* | Supporting              | Documented    | Include |
| KS-CAPE-005 | CAPE — Artifacts, Decks, Dashboards, and Forms | Confluence / DTD | Artifacts                  | Medium/High | Medium    | Current* | Contextual              | Documented    | Review  |
| KS-CAPE-006 | CAPE — Admin, Metrics, and Deployment          | Confluence / DTD | Operations / Deployment    | High        | High      | Current* | Supporting              | Documented    | Include |
| KS-CAPE-007 | CAPE — Data Policy                             | Confluence / DTD | Security / Data Governance | High        | Very High | Current* | Primary/Supporting      | Documented    | Include |
| KS-CAPE-008 | CAPE Feedback                                  | Confluence / DTD | Platform limitations       | Medium/High | High      | Current* | Supporting              | Observational | Include |
| KS-CAPE-009 | CAPE — Discovery & Definition                  | Kanban           | Project governance         | High        | Very High | Current  | Primary project context | Documented    | Include |
| KS-CAPE-010 | CAPE RPA Development Skill — Phase 1 & 2       | Kanban           | Project execution          | High        | Very High | Current  | Project context         | Documented    | Include |

The `*` should remain explicitly subject to verification of the actual Confluence page metadata/version when we do the final inventory update.

I would **not blindly label everything "Current" merely because the page was recently found.**

That would contradict the Trust Matrix philosophy we have already established.

---
# 9. The Inventory's source hierarchy should also be refined

The current hierarchy is:

1. Organizationally authoritative
2. Technology-specific/development
3. Operational knowledge
4. External authoritative
5. Supplementary.

That is good for RPA engineering knowledge.

But CAPE documentation introduces a different dimension.

I would not simply create a "Tier 0 CAPE" above everything else.

Instead, I recommend adding a source-domain classification.

For example:

```text
                    Knowledge Source
                           │
          ┌────────────────┴────────────────┐
          │                                 │
    RPA Domain Knowledge             CAPE Platform Knowledge
          │                                 │
          ▼                                 ▼
 RPA governance/standards          CAPE architecture/features
 AutoDrive/UiPath/etc.             Skill architecture
 Service Desk                       Tools/connectors
 External technical docs            Data/security model
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
                 Trust Assessment
                         │
          ┌──────────────┼──────────────┐
       Authority       Currency      Applicability
                         │
                         ▼
                  Permitted Skill Use
```
This is much cleaner than mixing CAPE architecture documentation with RPA engineering standards.

---

# 10. There is also a terminology correction we should make

The new documentation repeatedly distinguishes:

## Skills
Reusable domain knowledge loaded on demand.

## Agents
Configured behavior with prompts/hooks.

## Workflows
Shareable workflow objects.

## Tools
MCP/text/connectors.

## Projects
Conversation clusters with instructions and memory.

These should not be used interchangeably in our project documents.

Our project is specifically:
> CAPE RPA Development Skill

not:

> RPA Agent

not:

> RPA Workflow

not:

> RPA Chatbot.

This should be made explicit in the Project Specification's terminology.

---

# 11. One important correction to the original Project Specification

The original specification says:
> "CAPE (Capability Accelerator Productivity Engine) is an AI-enabled internal platform designed to support users through reusable domain-specific Skills and connected organizational tools."

That is fine.

But now we can make it technically stronger:

> "CAPE (Capability Accelerator Productivity Engine) is Inchcape's internal AI chat application and productivity platform in which users can access reusable Skills, agents, workflows, tools, connectors, projects, and artifacts. The RPA Development Skill is implemented as a domain-specific Skill within this existing platform rather than as an independent application or AI system."

That sentence is worth adding because it prevents architectural scope creep.

---

# 12. Should we change the Project Specification version?

Yes.

I would **not overwrite v0.1.0.**

I recommend:

## Current

`CAPE_RPA_Development_Skill_Project_Specification_v0.1.0`

## Corrected

`CAPE_RPA_Development_Skill_Project_Specification_v0.2.0`

with:

> Status: Revised Draft / Phase 1 Amendment

The reason is that this isn't a typo correction. We are incorporating newly discovered authoritative platform documentation into the project baseline.

---

# 13. What about the Inventory version?

Similarly:

## Current

`RPA Knowledge Inventory_v0.1`

## Corrected

`RPA Knowledge Inventory_v0.2`

But I would preserve the original v0.1 as an historical baseline.

The new v0.2 should explicitly state:

> Revision rationale: Incorporation of newly identified CAPE platform documentation and project execution evidence discovered during Phase 1.

This gives us an audit trail.

---

# 14. What I would NOT change

This is equally important.

The new documentation does not justify changing several fundamental conclusions.

For example, the Inventory's Finding 2 remains correct:

> The principal challenge is knowledge fragmentation and accessibility.

Finding 3 also remains correct:

> Source quality cannot be determined from repository location alone.

And the conclusion that AutoDrive requires priority attention remains valid.

Likewise, the Project Specification's core proposition remains valid:

> the problem is not fundamentally a lack of technical knowledge, but difficulty accessing, contextualizing, and consistently applying it.

So this is not a project restart.

It is a controlled Phase 1 amendment.

---

# 15. Recommended correction strategy

I recommend this exact sequence:

## Document A — Project Specification

Revise to v0.2.0

Changes:
1. CAPE definition.
2. CAPE architectural context.
3. Skill architecture and on-demand loading.
4. Distinction between Skills, Agents, Workflows, Tools and Projects.
5. CAPE technical architecture.

---

6. Connector/tool availability assumptions.
7. Security and data-policy context.
8. CAPE known limitations.
9. Skill-specific requirements.
10. Evaluation criteria influenced by known CAPE failure modes.
11. References.
12. Document control / revision history.

## Document B — RPA Knowledge Inventory

Revise to v0.2

Changes:

1. Add CAPE documentation as a knowledge-source domain.
2. Add CAPE source IDs.
3. Classify each source.
4. Add authority/relevance/currency/evidence/ownership assessment where supported.
5. Distinguish CAPE platform knowledge from RPA domain knowledge.
6. Add CAPE architecture as a dependency of the Skill.
7. Add CAPE limitations/feedback as contextual evidence rather than normative RPA guidance.
8. Update knowledge gaps.
9.  Update findings where necessary.
10.  Update inventory status and next step.
11.  Preserve the Trust Matrix as the next formal artifact.

---

# 16. The resulting Phase 1 chain becomes much stronger

The project now has a much cleaner evidence chain:

```text
PHASE 0
Discovery & Definition
        │
        ▼
Understand CAPE + RPA problem
        │
        ▼
PHASE 1
RPA Knowledge Inventory
        │
        ├── RPA organizational knowledge
        ├── Technology knowledge
        ├── Operational knowledge
        └── CAPE platform knowledge
                │
                ▼
       Source validation
                │
                ▼
PHASE 2
Knowledge Source Trust Matrix
        │
        ├── Authority
        ├── Currency
        ├── Applicability
        ├── Evidence quality
        └── Ownership
                │
                ▼
PHASE 3
Knowledge Architecture / Taxonomy
                │
                ▼
PHASE 4
RPA Development Skill Design
                │
                ▼
PHASE 5
Implementation in CAPE
                │
                ▼
PHASE 6
Evaluation + Pilot

```

This is materially better than treating the Inventory as merely a list of documents.

--- 
# 17. which document are we correcting?

Both.

But their roles are different:

| Document                                             | Action                   | Why                                                                                                       |
| ---------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| **CAPE RPA Development Skill Project Specification** | **Amend**                | New CAPE evidence changes the technical and architectural baseline of the project                         |
| **RPA Knowledge Inventory v0.1**                     | **Amend**                | New CAPE documentation is itself a relevant knowledge-source domain and changes the Phase 1 evidence base |
| **Trust Matrix**                                     | **Do not rewrite yet**   | It is the next Phase 2 artifact; the new CAPE sources should first enter the inventory                    |
| **RPA Development Skill itself**                     | **Do not implement yet** | We are still establishing the knowledge and trust foundation                                              |

So the order should be:

> New CAPE evidence → revise Project Specification → revise Inventory → freeze Phase 1 → build/update Trust Matrix → continue Phase 2.

This is consistent with the project's original principle of "Trust Before Breadth": we should not start building the Skill from newly discovered material until its role and trust have been classified.

---

# 16. Recommended project sequence

```text
[COMPLETED]
Project Specification v0.2.0
        │
        ▼
[COMPLETED]
RPA Knowledge Inventory v0.2.0
        │
        ▼
[NEXT]
RPA Knowledge Source Trust Matrix
        │
        ▼
[NEXT]
RPA Knowledge Taxonomy
        │
        ▼
[THEN]
RPA Development Skill Functional Specification
        │
        ├── RAG / retrieval architecture
        ├── knowledge ingestion
        ├── chunking
        ├── metadata
        ├── embeddings / vector search
        ├── retrieval strategy
        ├── source attribution
        ├── response grounding
        ├── fallback / escalation
        └── security & governance
        │
        ▼
[THEN]
Skill Implementation
        │
        ▼
Evaluation Dataset + Evaluation Framework
        │
        ▼
Pilot
        │
        ▼
Adoption Decision
```

