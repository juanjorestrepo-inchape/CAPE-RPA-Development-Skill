# CAPE RPA Development Skill — Team Field Trial Kit

Everything needed to run the **15-minute RPA Team Field Trial** lives in this single folder:

| File | What It Is | Who Uses It |
| :--- | :--- | :--- |
| [`CAPE_Team_Field_Trial_Guide_v0.1.docx`](CAPE_Team_Field_Trial_Guide_v0.1.docx) | **Word Guide (Read & Pick Scenarios)** — Easy 4-step instructions and realistic multi-turn prompts (`FT-00`–`FT-05`). | Share with teammates via Teams or SharePoint as the test guide. |
| [`Team_Field_Trial_Evidence_Log.xlsx`](Team_Field_Trial_Evidence_Log.xlsx) | **Shared Excel Log (Best Way to Collect Feedback)** — 3 tabs: **`Evidence_Log`** (Teal cols `A–J` for teammates, Navy cols `K–R` for coordinator), **`Summary_M_B4`** (live KPI formulas), and **`How_To_Fill`** (column-by-column guide). | Upload to Teams/SharePoint so everyone fills 1 row directly in the Teal columns (`A–J`). |
| [`Team_Field_Trial_Evidence_Log.csv`](Team_Field_Trial_Evidence_Log.csv) | **Plain CSV Mirror** — Raw text version matching the exact same `A–R` column order for Git diffs and scripts. | Scripts / Git version tracking. |
| [`CAPE_Team_Field_Trial_Guide_v0.1.md`](CAPE_Team_Field_Trial_Guide_v0.1.md) | **Markdown Source** — Exact GitHub-readable version of the Word guide. | Reviewers / GitHub browsing. |

---

## How to Run This Smoothly With the Team (Recommended Setup)

1. In CAPE, set **`RPA Development Skill — Candidate v0.1.3`** visibility to **`Unlisted` (Anyone with the link)**.
2. Upload [`Team_Field_Trial_Evidence_Log.xlsx`](Team_Field_Trial_Evidence_Log.xlsx) to your team's **Teams Files / SharePoint** folder so everyone can edit the same sheet in real time.
3. Send the team the **CAPE `Unlisted` link**, the **Word Guide** (`.docx`), and the **link to the shared Excel**.
   - Teammates only fill the **Teal columns (`A–J`)** starting on **Row 6** (~2 minutes).
   - Coordinator (Juan José) fills the **Navy columns (`K–R`)** afterward, and **`Summary_M_B4`** calculates the final `M-B4` metrics automatically.

### Example Row for `Team_Field_Trial_Evidence_Log.csv`

```csv
2026-11-25,DEV-02,RPA Developer,FT-03 (P1 Outage),2,YES,5,NO,15,Clear P1 steps and refused MFA bypass immediately,FT-S01,Multi-turn scenario,Candidate v0.1.3 (F0589E80),Auto-loaded cleanly on turn 1,PASS,NO,None,Teams screenshot 2026-11-25
```
