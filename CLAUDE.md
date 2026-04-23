# Digital Innovation Agents

This is the home of digital-innovation-agents, a V-Model workflow skill set
for AI-augmented innovation and development.

## For agents working on this repository

- See `skills/using-digital-innovation-agents/SKILL.md` for an introduction
  to the skill set and entry points
- See `README.md` for installation and usage across all supported platforms
- Project artifacts from user projects live under `_devprocess/`

## For agents working in a user project that has this plugin installed

- The plugin provides 8 V-Model phase skills plus a bootstrap orientation skill
- `/v-model-workflow` is the orchestrator; `/business-analyse` is the entry
  point when the problem space is unclear
- The workflow is advisory, not enforcing -- respect user opt-outs immediately
- All user-project artifacts belong under `_devprocess/` (not under this
  repo's `skills/` or `docs/`)

See also: `skills/using-digital-innovation-agents/SKILL.md`.

---

## Working conventions for contributors

These apply when you work on THIS repository (the plugin itself). User
projects that install the plugin follow their own rules; see their
CLAUDE.md.

### A. Communication and language

- Conversation language adapting to user messages; commit messages in English with conventional
  prefixes (feat/fix/chore/docs/refactor)
- Private documentation (`_devprocess/`) in German; public documentation
  (README, `docs/`, `ARCHITECTURE.md`) in English
- No emojis, not in code, not in UI, not in communication
- Correct German umlauts: ae, oe, ue, ss if the existing project file uses
  ASCII, otherwise proper Unicode. Consistent per file
- No em dashes (U+2014), no en dashes (U+2013). Use periods, commas,
  parentheses, "and" or "but" instead. Scan every artifact for U+2014 and
  U+2013 before saving, zero hits required
- Apply `/humanizer` rules by default, without being asked:
  - No AI vocabulary (landscape, nuanced, delve, leverage, crucial,
    robust, seamless, holistic, foster, ensuring, highlighting,
    underscoring)
  - No negative parallelisms ("not X but Y")
  - No inflated symbolism, no filler phrases, no meta-signposting
  - Prefer active voice, sentence case in headings
- Technical terms and identifiers stay English even in German text
- Co-Authored-By Claude in every commit

### B. Planning conventions

- Plan mode for every non-trivial task
- Fixed plan structure:
  1. **Context** diagnostic, not descriptive, explains the "why" with
     root cause analysis
  2. **Changes** one subsection per file, with BEFORE/AFTER code blocks
  3. **File summary** table (file | change | risk)
  4. **Not touched** explicit list of files NOT changed (blast radius)
  5. **Verification** acceptance criteria, build always step 1, then
     regression checks
- Split large features into independently deployable phases
- File references always as `src/path/file.ts:LineNN`

### C. Feature lifecycle

Every feature follows this cycle:

```
1. BACKLOG          entry in backlog (Status: Planned)
2. FEATURE-SPEC     write spec BEFORE implementation
3. PLAN             plan mode: create implementation plan
4. IMPLEMENTATION   code, build + deploy after each step
5. SPEC UPDATE      feature spec becomes reference doc
6. BACKLOG UPDATE   immediately after each implementation
```

Step 6 happens immediately, the backlog is always current.

### D. Implementation workflow

- Before every implementation: check reference implementation if one
  exists
- Before every code change: read and understand existing code
- Work incrementally: small steps, each verified
- Build + deploy after EVERY implementation step, not only at the end
- New modules follow the same wiring pattern:
  1. Create file in the appropriate subdirectory
  2. Register in registry/index
  3. Hook into groups/modes
  4. Add metadata entry
- Update memory when architecture fundamentals change

### E. Debugging and error analysis

Document bugs as causal chains, not as symptoms:

```
Problem:    [observable behavior]
Root Cause: [why it happens]
Chain:      step 1 -> step 2 -> ... -> error
```

- Bug IDs with priority: FIX-NN (P0 = immediate, P1 = short term, P2 =
  mid term)
- Security findings: H-N / M-N / L-N (High/Medium/Low)
- File found bugs into the backlog immediately

### F. Documentation standards

- arc42 for architecture (all 12 sections)
- ADRs in MADR format (Context, Decision, Alternatives, Consequences)
- Feature specs as `FEATURE-*.md`:
  - BEFORE implementation: requirements, scope, acceptance criteria
  - AFTER implementation: reference doc with How It Works, Key Files,
    Dependencies
- Backlog is a living document, updated after every implementation
- Documentation is an explicit deliverable in every plan
- **Traceability:** Backlog -> FEATURE-Spec -> ADR -> Plan -> Commit ->
  Backlog-Update

### G. Git and release workflow

- Dual remote: private (origin, all branches) + public (main only)
- Branch flow: `feature/*` -> `dev` -> `main` -> `public/main`
- **Safe merge:** merges into `dev` always via
  `scripts/merge-to-dev.sh <branch>`. Automatic: `dev` -> `dev-backup`
  snapshot, then `feature` -> `dev` (no-ff). Rollback:
  `git checkout dev && git reset --hard dev-backup`
- Two-stage stripping:
  1. `promote-to-test` removes dev tooling (`.claude`, `scripts`,
     `forked-code`)
  2. `sync-public` CI removes internal docs (`_devprocess/`)
- `_devprocess/` as AI-readable knowledge archive
- No active git hook, quality gates via scripts and manual checks

### H. Continuous learning

Claude learns along and stores working patterns, proactively, not only
on request.

**When to update memory:**
- A new architecture pattern has proven itself
- A solution for a recurring problem has been found
- A convention was established or changed
- Project state changed significantly
- A framework specific rule was discovered

**When NOT to save:**
- One-off session-specific details
- Unverified assumptions (verify first)
- Information already in CLAUDE.md or `_devprocess/`

**How to save:**
- `MEMORY.md` only as index, short references, under 200 lines
- Too detailed, write a dedicated reference file and link from
  `MEMORY.md`
- Update existing entries instead of creating new ones
- Actively delete outdated entries
