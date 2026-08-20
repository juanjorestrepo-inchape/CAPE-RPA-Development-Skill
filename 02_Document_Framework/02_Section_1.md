The proposed user-feedback exercise will fit particularly well here, because we can establish the current state from two complementary perspectives:

Internal RPA development workflow + actual CAPE user experience.

## CAPE Platform Context

CAPE (Capability Accelerator Productivity Engine) is Inchcape's internal AI productivity platform, developed by the Digital Delivery Centers. It provides a conversational AI interface through which users can access models, tools, connectors, skills, agents, workflows, projects, and generated artifacts.

CAPE is currently documented as a proof-of-concept platform and is deployed as a Databricks App using a FastAPI backend and a Vite/React frontend. The deployed application uses Lakebase Postgres as its persistent data store. Model access is implemented through the OpenAI SDK and an OpenAI-compatible server; the specific underlying model providers are configurable and are not disclosed in the available documentation.

CAPE's Skills architecture provides domain-specific knowledge modules that are loaded on demand when relevant to a user request. Skills are progressively disclosed rather than manually activated per conversation.

## Proposed Skill Operating Environment

The RPA Development Skill will operate as a knowledge and instruction layer inside CAPE's agentic architecture:

```text
RPA Developer Request
	|
	v
      CAPE
	|
	v
 Relevance Detection
	|
	v
RPA Development Skill
	|
	+-- RPA Knowledge
	+-- Development Standards
	+-- Architecture Guidance
	+-- Troubleshooting Guidance
	+-- Security / Governance
	+-- Lifecycle Procedures
	+-- Official Source References
	|
	v
 Grounded Response
```

The Skill is not the model and is not a repository containing all RPA documentation. It is a domain-specific knowledge and instruction module that CAPE can load when an RPA-development-related request requires it, providing grounded guidance based on validated RPA knowledge sources.

## Confirmed CAPE Technical Baseline

| Component | Documented implementation or boundary |
| --- | --- |
| Frontend | Vite, React 19, TypeScript, Tailwind 3 |
| Backend | FastAPI |
| Model access | OpenAI SDK against an OpenAI-compatible server |
| Transport | WebSocket with SSE fallback |
| Deployment | Databricks Apps |
| Data stores | SQLite locally; Lakebase Postgres in deployment |
| Code execution | Separate capability-stripped executor application |
| Tools | MCP, text, and connector tools; named and scoped |
| Connectors | Atlassian, Zoho ServiceDesk Plus, and Confluence API-token access; Outlook requires availability confirmation |
| Identity | Databricks Apps `X-Forwarded-Email` identity context |
| Skills | Indexed, progressively disclosed, and loaded on demand |

CAPE provides the chat, agent, tool, connector, storage, and artifact infrastructure. The RPA Development Skill does not recreate those platform capabilities.

## Governance and Security Boundary

CAPE platform data governance and RPA Skill knowledge governance are separate concerns. CAPE governs platform storage, encryption, retention, and access to chats, attachments, execution history, artifacts, credentials, and project memory. The Skill governs which validated RPA sources it may use and how it should represent uncertainty.

The Skill must operate within CAPE's authorization and security controls. It must not instruct users to bypass credential, privacy, access-control, connector, or organizational governance requirements.

## Known CAPE Limitations for Evaluation

Known platform observations and feedback should inform evaluation without becoming automatic Skill requirements. The evaluation should test handling of output truncation, poor readability or contrast, hidden navigation, subtle progress indicators, overengineering, unsupported inference, invented stakeholders or deadlines, and tied recommendations.

## Architecture Boundary

The project will document confirmed CAPE architecture separately from general Databricks platform capabilities. CAPE documentation confirms Databricks Apps, FastAPI, Lakebase Postgres, Databricks identity/proxy information, secret management, a separate Python executor application, and OpenAI-compatible model access.

Unity Catalog, AI Gateway, Genie, Agent Bricks, Lakeflow, Lakehouse, Genie Ontology, Genie Code, MCP through Genie, Lakewatch, and CustomerLake are not treated as CAPE components without additional CAPE-specific evidence.