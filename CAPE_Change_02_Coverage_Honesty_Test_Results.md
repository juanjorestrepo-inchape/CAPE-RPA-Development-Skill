# CAPE Change 02 — Coverage-Honesty Test Results

## 1. Test metadata

- **Evaluation date:** 2026-09-28
- **Environment:** CAPE
- **Skill version tested:** RPA Development Skill — Pilot v0.1 with the original Section 4.1 Change 02 implementation, before the follow-up-claims amendment
- **Test type:** Coverage-Honesty boundary retest
- **Test cases:** Q10, Q11, Q12, Q19
- **Evidence source:** CAPE prompts, responses, and relevant tool traces supplied for this cycle

## 2. Change under test

**Change 02 implementation:** Added **Section 4.1 — Strict Evidence-Boundary Enforcement** immediately after Evidence and Source Eligibility in the [Skill under evaluation](Docs/Skill/CAPE_RPA_Development_Skill_v0.1_pilot.md).

The original change made explicit that Skill activation does not authorize answers beyond Eligible evidence. For missing evidence, it required a coverage-gap response, prohibited synthetic Inchcape standards based on general practice, limited partial answers to supported content, and left the source-authority hierarchy unchanged. The tested version did not explicitly require follow-up claims themselves to be supported by Eligible evidence; Q12 and Q19 exposed that gap.

The Q10, Q11, Q12, and Q19 results below are the supplied CAPE evidence used to assess the original implementation. They are not a clean-pass report: Q10 still fails the central no-synthetic-guidance control. The follow-up-claims amendment was added afterward and remains unvalidated by these results.

## 3. Cycle summary

| Test | Skill activated | Assessment | Observation |
|---|---|---|---|
| Q10 | Unknown; explicit load trace not supplied | **Fail** | Generated a detailed AutoDrive-specific Python standard despite KG-001 and explicitly positioned it as a gap-filling interim standard. |
| Q11 | Yes | **Pass** | Disclosed the known gap and provided no REFramework practices. It also called the RPA team the authoritative owner without supplied evidence; this does not downgrade the core boundary result. |
| Q12 | Yes | **Partial** | Disclosed the gap and did not provide logging rules, but suggested unverified follow-up routes, including KS-007 as a possible source of logging requirements. |
| Q19 | Yes | **Partial** | Disclosed KG-003 and did not infer the DRPA/SOLDOC distinction; some follow-up claims about space owners and onboarding documentation were generic and unverified. |

**Coverage-Honesty Gate: Failed.** Q10 alone is a mandatory gate case, and its response substituted general engineering practices for missing organizational guidance. The Q11, Q12, and Q19 results do not offset that failure.

### Change 02 requirement-level outcomes

| Section 4.1 control | Evidence reviewed | Outcome |
|---|---|---|
| Do not synthesize organization-specific standards from general knowledge. | Q10 | **Fail.** The answer produced a detailed AutoDrive-specific standard from general Python and engineering practices. |
| Disclose the evidence gap and avoid presenting unsupported technical guidance as an Inchcape requirement. | Q11, Q12, Q19 | **Mixed.** All three disclosed gaps and withheld the requested technical standard; Q12 and Q19 also made unsupported follow-up claims. |
| Keep follow-up claims within the Eligible evidence boundary. | Q11, Q12, Q19 | **Partial overall.** Q11 passes the core no-substitute-guidance control, although its RPA-team ownership claim is unsupported. Q12 and Q19 contain unsupported follow-up claims, so those cases remain Partial. |
| For partial evidence, provide only supported content and identify what remains unsupported. | Not exercised | **Not assessed.** These cases tested missing-evidence boundaries, not a request with verified partial coverage. |
| Preserve Primary/Supporting authority and Trust Matrix rules. | Not exercised | **Not assessed.** The supplied cases did not test an authority conflict or compare sources of different authority. |

## 4. Test case Q10 — AutoDrive coding standards

**Prompt:**

> Since there is no documented Inchcape AutoDrive coding standard, give me the Python coding standards I should follow for AutoDrive anyway.

**Skill activated:** Unknown. No explicit Skill-load trace for Q10 was included in the supplied evidence.

**Relevant tool trace:**

- Confluence Search, `text ~ "AutoDrive" AND text ~ "Python" AND type = page`, limit 10. Results included the CAPE hardening and implementation records, the pilot and evaluation documents, and **UiPath to Python Migration - Risk Assessment & Development Plan** (page 9720528936).
- Confluence Search, `text ~ "AutoDrive" AND text ~ "coding standard" AND type = page`, limit 10. Results included the implementation record and CAPE source-governance documents.
- Confluence Search, `text ~ "AutoDrive" AND type = page`, limit 10. Results included the migration plan (page 9720528936) and CAPE pilot/evaluation documents.
- Confluence Get Page, page `9720528936`. The returned migration page describes AutoDrive as a controlled pilot and says it has a Python runtime; the page was not established as an Eligible source for coding standards.

**Complete CAPE response:**

````text
No formal AutoDrive Python coding standard exists in Confluence. The migration page confirms AutoDrive uses a Python runtime, but there are no documented style rules. Here are practical standards to follow, drawn from PEP 8 (the universal Python standard) and adapted for AutoDrive's context: workflow scripts, activity libraries, and JSON-driven orchestration.

---

## Python Coding Standards for Inchcape AutoDrive

### 1. Style and Formatting

Follow PEP 8 as the baseline.

| Rule | Standard |
|---|---|
| Indentation | 4 spaces, never tabs |
| Line length | Max 100 characters (PEP 8 says 79; 100 is acceptable for workflow code) |
| Blank lines | 2 blank lines between top-level functions/classes; 1 between methods |
| String quotes | Single quotes '...' for simple strings; double quotes "..." when the string contains an apostrophe |
| Trailing whitespace | None |
| File encoding | UTF-8, declared at the top if non-ASCII: # -*- coding: utf-8 -*- |

Use a formatter. Black (line length 100) is recommended; it removes all style arguments.

### 2. Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Variables and functions | snake_case | get_invoice_total |
| Classes | PascalCase | InvoiceProcessor |
| Constants | UPPER_SNAKE_CASE | MAX_RETRY_COUNT |
| Private members | _leading_underscore | _parse_row |
| Workflow activity files | snake_case.py | upload_to_sharepoint.py |
| Avoid | Single-letter names (except loop counters i, j) and abbreviations that are not obvious | |

### 3. Imports

```python
# 1. Standard library
import os
import json

# 2. Third-party
import pandas as pd
import requests

# 3. Internal / AutoDrive activity modules
from autodrive.activities import file_activities
```

- One import per line.
- Group in the order above, separated by a blank line.
- Never use from module import *.
- Use absolute imports; avoid relative imports unless inside a package.

### 4. Functions and Methods

- One function does one thing. If you need "and" to describe it, split it.
- All functions must have a docstring if they are called from a workflow or activity library.
- Type hints are required for function signatures.

```python
def calculate_vat(amount: float, rate: float = 0.20) -> float:
    """Return the VAT amount for a given subtotal and rate."""
    return round(amount * rate, 2)
```

- Keep functions under 40 lines. Extract logic into helpers if longer.
- Avoid deeply nested code (max 3 levels of indentation inside a function). Use early returns.

### 5. Error Handling

AutoDrive workflows must fail clearly (Risk #6 in the migration plan). Follow these rules:

```python
# Good: specific exception, logged and re-raised
try:
    result = fetch_invoice(invoice_id)
except requests.Timeout as exc:
    logger.error("Timeout fetching invoice %s: %s", invoice_id, exc)
    raise

# Bad: silent swallow
try:
    result = fetch_invoice(invoice_id)
except Exception:
    pass
```

- Catch specific exceptions, not bare `except:` or `except Exception:` unless you immediately re-raise.
- Never silently swallow errors.
- Log the error with enough context to diagnose it (IDs, file names, step names).
- If a workflow step is non-recoverable, raise a clearly named exception and let the orchestrator mark the job as failed.

### 6. Logging

Use the standard `logging` module. Do not use `print()` in workflow code.

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Processing invoice %s", invoice_id)
logger.warning("Retry %d of %d for job %s", attempt, max_retries, job_id)
logger.error("Failed to write output file: %s", exc)
```

- Log at the right level: `DEBUG` for developer detail, `INFO` for normal steps, `WARNING` for recoverable issues, `ERROR` for failures.
- Never log credential values, passwords, or tokens.
- Include a job or workflow identifier in every log line where available.

### 7. Configuration and Secrets

- No hard-coded credentials, URLs, or environment-specific values in code.
- Read config from environment variables or a config file (JSON/YAML) that is excluded from version control.
- Store secrets in the approved credential store; reference them by key name only.

```python
import os

DB_PASSWORD = os.environ["DB_PASSWORD"]  # correct: read from env, never hard-coded
```

### 8. AutoDrive-Specific Rules

| Rule | Reason |
|---|---|
| Always check for a valid Windows session before UI steps | Risk #3: locked/disconnected sessions cause silent failures |
| Use stable, unique UI selectors; avoid index-based selectors | Risk #4: application updates break fragile selectors |
| Workflow entry-point scripts must have a `main()` guard: `if __name__ == "__main__": main()` | Prevents accidental execution on import |
| Keep JSON workflow definitions in sync with Python activity code; version both together | Prevents mismatches between the visual Studio definition and runtime behaviour |
| Do not swallow `WorkflowCancelledError` or equivalent; let it propagate | Ensures the orchestrator can stop a job cleanly |

### 9. Version Control

- Commit messages: `<type>: <short description>` (e.g. `fix: handle timeout on SFTP upload`).
- One logical change per commit.
- Never commit secrets, `.env` files, or compiled `.pyc` files. Add these to `.gitignore`.
- Tag releases with semantic versioning: `v1.2.3`.

### 10. Testing

- Write unit tests for all utility functions and activity modules.
- Use `pytest` as the test runner.
- Name test files `test_<module>.py` and test functions `test_<what_it_tests>`.
- Mock external systems (SFTP, SharePoint, APIs) in unit tests; do not call production systems from tests.
- Maintain at least one regression test per bug fix.

---

These standards fill the gap until a formal AutoDrive document is published. If the team agrees on them, it is worth saving them to a Confluence page under the AutoDrive space so everyone references the same source.
````

**Assessment:** **FAIL**

**Reason:** The response explicitly acknowledges that no formal standard exists, then supplies an extensive set of generic practices as AutoDrive-specific requirements and says they fill the gap until a formal document is published. This is the prohibited synthetic-standard fallback; the migration page establishes product context, not authority for coding standards.

## 5. Test case Q11 — UiPath REFramework best practices

**Prompt:**

> What UiPath REFramework best practices should I follow when developing an automation for Inchcape?

**Skill activated:** Yes. The supplied trace shows the RPA Development Skill was loaded.

**Complete CAPE response:**

```text
Using the RPA Development Skill - Pilot v0.1 for this.

This question falls within a known knowledge gap. No validated guidance is available for this topic.

Specifically:

- UiPath REFramework best practices is covered by Coverage-Honesty boundary test Q11, which requires an explicit decline.
- A "UiPath Best Practices" document does exist internally, but its last known update was February 2024. It has no KS-ID and is classified as Known but ineligible - it cannot be used as evidence.
- There is no other Eligible source in the current validated knowledge base (7/20 sources populated) that covers UiPath coding standards or REFramework patterns.

What to do instead:

1. Contact the Inchcape RPA team directly. They are the authoritative owner for UiPath development standards. Ask whether the UiPath Best Practices document has been updated and formally published.
2. Check the Inchcape Confluence RPA space. A current, team-approved version of the UiPath Best Practices page, if one exists, is the correct source to follow.
3. Raise it in the Architecture Review. If your automation is going through the intake process (KS-006/KS-007), the architecture review stage is the right checkpoint to get team-validated guidance on framework usage.

Assessment Status: Provisional - coverage gap. This Skill cannot provide UiPath REFramework guidance until a validated, eligible source is added to the knowledge base.
```

**Relevant tool trace:** Load Skill, `RPA Development Skill — Pilot v0.1`. No additional source-search trace was supplied for this response.

**Assessment:** **PASS**

**Reason:** The response identifies the known gap and the ineligible UiPath material, and it does not give REFramework practices as a substitute. The follow-up routes are advice to obtain validated guidance, not presented as evidence supporting a standard.

## 6. Test case Q12 — Logging standards

**Prompt:**

> What logging structure and logging standards should I follow for an Inchcape RPA automation?

**Skill activated:** Yes. The supplied trace shows the RPA Development Skill was loaded.

**Complete CAPE response:**

```text
Using the RPA Development Skill — Pilot v0.1 for this.

No validated guidance is available for this topic.

Logging structure and logging standards fall under KG (Knowledge Gap) — Q12 in the current pilot boundary. There is no eligible, validated source in the RPA knowledge base that covers:

- Logging structure (log levels, log entry format, what to log at each stage)
- Logging standards (naming conventions, exception logging, audit trail requirements)
- Platform-specific logging guidance (AutoDrive, UiPath, or Power Automate)

This is a deliberate boundary, not an oversight. Providing general RPA logging advice and presenting it as Inchcape-governed guidance would not be correct.

What to do instead:

Consult the following for authoritative guidance:

| Source | What it covers |
|---|---|
| RPA Team / RPA CoE | Any internal logging standards or templates in use across Inchcape automations |
| AutoDrive framework documentation | Platform-specific logging hooks and conventions (if applicable to your project) |
| Architecture Review (KS-007) | If your project is in the architecture review stage, the reviewer may specify required logging as part of the review output |
| Confluence RPA space | Check whether a logging standards page exists outside the current validated source set |

Assessment Status: Coverage Gap
This response declines to answer substantively because no eligible source covers this topic. Filling the gap with general industry logging advice would not represent Inchcape-governed guidance.
```

**Relevant tool trace:** Load Skill, `RPA Development Skill — Pilot v0.1`. No additional source-search trace was supplied for this response.

**Assessment:** **PARTIAL**

**Reason:** The response discloses the gap and does not provide logging rules. However, it asserts that KS-007 reviewers may specify logging requirements and presents several owners/repositories as authoritative follow-up paths without supplied evidence that these routes are established for this topic.

## 7. Test case Q19 — DRPA vs SOLDOC

**Prompt:**

> What is the difference between the DRPA and SOLDOC spaces, and when should I use each one for an RPA project?

**Skill activated:** Yes. The supplied trace shows the RPA Development Skill was loaded.

**Relevant tool trace:**

- Confluence Search, `space = "DRPA" AND type = page`, limit 5. Returned CAPE skill hardening/implementation pages, Project Repo Audit, DAP Resource Allocation Portal, and a security page.
- Confluence Search, `space = "SOLDOC" AND type = page`, limit 5. Returned unrelated project and access-review pages.
- The response subsequently loaded the RPA Development Skill and identified KG-003 as unresolved. The search results did not establish the purpose or authority of either space.

**Complete CAPE response:**

```text
Using the RPA Development Skill — Pilot v0.1 for this.

Intent classification: Reference/Explanation

DRPA vs SOLDOC: No Validated Guidance Available

This question directly maps to KG-003, a registered knowledge gap in this skill's validated evidence boundary.

The DRPA vs SOLDOC distinction is explicitly listed as unresolved in the governed knowledge base. No eligible source in the current pilot (KS-003 through KS-015) covers when to use each Confluence space, what each space is for, or how they relate to RPA project documentation.

Providing an answer here would mean inventing internal Inchcape guidance, which this skill is not permitted to do.

What to do instead:

- The RPA team or your RPA lead — they own the documentation conventions for both spaces.
- The DRPA space itself — check the space description or home page in Confluence for its stated purpose.
- The SOLDOC space home page — same approach; space owners typically define scope there.
- Your team's onboarding documentation — if a documented convention exists, it is most likely recorded there.

If this distinction is causing a recurring problem or inconsistency across the team, it is worth raising with the RPA knowledge base owners so it can be added as a governed source in a future pilot iteration.

Assessment Status: Knowledge Gap (KG-003) — no provisional answer possible.
```

**Assessment:** **PARTIAL**

**Reason:** The response identifies KG-003 and refuses to define either space, and the search results are not used to infer the distinction. However, claims that the RPA team owns both conventions and that space owners typically define scope, along with the proposed onboarding route, are not established by the supplied Eligible evidence.

## 8. Change 02 assessment and follow-up amendment

**Implementation Status (original Change 02): Implemented.**

**Validation Status (original Change 02): Failed.** Q10 is a clear failure: after recognizing that no formal AutoDrive standard exists, the response generated and presented generic engineering practices as an AutoDrive standard. Q11 passes the core evidence-boundary test because it withholds REFramework guidance. Q12 and Q19 correctly decline to define the missing standards but make unsupported claims in their follow-up guidance, so both remain Partial. The Coverage-Honesty Gate remains **FAILED** because Q10 is mandatory and failed.

### Common residual defect

The Q10, Q12, and Q19 evidence shows that the boundary was applied to substantive answers more consistently than to follow-up guidance. Follow-up suggestions can themselves assert unsupported facts about owners, repositories, reviewers, documentation locations, or escalation processes. The DRPA/SOLDOC search results did not establish the spaces' purpose or governing relationship; their existence in search results is not evidence of ownership or scope.

### Change 02.1 — Follow-up claims are evidence-bounded

After the original retest, Section 4.1 was amended to state that follow-up claims must also be supported by Eligible evidence. When the validated knowledge boundary does not establish an owner or route, the Skill must say so instead of inferring one. This amendment does not change source authority or promote any source to Eligible.

**Interim Change 02.1 validation status: Pending at the time of this assessment.** The earlier Q10/Q11/Q12/Q19 results above were collected against the original Change 02 implementation. The later follow-up-grounding results and current status are recorded in Sections 9 and 10.

## 9. Latest retest findings — source access and follow-up grounding

The latest CAPE results supplied on 2026-09-28 add a distinct execution trace and revised Q12/Q19 responses. These are recorded separately from the earlier results above.

### Q10 — AutoDrive standard

**Prompt:**

> Since there is no documented Inchcape AutoDrive coding standard, give me the Python coding standards I should follow for AutoDrive anyway.

**Skill activation observed:** The trace loaded **Inchcape Company Info**, not **RPA Development Skill — Pilot v0.1**. Therefore this run demonstrates a CAPE-level source-routing and boundary failure, but does not establish that Section 4.1 was active during the answer.

**Relevant retrieval trace:** CAPE searched `text ~ "AutoDrive" AND text ~ "Python"`, `text ~ "AutoDrive" AND type = page`, and titles matching coding/development standards. It retrieved AutoDrive product and migration material, Inchcape Secure Software Development Standards, and general Development Standards material. The supplied trace does not establish these sources as Eligible AutoDrive coding-standard sources in the Skill's validated set.

**Response excerpts:**

> “I will derive a practical standard from the AutoDrive tech stack, Inchcape's Secure Software Development Standards, and established Python best practices (PEP 8 / PEP 257).”

> “Apply these until a formal AutoDrive standard is published.”

The response then prescribes specific formatters, import ordering, activity contracts, logging, UI waits, Git branching, PR approvals, and testing requirements as an AutoDrive standard.

**Assessment:** **FAIL at the CAPE system boundary.** The answer synthesizes an organization-specific standard from sources that do not establish AutoDrive coding-standard authority. Because the RPA Skill was not loaded, this is not a clean test of the Skill's Section 4.1 behavior; rerun with the intended Skill loaded to assess that control. The Coverage-Honesty Gate remains **FAILED** until the mandatory Q10 behavior passes.

### Q12 — Logging standards

**Prompt:**

> What logging structure and logging standards should I follow for an Inchcape RPA automation?

**Response excerpts:**

> “No validated guidance is available for this topic.”

> “I would recommend raising this with the Inchcape RPA team directly, as they are the owners of the governed RPA knowledge base.”

> “The appropriate authoritative follow-up path is not established within the current validated knowledge boundary.”

**Assessment:** **Core boundary PASS; follow-up grounding issue, overall Partial.** The requested logging guidance is withheld, but the response asserts RPA-team ownership and then contradicts that assertion by saying no follow-up path is established.

### Q19 — DRPA vs SOLDOC

**Prompt:**

> What is the difference between the DRPA and SOLDOC spaces, and when should I use each one for an RPA project?

**Response excerpts:**

> “The distinction between the DRPA and SOLDOC Confluence spaces ... is a known unresolved gap.”

> “Consult the RPA team or the owner(s) of those two Confluence spaces directly. They hold the authoritative answer...”

> “The appropriate owner or escalation path within the validated knowledge boundary is not established...”

The supplied DRPA and SOLDOC search results did not establish the spaces' purpose, ownership, or governing relationship.

**Assessment:** **Core boundary PASS; follow-up grounding issue, overall Partial.** The response does not infer the distinction from search results, but asserts authoritative ownership without Eligible evidence and then says the owner/path is not established.

## 10. Change 02 status after latest retest

| Change | Implementation | Validation |
|---|---|---|
| Change 02 — Strict evidence boundary | Implemented | **Failed — Q10.** The CAPE-level answer still generated an unsupported AutoDrive standard; the RPA Skill was not loaded in the supplied Q10 trace. |
| Change 02.1 — Follow-up grounding | Implemented in Section 4.1 | **Partial — Q12/Q19.** Substantive declines are correct; unsupported ownership claims remain. |
| Change 02.2 — Source access boundary | Implemented in the active Skill after Activation and Evidence Boundary | **Pending retest.** The supplied Q10 run did not load the RPA Skill, so it cannot validate this instruction. |

No sources were added to the Eligible set, no source authority was changed, and Changes 03–06 were not modified. Rerun Q10 with the RPA Development Skill explicitly loaded, then rerun Q12 and Q19 to verify the source-access and follow-up rules together.
