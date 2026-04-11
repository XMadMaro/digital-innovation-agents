---
name: Requirements Engineer Quality Standards
applyTo: "requirements/epics/**/*.md, requirements/features/**/*.md, requirements/handoff/**/*.md"
description: "Quality rules for Requirements Engineering - Epics and Features"
---

# Requirements Engineer - Quality Standards for Epics & Features

These instructions are **automatically** applied when working with Epic and Feature files. They define the quality standards for the handoff to the Architect.

> **Important:** These rules complement the Requirements Engineer Agent and ensure that all requirements are architect-ready.

---

## Supported File Types

These validation rules apply to:

```
[CHECK] requirements/epics/EPIC-*.md
[CHECK] requirements/features/FEATURE-*.md
[CHECK] requirements/handoff/*.md
```

**NOT supported** (created by the Developer Agent):
```
[X] requirements/issues/ISSUE-*.md       -> Developer Agent
[X] requirements/tasks/TASK-*.md         -> Developer Agent
[X] architecture/adr/ADR-*.md            -> Architect Agent
[X] architecture/arc42/**                -> Architect Agent
```

---

## Quality Goals

### For the Architect
The Architect must be able to **start immediately** with:
- [CHECK] Clearly identified Architecturally Significant Requirements (ASRs)
- [CHECK] Quantified Non-Functional Requirements (NFRs)
- [CHECK] Documented Constraints
- [CHECK] Prioritized Open Questions

### For the Developer Agent
After the Architecture phase, the Developer Agent must have:
- [CHECK] Clear Acceptance Criteria
- [CHECK] Testable Definition of Done
- [CHECK] Understanding of what to build (not how)

---

## Automatic Validations

### 1. File Naming Conventions

**Pattern validation on create/save:**

```javascript
const patterns = {
  epic: /^EPIC-\d{3}-[a-z0-9-]+\.md$/,
  feature: /^FEATURE-\d{3}-[a-z0-9-]+\.md$/
};
```

**Examples:**

```markdown
[CHECK] EPIC-001-customer-portal.md
[CHECK] FEATURE-042-user-authentication.md

[X] epic-001.md                       (missing prefix)
[X] EPIC-1-portal.md                  (number not 3-digit)
[X] EPIC-001-Customer Portal.md       (spaces not allowed)
[X] FEATURE-001-userAuth.md           (camelCase not allowed)
```

---

### 2. Epic-Level Validation (PoC & MVP only)

#### Mandatory Sections for Epics:

```markdown
CHECK on save:

1. [CHECK] Epic Hypothesis Statement present and complete?
2. [CHECK] Business Outcomes quantified? (numbers, metrics)
3. [CHECK] Leading Indicators defined?
4. [CHECK] MVP Features List present? (min. 3 Features)
5. [CHECK] Features prioritized? (P0/P1/P2)
6. [CHECK] Out-of-Scope explicitly defined?
7. [CHECK] Dependencies documented?
8. [CHECK] Risks identified?
9. [CHECK] Technical Debt documented? (PoC only)
10. [CHECK] HMW question present and properly linked to BA?
11. [CHECK] Critical Hypotheses table present with Feature links?
12. [CHECK] Leading Indicators derived from hypotheses?
```

#### Epic Hypothesis Statement - Completeness Check:

```markdown
Mandatory components:

[CHECK] FOR [target customer segment] - specific, not "users"
[CHECK] WHO [have need/problem] - clearly described
[CHECK] THE [product/solution] IS - solution named
[CHECK] A [product category] - categorized
[CHECK] THAT [provides key benefit] - quantified
[CHECK] UNLIKE [alternative] - competition named
[CHECK] OUR SOLUTION [differentiation] - USP clear
```

#### Business Outcomes - Quantification Check:

```markdown
ALLOWED (concrete):
[CHECK] "Conversion rate increases from 12% to 18% (+50%) within 6 months"
[CHECK] "Support tickets decrease by 40% (from 200/week to 120/week)"
[CHECK] "Time-to-market reduced from 8 weeks to 4 weeks (-50%)"

FORBIDDEN (too vague):
[X] "Improves user experience"
[X] "Makes the process faster"
[X] "Increases satisfaction"
```

#### HMW Question Validation:

```markdown
CHECK:
[CHECK] HMW question present in Epic?
[CHECK] HMW properly linked/traced back to BA document?
[CHECK] HMW bridges EXPLORE (problem) to IDEATION (solution)?

FORMAT:
"How might we help [user] to [job], without [pain]?"

EXAMPLE - GOOD:
"HMW: How might we help Sales Managers create pipeline reports
without manually aggregating data from 3 systems?
(Source: BA Section 8, Primary HMW)"

EXAMPLE - BAD:
"How can we make things better?"
```

#### Critical Hypotheses Table Validation:

```markdown
CHECK:
[CHECK] Critical Hypotheses table present?
[CHECK] Each hypothesis linked to validating Feature(s)?
[CHECK] Leading Indicators derived from hypotheses?
[CHECK] Success criteria defined per hypothesis?

FORMAT:
| ID | Hypothesis | Validating Feature | Leading Indicator | Success Criterion |
|----|------------|-------------------|-------------------|-------------------|
| H1 | [assumption] | FEATURE-001 | [metric] | [threshold] |
| H2 | [assumption] | FEATURE-002 | [metric] | [threshold] |

EXAMPLE - GOOD:
| H1 | Sales managers adopt automated reports if <1min generation | FEATURE-001 | Adoption rate week 1-2 | 80% prefer automated |
| H2 | API data consolidated with <5% discrepancy | FEATURE-003 | Reconciliation delta | <5% across 100 records |
```

---

### 3. Feature-Level Validation

#### Mandatory Sections for Features:

```markdown
CHECK on save:

1. [CHECK] Feature Description present? (1-2 paragraphs)
2. [CHECK] Benefits Hypothesis complete?
3. [CHECK] User Stories present? (min. 1-3)
4. [CHECK] Functional Acceptance Criteria testable? (min. 3)
5. [CHECK] Non-Functional Requirements quantified?
6. [CHECK] Architecture Considerations present?
7. [CHECK] ASRs identified and marked? (CRITICAL/MODERATE)
8. [CHECK] Definition of Done complete?
9. [CHECK] Dependencies documented?
10. [CHECK] Out of Scope defined?
11. [CHECK] Jobs to be Done table present (3 job types)?
12. [CHECK] User Stories structured by job type (functional/emotional/social)?
13. [CHECK] Hypothesis Validation section present (if feature validates a hypothesis)?
```

#### Jobs to be Done Table Validation:

```markdown
CHECK:
[CHECK] All 3 job types covered (functional/emotional/social)?
[CHECK] Current solution identified per job?
[CHECK] Desired outcome defined per job?

FORMAT:
| Job Type | Job Statement | Current Solution | Desired Outcome |
|----------|--------------|-----------------|-----------------|
| Functional | When [situation], I want to [action] | [current approach] | [desired state] |
| Emotional | When [situation], I want to feel [emotion] | [current experience] | [desired feeling] |
| Social | When [situation], I want to be perceived as [perception] | [current perception] | [desired perception] |

EXAMPLE - GOOD:
| Functional | When preparing weekly review, I want to pull all pipeline data into one view | Manual Excel from 3 sources (2h) | One-click generation (<5min) |
| Emotional | When presenting to C-suite, I want to feel confident in my numbers | Anxiety about manual errors | Trust in automated accuracy |
| Social | When sharing reports, I want to be seen as data-driven | Perceived as slow/manual | Perceived as analytical leader |
```

#### User Story Format Validation:

```markdown
CHECK each User Story:

[CHECK] "As [role] I want to [goal], so that [benefit]"
[CHECK] Role is specific (not just "user")
[CHECK] Goal is clear and actionable
[CHECK] Benefit is business-oriented
[CHECK] Stories structured by job type (functional/emotional/social)?

FORMAT:
## Functional Stories
"As [role] I want to [functional goal], so that [functional outcome]"

## Emotional Stories
"As [role] I want to [experience], so that I feel [emotion]"

## Social Stories
"As [role] I want to [visible action], so that [perception by others]"

Example - GOOD:
[CHECK] "As a Premium Customer I want to filter my order history,
    so that I can quickly find specific purchases"

Example - BAD:
[X] "As a user I want to see data"
```

#### Hypothesis Validation Section:

```markdown
CHECK (only if feature validates a hypothesis):

[CHECK] Linked hypothesis ID present?
[CHECK] Validation approach described?
[CHECK] Success criteria from hypothesis table referenced?
[CHECK] Measurement method defined?

FORMAT:
### Hypothesis Validation
- **Validates**: H1 -- "[hypothesis text]"
- **Approach**: [how this feature tests the hypothesis]
- **Measurement**: [what metric to track]
- **Success Criterion**: [threshold from hypothesis table]
- **Timeline**: [when to evaluate]
```

#### Acceptance Criteria - Testability Check:

```markdown
ALLOWED (testable):
[CHECK] "API Endpoint GET /api/users returns HTTP 200"
[CHECK] "Response time < 200ms for 95% of requests"
[CHECK] "All user inputs are XSS-sanitized"
[CHECK] "Max 3 clicks to reach target function"

FORBIDDEN (not testable):
[X] "System should be fast"
[X] "Secure system"
[X] "User-friendly interface"
[X] "Good performance"
```

---

### 4. Non-Functional Requirements (NFRs) -- CRITICAL

#### NFR Quantification Validation:

```markdown
MANDATORY CATEGORIES:

1. **Performance**
   [CHECK] Response Time: [X ms for Y% of requests]
   [CHECK] Throughput: [X requests/second]
   [CHECK] Resource Usage: [Max CPU/Memory]

2. **Security**
   [CHECK] Authentication: [OAuth 2.0, JWT, etc.]
   [CHECK] Authorization: [RBAC, ABAC, etc.]
   [CHECK] Encryption: [At Rest: AES-256, In Transit: TLS 1.3]
   [CHECK] Compliance: [GDPR Art. X, SOC2, HIPAA]

3. **Scalability**
   [CHECK] Concurrent Users: [X simultaneous users]
   [CHECK] Data Volume: [Y GB/TB]
   [CHECK] Growth Rate: [Z% per year]

4. **Availability**
   [CHECK] Uptime: [99.9% = ~8.7h downtime/year]
   [CHECK] RTO (Recovery Time): [X minutes]
   [CHECK] RPO (Recovery Point): [X minutes]

5. **Maintainability**
   [CHECK] Code Coverage: [Min. X%]
   [CHECK] Documentation Requirements
   [CHECK] Logging Requirements
```

**Examples - GOOD vs BAD:**

```markdown
[X] BAD (vague):
"System should be fast and scalable with high availability"

[CHECK] GOOD (quantified):
Performance:
  - Response Time: < 200ms for 95% of requests, < 500ms for 99%
  - Throughput: Min. 100 requests/second

Scalability:
  - Support for 10,000 concurrent users
  - Handling of 1TB data volume

Availability:
  - Uptime: 99.9% (max 8.7h downtime/year)
  - RTO: 15 minutes
  - RPO: 5 minutes
```

---

### 5. Architecturally Significant Requirements (ASRs) -- CRITICAL

#### ASR Identification & Marking:

```markdown
CHECK Architecture Considerations Section:

[CHECK] At least 1 ASR identified?
[CHECK] ASRs marked as CRITICAL or MODERATE?
[CHECK] For each ASR: explained WHY it is architecturally relevant?
[CHECK] Quality Attribute assigned? (Performance/Security/etc.)
[CHECK] Impact on architecture described?

ASR Template:
CRITICAL ASR #1: [Description]
- **Why ASR**: [Rationale]
- **Impact**: [Architecture decision required]
- **Quality Attribute**: [Performance/Security/Scalability/etc.]
- **Constraint**: [Technical/Business Constraints]
```

**Examples for ASRs:**

```markdown
[CHECK] GOOD - ASR correctly identified:

CRITICAL ASR: Response Time < 200ms for 95% of requests
- **Why ASR**: Influences fundamental architecture decisions
- **Impact**:
  - Requires caching layer (Redis/Memcached)
  - Requires CDN for static assets
  - Requires load balancing
- **Quality Attribute**: Performance

MODERATE ASR: GDPR Art. 17 (Right to be Forgotten)
- **Why ASR**: Influences data architecture
- **Impact**:
  - Soft delete pattern required
  - Data retention policies
- **Quality Attribute**: Security/Compliance

[X] BAD - Not an ASR, just an NFR:

"Code Coverage > 80%"
-> This is an NFR, but NOT an ASR (does not influence architecture)
```

---

### 6. Definition of Done Completeness Check

```markdown
CHECK Definition of Done:

[CHECK] All Functional Acceptance Criteria as checkboxes?
[CHECK] NFR validation included?
[CHECK] Testing Requirements defined?
   - Unit Tests (Coverage %)
   - Integration Tests
   - Performance Tests (if relevant)
   - Security Tests
[CHECK] Review Gates defined?
   - Architecture Review
   - Code Review
   - UAT
[CHECK] Documentation Requirements?

Minimum DoD:
- [ ] All Functional Acceptance Criteria met
- [ ] All NFRs validated
- [ ] Unit Tests (Coverage > [X%])
- [ ] Integration Tests passed
- [ ] Security Scan passed
- [ ] Architecture Review completed
- [ ] Code Review completed
- [ ] Documentation updated
- [ ] Deployed to Staging
- [ ] UAT passed
```

---

### 7. Architect Handoff Document Validation

#### Mandatory Sections for Architect Handoff:

```markdown
CHECK requirements/handoff/architect-handoff.md:

1. [CHECK] Executive Summary present?
2. [CHECK] Requirements Package complete?
3. [CHECK] ASRs Section present?
4. [CHECK] NFR Summary Table present?
5. [CHECK] Context & Integration Section?
6. [CHECK] Technology Stack Recommendations?
7. [CHECK] Constraints documented?
8. [CHECK] Open Questions Section?
9. [CHECK] Next Steps for Architect defined?
10. [CHECK] Traceability Matrix present?
11. [CHECK] Success Criteria defined?
```

---

## Quality Gate: Architect-Ready Check

**A Feature/Epic is Architect-Ready when:**

### Epic-Level (PoC/MVP):
```
[CHECK] Hypothesis Statement complete (7/7 components)
[CHECK] Business Outcomes quantified (Baseline, Target, Timeframe)
[CHECK] Leading Indicators defined
[CHECK] Features prioritized (P0/P1/P2)
[CHECK] Out-of-Scope explicitly defined
[CHECK] Dependencies documented
[CHECK] Technical Debt documented (PoC only)
[CHECK] HMW question present and linked to BA
[CHECK] Critical Hypotheses table present with Feature links
[CHECK] Leading Indicators derived from hypotheses
```

### Feature-Level:
```
[CHECK] Benefits Hypothesis clear
[CHECK] User Stories complete (As/want/so that)
[CHECK] User Stories structured by job type (functional/emotional/social)
[CHECK] Jobs to be Done table present (3 job types)
[CHECK] Acceptance Criteria testable (pass/fail)
[CHECK] NFRs quantified (ALL with numbers!)
[CHECK] ASRs identified and marked (CRITICAL/MODERATE)
[CHECK] Architecture Impact described
[CHECK] Definition of Done complete
[CHECK] Dependencies documented
[CHECK] Out of Scope defined
[CHECK] Hypothesis Validation section present (if validates a hypothesis)
```

### Handoff-Level:
```
[CHECK] All Epics/Features linked
[CHECK] All ASRs listed in handoff document
[CHECK] NFR Summary Table present
[CHECK] Open Questions prioritized
[CHECK] Constraints documented
[CHECK] Traceability Matrix present
[CHECK] Success Criteria defined
```

**When ALL checks pass:**
```
ARCHITECT-READY!

Status: All validations passed
Next: Handoff to Architect Agent

The Architect can now:
  1. Review ASRs
  2. Create ADRs
  3. Start ARC42 Documentation
  4. Make Technology Stack Decisions
```

---

## Feedback Loops

### With Business Analyst

```markdown
Feedback Types to BA:

1. **MISSING_CRITICAL_INFO**
   -> Example: "User Personas not defined"

2. **UNCLEAR_SCOPE**
   -> Example: "In-Scope vs Out-of-Scope unclear"

3. **MISSING_BUSINESS_OUTCOMES**
   -> Example: "No measurable Business Outcomes"

4. **MISSING_HMW**
   -> "No How-Might-We question in BA document.
      Required for Epic context and EXPLORE-to-IDEATION bridge.
      Please add HMW question to BA Section 8."

5. **MISSING_HYPOTHESES**
   -> "No critical hypotheses identified in BA document.
      Required for hypothesis-driven Feature validation.
      Please add Critical Hypotheses to BA Section 7.3."

6. **MISSING_JOBS**
   -> "Jobs to be Done not defined in BA document.
      Required for structuring User Stories by job type.
      Please add JTBD (functional/emotional/social) to BA Section 5.4."
```

### With Architect

```markdown
Feedback Types from Architect:

1. **REQUIREMENTS_UNCLEAR**
   -> Clarify affected feature

2. **NEED_ADDITIONAL_NFR**
   -> Add missing NFR with numbers

3. **ASR_NOT_CLEAR**
   -> Better explain WHY it is an ASR
```

---

## Summary

These instructions ensure:

[CHECK] **Epic Quality** - Complete business context for Architect
[CHECK] **Feature Quality** - Testable Acceptance Criteria, quantified NFRs
[CHECK] **ASR Identification** - Architect knows which requirements are critical
[CHECK] **NFR Quantification** - No vague statements, only numbers
[CHECK] **Handoff Completeness** - Architect has all information
[CHECK] **Traceability** - Every requirement linked to business goal
[CHECK] **HMW Linkage** - EXPLORE-to-IDEATION bridge maintained
[CHECK] **Hypothesis Validation** - Features linked to testable hypotheses
[CHECK] **Jobs to be Done** - User Stories structured by job type

**Goal:** Architect can **immediately** start with ADRs and ARC42, without asking back!

---

**Version:** 5.0 (Updated for innovation-driven requirements)
**Focus:** Epics & Features only (no Issues/Tasks)
**Quality Gate:** Architect-Ready Validation
