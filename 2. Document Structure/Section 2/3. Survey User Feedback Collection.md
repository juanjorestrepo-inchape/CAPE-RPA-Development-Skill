# Do we need a survey?
Yes, but I would NOT start with a giant survey. We should make it lightweight and targeted.

**We need two different types of user research, because they answer different questions**

## A. CAPE general-user feedback

This is what Maide and Isa started giving us.

Purpose:
> Understand the current CAPE experience and identify usability, reliability, data-handling, and adoption friction.

This should include people who use CAPE, not necessarily only RPA developers.

Questions could cover:

1. What do you currently use CAPE for?
2. What do you find most useful?
3. What frustrates you?
4. Have you encountered errors?
5. Have you had to retry prompts?
6. Does CAPE correctly understand files/tables?
7. What would make you use CAPE more?
8. What capabilities would you like to have?
9. How confident are you in CAPE's responses?

This gives us the CAPE platform/user perspective

## B. RPA Developer Needs Assessment
This survey should target RPA developers specifically. The central question is:

> What information do RPA developers repeatedly need, where do they currently obtain it, and what creates friction?

We could ask things such as:

1. Current information-seeking
2. How frequently do you need to search documentation to solve a development question?
3. Where do you normally look first?
4. How many sources do you typically consult?
5. How often do you ask another developer instead?
6. Which types of questions most frequently require assistance?

**Technical categories**
Ask them to select all that apply:

- Architecture / technology selection
- AutoDrive
- UiPath
- Power Automate
- Python/software engineering
- APIs/integrations
- Debugging
- Testing
- Logging/exception handling
- Security/credentials
- Documentation
- CAB/change management
- Incident management
- Other

## Efficiency

Questions such as:

- **How often do you encounter a question that takes longer than expected to resolve because you need to search for or interpret existing information?**

Then perhaps a Likert scale:

- **Never → Rarely → Sometimes → Often → Very often**

## Repetitive questions

- **How often do you ask another team member about something you believe may already be documented?**

Then perhaps a Likert scale:

- **Never → Rarely → Sometimes → Often → Very often**

## CAPE opportunity

- **How useful would it be to have an AI capability that could provide contextual guidance based on approved RPA documentation and technical sources?**

Then perhaps a Likert scale:

- **Not useful → Slightly useful → Moderately useful → Very useful → Extremely useful**

This gives us quantitative evidence.

---

We could also apply:

1. Survey
    Perception and frequency.

2. Short interviews / conversations
    Context and examples.

3. Real question collection
    Actual developer questions.

The third one is particularly valuable

---
# RPA Question Dataset

- This will eventually become one of the most valuable project artifacts.
- Ask developers to submit questions they have actually encountered.

**For example:**

| ID   | Question                             | Domain       | Current Resolution     | Source           | Difficulty | Repetition |
| ---- | ------------------------------------ | ------------ | ---------------------- | ---------------- | ---------- | ---------- |
| Q001 | Which platform should be used for X? | Architecture | Asked senior dev       | Confluence + SME | Medium     | High       |
| Q002 | Where should credentials be stored?  | Security     | Confluence             | Security policy  | Low        | High       |
| Q003 | Why is this UiPath workflow failing? | Debugging    | SME                    | Multiple sources | High       | Medium     |
| Q004 | What is required before Pre-CAB?     | Governance   | Confluence + colleague | CAB docs         | Medium     | High       |


This dataset serves three purposes simultaneously:

## Purpose 1 — Discovery
It tells us what developers actually need.

## Purpose 2 — Skill design
It tells us what knowledge and behaviors the Skill needs.

## Purpose 3 — Evaluation
The same questions can later become our evaluation benchmark.

So this is a very efficient approach:
> **Real questions → requirements → test dataset → Skill evaluation**


## Discovery Evidence of our Research Model

```text
                         DISCOVERY EVIDENCE
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
     RPA KNOWLEDGE         RPA DEVELOPERS       CAPE USERS
       INVENTORY             & QUESTIONS         & FEEDBACK
             │                  │                  │
             ▼                  ▼                  ▼
      What knowledge       What do they       What works /
       exists?             actually need?     what frustrates?
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                      CURRENT-STATE ANALYSIS
                                │
                                ▼
                        PAIN-POINT TAXONOMY
                                │
                                ▼
                         ROOT CAUSES
                                │
                                ▼
                       PROBLEM STATEMENT
                                │
                                ▼
                      SKILL REQUIREMENTS
```

I 


#### The Knowledge Inventory tells us:

***What knowledge exists?***

#### The Question Dataset tells us:

***What do developers actually need to know?***

```text
Knowledge Sources
       +
Developer Questions
       +
User Feedback
       ↓
RPA Skill Requirements
```


And there is another important discovery: sources can conflict

We now know that:
- DRPA and SOLDOC can contain corresponding documentation;
- Confluence and GitHub can both contain AutoDrive information;
- Service Desk contains operational experience;
- vendor documentation may disagree with internal practices;
- some internal documents may be old.

Therefore, the Knowledge Inventory should eventually support something like:

| Attribute     | Why we need it                      |
| ------------- | ----------------------------------- |
| Source        | Identify the document/system        |
| Repository    | Where it lives                      |
| Domain        | What knowledge it represents        |
| Authority     | How authoritative it is             |
| Currency      | How current it is                   |
| Scope         | Where it applies                    |
| Owner         | Who maintains it                    |
| Version       | Which revision                      |
| Skill Role    | Primary / Supporting / Contextual   |
| Conflict Risk | Potential overlap/conflict          |
| Status        | Validated / Needs Review / Excluded |
| Notes         | Important caveats                   |

This is more sophisticated than the original table, and I think we should use this structure.