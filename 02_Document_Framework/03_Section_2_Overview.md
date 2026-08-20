We should document:

how RPA developers currently obtain technical knowledge;
where that knowledge resides;
how a typical information-seeking interaction currently works;
what causes developers to search, ask, retry, or escalate;
which problems are caused by knowledge accessibility versus knowledge availability;
which problems are organizational versus technical;
what evidence we already have;
what still needs to be validated with users;
and finally, a concise formal problem statement.

---
```text
## 2. Problem Definition and Current State

### 2.1 Current RPA Knowledge-Access Model
### 2.2 Developer Information-Seeking Workflow
### 2.3 Current CAPE Experience
### 2.4 Observed Pain Points and Friction
### 2.5 Root-Cause Analysis
### 2.6 Impact on Developer Productivity and Consistency
### 2.7 User Validation Approach
### 2.8 Problem Statement
### 2.9 Opportunity Statement
### 2.10 Scope and Problem Boundaries
```
---

# Content 

## 2.1 Current RPA Knowledge-Access Model
Purpose
> Describe how an RPA developer currently obtains the information necessary to perform their work.

We already know from Section 1 that knowledge exists in:
- Confluence;
- Service Desk;
- technical documentation;
- development standards;
- organizational procedures;
- platform/vendor documentation;
- team experience.

Now we need to understand how those sources interact.

We should document

For example:

1. Developer has a question

→ searches Confluence
→ identifies potentially relevant documentation
→ interprets the documentation
→ checks whether it applies to the specific case
→ searches another source if necessary
→ asks another developer if uncertainty remains
→ potentially escalates to a subject-matter expert
→ implements the solution
→ validates whether the interpretation was correct.

This is important because the problem may not be:

> "There is no documentation."

It may instead be:

> "The knowledge exists, but the path from question → relevant knowledge → contextual interpretation → actionable decision contains friction."

That distinction should become one of the central findings of Section 2.

### Likely artifact

I recommend a diagram:

"Figure 3. Current-State RPA Knowledge-Access Flow"

Something like:
```text
[Developer encounters question]
              |
              v
     [Identify the problem]
              |
              v
      [Search knowledge]
        /           \
       /             \
[Confluence]     [Other sources]
       \             /
        \           /
         v         v
      [Interpret information]
              |
        +-----+-----+
        |           |
        v           v
   [Sufficient] [Uncertain]
        |           |
        |           v
        |      [Ask colleague /
        |       SME / escalate]
        |           |
        +-----+-----+
              |
              v
       [Apply solution]
              |
              v
       [Validate result]
```

This would make the problem immediately understandable.

---

## 2.2 Developer Information-Seeking Workflow

This subsection should go one level deeper.

- 2.1 describes the ecosystem.
- 2.2 describes the developer's behavior within that ecosystem.

We should identify the different types of questions developers encounter.

For example:

### Technical
- How should I implement this?
- Which library/framework should I use?
- Why is this exception occurring?
- How should this API be integrated?
  
### Architectural
- Should this process use AutoDrive, UiPath, or Power Automate?
- How should the components interact?
- What architecture is appropriate?

### Governance
- Does this require CAB?
- What documentation is required?
- What security controls apply?

### Operational
- How should this incident be handled?
- What is the expected support procedure?
- What happens during hypercare/BAU?

### Knowledge retrieval
- Where is the relevant documentation?
- Which Confluence page contains the standard?
- Which procedure is the current one?

This gives us a taxonomy of information needs.

---

## 2.3 Current CAPE Experience

This is where your new idea becomes relevant.

We should document CAPE as it currently exists, before discussing the RPA Development Skill.

### Verified first-party CAPE baseline

The project now has internal CAPE product and architecture documentation in addition to UI observations and informal user feedback. This documented baseline confirms that:

- CAPE is Inchcape's internal chat application and is currently a proof of concept.
- CAPE is deployed on Databricks Apps using a FastAPI runtime.
- The deployed application uses Lakebase Postgres.
- CAPE provides streaming chat, attachments, a Python code interpreter, connectors, tools, agents, workflows, projects, and artifacts.
- Skills are packaged domain knowledge loaded on demand when relevant.
- Skills are auto-pooled and progressively disclosed rather than equipped like account-bound tools.

The technical reference is maintained in `03_Knowledge_Research/06_CAPE_First_Party_Technical_Reference_v0_1.md`.

This evidence replaces several previous architectural assumptions, but it does not replace structured user validation.

### Previously observed CAPE behavior

We also know from existing observations that:

- CAPE is available as an enterprise AI capability.
- It has Skills.
- Skills are invoked automatically when relevant.
- It may provide per-user, authorized access to scoped Confluence and Service Desk connector capabilities; availability and permissions must be verified for each deployment and user.
- It already provides several general-purpose capabilities.

### Implication for the RPA Development Skill

The Skill should not be conceptualized as a container for all RPA documentation. Based on the first-party CAPE documentation, it should be defined as an on-demand domain-specific knowledge and instruction module that CAPE loads for relevant RPA development requests and uses with validated RPA sources.

This distinction should guide the future Skill architecture, source-selection logic, response behavior, testing methodology, and evaluation criteria.

Platform issues such as session expiration, context errors, document/table conversion failures, connector availability, and proof-of-concept maturity should be tracked separately from the requirements of the RPA Development Skill. They may affect adoption and perceived usefulness without being problems the Skill itself can solve.

The documented CAPE feedback also identifies evaluation concerns including poor contrast, weak branding, hidden navigation, subtle progress indicators, long-output truncation, overengineering, unsupported inference, invented stakeholders or deadlines, incorrect handling of ties, and incorrect classifications. These are platform or behavior risks to test and classify, not assumptions to convert directly into Skill requirements.

Then we introduce the initial user feedback.

But we must label it correctly:

> Preliminary informal user observations

Not "research findings" yet.

For example:

### Preliminary observations:

#### Maide
- Session/sign-in expiration.
- Occasional context errors requiring a refresh and repetition of the prompt.

#### Isa
- Difficulty processing table data.
- Cases where tables are present but are interpreted as empty during conversion, resulting in failure.

Then explicitly state:

> These observations are preliminary and are not yet sufficient to establish frequency, severity, root cause, or generalizability. They will therefore be treated as hypotheses to be investigated through structured user validation.

That sentence is important.


## 2.4 Observed Pain Points and Friction
### Purpose
> Consolidate the observed and potential sources of friction experienced by RPA developers when locating, interpreting, validating, and applying knowledge.
The previous sections established where knowledge resides and how developers currently navigate available sources when seeking information.
This section focuses on identifying the points where that process becomes inefficient, inconsistent, or unreliable.
Rather than documenting isolated issues, it is useful to organize pain points into categories that describe where friction occurs throughout the knowledge-access journey.
### Pain-Point Taxonomy
The following categories provide an initial framework for organizing observations, feedback, and validation findings.
#### Knowledge Discovery
Challenges associated with locating relevant information.
Examples:
- Finding the correct documentation.
- Identifying the appropriate Confluence page.
- Knowing where a specific procedure or standard resides.
- Searching across multiple repositories before finding an answer.
#### Knowledge Interpretation
Challenges associated with understanding and applying information.
Examples:
- Understanding how a standard applies to a specific situation.
- Determining whether documented guidance is relevant to the current use case.
- Translating documentation into implementation decisions.
- Resolving ambiguity within procedures or standards.
#### Repetition
Challenges associated with recurring requests for assistance.
Examples:
- Repeatedly asking experienced developers similar questions.
- Reinvestigating previously solved problems.
- Frequently revisiting documentation for clarification.
#### Consistency
Challenges associated with obtaining uniform guidance.
Examples:
- Different developers receiving different recommendations.
- Inconsistent interpretation of standards.
- Variations in implementation approaches across projects.
#### Context
Challenges associated with providing sufficient information to obtain meaningful assistance.
Examples:
- Difficulty describing a problem accurately.
- Missing contextual details required for troubleshooting.
- Uncertainty regarding what information should be provided.
#### Reliability
Challenges associated with tool stability and user experience.
Examples:
- Errors during interactions.
- Session expiration.
- Refresh requirements.
- Failed or inconsistent responses.
#### Data Handling
Challenges related to the processing of structured information.
Examples:
- Tables not being interpreted correctly.
- Structured content being treated as empty.
- Conversion failures when processing tabular data.
#### Trust
Challenges associated with confidence in generated guidance.
Examples:
- Uncertainty regarding recommendation accuracy.
- Need for manual verification.
- Concerns regarding completeness of responses.
#### Source Authority
Challenges associated with determining which source should be trusted.
Examples:
- Multiple documents containing overlapping information.
- Conflicting guidance across sources.
- Uncertainty regarding the authoritative standard.
#### Adoption
Challenges associated with integrating CAPE into daily workflows.
Examples:
- Preference for consulting colleagues instead of using available tools.
- Resistance to changing existing behaviors.
- Workflow interruptions reducing perceived value.
### Key Observation
The emerging challenge may not be the absence of knowledge.
Instead, preliminary evidence suggests that friction may occur during the process of discovering, interpreting, validating, and applying existing knowledge.
This distinction is important because it shifts the focus from knowledge availability to knowledge accessibility and usability.
---

## 2.5 Root-Cause Analysis
### Purpose
> Identify the underlying causes of observed pain points rather than focusing exclusively on symptoms.
Observed behaviors do not necessarily reveal the root cause of a problem. Similar symptoms can emerge from multiple contributing factors and may require different interventions.
### Example
#### Symptom
A developer asks a colleague how a particular RPA standard should be applied.
#### Possible Root Causes
- Documentation is difficult to locate.
- Relevant information is distributed across multiple documents.
- Documentation lacks contextual examples.
- The authoritative source is unclear.
- The developer is unfamiliar with the process.
- Information is available but fragmented across repositories.
- Documentation is outdated, incomplete, or ambiguous.
Although the symptom is the same, each root cause implies a different corrective action.
### Analysis Approach
Where useful, root-cause analysis techniques may be applied to better understand contributing factors.
Potential approaches include:
- 5 Whys analysis.
- Fishbone (Ishikawa) analysis.
- Cause-and-effect mapping.
- Workflow decomposition.
The objective is not to force the use of a specific methodology, but to avoid jumping directly from symptoms to solutions without understanding the factors driving the observed behavior.
### Preliminary Root-Cause Themes
Based on the information collected so far, potential root-cause themes include:
- Information fragmentation.
- Difficulty locating relevant knowledge.
- Lack of contextual guidance.
- Documentation inconsistency.
- Unclear source ownership or authority.
- Knowledge dependency on individual experience.
- Documentation quality and maintenance challenges.
These themes should be treated as hypotheses until validated through user feedback and additional evidence.
---

## 2.6 Impact on Developer Productivity and Consistency
### Purpose
> Assess how current knowledge-access challenges may influence developer efficiency, effectiveness, and consistency.
One of the primary objectives of this initiative is to help developers work faster and more consistently.
To understand the value of any potential improvement, it is necessary to evaluate the impact of the current state.
### Productivity Dimension
Potential impacts include:
- Time spent searching for information.
- Repeated documentation review.
- Recurring requests to experienced developers.
- Context switching between systems and sources.
- Delays during troubleshooting activities.
- Duplicate investigation efforts.
- Slower onboarding for new team members.
- Frequent interruptions of senior developers and SMEs.
### Consistency Dimension
Potential impacts include:
- Different interpretations of the same standard.
- Variations in solution implementation.
- Inconsistent exception-handling approaches.
- Inconsistent documentation practices.
- Variability in governance application.
- Dependence on individual experience and tribal knowledge.
### Evidence Considerations
At this stage, these impacts should be considered potential consequences rather than quantified findings.
For example, it would be inappropriate to state:
> "The current model reduces productivity by X%."
unless sufficient measurement data exists.
Instead, the assessment should focus on statements such as:
> "The current model creates potential productivity costs through repeated searches, repeated consultation, and fragmented knowledge access."
Any quantitative claims should be supported by future measurement and validation activities.
---

## 2.7 User-Centered Validation
### Purpose
> Validate assumptions about developer behavior, pain points, and expectations through direct user engagement.
The observations documented in previous sections should be treated as initial hypotheses rather than established findings.
To ensure that requirements are grounded in actual user needs, the project will incorporate a lightweight user-centered validation approach.
### Validation Objectives
The validation effort should investigate:
- Actual CAPE usage patterns.
- User experience during knowledge retrieval.
- Recurring frustrations and pain points.
- Perceived value of current capabilities.
- Missing functionality.
- Barriers to adoption.
- Expectations for AI-assisted RPA development.
### Validation Process
#### Stage 1 – Explore
Collect feedback from CAPE users and RPA developers.
Possible activities:
- Informal interviews.
- Surveys.
- User journey discussions.
- Observation of information-seeking activities.
#### Stage 2 – Synthesize
Analyze and organize findings into meaningful themes.
Possible activities:
- Grouping observations.
- Categorizing pain points.
- Identifying recurring patterns.
- Highlighting common workflow challenges.
#### Stage 3 – Validate
Determine whether identified problems are:
- Recurring.
- Relevant.
- Significant.
- Actionable.
The outcome should be a validated understanding of which issues are sufficiently important to influence solution requirements.
### Validation Principle
User feedback should be treated as evidence rather than conclusions.
The purpose of validation is to determine which assumptions are consistently experienced across the developer population and therefore represent legitimate business and user needs.
---

## 2.8 Problem Statement
### Purpose
> Define the current problem in a concise, evidence-based manner.
The problem statement should summarize the findings developed throughout Sections 2.1 through 2.7 and describe the challenge independently of any proposed solution.
### Conceptual Direction
> RPA developers operate within a technically diverse environment supported by substantial organizational, operational, and technical documentation. While the required knowledge often exists, locating, interpreting, validating, and consistently applying that information may require fragmented searches, repeated consultation, and significant contextual interpretation. This introduces avoidable friction into development activities and creates the potential for inconsistent outcomes when addressing similar technical, operational, or governance-related questions.
### Important Consideration
This statement should be refined after user validation activities have been completed and sufficient evidence has been gathered to support the final wording.
---

## 2.9 Opportunity Statement
### Purpose
> Define the improvement opportunity revealed by the identified problem.
While the problem statement focuses on current limitations, the opportunity statement focuses on what could be improved.
### Conceptual Direction
> There is an opportunity to improve the accessibility, discoverability, and usability of existing RPA knowledge by enabling developers to obtain contextual, trusted, and actionable guidance at the point of need while preserving the authority of established documentation, governance processes, and subject-matter expertise.
### Guiding Principle
The opportunity should remain independent of any specific solution.
For example, the opportunity exists regardless of whether the eventual response includes:
- A CAPE Skill.
- Enhanced search capabilities.
- Documentation improvements.
- Knowledge-management initiatives.
- Process refinements.
Separating the problem from the solution helps ensure that design decisions remain evidence-driven and objectively evaluated.
---

## 2.10 Scope and Problem Boundaries
### Purpose
> Define what is included and excluded from the problem space in order to maintain focus and prevent uncontrolled scope expansion.
Establishing clear boundaries ensures that the initiative remains focused on improving RPA knowledge access rather than attempting to address unrelated organizational or platform-level issues.
### In Scope
The investigation and potential solution space include:
- RPA developer knowledge access.
- Technical implementation guidance.
- RPA standards and best practices.
- Architecture guidance.
- Troubleshooting support.
- Integration knowledge.
- Testing practices.
- Security requirements.
- Governance guidance.
- Documentation discovery and interpretation.
- Operational and support knowledge.
- CAPE-assisted developer support.
### Initially Out of Scope
The following areas are not currently considered part of the primary problem scope:
- CAPE authentication or sign-in issues.
- Redesign of CAPE core platform capabilities.
- Modifications to Service Desk systems or processes.
- Replacement of Confluence.
- Replacement of human SMEs.
- Automation of production governance decisions.
- Autonomous execution of RPA processes.
- Organizational approval and compliance decisions.
### Scope Considerations from Preliminary Feedback
Certain observations may be relevant to usability and adoption without necessarily becoming functional requirements.
#### CAPE Session Expiration
- May represent a user-experience concern.
- May affect adoption rates.
- Does not necessarily fall within the scope of an RPA Development Skill.
#### Table-Processing Limitations
- May affect overall CAPE usability.
- May influence user satisfaction.
- Should not automatically be considered a functional requirement for the proposed solution.
Maintaining these boundaries helps prevent scope contamination and keeps the initiative focused on validated knowledge-access challenges.
---
## Evidence Strategy
Before drawing formal conclusions, findings should be classified according to their level of evidence.
### Level 1 – Established Facts
Information confirmed through documentation, systems, or organizational knowledge.
Examples:
- RPA knowledge exists within Confluence.
- CAPE is available as an enterprise AI capability.
- CAPE has access to defined organizational knowledge sources.
### Level 2 – Observed Behavior
Information derived from direct experience or preliminary user observations.
Examples:
- Developers may search multiple sources before finding an answer.
- Users occasionally experience session-expiration issues.
- Structured tables may not always be processed successfully.
### Level 3 – To Be Validated
Assumptions that appear plausible but require confirmation through user feedback or measurement.
Examples:
- Repetitive questions consume significant developer time.
- Information fragmentation contributes to productivity loss.
- Knowledge discovery challenges affect development efficiency.
### Level 4 – Hypotheses
Expected outcomes or benefits that must be tested.
Examples:
- CAPE can improve knowledge accessibility.
- An RPA Development Skill can improve developer efficiency.
- AI-assisted guidance can improve implementation consistency.
Applying this evidence hierarchy will improve the credibility of findings and ensure conclusions remain aligned with available evidence.
---
## Recommended Workflow Before Writing Section 2
```text
STEP 1
Establish the current knowledge ecosystem
↓
STEP 2
Map the current developer information-seeking workflow
↓
STEP 3
Define the types of RPA questions and knowledge needs
↓
STEP 4
Collect and organize preliminary CAPE user observations
↓
STEP 5
Conduct lightweight user validation
↓
STEP 6
Synthesize pain points
↓
STEP 7
Analyze probable root causes
↓
STEP 8
Assess productivity and consistency impact
↓
STEP 9
Write the formal Problem Statement
↓
STEP 10
Write the Opportunity Statement
↓
STEP 11
Define scope and boundaries
```

