---
title: "Q11/Q12 Final Bundle — Manifest"
date: 2026-10-23
tags:
  - cape
  - testing
  - manifest
status: reference
---

# Q11/Q12 Final Bundle — Manifest

- **Baseline commit:** `9f7108d2d7517a30a58be59a596eb451fb157995`
- **Generated:** 2026-10-23 15:06:40 local
- **Bundle:** `Q11_Q12_Final_2026-10-23`
- **ZIP:** `CAPE_Q11Q12_Final_Bundle.zip`
- **Pass:** Final Consistency Corrections R1–R8

## Artifact inventory

| Path | Bytes | SHA-256 |
|---|---:|---|
| `original/CAPE_Live_Evaluation_Scorecard.md` | 18773 | `c070b7ce06426e63048e63352a4e0fc81ca7a6afaf6edbe5a31a935786225fbb` |
| `original/CAPE_Testing.md` | 13481 | `9cf3cf60b89472c6f04355d59ff3f499c81ba281e84cd534c2ffdb9997d8a0b9` |
| `original/CAPE_Testing_Results_Follow_Up.md` | 85350 | `149ddce53111fc2f9e9de6b710212688683db775eb626a5694c7d2a3e3d1ad0f` |
| `original/CAPE_Testing_Results_Registered.md` | 160695 | `be91f979ed4d7d1efb8720e75b8bd3b787066f0051661b9c5ba5add9a25875a5` |
| `corrected/CAPE_Live_Evaluation_Scorecard.md` | 22952 | `6d3f473ef84cf0483347857f93771cc2013829e92b41dabc902b02e4acd4febe` |
| `corrected/CAPE_Testing.md` | 15276 | `aa2e78f78aeaace8d90d6cc2530300684eaf755f3d3271604f62e898f63be9c5` |
| `corrected/CAPE_Testing_Results_Follow_Up.md` | 93669 | `bcb7554f6f00c63afa83d43a641dbb657348977503bce7fb85759c70b4515ba6` |
| `corrected/CAPE_Testing_Results_Registered.md` | 165881 | `f03d378f10a3f1a23658f6bb07c650fabc286d73bcb7936b40e7d96b319bd1e1` |
| `diffs/CAPE_Live_Evaluation_Scorecard.md.diff` | 14430 | `21dadc08bb8aba618bb26cbd16854ec1bcaa290a47c3b326d4edd7783cea4c27` |
| `diffs/CAPE_Testing.md.diff` | 2343 | `4ab7c15402e61211b276d31f7aecc3b1bc8246369b49d4dccccec79afa87d762` |
| `diffs/CAPE_Testing_Results_Follow_Up.md.diff` | 9358 | `aa397b0cbc026b09c3cc60474d35a624169bee43b893c9752036cc64f8663487` |
| `diffs/CAPE_Testing_Results_Registered.md.diff` | 2271 | `6385922ec3450c1b85f9e825f8074a10b8db89dceee4c3f5a495aa03d2192b20` |
| `ALL_DIFFS.patch` | 28393 | `cb419c587b3733af3c4581749c40bd93318e593c47c7e14a9a5e652e884be1d8` |
| `VERIFICATION_REPORT.md` | 13159 | `05f4bee59b68216196fec4435b235ea1b62418624adfd1c83a3c89218c9327c0` |

## Diff summary

```text
Docs/Skill/Tests/CAPE_Live_Evaluation_Scorecard.md |   76 +++++++++------
Docs/Skill/Tests/CAPE_Testing.md                   |   31 +++---
Docs/Skill/Tests/CAPE_Testing_Results_Follow_Up.md |   99 +++++++++++++++++++-
Docs/Skill/Tests/CAPE_Testing_Results_Registered.md |    6 +
4 files changed, 155 insertions(+), 57 deletions(-)
```

## Notes

- Originals are the exact baseline blobs from the commit above.
- Corrected files are the current working-tree files with R1–R8 applied.
- Diffs are unified diffs from baseline `original/` to `corrected/` files.
- `ALL_DIFFS.patch` contains the concatenated unified diffs for all four files.
- `MANIFEST.md` does not hash itself.
- The ZIP hash is reported separately in `CAPE_Q11Q12_Final_Bundle.zip.sha256`.
