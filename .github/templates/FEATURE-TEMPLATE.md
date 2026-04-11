# FEATURE-XXX: [Feature Title]

> **Epic:** [EPIC-XXX](../epics/EPIC-XXX-*.md) - [Epic Name] *(PoC/MVP only)*  
> **ID:** FEATURE-XXX  
> **Priority:** P0-Critical | P1-High | P2-Medium  
> **Effort:** S (1-2 Sprints) | M (3-5 Sprints) | L (6+ Sprints)  
> **Status:** Not Started | In Progress | Done  
> **Created:** YYYY-MM-DD  

---

## Feature Description

[1-2 paragraphs: What is the feature and why is it needed? Make the business context clear.]

---

## Benefits Hypothesis

**We believe that** [description of the feature]  
**will deliver the following measurable outcomes:**
- [Outcome 1 with metric]
- [Outcome 2 with metric]

**We know we are successful when:**
- [Success metric 1 with concrete target value]
- [Success metric 2 with concrete target value]

---

## Jobs to be Done (from BA)

> Reference: BA Section 5.4

| Job Type | Job | Addressed in Story |
|----------|-----|--------------------|
| Functional | [What the user wants to accomplish] | Story 1 |
| Emotional | [How the user wants to feel] | Story 2 |
| Social | [How the user wants to be perceived] | Story 3 |

---

## User Stories

### Story 1: {Name} (Functional Job)

**As a** [specific user role -- not just "user"]  
**I want to** [concrete functionality]  
**so that I can accomplish** {functional job}

**Example Scenario:**
> [Concrete example of how the user uses this functionality]

### Story 2: {Name} (Emotional Job)

**As a** [user role]  
**I want to** [functionality]  
**so that I experience** {desired feeling}

### Story 3: {Name} (Social Job)

**As a** [user role]  
**I want to** [functionality]  
**so that I am perceived as** {perception}

---

## Functional Acceptance Criteria

> CRITICAL: Every criterion must be testable! Pass/fail must be unambiguous.

**This feature is functionally complete when:**

- [ ] **AC1:** [Concrete and testable]
  - Verification: [How is this tested?]
  
- [ ] **AC2:** [Concrete and testable]
  - Verification: [How is this tested?]
  
- [ ] **AC3:** [Concrete and testable]
  - Verification: [How is this tested?]
  
- [ ] **AC4:** [Concrete and testable]
  - Verification: [How is this tested?]
  
- [ ] **AC5:** [Concrete and testable]
  - Verification: [How is this tested?]

**Examples:**
- [GOOD] "API endpoint GET /api/users returns HTTP 200 and JSON array"
- [GOOD] "Login with invalid credentials shows error message within 500ms"
- [BAD] "System should be fast" (not testable!)
- [BAD] "User-friendly interface" (not testable!)

---

## Gherkin Scenarios

### Scenario 1: [Happy Path]

```gherkin
Feature: [Feature Name]

Scenario: [Descriptive name -- successful case]
  Given [Precondition with concrete values]
  And [Further precondition]
  When [User action with concrete values]
  And [Further action if needed]
  Then [Expected result with concrete values]
  And [Further expected results]
  And [State changes/side effects]
```

### Scenario 2: [Error Case]

```gherkin
Scenario: [Descriptive name -- error case]
  Given [Precondition]
  And [Error condition that leads to failure]
  When [User action]
  Then [Expected error handling]
  And [No unwanted side effects]
```

### Scenario 3: [Edge Case]

```gherkin
Scenario: [Descriptive name -- edge case]
  Given [Boundary condition]
  When [Action]
  Then [Expected behavior at boundary]
```

---

## Non-Functional Requirements (NFRs)

> CRITICAL for Architect! All NFRs must be quantified -- no vague statements!

### Performance

| Requirement | Target | Measurement Method |
|-------------|--------|-------------------|
| Response Time | < [X] ms for [Y]% of requests | [Tool/Method] |
| Throughput | [X] requests/second | Load Test |
| Resource Usage | Max [X] MB RAM, [Y] CPU cores | Monitoring |

### Security

| Requirement | Specification | Compliance |
|-------------|---------------|------------|
| Authentication | [OAuth 2.0 / JWT / Session] | [Standard] |
| Authorization | [RBAC / ABAC] with roles: [X, Y, Z] | [Standard] |
| Encryption at Rest | [AES-256] | [GDPR Art. X] |
| Encryption in Transit | [TLS 1.3] | [Standard] |
| Input Validation | [XSS, SQL Injection Prevention] | OWASP |

### Scalability

| Requirement | Target | Growth |
|-------------|--------|--------|
| Concurrent Users | [X] simultaneous users | +[Y]% per year |
| Data Volume | [X] GB/TB | +[Y] GB/month |
| Horizontal Scaling | [Yes/No] - [Strategy] | - |

### Availability

| Requirement | Target | Meaning |
|-------------|--------|---------|
| Uptime | [99.9]% | Max [8.7h] downtime/year |
| RTO (Recovery Time) | [X] minutes | Max time to recovery |
| RPO (Recovery Point) | [X] minutes | Max data loss |

### Maintainability

| Requirement | Target |
|-------------|--------|
| Code Coverage | Min. [X]% |
| Documentation | [API Docs, Inline Comments] |
| Logging | [Structured Logging, Log Levels] |

---

## Architecture Considerations (for Architect)

### Architecturally Significant Requirements (ASRs)

> ASRs are NFRs that influence fundamental architecture decisions.

#### CRITICAL ASRs (Must address in Architecture)

**ASR #1:** [Description -- e.g. "Response Time < 200ms for 95% of requests"]
- **Why ASR:** [Reasoning why architecture-relevant]
- **Quality Attribute:** [Performance / Security / Scalability / Availability]
- **Architectural Impact:** [Which decisions are influenced?]
  - Requires: [e.g. Caching layer, CDN, Load Balancing]
- **Constraint:** [Technical/Business constraints]
- **Recommendation:** [If available]

**ASR #2:** [Description]
- **Why ASR:** [Reasoning]
- **Quality Attribute:** [Attribute]
- **Architectural Impact:** [Impact]
- **Constraint:** [Constraint]

#### MODERATE ASRs (Should address in Architecture)

**ASR #3:** [Description]
- **Why ASR:** [Reasoning]
- **Quality Attribute:** [Attribute]
- **Architectural Impact:** [Impact]

### Context & Boundaries

**Interacting Systems:**
- [System A]: [Type of interaction]
- [System B]: [Type of interaction]

**Integration Points:**
- [API/Message Queue/Database]

**Data Flow:**
```
[User] -> [Frontend] -> [API Gateway] -> [Service] -> [Database]
                                      -> [External API]
```

### Constraints (for Architect)

**Technical:**
- [Constraint 1]: [Reasoning]

**Platform:**
- [Cloud Provider / On-Premise]

**Compliance:**
- [GDPR / HIPAA / SOC2 / PCI-DSS]

### Open Questions for Architect

> Questions the Architect must answer/decide.

**High Priority (blocking):**
- [?] [Technical decision the Architect must make]
- [?] [Architecture pattern question]

**Medium Priority (non-blocking):**
- [?] [Integration strategy question]
- [?] [Optional optimization]

---

## Definition of Done

**Functional:**
- [ ] All Functional Acceptance Criteria fulfilled
- [ ] All Gherkin Scenarios pass

**Quality:**
- [ ] All NFRs validated
- [ ] Unit tests written (Coverage > [X]%)
- [ ] Integration tests passed
- [ ] Performance tests passed (if relevant)
- [ ] Security scan passed

**Process:**
- [ ] Architecture Review completed (QG2)
- [ ] Code Review completed
- [ ] API documentation updated
- [ ] Deployed to Staging
- [ ] UAT passed

---

## Hypothesis Validation (if applicable)

> Only fill in if this feature validates a critical hypothesis from the Epic.

| Hypothesis (BA Ref) | Test Method | Success Criterion | Result |
|---------------------|-------------|-------------------|--------|
| [BA-X.X: Hypothesis] | [How tested] | [What counts as success] | Pending / Validated / Disproven |

**If disproven:** {pivot plan}

---

## Dependencies

### Blocked By (Must be completed first)

| Dependency | Type | Status | Impact if Delayed |
|------------|------|--------|-------------------|
| [FEATURE-XXX](./FEATURE-XXX-*.md) | Feature | Not Started / In Progress / Done | [Impact] |
| [External System] | External | Green/Yellow/Red | [Impact] |

### Blocks (Waiting on this Feature)

| Dependent Feature | Why Blocked |
|-------------------|-------------|
| [FEATURE-XXX](./FEATURE-XXX-*.md) | [Reasoning] |

---

## Out of Scope

> Explicitly what is NOT part of this feature (commonly confused).

| Feature/Capability | Reasoning | Where Addressed |
|--------------------|-----------|-----------------|
| [Capability X] | [Why not here] | [FEATURE-XXX / Phase 2 / Never] |
| [Capability Y] | [Why not here] | [Where instead] |

---

## Assumptions

| Assumption | Risk if Wrong | Validation Method |
|------------|---------------|-------------------|
| [Technical assumption] | [Impact] | [How to validate] |
| [Business assumption] | [Impact] | [How to validate] |
| [Data assumption] | [Impact] | [How to validate] |

---

## Quality Gate 1 (QG1) - Feature Ready for Architect

**Feature is ready for Architect when:**

- [ ] Feature Description clear (business context)
- [ ] Benefits Hypothesis with measurable outcomes
- [ ] Jobs to be Done referenced (from BA Section 5.4)
- [ ] Min. 1-3 User Stories (As a/I want to/so that) structured by job type
- [ ] Min. 3-5 testable Acceptance Criteria
- [ ] Min. 2-3 Gherkin Scenarios (Happy Path + Error)
- [ ] NFRs quantified (ALL with numbers!)
  - [ ] Performance (Response Time, Throughput)
  - [ ] Security (specific: OAuth, TLS, etc.)
  - [ ] Scalability (Concurrent Users, Data Volume)
  - [ ] Availability (Uptime %, RTO, RPO)
- [ ] ASRs identified and marked (CRITICAL/MODERATE)
- [ ] Architectural Impact described
- [ ] Hypothesis Validation section filled in (if this feature validates a critical hypothesis)
- [ ] Definition of Done complete
- [ ] Dependencies documented
- [ ] Out of Scope defined
- [ ] Filename pattern: `FEATURE-XXX-descriptive-slug.md`

**When all checks pass:** Feature can be included in Architect handoff!

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Feature created | [Name] |

---

## References

- **Epic:** [Link] *(PoC/MVP only)*
- **BA Document:** [Link]
- **Related ADRs:** [Add after Architect phase]

---

**Template Version:** 3.0  
**Workflow:** BA -> RE (creates Feature) -> Architect -> Developer  
**Created by:** Requirements Engineer
