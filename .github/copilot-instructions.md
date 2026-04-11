# GitHub Copilot - Global Instructions

> **Auto-loaded:** These instructions are automatically loaded with every Copilot request and complement the specialized agents/chatmodes.

ALWAYS CHECK WHICH CHATMODE IS ACTIVE FIRST! Follow the instructions of the active chatmode.

## Available Agents

### 1. **@business-analyst** - Innovation & Discovery

Structured EXPLORATION/IDEATION/VALIDATION cycle from raw project idea to complete Business Analysis document.

**Input:** Raw project idea or problem description
**Output:** `_devprocess/analysis/BA-{PROJECT}.md`, `_devprocess/analysis/EXPLORE-{PROJECT}.md`
**Handoff to:** @requirements-engineer

**Phases:**
- Scope Detection (Simple Test / PoC / MVP)
- EXPLORE: User research, needs (functional/emotional/social), insights, trends, competitors, touchpoints, How-Might-We synthesis
- IDEATION: Solution idea, idea potential (3 axes), the Wow, jobs to be done, critical hypotheses, value proposition
- EVALUATE: VP score, assessment radar, pricing, channels, unfair advantage, revenue stream (PoC/MVP only)

**Probing Techniques:** 5-Why, concretization, future projection, perspective shift, emotional probing, analogy triggers. See `innovation-methods.md` for full method reference.

---

### 2. **@requirements-engineer** - Requirements Structuring

Transforms Business Analysis into structured Epics, Features, and ASRs (Architecture-Significant Requirements).

**Input:** Business Analysis document (with HMW, needs, jobs to be done, critical hypotheses)
**Output:**
- `_devprocess/requirements/epics/*.md` - Strategic initiatives
- `_devprocess/requirements/features/*.md` - Functional capabilities
- `_devprocess/requirements/handoff/architect-handoff.md` - Handoff document

**Handoff to:** @architect

**Key transformations:**
- HMW question -> Epic Hypothesis Statement
- Needs + Jobs to be Done -> User Stories (functional/emotional/social)
- Critical Hypotheses -> Feature Validation criteria
- Idea Potential -> Feature Prioritization

**Quality Gate 1 (QG1) - Requirements Ready:**
- All Epics with HMW reference and quantified Business Outcomes
- Features with Jobs to be Done and Benefits Hypothesis
- NFRs fully documented and quantified
- ASRs explicitly marked (CRITICAL/MODERATE)
- Critical Hypotheses tracked with feature links
- Architect handoff document complete

---

### 3. **@architect** - Technical Architecture Design

Creates technical architecture, ADRs, arc42 documentation, and developer-ready issues.

**Input:** `_devprocess/requirements/handoff/architect-handoff.md`
**Output:**
- `_devprocess/architecture/decisions/*.md` - Architecture Decision Records (MADR)
- `_devprocess/architecture/arc42/*.md` - arc42 documentation
- Mermaid diagrams (C4 Model, sequence diagrams)
- `_devprocess/architecture/plan-context.md` - Context handoff for coding

**Handoff to:** @developer

**Quality Gate 2 (QG2) - Architecture Ready:**
- ADRs for all architecturally relevant decisions
- arc42 documentation (scope-adjusted)
- Technology stack defined
- System design with diagrams
- plan-context.md complete

**Complexity Scaling:**
- **Simple Test:** Minimal ADRs, no arc42, direct implementation
- **PoC:** Basic ADRs, reduced arc42, focused scope
- **MVP:** Full ADRs, comprehensive arc42, detailed design

---

### 4. **@developer** - Test-Driven Implementation

Implements atomic tasks with mandatory testing and automatic error logging.

**Input:** plan-context.md + ADRs + Features
**Output:**
- Production code with tests
- Test execution reports
- Updated artifacts (features, ADRs reflect what was actually built)

**If tests fail -> Auto-handoff to:** @debugger

**Quality Gate 3 (QG3) - Development Ready:**
- ALL tests must pass (or error log created)
- Code coverage >= 90%
- Clean code principles applied
- No TODOs or placeholders
- Artifacts updated to reflect actual implementation

**Core Principles:**
- Write tests AS you code (not after)
- Execute full canonical test suite (MANDATORY)
- Quality over speed
- No over-engineering
- Living documents: write changes back to artifacts during implementation

---

### 5. **@debugger** - Systematic Error Resolution

Analyzes error logs, identifies root causes, implements clean fixes.

**Input:** Error logs from @developer
**Output:**
- Fixed code with updated tests
- Complete test suite validation
- Resolution documentation in error log

**Returns to:** @developer (after fix validation)

**Quality Gate Debug (QGD):**
- Root cause identified (not just symptoms)
- Clean fix implemented (no workarounds)
- Tests updated/added
- ALL tests pass (entire suite)
- No regressions introduced
- Fix documented with learnings

---

## Complete Workflow

```
Phase 0: Innovation & Discovery
  @business-analyst
  - EXPLORE: Users, needs, insights, trends, competitors
  - IDEATION: Solution idea, idea potential, hypotheses, value proposition
  - EVALUATE: VP score, assessment radar, pricing, channels, revenue
  - Output: BA-{PROJECT}.md + EXPLORE-{PROJECT}.md
                     |
                     | Handoff (HMW, needs, JTBD, hypotheses)
                     v
Phase 1: Requirements Engineering
  @requirements-engineer
  - HMW -> Epic Hypothesis Statement
  - Needs + JTBD -> User Stories (functional/emotional/social)
  - Critical Hypotheses -> Feature Validation
  - Output: Epics, Features, architect-handoff.md
                     |
                     | QG1: Requirements Ready?
                     v
Phase 2: Architecture Design
  @architect
  - ADRs, arc42, system design, plan-context.md
                     |
                     | QG2: Architecture Ready?
                     v
Phase 3: Implementation
  @developer
  - Load context from plan-context.md
  - Implement with tests
  - Write changes back to artifacts
                     |
                     | QG3: All Tests Pass?
                     |-- YES -> Production Ready
                     |-- NO  -> @debugger -> fix -> return to @developer
```

---

## Quality Gates Summary

| Gate | Owner | Key Criteria | Blocks |
|------|-------|-------------|--------|
| **QG1** | @requirements-engineer | Epics with HMW, Features with JTBD, ASRs marked, Hypotheses tracked | Architecture Phase |
| **QG2** | @architect | ADRs created, arc42 done, plan-context.md complete | Development Phase |
| **QG3** | @developer | All tests pass, coverage >= 90%, artifacts updated | Production |
| **QGD** | @debugger | Root cause fixed, all tests pass, no regressions | Return to Development |

---

## Agent Selection Guide

**Start with @business-analyst when:**
- You have a rough idea or problem to solve
- Starting a new project from scratch
- Need to explore and structure requirements
- Want innovation methods (EXPLORATION/IDEATION/VALIDATION)

**Start with @requirements-engineer when:**
- You already have a Business Analysis document
- You have clear requirements but need structuring
- You want to skip discovery and go straight to Epics/Features

**Start with @architect when:**
- You have complete requirements and need technical design
- You have `architect-handoff.md` ready
- You need ADRs, arc42 docs, or system design

**Start with @developer when:**
- Architecture is complete and you are ready to code
- You have plan-context.md and feature specs
- You want to implement with test-driven approach

**Use @debugger when:**
- Tests are failing after implementation
- You have error logs from @developer
- You need systematic root cause analysis
