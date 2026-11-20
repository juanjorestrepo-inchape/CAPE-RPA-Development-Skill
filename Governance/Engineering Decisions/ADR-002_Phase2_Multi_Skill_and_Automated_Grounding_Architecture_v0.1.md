# ADR-002: Phase 2 Target Architecture — Bounded-Context Multi-Skill Decomposition & Automated Grounding Evaluation

**Document ID:** `CAPE-RPA-ARCH-ADR-002`
**Status:** `PROPOSED — PHASE 2 TARGET ARCHITECTURE (QUARANTINED OUT OF Q4 2026 PILOT SCOPE)`
**Date:** 20 November 2026
**Author:** Juan José Restrepo Rosero
**Related Artifacts:** [`CAPE_RPA_Skill_Execution_Metrics_and_Optimization_Playbook_v0.1.md`](../Delivery/CAPE_RPA_Skill_Execution_Metrics_and_Optimization_Playbook_v0.1.md) · [`CAPE_Platform_Defect_and_Telemetry_RFC_v0.1.md`](../Delivery/CAPE_Platform_Defect_and_Telemetry_RFC_v0.1.md) · [`06_CAPE_First_Party_Technical_Reference_v0_1.md`](../../03_Knowledge_Research/06_CAPE_First_Party_Technical_Reference_v0_1.md)

> **Governance Quarantine Notice:** Per `Pilot Specification v0.1` and [`Owner_Review_Package_Candidate_v0.1.2.md`](../Owner%20Review/v0.1.2/Owner_Review_Package_Candidate_v0.1.2.md) §3.4, this ADR is strictly a **post-pilot Phase 2 architectural recommendation**. It does **not** authorize building vector databases, splitting the active Pilot Skill, or expanding knowledge scope during Q4 2026.

---

## 1. Context & Architectural Problem Statement

The Q4 2026 pilot proved that a **context-based Skill** governed by **Trust Before Breadth** achieves high boundary honesty (`4/4 PASS` on `Q10, Q11, Q12, Q19`, `0` fabrications). However, local telemetry exposes a hard structural scaling ceiling:

1. **Character-Budget Saturation:** Covering just **7 of 20** planned pilot sources already consumes `22,139` LF chars in Active v0.1 and `23,435` LF chars in Candidate v0.1.2 — leaving only **`565` characters** below CAPE's 24,000-character limit.
2. **Routing Precision Trade-Off:** Live testing (`Q16-A` missed activation vs. `N5` tool-level false load on generic Python desktop automation) shows that a single broad Skill description simultaneously risks under-triggering on specialized governance terms and over-triggering on generic automation words.
3. **Manual Evaluation Bottleneck:** Claim-level grounding audits (Change 05 `C05-01`–`C05-04`) and 20-question regressions currently require manual transcript inspection because CAPE lacks an automated evaluation harness and native JSON trace exports (`CAPE-RPA-PLT-RFC-001` §3).

---

## 2. Evaluated Architectural Alternatives

| Option | Description | Pros | Cons / Risks | Verdict |
| :--- | :--- | :--- | :--- | :---: |
| **Option 1: Monolithic Skill Compression** | Keep one single RPA Skill and aggressively compress prose to fit 20 sources under 24,000 chars. | Zero routing changes; single file to maintain. | Breaks above ~10 sources; forces removal of explicit boundary rules, directly threatening Coverage-Honesty (`Q10`–`Q12`, `Q19`). | **Rejected** |
| **Option 2: Custom External Vector DB / RAG Pipeline** | Build an independent embedding + vector search service outside CAPE's native Confluence connector. | Unlimited document capacity; semantic chunk retrieval. | High infrastructure & security maintenance; duplicates CAPE connectors; high risk of surfacing stale/unvalidated pages unless Trust Matrix metadata filtering is rebuilt from scratch. | **Deferred (Phase 3+)** |
| **Option 3: Bounded-Context Multi-Skill + Native Metadata + Offline Claim-Eval CI** | Decompose into **3 cohesive domain Skills** aligned to DDD Bounded Contexts (each `< 16,000` chars), pair with native CAPE Confluence metadata, and add an offline claim-grounding evaluator. | Preserves CAPE's zero-infra on-demand Skill loading; >30% character headroom per Skill; sharper activation routing; reuses governed Trust Matrix directly. | Requires clear routing boundaries between the 3 Skills and upstream authoring of missing sources (`KG-001`–`KG-003`) before activating Skill 3. | **Recommended** |

---

## 3. Recommended Phase 2 Architecture (Option 3)

```text
User Query in CAPE
       │
       ▼
CAPE On-Demand Skill Router (Tightened Discovery Descriptions)
  ├──► Skill 1: RPA Governance & Delivery   (KS-006, KS-007, Intake, CAB, Repo Standard)   [<16k chars]
  ├──► Skill 2: RPA Architecture & Security (KS-003, KS-004, KS-005, KS-010, Vaults/Auth)  [<16k chars]
  └──► Skill 3: RPA Standards & Operations  (KS-015 + newly validated KG-001/002/Q12)      [<16k chars]
       │
       ▼
CAPE Native Confluence Connector (w/ RFC native metadata: page_id, space_key, version)
       │
       ▼
Offline CI Grounding Evaluator (Change 05 Claim Matrix: A/B/C/D + Temporal + Provenance)
```

### 3.1 Bounded-Context Skill Decomposition
- **Shared Governance Core (Template-Driven):** All three Skills inherit identical non-negotiable `Trust Before Breadth` guardrails (Deterministic Gap Rule, Primary-over-Supporting precedence, Provisional disclosure, and Tool-Call Deduplication) generated from a single shared source of truth in Git so rules never drift.
- **Sharper Activation Descriptions:** Splitting discovery metadata reduces cross-domain false loads like `N5` (generic Python automation) while allowing `Skill 1` to list exact governance triggers (`"Architecture Review Framework"`, `"Project Intake Framework"`, `"CAB"`, `"PSC"`) to eliminate misses like `Q16-A`.

### 3.2 Automated Claim-Level Evaluation (Change 05 Evolution)
Once CAPE exposes read-only JSON conversation exports (`CAPE-RPA-PLT-RFC-001` §3), extend `scripts/cape_quality_gate.py` with an offline evaluation runner inspired by **RAGAS faithfulness** and Change 05's 4-tier verdict taxonomy:
- **Faithfulness / Claim Decomposition (`C05-02`):** Flag any substantive assertion not supported by the retrieved Confluence snapshot (`A/B` vs. `C` Unsupported / `D` Contradicted).
- **Temporal & Prerequisite Ordering (`C05-01`):** Deterministic sequence checks (e.g., Phase 5 Development always precedes Phase 7 Internal CAB and Phase 8 Global CAB).
- **Provenance Assertion (`C05-04`):** Automated check that `source_version_at_execution` matches the live DRPA Confluence version and flags any `SOLDOC` duplicate automatically.

---

## 4. Entry Preconditions & Consequences

### Preconditions Before Implementing Phase 2
1. Formal closure of the Q4 2026 Pilot (`Coverage-Honesty Gate: CLEARED` and Change 07 report delivered).
2. Resolution of upstream governance dependencies (`DEP-01`–`DEP-10`, `DEC-SRC-01` DRPA canonical precedence, and Change 05 Gate `G6` / `E-23`).
3. Authoring and validation of missing enterprise standards (`KG-001` AutoDrive, `KG-002` UiPath REFramework, `Q12` Logging/Exception Standards) before populating `Skill 3`.
4. CAPE Platform confirmation on character-counting rules and native connector metadata (`CAPE-RPA-PLT-RFC-001`).

### Architectural Trade-Offs Accepted
- **Multi-Skill coordination:** Cross-cutting queries (e.g., `Q15`/`Q16` spanning Architecture Overview and Architecture Review) must either allow CAPE to co-load two Skills or define a clear boundary handoff rule tested explicitly in Phase 2 regression.
- **No premature RAG complexity:** Avoids standing up external vector infrastructure until governed Confluence content exceeds what 3 bounded Skills + native Confluence search can reliably cover.
