- Validacion con el usuario (Algo de Design Thinking)
	a. Pedir feedback sobre CAPE
	b. Experiencias, que gusta y que se puede mejorar
- Darme a conocer:
	a. Recuerda que hablaste con Juan Jose Restrepo Rosero



Maide:
- Sign in expires
- Sometimes when I run something, context in error, refresh and do prompt again

Isa:
- CAPE does not take the table data
- Tables can be empty, but they were there but when doing the conversion it fails


---

What you currently have is informal exploratory feedback, not validated user research.

### Maide
| Observation                                 | Potential implication                                                       |
| ------------------------------------------- | --------------------------------------------------------------------------- |
| Sign-in expires                             | Authentication/session persistence creates friction in continued CAPE usage |
| Sometimes execution returns a context error | Reliability/context management may interrupt the user's workflow            |
| Refresh + repeat prompt is required         | Users incur additional interaction cost and may lose confidence in the tool |


### Isa
| Observation                                         | Potential implication                                           |
| --------------------------------------------------- | --------------------------------------------------------------- |
| CAPE does not take table data                       | Input/data-ingestion limitation                                 |
| Tables may exist but appear empty during conversion | Possible document/table parsing or conversion reliability issue |
| Conversion subsequently fails                       | Structured-data handling can affect successful task completion  |


## Dedicated user-validation workstream
Conceptually, our project now has two complementary evidence streams:

```text
                    CAPE RPA DEVELOPMENT SKILL
                               │
                ┌──────────────┴──────────────┐
                │                             │
         RPA DEVELOPMENT                 CAPE USER
            PERSPECTIVE                  PERSPECTIVE
                │                             │
        Developer pain points          User experience
        Technical questions            Usability friction
        Knowledge gaps                 Reliability issues
        Repetitive tasks               Adoption barriers
        Development standards          Improvement opportunities
                │                             │
                └──────────────┬──────────────┘
                               │
                       REQUIREMENTS
                               │
                       SKILL DESIGN
                               │
                     VALIDATION & METRICS
```

# CAPE User Feedback Study:

Phase A — Exploratory feedback

Start with a small number of CAPE users and ask about their actual experience.

Possible questions:

1. What do you currently use CAPE for?
2. What do you find most useful about CAPE?
3. What frustrates you when using CAPE?
4. What tasks does CAPE currently make easier?
5. Where does CAPE fail or require you to retry?
6. What information or capabilities do you wish CAPE handled better?
7. What would make you use CAPE more frequently?

Then we can conduct a second round specifically around the RPA Skill.

## Phase B — Categorize the feedback

Rather than collecting random comments, classify them.

For example:
| Category            | Example                                  |
| ------------------- | ---------------------------------------- |
| Authentication      | Session/sign-in expiration               |
| Reliability         | Context errors                           |
| Data ingestion      | Tables not recognized                    |
| Document processing | Table conversion failures                |
| Usability           | Repeated prompting / refreshing          |
| Knowledge           | Missing or difficult-to-find information |
| Accuracy            | Incorrect or incomplete answers          |
| Trust               | Confidence in generated recommendations  |
| Adoption            | Reasons to use or avoid CAPE             |
| Behavioral quality  | Unsupported inference, invented facts, or incorrect classifications |
| Decision quality    | Handling of ties and multiple valid recommendations |
| Output usability    | Truncation, contrast, navigation, progress visibility, or overengineering |

This will eventually become useful for both requirements engineering and prioritization.

## Phase C — Prioritize

We can eventually classify each observation according to:

> Frequency × Impact × Relevance

For example:

> High frequency + high impact → priority problem

while:

> Low frequency + low impact → monitor

This prevents the project from becoming a collection of anecdotes.

---

And this connects directly to Nikko's requirement

This is the strongest reason to add it.

> "Keep some measure of whether it actually works."

We can now build the project around two types of validation:

1. Technical validation

> Does the Skill provide correct and consistent RPA guidance?

Examples:
- correctness;
- source alignment;
- governance compliance;
- response consistency;
- handling of ambiguous questions.
- avoiding unsupported inference and invented stakeholders or deadlines;
- handling tied recommendations explicitly;
- avoiding unnecessary complexity and practical output truncation.

2. User validation

> Does the Skill actually improve the developer/user experience?

Examples:
- perceived usefulness
- time saved;
- reduced information searching;
- reduced repetitive questions;
- willingness to reuse;
- trust;
- adoption;
- observed friction.

Together:

> Technical quality + User value = evidence of Skill effectiveness

That is a considerably stronger project than simply creating a prompt/Skill and showing Nikko that it works.

#### One thing I want us to preserve
The feedback from Maide and Isa should not automatically become requirements for the RPA Development Skill.

For example, session expiration may be a CAPE platform issue, not an RPA Skill issue.

Likewise, table conversion may be a CAPE document-processing limitation, rather than something the RPA Skill itself should solve.

We should therefore maintain a distinction:

CAPE platform limitations
vs.
RPA Development Skill requirements

But the platform limitations are still important because they can affect adoption, perceived usefulness, and the overall user experience.

That distinction will be important when we perform the user-feedback analysis later.

---

So the project has now gained an additional dimension

Originally:

> RPA knowledge → Skill → developer efficiency → validation

Now:

> RPA knowledge + real CAPE user experience → requirements → Skill → technical & user validation → adoption

That is a meaningful improvement to the project design.

## Complementing
About the new user-feedback component

I would also not modify Figure 1 or Figure 2 yet to include the Design Thinking/user-feedback component.

The diagrams currently communicate the project proposition very cleanly. Adding user research to them would make them unnecessarily busy.

Instead, the user-feedback work should become part of the project's research and validation approach later:

CAPE user experience → User feedback → Pain-point identification → Requirements refinement → Skill design → Validation

This is particularly useful because the feedback you already collected from Maide and Isa gives us an initial set of observations, but not yet validated requirements.

We should eventually distinguish three things:

CAPE platform limitations
e.g., session expiration, context errors, table-processing problems.
RPA developer needs
e.g., debugging, architecture decisions, coding standards, APIs, security, governance.
RPA Development Skill requirements
e.g., source prioritization, contextual answers, citation/traceability, uncertainty handling, recommended practices.

That distinction will prevent us from accidentally trying to solve CAPE's underlying platform problems through the RPA Skill.

