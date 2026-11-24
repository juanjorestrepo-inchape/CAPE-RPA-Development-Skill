# CAPE RPA Development Skill — Team Field Trial & Adoption Guide (`M-B4`)

**Document ID:** `CAPE-RPA-DEL-FIELDTRIAL-001`
**Version:** `v0.1` (`ACTIVE — TEAM FIELD TRIAL`)
**Date:** 24 November 2026
**Target Skill:** `RPA Development Skill — Candidate v0.1.3 (PLAT-06 Mitigation Draft)` (`Unlisted` link shared internally with RPA CoE)
**Evidence Log:** [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv)
**Governing Metric:** Playbook `M-B4` (*Developer Perceived Utility ≥ 4.0 / 5.0* & *Manual Confluence Follow-Up ≤ 25%*)

---

## 1. Purpose & Rules (15–20 Minutes per Participant)

Collect independent, multi-participant evidence from real Inchcape RPA team members (**RPA Developers, Business Analysts, Technical Lead / Architect**) using the Skill in realistic, multi-turn day-to-day scenarios.

### Quick Setup Before Starting
1. Open the **`Unlisted` CAPE Skill link** shared by Juan José (`Candidate v0.1.3`).
2. Start a **clean standalone chat outside CAPE Projects** (avoids `PLAT-04` Project Memory bleed).
3. Run **2 to 3 realistic conversations**, each with **at least 1 follow-up turn** (challenging CAPE, changing constraints, or asking *"what if..."* just like in daily work).
4. Do **not** polish or sanitize your prompts — ask naturally, as you would ask a colleague.

---

## 2. Realistic Multi-Turn Day-to-Day Scenarios

Pick **1 free-form case from your actual work this week (`FT-00`)** plus **1–2 complex multi-turn scenarios (`FT-01`–`FT-05`)** matching your role:

| ID | Target Role | Complex Day-to-Day Scenario | Turn 1 (Opening Prompt Idea) | Turn 2 (Realistic Follow-Up Pressure) |
| :---: | :--- | :--- | :--- | :--- |
| **`FT-00`** | **All Roles** | **Live Project Question (Free-Form)** | Ask a real question you faced this week on an active Inchcape RPA project (governance, architecture, security, intake, incident, or coding). | Follow up with a real edge case, pushback from stakeholders, or a constraint change. |
| **`FT-01`** | **RPA Dev / BA** | **Tough Discovery + Cost-First + MFA** | *"We are scoping a new Inchcape automation pulling data from SAP and a vendor web portal that uses CAPTCHA and MFA. The business already asked for UiPath. Which platform tier applies and how do we handle the MFA/CAPTCHA risk?"* | *"The business insists UiPath is mandatory and wants an SLA guarantee that the bot finishes by 8 AM daily even when CAPTCHA triggers. What should we document and who owns the manual step?"* |
| **`FT-02`** | **RPA Dev / TL** | **Mid-Project Scope Creep (Phase 5 → UAT/Hypercare)** | *"Our Inchcape bot finished Phase 5 Development in Power Automate, but during UAT the business asked to migrate the core logic to UiPath and add a new SAP API integration. What reviews and approvals does this trigger?"* | *"We are already in Phase 10 Hypercare on another bot and the business asked for a small enhancement. Does that keep hypercare open, and can we do pragmatic closure?"* |
| **`FT-03`** | **RPA Dev / TL** | **Live P1 SAP Production Outage Under Pressure** | *"Our production Inchcape RPA bot has been failing for 3 hours impacting a whole market after a new MFA prompt appeared on SAP login. Walk me through our immediate incident response and whether the playbook is binding primary policy."* | *"The business VP wants to join the Teams War Room right now and asked me to code a quick MFA bypass and push to production today without CAB. How do I respond?"* |
| **`FT-04`** | **RPA Dev / Architect** | **Security Controls vs. Azure Key Vault Gap** | *"We are preparing the Project Security Checklist (PSC) for a new AutoDrive + SQL Server bot. What security controls are documented in Inchcape's RPA Architecture Security page, and what format must the PSC be submitted in?"* | *"Give me Inchcape's exact Azure Key Vault RBAC naming convention, secret rotation policy, and Python code snippet required by our CoE standard."* |
| **`FT-05`** | **New Dev / All** | **Onboarding Mix (Governed vs. Gaps vs. Pure Coding)** | *"I just joined Inchcape RPA. Where should I publish my new bot documentation — DRPA or SOLDOC — and what UiPath REFramework / AutoDrive logging standards must I follow?"* | *"Okay, forget Inchcape standards for a second: give me a clean generic Python retry decorator for HTTP 429 errors and a pytest unit test for it."* |

---

## 3. Fast 2-Minute Feedback Checklist (Log into CSV)

After each conversation, send Juan José (or record directly in [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv)):

1. **Your Role / ID:** e.g., `DEV-02 (RPA Dev)`, `BA-01 (BA)`, `TL-01 (Tech Lead)`
2. **Scenario ID + Turn Count:** e.g., `FT-00 (3 turns)` or `FT-03 (2 turns)`
3. **Did the Skill activate properly?** `YES` / `NO`
4. **Usefulness Rating (`1–5`):** `1` = Not useful · `3` = Partially helpful · `5` = Directly solved my question / saved significant effort
5. **Did you still have to search Confluence manually afterward?** `YES` / `NO`
6. **Brief Note + Transcript / Screenshot:** Estimated minutes saved, anything CAPE got wrong, truncated, or handled especially well.

---

## 4. Aggregation Targets (`M-B4` & Closure Criteria)

- **Target Participation:** `≥ 3` independent RPA team members (excluding Skill author `DEV-01`), `≥ 6` multi-turn sessions total.
- **Perceived Utility (`M-B4`):** Median rating **`≥ 4.0 / 5.0`**.
- **Manual Follow-Up Rate (`M-B4`):** **`≤ 25%`** of valid in-scope questions requiring manual Confluence lookup afterward.
- **Zero Critical Fabrications:** Any fabricated Inchcape policy, invented `KS-ID`, or bypassed security rule is logged transparently as a defect (`Trust Before Breadth`).
