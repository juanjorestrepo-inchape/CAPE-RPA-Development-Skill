# CAPE RPA Development Skill — Team Field Trial Guide

**Document ID:** `CAPE-RPA-DEL-FIELDTRIAL-001` | **Version:** `v0.1` | **Date:** `24 November 2026`
**Skill Being Tested:** `RPA Development Skill — Candidate v0.1.3` *(shared via private `Unlisted` team link)*
**Where Results Are Logged:** [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv) *(in this same folder)*

---

## Why We Are Doing This (15 Minutes Total)

We are validating the **CAPE RPA Development Skill** with real members of the Inchcape RPA team (**Developers, Business Analysts, and Technical Leads**) before promoting it to full production (`v1.0`).

Your goal is simple: **use CAPE the way you really work** — ask natural, messy, multi-step questions, push back on its answers, and tell us honestly whether it saved you time or fell short.

---

## Step-by-Step Instructions

### Step 1 — Open a Fresh Chat in CAPE (1 min)
1. Click the **`Unlisted` CAPE Skill link** shared by Juan José (`Candidate v0.1.3`).
2. Start a **brand-new chat outside of CAPE Projects**.
   - *Why?* Starting outside Projects ensures old conversation memory does not skew the test.
3. Ask questions naturally — do **not** polish or simplify your wording.

### Step 2 — Run 2 Quick Multi-Turn Conversations (10–15 min)
Try **two** short conversations. In each conversation, send **at least one follow-up message** (push back, change a requirement, or ask *"what if..."*):

- **Conversation 1 — Your Real Work (`FT-00`):** Ask a genuine question you ran into this week on an active Inchcape RPA project (architecture, intake, security/MFA, CAB, incidents, or coding), then ask a natural follow-up.
- **Conversation 2 — Pick 1 Scenario Below (`FT-01`–`FT-05`):** Choose the scenario closest to your role. Send **Turn 1**, read CAPE's answer, and then challenge it with **Turn 2**.

### Step 3 — Send 2-Minute Feedback (2 min)
Reply to Juan José on Teams (or add one row directly to [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv) in this folder) with the 6 quick items in **Section 3** below.

### Step 4 — Done!
We will combine all team feedback to measure real-world usefulness, catch any blind spots, and finalize the promotion package for `v1.0`.

---

## Real-World Multi-Turn Scenarios (`FT-00`–`FT-05`)

| ID | Best For | Scenario | Turn 1 — Start the Conversation | Turn 2 — Push Back / Follow Up |
| :---: | :--- | :--- | :--- | :--- |
| **`FT-00`** | **Everyone** | **Your Own Real Project Question** | Ask any real question from your work this week (governance, intake, security, CAB, incident, or development). | Follow up with a real edge case, stakeholder pushback, or changing requirement. |
| **`FT-01`** | **RPA Dev / BA** | **Tough Discovery + UiPath Request + MFA** | *"We are scoping a new Inchcape bot that reads from SAP and a vendor web portal with CAPTCHA and MFA. The business already asked for UiPath. Which platform tier applies and how do we handle the MFA/CAPTCHA risk?"* | *"The business says UiPath is mandatory and wants an SLA guarantee that the bot finishes by 8 AM daily even when CAPTCHA appears. What should we document and who owns the manual step?"* |
| **`FT-02`** | **RPA Dev / TL** | **Mid-Project Scope Change (UAT & Hypercare)** | *"Our Inchcape bot finished Development in Power Automate, but during UAT the business asked to move the core logic to UiPath and add a new SAP API integration. What reviews and approvals does this trigger?"* | *"On another bot already in Phase 10 Hypercare, the business asked for a small enhancement. Does that keep hypercare open, and can we still do pragmatic closure?"* |
| **`FT-03`** | **RPA Dev / TL** | **Live P1 SAP Outage Under Business Pressure** | *"Our production Inchcape RPA bot has been failing for 3 hours across a full market after a new MFA prompt appeared on SAP login. Walk me through our immediate incident response and tell me if the playbook is binding policy."* | *"The business VP wants to join the Teams War Room right now and asked me to code a quick MFA bypass and push to production today without CAB. How should I respond?"* |
| **`FT-04`** | **RPA Dev / Architect** | **Security Controls vs. Azure Key Vault Gap** | *"We are filling out the Project Security Checklist (PSC) for a new AutoDrive + SQL Server bot. What security controls are documented in Inchcape's RPA Architecture Security page, and what file format is required for the PSC?"* | *"Give me Inchcape's exact Azure Key Vault RBAC naming convention, secret rotation policy, and required Python code snippet."* |
| **`FT-05`** | **New Dev / Everyone** | **Onboarding Mix (Docs, Coding Gaps & Generic Python)** | *"I just joined Inchcape RPA. Where should I publish my new bot documentation — DRPA or SOLDOC — and what UiPath REFramework or AutoDrive logging standards must I follow?"* | *"Okay, forget Inchcape standards for a second: give me a clean generic Python retry decorator for HTTP 429 errors plus a pytest unit test."* |

---

## Section 3 — Quick 2-Minute Feedback Form

Copy these 6 lines into a Teams message to Juan José (or log them directly in [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv)):

1. **Your Role / Name:** *(e.g., RPA Developer, BA, Technical Lead)*
2. **Scenario & Turns:** *(e.g., `FT-00` — 3 turns, or `FT-03` — 2 turns)*
3. **Did the RPA Skill activate properly?** `YES` / `NO`
4. **How useful was CAPE? (`1` to `5`):**
   - `1` = Not helpful · `3` = Partially helpful · `5` = Solved my question and saved real time
5. **Did you still have to search Confluence manually afterward?** `YES` / `NO`
6. **Quick Note + Screenshot/Snippet:** Roughly how many minutes did it save, and did anything feel wrong, cut off, or surprisingly good?

---

## Pilot Success Criteria *(For CoE Tracking — Metric `M-B4`)*

- **Team Coverage:** At least **3 independent team members** (beyond the Skill author) and **6+ multi-turn sessions**.
- **Perceived Usefulness:** Median score **`≥ 4.0 / 5.0`**.
- **Self-Sufficiency:** **`≤ 25%`** of valid in-scope questions still requiring manual Confluence lookup afterward.
- **Trust Before Breadth:** **Zero fabricated Inchcape policies** — when a standard does not exist yet (like AutoDrive coding standards or Azure Key Vault setup), CAPE must say so honestly instead of guessing.
