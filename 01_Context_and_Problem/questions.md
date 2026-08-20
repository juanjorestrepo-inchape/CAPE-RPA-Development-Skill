## 1. What RPA platform does your team actually use?

The team uses a **multi-platform, cost-first architecture** with four tools:

| Tool | Role | Cost | Priority |
|------|------|------|----------|
| **AutoDrive** | In-house Python framework (PyAutoGUI, pywin32, Selenium, OpenCV) for UI automation and data tasks | Free | 1st choice (default) |
| **Power Automate Cloud** | Microsoft ecosystem automation (SharePoint, Forms, Teams) | Licensed (M365) | For MS workloads |
| **UiPath** | Enterprise RPA for complex, multi-system processes | Licensed (expensive, per-bot) | Last resort |
| **Azure AI Foundry / Databricks** | AI/ML layer for intelligent document processing | Consumption-based | AI layer |

The decision framework: every request starts with AutoDrive. UiPath only kicks in when AutoDrive can't handle it (3+ applications, persistent state, enterprise-grade orchestration) and requires market approval of the licensing cost.

[RPA Strategy](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/6890094871/RPA+Strategy) · [RPA Architecture — Overview](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/9025257486/RPA+Architecture+Overview)

---

## 2. What does the current development lifecycle look like?

A **10-phase Project Intake Framework** from request to BAU handover:

1. **Request & Approval** — Market submits DAP Request Form via Distribution Excellence
2. **Discovery & Scoping** — Gather data, recordings, access requirements → Scoping Document
3. **Project Repository Document** — Developer documents exec summary, scope, tech stack, technical flow, procedures
4. **Architecture Review & Kickoff** — Scrum Master schedules kickoff; Architecture team approves or requests revisions
5. **Development** — Build per approved technical flow; maintain Project Updates section
6. **UAT** — BA/Scrum Master coordinates testing; user provides formal email sign-off
7. **Internal CAB (Pre-CAB)** — Present readiness using Major Release CAB Framework
8. **Global CAB (Production CAB)** — Regression testing, risk review, cutover plan finalized
9. **Deployment** — Deploy per approved cutover plan; confirm success
10. **Hypercare & BAU Handover** — Monitor post-deployment; KT to BAU team at least 2 weeks before hypercare ends

[RPA Project Intake Framework](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/8848212048/RPA+Project+Intake+Framework)

---

## 3. What documentation exists in Confluence?

Based on the DRPA and SOLDOC spaces, the documentation library includes:

- **RPA Service Definition Document** — Team overview, solution overview, tech stack, service architecture
- **RPA Strategy** — Cost-first decision framework, tool comparison, capability thresholds
- **RPA Project Intake Framework** — 10-phase delivery lifecycle
- **RPA Architecture — Overview** — Trigger sources, automation platforms, target systems, data/integration layers, monitoring, governance
- **UiPath Best Practices** — Naming conventions, workflow design, readability, logging, exception handling, security
- **Power Automate Best Practices** — Naming conventions, variables, action naming
- **UiPath Security Guidelines** — Orchestrator assets, role-based access, secure development/deployment
- **RPA User Access Process** — UiPath Orchestrator access procedure
- **RPA CAPTCHA and MFA Policy** — How to handle CAPTCHAs/MFA in automation
- **RPA CI Framework** — Critical Incident severity matrix (P0-P4), coverage model, escalation
- **Critical Incident Playbook** — Step-by-step incident response and RCA process
- **RPA Incident Reports** — Historical incident log
- **RPA Data Policy** — Data ownership, protection, compliance, auditing
- **Change Management** — Major, minor, standard, emergency change classifications
- **Solution Documentation** — Project repository with all active/BAU projects
- **Job Descriptions** — Associate, Consultant, Developer, Tech Lead roles
- **Proposal: In-House RPA Tool Development** — AutoDrive origin and rationale
- **SAP Robot (RPA) User Policy** — SAP service account standards

[RPA - Solution Documentation](https://inchcapeglobal.atlassian.net/wiki/spaces/SOLDOC/pages/8848212104/RPA+-+Solution+Documentation) · [DRPA Space](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/overview)

---

## 4. What questions do developers repeatedly ask?

Based on the documentation, governance goals, and incident history, the recurring themes are:

- **Access & credentials** — "How do I get UiPath Orchestrator access?", "Where are credentials stored?", "How do I request VM/PROD access?" (documented in RPA User Access Process and Security Guidelines)
- **Naming conventions** — "How should I name variables/arguments/workflow files?" (addressed in UiPath & Power Automate Best Practices)
- **Architecture approvals** — "Can AutoDrive handle this or do I need UiPath?" (Strategy decision tree)
- **CAB/Change process** — "What do I need before Pre-CAB?", "How do I raise a Hypercare ticket?" (Intake Framework Phase 7-8)
- **Incident handling** — "How do I classify this issue?", "Who do I escalate to?" (CI Framework escalation matrix)
- **CAPTCHA/MFA** — "What do I do when the bot hits MFA?" (CAPTCHA/MFA Policy)
- **Governance/audit prep** — Repeated governance questions are being converted into reusable checklists per Q3 2026 goals

[2026-Q3 Goals — Personal Goals](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9381446207/2026-Q3+Goals+Personal+Goals)

---

## 5. What are the biggest sources of wasted time?

From the documentation and project history:

- **VM procurement** — Previously took ~4 months for a single project; identified as a top challenge in the Americas migration
- **Credential lockouts / password management** — Incidents caused by VM memory full (unrestarted for 26 days), credential expiry, and PAM360 access issues
- **CAB process overhead** — 10-phase lifecycle with Pre-CAB + Production CAB; requires regression testing, risk docs, cutover plans
- **ManageEngine deep-link restrictions** — API testing revealed "URL not authorized" errors when trying to navigate tickets directly, forcing workarounds
- **CAPTCHA/MFA manual interventions** — Bot failures that are accepted risk (P4 priority), but still consume developer attention
- **Knowledge transfer gaps** — Noted in the Americas migration ("changes not properly handed over to the Operations team")
- **Zoho API limitations** — Cannot retrieve full email conversation body, requiring fallback to UiPath/web-based approaches
- **Documentation rework** — Weekly bot score checks enforce documentation quality; Q3 goals explicitly target repeated governance questions being answered individually instead of via checklists

[RPA Americas Migration Plan](https://inchcapeglobal.atlassian.net/wiki/pages/viewpageattachments.action?pageId=7333183548&preview=%2F7333183548%2F8116076600%2FRPA+Americas+Migration+Plan.pptx) · [RPA Incident Reports](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/6870827686/RPA+Incident+Reports)

---

## 6. What capabilities can a CAPE Skill actually access?

Per the CAPE documentation, a skill can leverage:

**Built-in tools:**
- `run_code` — Python code interpreter with common data libraries
- `http_request` — Authorized HTTP access through CAPE's scoped tools and platform validation
- `search_chat_history` — User's own past conversations
- `load_skill` / `save_skill` — Load and save reusable skills

**Connectors (per-user authenticated access):**
- **Atlassian** — Jira and Confluence
- **Zoho ServiceDesk Plus Cloud** — ManageEngine SDP tickets (10 named read-only tools)
- **Outlook** — Microsoft 365 mail and calendar via Microsoft Graph; availability and maturity require confirmation
- **Confluence (API token)** — 8 named scoped tools for Confluence content

**Other capabilities:**
- Image and file attachments (PDF, Word, PowerPoint, Excel, CSV)
- Rich artifacts (shareable HTML/Markdown, forms, presentation decks, dashboards, diagrams)
- Budget-aware agentic tool loop with iteration cap

[CAPE — Tools and Connectors](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474015883/CAPE+Tools+and+Connectors) · [CAPE — Overview and Features](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474801809/CAPE+Overview+and+Features)

---

## 7. How are Skills technically defined?

In CAPE, skills are **packaged domain knowledge the assistant loads on demand**:

- Every chat lists available skills as a **budgeted index** — the model pulls a skill body only when relevant (skill content does NOT ride every request)
- A skill's `tool_type` can be:
  - `mcp` — Standard MCP server config, connected at chat time over stdio, sessions cached by config hash
  - `text` — Free-form instructions injected into the system prompt
  - `connector` — Per-user access to a SaaS provider
- Skills can carry `<<VAR>>` placeholders filled from a per-user value form
- Users can create skills via the `save_skill` built-in tool or through admin-managed global skills
- Shipped skills cover: form building, presentations, dashboards, diagrams, branding, email writing, minutes, grammar/rewrite, spreadsheets, company info, and a meta skill for creating new skills from chat

[CAPE — Overview and Features](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474801809/CAPE+Overview+and+Features)

---

## 8. What sources can be embedded/referenced?

A CAPE skill can reference:

- **Confluence pages** — via Atlassian connector or API token connector (8 scoped tools, Markdown in/out)
- **Jira issues/projects** — via Atlassian connector
- **ManageEngine/Zoho SDP tickets** — via Zoho ServiceDesk Plus Cloud connector (read-only)
- **Outlook email/calendar** — via Microsoft Graph connector
- **Authorized HTTP access** — via CAPE's scoped tools, subject to connector availability, validation, and platform security controls
- **User-uploaded files** — PDF, Word, PowerPoint, Excel, CSV, text files (converted to Markdown as context)
- **Images** — Attached and sent to model as vision content
- **Chat history** — User's own past conversations via `search_chat_history`
- **Other MCP servers** — Any standard MCP-compatible external tool

[CAPE — Tools and Connectors](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474015883/CAPE+Tools+and+Connectors)

---

## 9. Can Skills provide citations?

**Not explicitly documented as a built-in feature in CAPE's current architecture.** The documentation describes how skills are loaded on demand and how the assistant processes content, but there's no documented citation-linking mechanism in the CAPE skill framework. However:

- The `load_skill` mechanism references specific skill bodies by name
- Confluence connectors return page content that could be linked back
- The `http_request` tool could fetch and reference source URLs
- A skill defined as `text` type (free-form instructions) could include citation instructions in its prompt

For Atlassian's Rovo (the product you're chatting with right now), citations are a built-in feature — answers include source links. For CAPE, this would need to be **engineered into the skill's instructions** or built as a feature.

---

## 10. What level of control do you have over Skill instructions?

**Full control:**

- **Admin-managed global skills** — Owned by a reserved system user, always public, managed through the admin dashboard
- **User-created skills** — Any user can `save_skill` from a conversation to create private skills
- **Text-type tools** — Free-form instructions injected directly into the system prompt (full natural-language control)
- **MCP-type tools** — Standard MCP server configs with customizable parameters
- **`<<VAR>>` placeholders** — Configurable per-user variables filled from value forms when equipped
- **EquipBar** — Users equip and manage tools; Skills are indexed and loaded automatically when relevant
- **Budgeted skill index** — Admin controls which skills are listed and their priority

The instructions are configurable text executed within CAPE's existing tool, authorization, security, and governance boundaries — they define the Skill's behavior without bypassing platform controls.

[CAPE — Tools and Connectors](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474015883/CAPE+Tools+and+Connectors)

---

## 11. How is CAPE currently evaluated?

CAPE is evaluated through a **feedback-driven approach**:

- **CAPE Feedback page** — Contains user-submitted test prompts with structured evaluation criteria (requirements passed/failed, readability issues, mathematical correctness, layout quality)
- **Test Result checklists** — Each output is graded against the original prompt requirements
- **Usage-and-cost Metrics page** — Admin dashboard tracks usage data and LLM costs
- **Manual QA-style testing** — Users submit complex prompts and evaluate outputs for correctness, scoring, design, and text contrast
- **Status: Proof of Concept** — The product is acknowledged as POC stage, meaning evaluation is informal and iterative rather than production-grade

No documented automated eval framework (like evals or benchmark suites) was found. The process appears to be human-reviewed against prompt requirements.

[CAPE Feedback](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9345368871/CAPE+Feedback) · [CAPE (Capability Accelerator Productivity Engine)](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474736299/CAPE+Capability+Accelerator+Productivity+Engine)

---

## 12. What does "Service Desk read-only" actually expose?

The **Zoho ServiceDesk Plus Cloud** connector exposes **10 named read-only tools** for ManageEngine SDP tickets. Based on the ManageEngine API Integration documentation, the connector likely surfaces:

- Ticket/request listing and details (ID, subject, status, priority, category, subcategory)
- Requester information
- Technician assignment
- Ticket timestamps (created, resolved, due by, completed)
- Urgency and impact fields
- Group and site assignment
- Service category
- Request type (Incident, Service Request, etc.)
- Approval status and escalation status
- Notes indicator

**Key limitations documented:**
- Read-only (no write/update operations)
- Security: every upstream response body is redacted before reaching the model (credentials never leak)
- Connector tokens are stored per-user and encrypted

[CAPE — Tools and Connectors](https://inchcapeglobal.atlassian.net/wiki/spaces/DTD/pages/9474015883/CAPE+Tools+and+Connectors) · [Manage Engine API Integration](https://inchcapeglobal.atlassian.net/wiki/spaces/PA/pages/7274726145/Manage+Engine+API+Integration)

---

## 13. What RPA coding standards already exist internally?

Yes, documented standards exist:

### UiPath Best Practices
- **Naming**: Solution = "AU_ANX_Service_Order" pattern; Variables = camelCase with data type prefix (str, int, arr, dt); Arguments = direction prefix (In_, Out_); Workflow files = verb-based short names; Activities = meaningful names (not defaults); Assets/Queues = include process name + descriptions
- **Workflow Design**: Annotations at top of every workflow (description, I/O args, pre/post conditions); Comments activity for logic; Folder organization (by application/function); Use REFramework additional folders; Config files under "Config" folder
- **Readability**: Annotations for variables/arguments; organized project folders; clear naming so any developer can maintain
- **Logging & Exception handling**: Checkpoints, decisions, structured exception handling
- **Security**: Azure DevOps for source control; credential management via Orchestrator assets, Key Vault, PAM360
- **Backing up**: Azure DevOps (primary) and GitHub (secondary)

### Power Automate Best Practices
- **Action Names**: Original action description + context using colon separator, proper case
- **Variables**: Meaningful, distinct, readable names (multi-word allowed in Power Automate)

### General Governance
- **SAP Robot User Policy**: Service-type accounts only, least privilege, secure vault storage, annual review
- **RPA Data Policy**: Data ownership, protection, compliance, auditing standards
- **Weekly bot score checks**: Projects scored against repository/documentation/task standards (goal: score 100)

[UiPath Best Practices](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/6861160561/UiPath+Best+Practices) · [Power Automate Best Practices](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/6861029893/Power+Automate+Best+Practices) · [UiPath Security Guidelines](https://inchcapeglobal.atlassian.net/wiki/spaces/DRPA/pages/6861160855/UiPath+Security+Guidelines)



```text
                    CAPE
                     │
           RPA Development Skill
                     │
       ┌─────────────┼─────────────┐
       │             │             │
  Technology      Engineering   Governance
       │             │             │
 ┌─────┼─────┐   ┌───┼────┐   ┌────┼─────┐
 │     │     │   │   │    │   │    │      │
Auto  PA   UiPath Python API  Testing CAB Security
Drive
       │
       └──────────────┐
                      │
               Organizational
                  Knowledge
                      │
             ┌────────┼────────┐
             │        │        │
         Confluence Service  Internal
                     Desk    Standards
```


## Choosing the best OCR Engine depending on the context
| OCR Engine | Paid/Free | When to use? | Where to get API Key | Where to get the Endpoint |
|------------|-----------|--------------|----------------------|---------------------------|
| Tesseract OCR | Free | Practice / Learning | N/A | N/A |
| Microsoft OCR | Free | Practice / Learning | N/A | N/A |
| Microsoft Azure Computer Vision OCR | Paid | Scrape Full Bodies of Text | Computer Vision API: https://azure.microsoft.com/ | The endpoint associated with your Microsoft Azure Computer Vision OCR API key |
| Google Cloud Vision OCR | Paid | Scrape Portions of Text | Cloud Vision API: https://cloud.google.com/ | N/A |
| UiPath Screen OCR | Paid | Optimized for usage on screen content | Document Understanding API: https://cloud.uipath.com/ | https://ocr.uipath.com/ |
| UiPath Document OCR | Paid | Optimized for usage on scanned documents | Document Understanding API: https://cloud.uipath.com/ | https://docs.uipath.com/document-understanding/docs/public-endpoints |