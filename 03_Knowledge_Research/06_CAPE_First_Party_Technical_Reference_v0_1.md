# CAPE First-Party Technical Reference v0.1

## Purpose

This document records verified CAPE product and architecture information obtained from CAPE's own internal Confluence documentation. It supplements the RPA knowledge inventory and provides the platform context required to define the RPA Development Skill correctly.

This document is a technical reference, not a source trust decision. The source itself must still be recorded and assessed in the RPA Knowledge Source Trust Matrix.

## Evidence status

- Source type: first-party internal product documentation
- Product: CAPE (Capability Accelerator Productivity Engine)
- Internal assistant persona and code name: dappy
- Current product status: proof of concept
- Main relevance: platform capabilities, Skill behavior, connectors, deployment, security, and implementation constraints
- Validation status: documented baseline; source owner and page identifiers should be recorded during Trust Matrix population

## What CAPE is

CAPE is Inchcape's internal chat application for sharing and using agents, skills, workflows, tools, projects, and artifacts. It provides a streaming chat experience with a server-side agentic tool loop and budget-aware iteration.

Current documented capabilities include:

- Streaming responses over WebSocket with an SSE fallback
- Markdown rendering, including GFM tables and syntax-highlighted code
- Image and file attachments
- A Python code interpreter that can edit files and return downloads
- On-demand skills
- Per-user connectors for Atlassian, Zoho ServiceDesk Plus, and Confluence; Outlook is documented but its availability and maturity require confirmation
- Shareable MCP and text tools
- Rich HTML and Markdown artifacts
- Forms, presentation decks, dashboards, and diagrams
- User-built agents, workflows, and projects
- Administration, metrics, feedback, and reporting surfaces

## CAPE architecture

The documented technology stack is:

- Frontend: Vite, React 19, TypeScript, and Tailwind 3
- Backend: FastAPI
- Model access: OpenAI SDK against an OpenAI-compatible server
- Transport: WebSocket chat events with an SSE fallback
- Local data store: SQLite by default
- Deployed data store: Lakebase Postgres
- Deployment target: Databricks Apps on the FastAPI runtime

On the deployed application, Lakebase Postgres is provisioned as part of deployment. Secrets and encryption keys are supplied through a secret scope. The code interpreter runs as a separate executor app that CAPE authenticates to and load-balances across a pool.

## Skills architecture

The most important implication for this project is that Skills are not a static documentation repository. CAPE documentation defines Skills as packaged domain knowledge that the assistant loads on demand.

The documented behavior is:

- Every chat receives a budgeted index of available skills.
- The model pulls a Skill body only when the request is relevant.
- Skill content does not ride with every request.
- Skills are auto-pooled and progressively disclosed.
- The Skills popover is read-only because Skills are not equipped in the same way as account-bound tools.

### Project implication

The RPA Development Skill should therefore be defined as:

> A domain-specific knowledge and instruction module that CAPE can load when an RPA-development-related request requires it, providing grounded guidance based on validated RPA knowledge sources.

It should not be defined as:

> A container into which all RPA documentation is placed.

This distinction affects the future Skill architecture, knowledge structure, source selection, testing methodology, and evaluation criteria.

## Tools and connectors relevant to the project

CAPE documents the following built-in tools:

- `run_code`
- `http_request` subject to named/scoped access, validation, authorization, and platform security controls
- `search_chat_history`
- `load_skill`
- `save_skill`

Documented connector categories include:

- Atlassian for Jira and Confluence
- Zoho ServiceDesk Plus Cloud for read-only ManageEngine ticket access
- Outlook for Microsoft 365 mail and calendar; documented availability remains subject to confirmation
- Confluence API-token access for scoped Confluence content

Connector availability and maturity should be validated before being treated as a requirement of the RPA Development Skill. In particular, Outlook availability should be confirmed because the documentation indicates it may still be under development.

## Security and data handling context

The CAPE documentation states that:

- Upstream response bodies are redacted before reaching the model.
- User-supplied URLs pass through SSRF validation.
- Tools are named and scoped rather than exposing a generic raw-request escape hatch.
- Tool exceptions are guarded so they do not terminate the chat stream.
- Opaque data is protected with randomized encryption at the store row boundary.
- Email identity columns use deterministic encryption so they remain usable as lookup keys.
- Local development may use plaintext passthrough when encryption keys are unset; this is a development-only fallback and is not an acceptable deployed configuration.

These facts provide platform context, but they do not replace RPA-specific security, credential, access, or governance requirements.

## Boundary between CAPE limitations and Skill requirements

The following distinction should remain explicit throughout the project:

### CAPE platform capabilities and limitations

Examples include:

- session or sign-in expiration
- context errors requiring refresh and prompt repetition
- table or document conversion failures
- connector availability
- proof-of-concept maturity
- tool and iteration budgets

### RPA Development Skill requirements

Examples include:

- source prioritization and trust rules
- grounded answers based on validated RPA knowledge
- architecture and platform-selection guidance
- security and governance guidance
- uncertainty handling and escalation
- consistent response structure
- traceability to approved or contextual sources

Platform limitations may affect adoption and perceived usefulness, but they should not automatically become responsibilities of the RPA Development Skill.

## Known CAPE behavioral limitations for evaluation

The CAPE feedback evidence identifies platform and response-quality risks that should be tested separately from RPA knowledge quality:

- poor contrast or weak branding in generated outputs;
- hidden navigation or subtle progress indicators;
- long-output truncation;
- overengineering simple requests;
- incorrect handling of ties or classifications;
- unsupported inference, including invented stakeholders or deadlines.

These observations are evaluation inputs and platform context. They do not authorize the Skill to invent missing facts or replace CAPE platform fixes with Skill instructions.

## Implications for the project

The newly verified CAPE information requires the following updates to the project direction:

1. Replace architectural assumptions with documented CAPE evidence where available.
2. Treat the CAPE documentation as a first-party source candidate in the Trust Matrix.
3. Update the Skill definition to describe on-demand domain knowledge and instructions.
4. Keep platform architecture separate from RPA source governance.
5. Include CAPE loading behavior, context limits, connectors, and tool boundaries in the future Skill specification.
6. Test whether the Skill loads and responds appropriately for relevant RPA requests rather than testing only whether documentation is present.
7. Track CAPE platform limitations separately from RPA developer needs and Skill requirements.

## Required follow-up

Before freezing the revised Phase 1 baseline:

- record exact Confluence page URLs or identifiers;
- confirm the accountable owner for the CAPE documentation;
- assess the source using the RPA Knowledge Source Trust Matrix;
- verify which documented connectors and capabilities are currently available in the CAPE user interface;
- update the RPA Development Skill Specification when that artifact is created.

## CAPE feedback mechanism

CAPE includes a feedback mechanism for bugs, ideas, and general feedback. The documented mechanism supports a message, up to three screenshots, automatically captured origin, encrypted messages and screenshots, an administrator feedback inbox, and CSV export.

This provides a potential existing evidence stream for the project, complementary to project-specific RPA user discovery. It should be used to distinguish platform experience issues from RPA developer needs and Skill requirements.

## Databricks boundary

The CAPE documentation confirms Databricks Apps, Lakebase Postgres, Databricks identity/proxy information, secret management, and the separate executor application. It does not establish that CAPE uses Unity Catalog, AI Gateway, Genie, Agent Bricks, Lakeflow, Lakehouse, Genie Ontology, Genie Code, MCP through Genie, Lakewatch, or CustomerLake.

Those concepts must remain separate potential Databricks platform context until supported by CAPE-specific evidence.
