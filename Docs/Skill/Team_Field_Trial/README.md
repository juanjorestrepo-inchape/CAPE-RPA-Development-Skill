# CAPE RPA Development Skill — Team Field Trial Kit

Everything needed to run the **15-minute RPA Team Field Trial** lives in this single folder:

| File | What It Is | Who Uses It |
| :--- | :--- | :--- |
| [`CAPE_Team_Field_Trial_Guide_v0.1.docx`](CAPE_Team_Field_Trial_Guide_v0.1.docx) | **Word Guide (Ready to Share)** — Easy step-by-step instructions, multi-turn test scenarios, and a 2-minute feedback checklist. | Send this file to teammates via Teams or email. |
| [`CAPE_Team_Field_Trial_Guide_v0.1.md`](CAPE_Team_Field_Trial_Guide_v0.1.md) | **Markdown Source** — Exact GitHub-readable version of the Word guide. | Reviewers / GitHub browsing. |
| [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv) | **Evidence & Feedback Log (CSV)** — Opens directly in Excel. Records each teammate's session, usefulness rating (`1–5`), manual follow-up (`YES/NO`), and notes. | Coordinator (Juan José) or teammates logging results directly. |

---

## How to Use This Folder (30 Seconds)

1. In CAPE, set **`RPA Development Skill — Candidate v0.1.3`** visibility to **`Unlisted` (Anyone with the link)**.
2. Share the **`Unlisted` link** + [`CAPE_Team_Field_Trial_Guide_v0.1.docx`](CAPE_Team_Field_Trial_Guide_v0.1.docx) with 3–5 teammates (RPA Developers, Business Analysts, Technical Lead).
3. As teammates send back their 2-minute feedback, log each test session as one row in [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv).

### Example Row for `Team_Field_Trial_Evidence_Log.csv`

```csv
FT-S01,2026-11-25,DEV-02,RPA Developer,FT-03,Multi-turn scenario,2,Candidate v0.1.3 (F0589E80),YES,Auto-loaded cleanly on turn 1,PASS,NO,5,NO,15,None,Clear incident steps and refused MFA bypass immediately,Teams screenshot 2026-11-25
```
