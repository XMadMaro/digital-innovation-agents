# FAQ: Skills und V-Model-Workflow

Kurzantworten zu typischen Fragen rund um das Digital-Innovation-Agents-Plugin.

## 1. Was ist der Dokumentations-/Artefakt-Graph?

Kein Git-Artefakt, keine Conventional Commits. Der Graph ist eine **semantische Sicht auf die Markdown-Artefakte** des V-Model-Sets, on-demand aus den Source-Dateien geparst.

- **Knoten:** BA-Sektionen, Epics, Features, Success Criteria, ADRs, arc42-Sektionen, PLANs, Backlog-Items, Code-Files
- **Kanten:** Referenzen in YAML-Frontmatter und Markdown-Links (z. B. Feature `epic:` → Epic, Feature `related-adrs:` → ADRs, Feature `source:` → Code-Pfad, arc42 §9 → ADRs)
- **Invarianten:** N-1..N-7 (Nodes), E-1..E-9 (Edges), S-1..S-4 (Semantic), definiert in `skills/project-conventions/references/graph-invariants.md`
- **Parser:** `skills/v-model-workflow/tools/parse-graph.py` (Python-stdlib, kein Persist auf Disk)
- **Viewer:** Cytoscape.js-HTML mit Lenses (Übersicht, Persona, Phase, Health, Epic-Fokus)

**Zweck:** Integrität (Dead Links, Orphans, Missing Success Criteria), Navigation in Meetings, Gate beim Phasenübergang via `consistency-check`.

## 2. Wie funktioniert Traceability?

Kein externes Tracing-Tool. Traceability ist ein **geschlossener Markdown-Graph im Repo**, erzwungen durch Invarianten und Frontmatter.

**Kette (CLAUDE.md §F):** `BA → Epic → Feature → ADR → PLAN → Commit → Backlog-Update`

**Mechanik:**
- Pflicht-Frontmatter-Felder: `epic:`, `feature:`, `depends-on: [...]`
- Backlog (`docs/context/10_backlog.md`) ist **Single Source of Traceability**, jede Entität hat genau eine Row
- `coding`-Skill aktualisiert per **Continuous Writeback** bei Implementierung
- Commit-Messages enthalten FEATURE-/ADR-/PLAN-IDs, rückwärts rekonstruierbar via `git log --grep`

**Session ↔ Feature-Korrelation:** Über die FEATURE-ID im PLAN (`_devprocess/implementation/plans/PLAN-*.md`, Frontmatter `feature:`, `status: Active`). Eine Session = ein PLAN. Agent-Logs werden **nicht** ins Repo geschrieben.

## 3. Behandelt der Coding-Block auch Infrastruktur und Ops?

**Coding-Skill:** Feature-Spec → Code. Infrastruktur läuft **als ADR**, nicht als separater Block. Terraform, K8s, CI-Dateien referenzieren ihr Feature genauso wie App-Code.

**Ops-Automatisierung, Self-Healing, MCP auf App Insights, Nexus/Sonar:** Nicht im Default-Skill-Set. Zwei Wege:
1. **Eigene Skills schreiben** (z. B. `ops-self-healing` mit MCP-Tools). Das Plugin-Layout unterstützt beliebige Custom-Skills.
2. **MCP-Server direkt verdrahten.** Claude Code spricht MCP nativ. Nexus, Sonar, App Insights wären jeweils eigene MCPs.

**Security:** Der `security-audit`-Skill deckt SCA, OWASP Top 10, OWASP LLM Top 10 ab. Fachlich überlappt er mit Sonar/Nexus, läuft aber als One-Shot-Audit, nicht als kontinuierliche Pipeline.

## 4. Wo liegen Coding-Rules, wenn es nur Skills gibt?

Es gibt mehrere Layer, die Claude Code bei jedem Start lädt:

- **Global user** unter `~/.claude/CLAUDE.md`: Arbeitsweise über alle Projekte hinweg (Sprache, Git, Dokumentation).
- **Project** unter `<repo>/CLAUDE.md`: projekt-spezifische Regeln, in den Repo eingecheckt und damit für alle Contributor sichtbar.
- **Memory** unter `~/.claude/projects/<slug>/memory/MEMORY.md` plus einzelne Referenz-Dateien: Auto-Memory, persistent über Sessions hinweg.
- **Skills** unter `skills/<skill>/SKILL.md` plus `references/`: phasen-spezifische Workflows (Business Analysis, Requirements, Architecture usw.).
- **References** unter `skills/project-conventions/references/*.md`: **hier liegen die Coding-Rules**, u. a. `directory-structure.md`, `naming-conventions.md`, `codebase-awareness.md`, `graph-invariants.md`.

Keine GitHub-Copilot-`instructions/`-Datei, kein `.cursor-rules`. Stattdessen **CLAUDE.md (global + project) + Skill-SKILL.md + referenzierte Markdown-Files**.

## 5. Hooks für deterministische Prüfungen, Pre-Commit, Agnostik?

Ja, aber heute minimal. Zwei Ebenen:

**a) Claude-Code-Hooks** (`hooks/hooks.json`):
```json
{
  "hooks": {
    "SessionStart": [
      { "matcher": "startup|clear|compact",
        "hooks": [{ "type": "command",
                    "command": "run-hook.cmd session-start",
                    "async": false }] }
    ]
  }
}
```
Aktuell nur `SessionStart`. Verfügbare Events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`. Damit lassen sich deterministische Checks (z. B. Graph-Check nach jedem Edit) als Shell-Scripts verdrahten, ohne LLM-Call.

**b) Git-Hooks:** CLAUDE.md §G sagt explizit: **kein aktiver Git-Hook**. Pre-Commit-Logik läuft über Shell-Scripts (`scripts/merge-to-dev.sh`, `promote-to-test`, `sync-public`-CI). Grund: Hook-Bypasses und Cross-OS-Probleme. Quality Gates greifen stattdessen in CI, im `release`-Skill und im `consistency-check` am Phasenende.

**Agnostisch aufsetzbar?** Ja. `hooks.json` ist Claude-Code-Standard, Cursor hat eine parallele Form (`hooks/hooks-cursor.json`). Shell-Scripts und Invarianten-Files sind reines Markdown/Shell/Python-stdlib. Für ein härteres Gate wäre ein Pre-Commit-Hook mit `consistency-check --fix` in zehn Zeilen nachrüstbar. Bewusste Entscheidung gegen einen aktiven Hook, weil Artefakt-Drift während Refactorings temporär gewollt ist.

---

**TL;DR:** Der V-Model-Workflow hier ist datei-basiert und Markdown-getrieben. Traceability lebt im Repo, nicht in einem externen Tool. Der Graph ist eine virtuelle Sicht auf die Referenzen. Ops und Self-Healing wären Custom-Skills. Coding-Rules sitzen in `CLAUDE.md` und `project-conventions/references/`. Hooks sind heute minimal, aber das Gerüst steht.
