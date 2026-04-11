---
name: Business Analyst Quality Standards
description: "Quality standards for Business Analysis documents - Ensures complete handoff to Requirements Engineer"
---

# Business Analyst - Quality Standards for BA Documents

These instructions define the quality standards for Business Analysis documents and ensure that the Requirements Engineer receives all required information.

> **Goal:** The Requirements Engineer can **immediately** start creating Epics/Features without needing to ask the BA clarifying questions.

---

## Quality Goals

### For the Requirements Engineer
The RE must be able to **directly** derive from the BA document:
- [CHECK] Who are the users? (-> User Stories)
- [CHECK] What is the problem? (-> Problem Statement)
- [CHECK] What are the needs? (-> Functional Requirements)
- [CHECK] What is the solution? (-> Features)
- [CHECK] What is in-scope/out-of-scope? (-> Epic Boundaries)
- [CHECK] How-Might-We question (-> Bridge EXPLORATION to IDEATION)
- [CHECK] Value Proposition (-> Solution Hypothesis)
- [CHECK] Needs -- functional, emotional, social (-> User-Centered Design)
- [CHECK] Insights -- functional, emotional, social, analogies (-> Innovation Basis)
- [CHECK] Jobs to be Done -- functional, emotional, social (-> Prioritization)
- [CHECK] Idea Potential -- 3 axes with scores (-> Go/No-Go Decision)
- [CHECK] Critical Hypotheses (-> What must be validated)

---

## Mandatory Sections by Scope

### Simple Test (Minimal)

```markdown
MANDATORY SECTIONS:
[CHECK] 1. Executive Summary (1 paragraph)
[CHECK] 2. Problem Statement (brief)
[CHECK] 4. User & Target Group (primary group)
[CHECK] 4b. User with needs (user-need mapping)
[CHECK] 5. Needs (Functional Jobs, Pains)
[CHECK] 9. Solution Idea (Core idea, Key Features)
[CHECK] 11. Scope (In-Scope only)

OPTIONAL:
[ ] 3. Stakeholder Analysis
[ ] 6. Current Process
[ ] 7. Data & Integration
[ ] 10. Value Proposition
[ ] 12. Success Metrics
```

### Proof of Concept (Moderate)

```markdown
MANDATORY SECTIONS:
[CHECK] 1. Executive Summary (1-2 paragraphs)
[CHECK] 2. Problem Statement (complete)
[CHECK] 3. Stakeholder Analysis (table)
[CHECK] 4. User & Target Group (primary + secondary)
[CHECK] 5. Needs -- functional/emotional (typed and prioritized)
[CHECK] 6. Current Process (description)
[CHECK] 7. Data & Integration (overview)
[CHECK] 7.1. Idea Potential (3 axes with scores)
[CHECK] 7.3. Critical Hypotheses (what must be validated)
[CHECK] 8. How Might We (at least 1)
[CHECK] 9. Solution Idea (Core idea, Features)
[CHECK] 10. Value Proposition
[CHECK] 11. Scope (In + Out + Assumptions)

OPTIONAL:
[ ] 12. Success Metrics (recommended)
```

### MVP (Complete)

```markdown
MANDATORY SECTIONS (ALL):
[CHECK] 1. Executive Summary (2-3 paragraphs)
[CHECK] 2. Problem Statement (with quantified impact)
[CHECK] 3. Stakeholder Analysis (complete table)
[CHECK] 4. User & Target Group (Personas with details)
[CHECK] 4b. Exploration Board complete
[CHECK] 5. Needs + Insights (functional/emotional/social -- detailed)
[CHECK] 5.4. Jobs to be Done (functional/emotional/social)
[CHECK] 6. Current Process (with Pain Points)
[CHECK] 7. Data & Integration (detailed)
[CHECK] 7.1. Idea Potential (3 axes scored 0-10 with rationale)
[CHECK] 7.2. The Wow (differentiator)
[CHECK] 7.3. Critical Hypotheses (at least 2 with test method)
[CHECK] 8. How Might We (at least 2)
[CHECK] 9. Solution Idea (Core idea, Features, Wow-Feature)
[CHECK] 10. Value Proposition (complete)
[CHECK] 11. Scope (In + Out + Assumptions + Constraints)
[CHECK] 11. Evaluate section (VP Score, Assessment Radar)
[CHECK] 12. Success Metrics (KPIs with target values)
[CHECK] 13. Next Steps (with open questions)
```

---

## Section Validations

### 1. Executive Summary

```markdown
CHECK:
[CHECK] Problem described in one sentence?
[CHECK] Solution idea described in one sentence?
[CHECK] Expected impact/benefit stated?

EXAMPLE - GOOD:
"Manually creating reports costs the team 10h/week.
An automated solution should reduce this to 1h and
lower the error rate from 15% to under 2%."

EXAMPLE - BAD:
"We want to improve report creation."
```

### 2. Problem Statement

```markdown
CHECK:
[CHECK] Context/background clear?
[CHECK] Specific problem defined (not vague)?
[CHECK] Impact described? (PoC/MVP: quantified)

EXAMPLE - GOOD:
"Context: Sales team creates weekly pipeline reports.
Problem: Manual data aggregation from 3 systems takes 2h per report.
Impact: 10h/week time loss, 15% error rate, delayed decisions."

EXAMPLE - BAD:
"Reporting is inefficient and needs improvement."
```

### 4. User & Target Group

```markdown
CHECK:
[CHECK] Primary user group identified?
[CHECK] Characteristics described? (Tech level, context)
[CHECK] Current situation described?
[CHECK] Frustrations/Pain Points listed?

EXAMPLE - GOOD:
"Primary users: Sales Managers (5 people)
Characteristics: Business user, Excel-proficient, no SQL
Current situation: Manually copy data from CRM, ERP, Excel
Frustrations: Time effort, error-prone, no real-time data"

EXAMPLE - BAD:
"Users are sales people who need reports."
```

### 4.2 Needs

```markdown
CHECK:
[CHECK] At least 3 needs identified?
[CHECK] Typed as functional/emotional/social?
[CHECK] Prioritized?

FORMAT:
Functional: "I need to [capability] so that [outcome]"
Emotional: "I want to feel [emotion] when [situation]"
Social: "I want to be seen as [perception] by [audience]"

EXAMPLE - GOOD:
"Functional: I need to generate reports in under 5 minutes
 so that I can respond to management requests same-day.
 Emotional: I want to feel confident that my numbers are correct.
 Social: I want to be seen as data-driven by my leadership team."

EXAMPLE - BAD:
"User needs better reports."
```

### 4.3 Insights

```markdown
CHECK:
[CHECK] At least 2 per category (functional, emotional)?
[CHECK] Insights derived from observations or research?
[CHECK] Analogies included where applicable?

FORMAT:
Functional Insight: "[Observation] because [root cause]"
Emotional Insight: "[Behavior] driven by [underlying emotion]"
Social Insight: "[Pattern] because [social dynamic]"
Analogy: "[Similar domain] solved this by [approach]"
```

### 5. Needs & Jobs to be Done

```markdown
CHECK:
[CHECK] At least 2-3 functional jobs listed?
[CHECK] At least 2-3 pains identified?
[CHECK] At least 2-3 gains described?

FORMAT:
Jobs: "As [role] I need to [activity] in order to [goal]"
Pains: Concrete obstacles, frustrations, risks
Gains: Desired outcomes, improvements
```

### 5.4 Jobs to be Done

```markdown
CHECK:
[CHECK] All 3 job types covered (functional/emotional/social)?
[CHECK] Current solution identified?
[CHECK] Desired outcome per job type defined?

FORMAT:
Functional Job: "When [situation], I want to [action], so I can [outcome]"
Emotional Job: "When [situation], I want to feel [emotion]"
Social Job: "When [situation], I want to be perceived as [perception]"

EXAMPLE - GOOD:
"Functional: When preparing the weekly review, I want to pull all
 pipeline data into one view, so I can present a complete picture.
 Current solution: Manual Excel consolidation from 3 sources.
 Emotional: I want to feel confident that my data is accurate.
 Social: I want to be perceived as well-prepared by the C-suite."

EXAMPLE - BAD:
"User wants faster reports."
```

### 7.1 Idea Potential

```markdown
CHECK:
[CHECK] All 3 axes scored 0-10 with rationale?
[CHECK] Scores reflect evidence, not wishful thinking?

FORMAT:
Axis 1 - Desirability: [0-10] -- [Rationale]
Axis 2 - Feasibility: [0-10] -- [Rationale]
Axis 3 - Viability: [0-10] -- [Rationale]

EXAMPLE - GOOD:
"Desirability: 8/10 -- 5 out of 5 interviewed sales managers
 confirmed this as their top pain point.
 Feasibility: 6/10 -- API integrations exist for 2 of 3 systems;
 third requires custom connector.
 Viability: 7/10 -- Estimated 10h/week savings justifies
 development cost within 3 months."
```

### 7.2 The Wow

```markdown
CHECK:
[CHECK] Differentiator clearly described?
[CHECK] Explains why this is better than alternatives?

EXAMPLE - GOOD:
"The Wow: One-click report generation that auto-detects anomalies
 and highlights them with plain-language explanations -- something
 no existing BI tool does without manual configuration."

EXAMPLE - BAD:
"It will be really fast."
```

### 7.3 Critical Hypotheses

```markdown
CHECK:
[CHECK] At least 2 hypotheses defined?
[CHECK] Test method defined for each?
[CHECK] Success criteria stated?

FORMAT:
Hypothesis: "We believe that [assumption]"
Test: "We will validate this by [method]"
Success Criterion: "We know we are right when [measurable outcome]"

EXAMPLE - GOOD:
"H1: We believe that sales managers will adopt automated reports
 if generation takes under 1 minute.
 Test: Prototype test with 3 sales managers, measure adoption.
 Success: 80% prefer automated over manual within 2 weeks.

 H2: We believe that API data from all 3 systems can be
 consolidated with <5% data discrepancy.
 Test: Integration spike with sample data.
 Success: Reconciliation delta <5% across 100 records."

EXAMPLE - BAD:
"Users will like it."
```

### 8. How Might We

```markdown
CHECK:
[CHECK] At least 1 HMW question formulated? (PoC/MVP: at least 2)
[CHECK] Format: "How might we help [user] to [job], without [pain]?"
[CHECK] Primary HMW question marked?

EXAMPLE - GOOD:
"How might we help Sales Managers create pipeline reports
without manually aggregating data from 3 systems?"

EXAMPLE - BAD:
"How can we improve reporting?"
```

### 9. Solution Idea

```markdown
CHECK:
[CHECK] Core idea described in 2-3 sentences?
[CHECK] High-Level Concept/Analogy present? (MVP)
[CHECK] Key Features listed? (at least 3)
[CHECK] Wow-Feature identified? (MVP)

KEY FEATURES FORMAT:
1. **[Feature Name]**: [1-sentence description]
   - Solves: [Which Pain/Job]

EXAMPLE:
1. **Automatic Data Aggregation**: Pulls data from CRM, ERP, Excel together
   - Solves: Manual copying (2h -> 5min)
```

### 10. Value Proposition

```markdown
CHECK:
[CHECK] All placeholders filled in?
[CHECK] Differentiator clear?

FORMAT:
"For [user], who [problem],
our solution is a [product category],
that provides [key benefit].
Unlike [alternative], our solution enables [differentiator]."

EXAMPLE - GOOD:
"For Sales Managers who must create weekly pipeline reports,
our solution is an automated reporting dashboard
that aggregates real-time data from all systems.
Unlike manual Excel reports, our solution enables
instant updates and eliminates transcription errors."
```

### 11. Scope & Prioritization

```markdown
CHECK:
[CHECK] In-Scope clearly defined? (at least 3 items)
[CHECK] Out-of-Scope explicitly listed? (at least 2 items)
[CHECK] Assumptions documented?
[CHECK] Constraints listed? (PoC/MVP)

IMPORTANT FOR RE:
- In-Scope -> becomes Epics/Features
- Out-of-Scope -> explicitly NOT part of the project
- Assumptions -> must be validated
- Constraints -> influence architecture decisions
```

### 11. Evaluate (MVP only)

```markdown
CHECK:
[CHECK] VP Score complete?
[CHECK] Assessment Radar scored?
[CHECK] All dimensions rated with justification?
```

### 12. Success Metrics (PoC/MVP)

```markdown
CHECK:
[CHECK] At least 2-3 KPIs defined?
[CHECK] Baseline value stated? (current state)
[CHECK] Target value defined?

EXAMPLE - GOOD:
- **Report creation time**: 2h -> 5min (-96%)
- **Error rate**: 15% -> <2%
- **Timeliness**: Weekly -> Real-time

EXAMPLE - BAD:
- "Faster reports"
- "Fewer errors"
```

---

## Handoff Checklist for Requirements Engineer

Before handoff to RE, validate:

### Minimal (Simple Test)
```
- [ ] Problem is clear and specific
- [ ] At least one user group defined
- [ ] User with needs mapped
- [ ] Key Features (high-level) listed
- [ ] In-Scope defined
```

### Standard (PoC)
```
- [ ] Problem is clear and specific
- [ ] User group(s) with characteristics defined
- [ ] Needs (functional/emotional) captured and typed
- [ ] How Might We question formulated
- [ ] Solution idea with Key Features described
- [ ] Value Proposition formulated
- [ ] In-Scope and Out-of-Scope defined
- [ ] Assumptions documented
- [ ] Idea Potential scored (3 axes)
- [ ] Critical Hypotheses defined with test methods
```

### Complete (MVP)
```
- [ ] Executive Summary contains Problem, Solution, Impact
- [ ] Problem Statement with quantified impact
- [ ] Stakeholder table complete
- [ ] User Personas with details
- [ ] Exploration Board complete
- [ ] Needs (functional/emotional/social) detailed and prioritized
- [ ] Insights (functional, emotional, social, analogies) documented
- [ ] Jobs to be Done (all 3 types) defined
- [ ] Current process with Pain Points
- [ ] Data & Integrations identified
- [ ] How Might We questions (at least 2)
- [ ] Solution idea with Wow-Feature
- [ ] Value Proposition complete
- [ ] Idea Potential (3 axes scored 0-10 with rationale)
- [ ] Critical Hypotheses (at least 2 with test method)
- [ ] Scope clear (In/Out/Assumptions/Constraints)
- [ ] Evaluate section (VP Score, Assessment Radar)
- [ ] KPIs with baseline and target values
- [ ] Open questions for RE listed
```

---

## Anti-Patterns in BA Documents

### BAD: Vague Problem Description
```
WRONG: "The system is slow and unreliable"
RIGHT: "Average load time is 8 seconds,
        target is <2 seconds. System is unreachable 2x/week."
```

### BAD: Unspecific Users
```
WRONG: "Users are employees"
RIGHT: "Primary users: Sales Managers (5), secondary: CFO for reports"
```

### BAD: Missing Prioritization
```
WRONG: Long feature list without prioritization
RIGHT: Must-Have (In-Scope) vs Nice-to-Have (Out-of-Scope) separated
```

### BAD: Prescribing Technical Solutions
```
WRONG: "We need a React app with PostgreSQL backend"
RIGHT: "We need a web application with data persistence"
(Technology decisions belong to the Architect!)
```

### BAD: No Measurable Success Metrics
```
WRONG: "Users should be more satisfied"
RIGHT: "NPS should increase from 30 to 50"
```

---

## Handoff Format for Requirements Engineer

```markdown
## 13. Next Steps

COMPLETED: Exploration & Ideation

NEXT STEP: Handoff to Requirements Engineer

**For Requirements Engineer**:
- Create Epics based on Section 9.3 (Key Features)
- Derive User Stories from Section 4 (User) + Section 5 (Needs) + Section 5.4 (Jobs to be Done)
- Structure User Stories by job type (functional/emotional/social)
- Define NFRs based on Section 11.4 (Constraints)
- Use Section 12 (KPIs) for Acceptance Criteria
- Link Critical Hypotheses (Section 7.3) to Features that validate them
- Derive Leading Indicators from Critical Hypotheses
- Include HMW question (Section 8) in Epic context

**Open Questions for RE**:
- [Specific question 1 that RE should clarify]
- [Specific question 2]

**Document Reference**:
- Problem Statement: Section 2
- User Context: Section 4
- Needs/Jobs: Section 5 + 5.4
- Insights: Section 4.3
- Idea Potential: Section 7.1
- Critical Hypotheses: Section 7.3
- Key Features: Section 9.3
- Scope Boundaries: Section 11
- Evaluate: Section 11 (MVP)
```

---

## Quality Score

Rate the BA document before handoff:

| Criterion | Weight | Score |
|-----------|--------|-------|
| Problem clearly defined | 15% | [ ] |
| User identified | 10% | [ ] |
| Needs/Insights (typed, prioritized) | 15% | [ ] |
| Solution idea concrete | 15% | [ ] |
| Scope defined | 10% | [ ] |
| Metrics present | 10% | [ ] |
| Idea Potential (3 axes scored) | 10% | [ ] |
| Critical Hypotheses (with tests) | 10% | [ ] |
| HMW + Value Proposition | 5% | [ ] |

**Minimum score for handoff:**
- Simple Test: 60%
- PoC: 75%
- MVP: 90%

---

## Feedback Loop with User

When critical information is missing:

```markdown
WARNING: The following items are still needed for a complete BA document:

- [ ] [Missing information 1]
- [ ] [Missing information 2]

Can we clarify these points before I hand off to the
Requirements Engineer?
```

---

**Version:** 2.0
**Focus:** Output quality and RE handoff
**Quality Gate:** BA document completeness
