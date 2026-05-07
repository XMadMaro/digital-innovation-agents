# Digital Innovation Agents

This is the home of digital-innovation-agents, a V-Model workflow skill set
for AI-augmented innovation and development.

## For agents working on this repository

- See `skills/dia-bootstrap/SKILL.md` for an introduction
  to the skill set and entry points
- See `README.md` for installation and usage across all supported platforms
- Project artifacts from user projects live under `_devprocess/`

## For agents working in a user project that has this plugin installed

- The plugin provides 8 V-Model phase skills, a bootstrap orientation
  skill, plus `/dia-migration` for upgrading legacy or brownfield repos
- `/dia-guide` is the guide; `/business-analysis` is the
  entry point when the problem space is unclear; `/dia-migration` is the
  entry point for an inherited repo that needs to come up to v2 conventions
- The workflow is advisory, not enforcing, respect user opt-outs immediately
- All user-project artifacts belong under `_devprocess/` (not under this
  repo's `skills/` or `docs/`)

See also: `skills/dia-bootstrap/SKILL.md`.

## Three-layer documentation model (drift-resistance refactor, 2026-04-30)

The V-Model artifacts in user projects live in three layers, each with a
different cadence and a different owner. Mixing layers is the dominant
source of doc-vs-code drift, so the boundaries are binding.

| Layer            | Purpose                                                                                                         | Lives in                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Wayfinder        | Concept-to-file lookup, navigational, grep-friendly                                                             | `src/ARCHITECTURE.map`, JSDoc headers in entry-point files, module READMEs                                        |
| Rule sets        | Stable truths: stack, conventions, design rules, domain glossary. Hard cap 500 lines total.                      | `_devprocess/rules/technical.md`, `design.md`, `domain.md`                                                        |
| Backlog          | Single source of truth for state and the artifact relation graph                                                 | `_devprocess/context/BACKLOG.md`                                                                               |
| Detail artifacts | Audit trail of the engineering process: BA, Epics, Features, Plans, Fixes, ADR detail                            | `_devprocess/analysis/`, `_devprocess/requirements/`, `_devprocess/architecture/`, `_devprocess/implementation/`  |

**Status, phase, last-change, and claim of every artifact live in the
backlog row, not in the artifact frontmatter.** Artifact frontmatter
carries identity (id, title, created) and relations (epic, adr-refs,
feature-refs) only.

**ADR abstraction rule:** ADR core sections (Context, Decision Drivers,
Considered Options, Decision, Consequences) contain NO code paths,
file names, line numbers, or method signatures. Code-level hints belong
in the optional `## Implementation Notes` appendix at the bottom, which
is allowed to go stale. The wayfinder is the canonical source for
current paths.

**ADR/FEATURE/PLAN separation:**

- **ADR** answers "what is the architectural decision and why?". No
  tasks, no code paths in core sections.
- **FEATURE** answers "what should the user be able to do?". No tasks,
  no implementation details.
- **PLAN** answers "how is it concretely implemented?". Tasks with
  file paths and verify commands live HERE and only here.

See `skills/project-conventions/SKILL.md` for the complete model.

## Workflow activation contract (added 2026-05-07)

User projects activate the plugin via `/dia-setup`. The skill writes
`.dia/config.toml` with one of three modes (`off`, `git-only`,
`github-sync`) and manages an anchor block in agent-facing files
(CLAUDE.md, AGENTS.md, GEMINI.md, .cursorrules,
.github/copilot-instructions.md, .windsurfrules).

Phase skills and `flow.py` read the mode and adapt:

- `off`: skills are advisory only, hooks are silent, flow.py is
  a no-op everywhere.
- `git-only`: skills run, local hooks active, flow.py manages
  phase tags only. No GitHub issue or project sync.
- `github-sync`: full integration. flow.py runs `create-issue`,
  `open-draft-pr`, `sync-status`, `promote-to-epic`,
  `validate-fix` and mirrors backlog state to GitHub.

This plugin repo runs `mode = "off"` (see `.dia/config.toml`). The
plugin is not applied to itself; we develop the skills here.

## BACKLOG status vocabulary (added 2026-05-07)

Status values are GitHub-aligned: `Backlog`, `Ready`, `In Progress`,
`In Review`, `Done`. Existing user projects migrate via
`tools/migration/migrate_status_vocabulary.py`, which maps the
legacy DIA values:

```
Planned   -> Ready
Active    -> In Progress
Review    -> In Review
Waiting   -> Backlog
Deferred  -> Backlog
```

`Done` stays `Done`.

## Hotfix lane (added 2026-05-07)

`/coding` allows a fast path for trivial bug fixes: max 3 files,
no breaking change, fits an existing FEAT, under 15 minutes. The
fix runs first; the FIX-Row, detail file, commit, and (in
`github-sync`) GitHub issue follow right after. Mandatory closing
step: `flow.py validate-fix --item FIX-EE-FF-NN`. Anti-misuse
signal: directions meeting flags hotfix share over 30%.

## Phase tag rename (added 2026-05-07)

The security phase tag is `<id>/sec-done`, set with
`flow.py tag-phase --phase sec`. Legacy `audit-done` is still
accepted as an alias.

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
1. BACKLOG          entry in backlog (Status: Ready)
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

- Bug IDs with priority: FIX-NN-NN-NN (P0 = immediate, P1 = short term, P2 =
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
