# CAPE RPA Development Skill — 1-Page Developer Quick-Start Guide

**Document Type:** Diátaxis How-To / Quick-Start (`Pilot v0.1`)
**Audience:** Inchcape RPA Developers & Technical Delivery Team
**Governing Principle:** **Trust Before Breadth** — confidence must match validated Inchcape evidence.

---

## 1. What This Skill Does (and Does Not Do)

- **Does:** Helps you quickly locate and interpret **governed Inchcape RPA guidance** (intake phases, architecture reviews, security/CAPTCHA/MFA policies, and incident playbooks) with direct Confluence traceability.
- **Does NOT:** Replace Confluence as the source of record, bypass Architecture Review / CAB / Service Desk approvals, or invent Inchcape coding standards where none are validated.

---

## 2. How to Get Accurate Results Every Time

1. **Use a clean standalone CAPE chat (outside Projects):** Avoid running governance queries inside an unrelated CAPE Project (e.g., `Ticket Tracker`), as Project Memory can carry over stale page IDs from earlier chats (`PLAT-04`).
2. **State Inchcape RPA context clearly:** Include `"Inchcape RPA"` or the framework name (e.g., *"RPA Project Intake Framework"*, *"RPA Architecture Review Framework"*) so CAPE auto-loads the Skill reliably.
3. **Check the source & status block before acting:** Always verify the cited `KS-ID` / Confluence Page ID, `DRPA` space, and `Assessment Status`.
4. **If CAPE refuses a question, that is intentional:** A refusal with a gap code (`KG-001`–`KG-003`) means no validated Inchcape standard exists yet — do not assume CAPE is broken.

---

## 3. What Is Covered Today vs. Intentionally Declined

| Status | Domains & Governed Sources (Pilot v0.1) | Example Questions |
| :--- | :--- | :--- |
| **Covered (7 Populated Sources)** | **`KS-006`** RPA Project Intake Framework (10 phases, Internal/Global CAB) · **`KS-007`** RPA Architecture Review Framework (Phase 4 gate, PSC DOCX) · **`KS-003`** Architecture Overview · **`KS-004`** Functional Architecture · **`KS-005`** Security Architecture · **`KS-010`** CAPTCHA & MFA Policy · **`KS-015`** Critical Incident Playbook *(Supporting)* | *"How do I initiate an Inchcape RPA project?"* · *"What are the prerequisites for an RPA Architecture Review?"* · *"Can our bot bypass MFA or treat CAPTCHA delays as a bot defect?"* |
| **Intentionally Declined (Known Gaps)** | **`KG-001`** AutoDrive coding standards · **`KG-002`** UiPath REFramework / stale `UiPath Best Practices` (Feb 2024) · **Logging & Exception structure** (`Q12`) · **`KG-003`** `DRPA` vs. `SOLDOC` publishing rule | *"What are the AutoDrive coding standards?"* · *"What UiPath REFramework best practices apply?"* · *"How should I structure bot logging?"* |

---

## 4. Reading Governance Labels in CAPE Answers

- **`Primary`:** Authoritative Inchcape RPA guidance for that domain (e.g., `KS-006`, `KS-007`, `KS-010`).
- **`Supporting` (e.g., `KS-015`):** Operational playbook with an open **Role Ambiguity** flag — useful for incident response, **not** an official Primary enterprise policy.
- **`Provisional`:** Pilot validation status; always confirm critical delivery or security decisions directly on the cited Confluence page.
- **`DRPA` vs. `SOLDOC` duplicate warning:** When both spaces contain copies of a page, treat `DRPA` as the active pilot reference and verify live versions in Confluence.

---

## 5. Known CAPE Platform Quirks & How to Report Issues

- **Duplicate concatenated response (`PLAT-03`):** Occasionally CAPE prints the same answer twice after multi-tool Confluence searches; read the first complete block and ignore the duplicate.
- **Long-page truncation (`PLAT-05`):** If CAPE notes that a long page (e.g., `KS-006` Phase 10 or `KS-007` Step 9) was truncated, click the cited Confluence link to read the final section directly.
- **Found a missing standard or stale page?** Report the question and Confluence link to the **RPA CoE / Technical Delivery Manager (Nikko Gonzales)** so it is tracked for Phase 2 knowledge population.
