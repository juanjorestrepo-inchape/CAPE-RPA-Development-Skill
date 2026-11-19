# Change 05 — Q1 / Q1 V2 Evidence Register

**Version:** 0.1.1
**Status:** Draft — working references only
**Parent document:** `Change_05_Evidence_Annex_Q1_Q1V2_v0.1.1.md`

> The reference labels below (`ER-01`, etc.) are local working identifiers, not an approved Inchcape evidence-ID convention.

| Ref | Evidence item | Location / identifier | Supports | Evidence quality / limitation | Next action |
|---|---|---|---|---|---|
| ER-01 | Controlled Walkthrough record | DRPA Page `9699365417`, 26 Aug 2026 | Separate 26 Aug execution; original PASS; KS-006 source selection | No Q1 transcript or run-specific trace recovered | Preserve page link and PASS; do not apply the 2 Sep claim matrix |
| ER-02 | Live CAPE Pilot record | DRPA Page `9698968291`, 2 Sep 2026 | Live evaluation context; page-level Q1 PASS; Skill activation | Page contains inconsistent Q1 descriptions; PASS not unambiguously tied to 01:51 or 04:05 response | Retain ambiguity in annex (Request C; Findings E-10, E-15) |
| ER-03 | Q1 original run log | Local registered answer, lines 395–876: reported Load Skill → Confluence Search → Confluence Get Page `8848212048`; approximately 01:51 PM is separately user-reported | Q1 original response, reported tool sequence and Get Page output | The local record preserves the response body and reported Get Page output, but records no execution time or returned page version; no independent CAPE telemetry corroborates the events | Attach original export if available; retain the sequence and timestamp as user-reported evidence (Request B; Finding E-14, with E-17 where applicable) |
| ER-04 | Q1 V2 screenshot 1 | `image-20260914-161927.png`, attachment `att9723117681` | Prompt and first part of 04:05 PM response | Screenshot uploaded 14 Sep; footer/time context cross-checked by screenshot 2 | Link/attach screenshot |
| ER-05 | Q1 V2 screenshot 2 | `image-20260914-162025.png`, attachment `att9722658911` | End of response and “Sep 2, 04:05 PM” footer | Does not show timezone; visible captured tool panel shows Load Skill only; not a complete audit log | Link/attach screenshot |
| ER-06 | Q6 screenshot | `image-20260914-162707.png`, attachment `att9722396860` | Indirect KS-007 context | CAPE response; page ID/version not visible; not a substitute for the KS-007 V5 historical body | Do not use as source-content proof |
| ER-07 | KS-006 V1 historical page | DRPA `8848212048`, timestamp `2026-02-20T04:11:09.255Z` | Ten-phase lifecycle and CAB ordering | Reconstructed from V1→V2 history diff; not a standalone export | Attach history diff / controlled copy (Finding E-08) |
| ER-08 | KS-003 V3 | DRPA `9025257486`, 1 Apr 2026 | Platform tiers and cost-first selection | Reported unchanged since V3; KS-ID/Page ID mapping not formally encoded upstream | Preserve as assessment mapping; do not infer canonical precedence |
| ER-09 | KS-007 V5 chronology and content reference | DRPA `8853815357`, 25 Jun 2026 14:50:24.930 UTC | Establishes the version identified as current during Q1 by page history | Exact complete V5 body is not independently preserved and verified in this package. Manual comparison material is not treated as a verified full export. | Obtain and preserve the exact historical V5 content (Request A; Finding E-06) |
| ER-10 | KS-007 V6 conflict | Implementation Record `9759916259`, §0.1 r4 and §7 | Identifies V6 as page used for “the pilot” | V6 date 16 Sep is after Q1 dates; scope of “the pilot” unclear | Preserve as conflict; resolve separately |
| ER-11 | Local Q1 registered answer | `Docs/Skill/Tests/CAPE_Testing_Results_Registered.md`, Q1 section, lines 395–876 (verified locally in this review) | Prompt, response and reported Load Skill / Search / Get Page details, including the returned page body | The record states that execution time was not seen or recorded and does not identify a returned page version; events are not independently corroborated by CAPE telemetry | Preserve as a user-reported historical record; do not treat it as independently verified runtime telemetry |
| ER-12 | Live evaluation evidence file | `Docs/Skill/Tests/CAPE_RPA_Development_Skill_v0.1_Live_Evaluation_Evidence.md`, links at lines 651 and 1968 (verified locally in this review) | Two links to a `Q1 Version 2` anchor | The links are present, but the referenced heading/anchor is absent from the local file; no target section was located | Preserve as a local traceability issue; do not infer missing Q1 V2 content from the broken anchor |
| ER-13 | Live pilot results DOCX | `Docs/Word/Tests/RPA_Development_Skill_Live_Pilot_Evaluation_Results.docx` | 2 Sep date, Skill v0.1, live CAPE environment, Q1 PASS summary | Summary does not preserve complete Q1-specific raw trace or PASS-to-run attribution | Retain as summary evidence |
| ER-14 | Pilot Specification v0.1 | Uploaded project file `RPA_Development_Skill_Pilot_Specification_v0.1.docx` | Context-based pilot boundary; source correctness and grounding criteria; Q1 expected KS-006 Primary | Governing pilot artifact; not a runtime log | Cross-reference relevant sections, including §0.2, §3, §5, §6, §7 and §9 where applicable |
| ER-15 | Functional Specification v0.1 Tranche 1 | Uploaded project file `RPA_Development_Skill_Functional_Specification_v0.1_Tranche1(1).docx` | Source selection, priority and conflict behavior; boundary between Tranche 1 and future grounding/citation work | Tranche 1 defers detailed grounding and citation requirements to Tranche 2 | Do not attribute detailed claim-grounding requirements to Tranche 1 |
| ER-16 | Trust Matrix v0.1 | Uploaded project file `RPA_Knowledge_Source_Trust_Matrix_v0.1(2).docx` | KS-006 and KS-007 Primary / Provisional source classifications | Does not establish canonical Page ID mapping | Cite source-role status only |
| ER-17 | Knowledge Taxonomy v0.1.1 | Uploaded project file `RPA_Knowledge_Taxonomy_v0.1.1(1).docx` | Governance & Delivery Lifecycle domain; KS-006 and KS-007 mapping | Taxonomy organizes source knowledge; does not upgrade trust or settle canonical identity | Preserve KG-003 as unresolved |
| ER-18 | Knowledge Inventory v0.2.0 | Uploaded project file `RPA Knowledge Inventory_v0.2.0(5).docx` | KS-006 / KS-007 inventory entries and DRPA/SOLDOC context | Inventory discovery classifications are preliminary; Trust Matrix is the formal source-governance mechanism | Do not infer canonical precedence |

## Evidence handling rules

1. Keep the three execution records separate.
2. Preserve original recorded outcomes independently from retrospective content assessments.
3. Never infer source absence from missing logs.
4. Do not treat a Skill-load event as proof of external retrieval.
5. Do not treat a source citation in an answer as proof that a specific page version was retrieved at runtime.
6. Exclude later source versions from historical assessment unless a later execution date is established.
7. Keep DRPA/SOLDOC canonical precedence unresolved under KG-003.
8. Distinguish user-reported execution evidence from independently corroborated telemetry.
9. Do not describe reconstructed or manually captured historical content as a direct export.
10. Do not upload this register or the annex to Confluence until owner review and document-control approval.
11. Preserve Finding E-23 as OPEN — REQUIREMENT / SOURCE VERIFICATION REQUIRED; do not close or claim existing coverage without verified primary evidence from Confluence Page 7 §5.4 or formal Project Owner ratification.