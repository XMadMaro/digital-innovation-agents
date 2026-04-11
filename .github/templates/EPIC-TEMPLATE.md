# EPIC-XXX: [Epic Title]

> **ID:** EPIC-XXX  
> **Scope:** PoC | MVP  
> **Status:** Not Started | In Progress | Done  
> **Priority:** P0-Critical | P1-High | P2-Medium  
> **Created:** YYYY-MM-DD  
> **BA Document:** [Link to Business Analysis Document]

---

## How-Might-We (from BA)

> Carried over from the Exploration Board / BA Section 1.2

**How might we help** {user} **achieve** {need}, **despite** {obstacle}?

---

## Epic Hypothesis Statement (SAFe Format)

> Maps directly from BA deliverables into a testable hypothesis.

**FOR** {target customer -- from HMW "user"}  
**WHO** {have need/problem -- from HMW "need" + "obstacle"}  
**THE** {product/solution -- from BA Value Proposition}  
**IS A** {product category -- from BA High-Level Concept}  
**THAT** {provides key benefit -- from BA Idea Potential "Value"}  
**UNLIKE** {competitive alternative -- from BA Competitor Analysis}  
**OUR SOLUTION** {primary differentiator -- from BA "The Wow" / "Unfair Advantage"}

---

## Business Outcomes (Quantified!)

> CRITICAL: No vague statements! Every outcome must be measurable.

### Primary Outcomes

| Outcome | Baseline (Current) | Target | Timeframe | Measurement Method |
|---------|--------------------|--------|-----------|-------------------|
| [Outcome 1] | [Current value] | [Target value] | [X months] | [How measured] |
| [Outcome 2] | [Current value] | [Target value] | [X months] | [How measured] |
| [Outcome 3] | [Current value] | [Target value] | [X months] | [How measured] |

**Examples of good outcomes:**
- [GOOD] "Conversion rate increases from 12% to 18% (+50%) within 6 months"
- [GOOD] "Support tickets decrease by 40% (from 200/week to 120/week)"
- [BAD] "Improves user experience" (too vague!)

### Leading Indicators

| Indicator | Description | Measurement Cycle | Target Value |
|-----------|-------------|-------------------|-------------|
| [Indicator 1] | [What shows early if we are on track] | [Weekly/Monthly] | [Value] |
| [Indicator 2] | [Early success measure] | [Weekly/Monthly] | [Value] |

---

## Critical Hypotheses (from BA)

> Hypotheses that must be validated before or during epic execution. Traced back to BA deliverables.

| BA Ref | Hypothesis | Validated by Feature | Status |
|--------|-----------|---------------------|--------|
| BA-1.x | [Hypothesis statement] | FEATURE-XXX | Open / Validated / Disproven |
| BA-2.x | [Hypothesis statement] | FEATURE-XXX | Open / Validated / Disproven |
| BA-3.x | [Hypothesis statement] | FEATURE-XXX | Open / Validated / Disproven |

---

## MVP Features

| Feature ID | Name | Priority | Effort | Status | Link |
|------------|------|----------|--------|--------|------|
| FEATURE-001 | [Name] | P0-Critical | M | Not Started | [Link](../features/FEATURE-001-*.md) |
| FEATURE-002 | [Name] | P0-Critical | L | Not Started | [Link](../features/FEATURE-002-*.md) |
| FEATURE-003 | [Name] | P1-High | S | Not Started | [Link](../features/FEATURE-003-*.md) |

**Priority Legend:**
- **P0-Critical:** MVP does not work without this
- **P1-High:** Important for complete user experience
- **P2-Medium:** Adds value but not essential

**Effort Legend:**
- **S:** 1-2 Sprints
- **M:** 3-5 Sprints
- **L:** 6+ Sprints

---

## Explicitly Out-of-Scope

> Clearly define what is NOT part of this epic!

| Feature/Capability | Reasoning | Planned For |
|--------------------|-----------|-------------|
| [Feature X] | [Why out-of-scope] | Phase 2 / Never |
| [Feature Y] | [Why out-of-scope] | Phase 2 / Never |
| [Feature Z] | [Why out-of-scope] | Phase 2 / Never |

---

## Dependencies

### Upstream (Blocks this Epic)

| Dependency | Type | Owner | Status | Impact if Delayed |
|------------|------|-------|--------|-------------------|
| [Dependency 1] | Technical/Business/External | [Team/Person] | Green/Yellow/Red | [Impact] |

### Downstream (Blocked by this Epic)

| Dependent Epic/Feature | Why Blocked |
|------------------------|-------------|
| [Epic/Feature] | [Reasoning] |

---

## Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | H/M/L | H/M/L | [Strategy] |
| [Risk 2] | H/M/L | H/M/L | [Strategy] |
| [Risk 3] | H/M/L | H/M/L | [Strategy] |

---

## Technical Debt (PoC only!)

> CRITICAL: Only relevant for PoC! MVP should not have deliberate tech debt.

| Shortcut | Description | Impact for MVP Conversion | Estimated Cleanup Effort |
|----------|-------------|--------------------------|-------------------------|
| [Shortcut 1] | [What is simplified] | [What must change for MVP] | [X days] |
| [Shortcut 2] | [What is simplified] | [What must change for MVP] | [X days] |

**MVP Conversion Impact:**
- [ ] Low (1-2 weeks cleanup)
- [ ] Medium (1 month refactor)
- [ ] High (2-3 months re-development)

---

## Assumptions

| Assumption | Risk if Wrong | Validation Method |
|------------|---------------|-------------------|
| [Assumption 1] | [Impact] | [How to validate] |
| [Assumption 2] | [Impact] | [How to validate] |

---

## Constraints

### Technical Constraints
- [Constraint 1]: [Description and reasoning]

### Business Constraints
- **Budget:** [Limit]
- **Timeline:** [Deadline]
- **Resources:** [Team availability]

### Compliance/Regulatory
- [Regulation]: [Requirement]

---

## Timeline & Milestones

| Milestone | Target Date | Status | Quality Gate |
|-----------|-------------|--------|--------------|
| Requirements Complete | YYYY-MM-DD | Not Started | QG1 |
| Architecture Complete | YYYY-MM-DD | Not Started | QG2 |
| Feature 1-3 Complete | YYYY-MM-DD | Not Started | QG3 |
| All Features Complete | YYYY-MM-DD | Not Started | QG4 |
| Production Release | YYYY-MM-DD | Not Started | QG5 |

---

## Quality Gate 1 (QG1) - Requirements Complete

**Epic is ready for Architect when:**

- [ ] HMW question present (carried over from BA)
- [ ] Epic Hypothesis Statement complete (all 7 components with BA mapping)
- [ ] Business Outcomes quantified (Baseline -> Target -> Timeframe)
- [ ] Leading Indicators defined
- [ ] Critical Hypotheses documented (with BA references)
- [ ] Min. 3 Features defined and prioritized (P0/P1/P2)
- [ ] All Features exist as separate documents
- [ ] Out-of-Scope explicitly defined
- [ ] Dependencies documented
- [ ] Risks identified
- [ ] Technical Debt documented (PoC only)
- [ ] Filename pattern correct: `EPIC-XXX-descriptive-slug.md`

**When all checks pass:** Handoff to Architect possible!

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Epic created | [Name] |
| YYYY-MM-DD | [Change] | [Name] |

---

## References

- **BA Document:** [Link]
- **Related ADRs:** [Add after Architect phase]
- **arc42 Documentation:** [Add after Architect phase]

---

**Template Version:** 3.0  
**Workflow:** BA -> RE (creates Epic) -> Architect -> Developer  
**Scope:** Only for PoC and MVP (Simple Test has no Epics)
