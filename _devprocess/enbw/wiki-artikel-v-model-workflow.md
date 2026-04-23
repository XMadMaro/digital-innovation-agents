Kernidee

Ein Set spezialisierter Skills (Digital Innovation Agents) begleitet das
Mensch-Agent-Team durch einen V-Model-Zyklus mit den Phasen Business
Analysis, Requirements Engineering, Architektur, Coding, Testing,
Security-Audit und Release-Closure. Zwischen den Phasen liegen
Quality-Gates. Alle Artefakte (BA, Epics, Features, ADRs, arc42,
Backlog, Handoffs) sind Markdown-Dateien im Repository und werden von
jeder Phase zurückgeschrieben. Ergebnis ist ein Dokumentationsgraph,
der mit dem Code synchron bleibt, und eine durchgängige Traceability
von der Hypothese in der BA bis zum Commit.



1. Problem

AI-Coding-Assistenten sind schnell im Code-Produzieren. Sie sind nicht
von selbst gut darin, das richtige Problem zu treffen. Beobachtungen
aus AI-gestützten Projekten:

Features werden implementiert, bevor der Nutzungskontext geklärt ist.
Der Code ist sauber, das Feature geht am Nutzer vorbei.

Requirements, Architektur-Entscheidungen und Code driften auseinander,
weil die Dokumente nach dem Go-Live nicht gepflegt werden.

Jede neue AI-Session beginnt ohne Kontext. Die Modelle haben kein
Gedächtnis für Projektentscheidungen. Teams wiederholen denselben
Kontext mehrfach.

Die Grenze zwischen "neues Feature", "Improvement" und "Bugfix" verschwimmt.
Der Backlog wird zum unstrukturierten Sammelbecken.

Security, Tests und Compliance werden erst am Ende bearbeitet statt
innerhalb des Arbeitsflusses.

Der V-Model-Workflow der Digital Innovation Agents greift an genau
diesen Punkten. Er führt jedes Projekt durch dieselben Quality-Gates,
hält den Artefakt-Graphen im Repository und macht die
Prozessdokumentation zu einem Nebenprodukt der Entwicklung statt zu
einer separaten Aufgabe.



2. Kontext

Wo das Pattern eingesetzt wird:

Alle Innovations- und Produkt-Initiativen der Agentic Factory, die mit
AI-Coding-Assistenten arbeiten.

Brownfield-Übernahmen bestehender Codebases ohne V-Model-Artefakte.

Greenfield-Prototypen vom ersten "Simple Test" bis zum MVP.

Rahmenbedingungen:

Das Skill-Set ist plattformagnostisch. Claude Code, Cursor, Codex,
OpenCode, Gemini CLI und GitHub Copilot werden aus einer gemeinsamen
Quelle bedient. Keine Bindung an einen LLM-Anbieter, eine IDE oder eine
CLI.

Alle Artefakte sind Markdown im Repository (docs/ oder _devprocess/).
Kein zusätzliches PM-Tool, keine externe Datenbank.

Der Workflow ist beratend, nicht bindend. Der Nutzer kann jederzeit
aussteigen, einzelne Phasen überspringen oder das Plugin deaktivieren.

Scope-Adaption: Simple Test (Stunden), Proof of Concept (Tage), MVP
(Wochen). Die Skills passen Tiefe und Pflichtsektionen an den Scope an.

Constraints, die wir in der Adaption für EnBW CoWork gewählt haben:

Brownfield-Einstieg. CoWork hatte bei Einführung des Workflows bereits
36 ADRs und eine v3.3.0-Codebase. Das Team startete mit
/reverse-engineering, nicht mit /business-analyse.

Dialog-Sprache Deutsch, Skill-Instruktionen Englisch. Die Skills
erkennen die Nutzersprache und antworten entsprechend.

Trade-offs:

Struktur kostet Zeit. Jede Phase hat ein Quality-Gate, Handoffs werden
geloggt. Dafür entfällt spätere Archäologie nach Entscheidungen.

Artefakte bleiben im Repo. Nutzer ohne Markdown-Affinität brauchen
einen Renderer (VitePress, GitHub Pages).

Der Workflow kann überdimensioniert sein. Für einen 4-Stunden-Fix
passt Scope "Simple Test", nicht der volle MVP-Pfad.



3. Lösung (Kurz)

Neun Skills, ein Artefakt-Graph im Repository, definierte
Phasenübergänge mit Quality-Gates und eine Orchestrator-Rolle, die das
Team durch den V führt.

Komponenten:

Orchestrator-Skill /v-model-workflow. Führt durch alle Phasen, ruft
die Phasen-Skills auf, prüft Handoffs, kann jederzeit vom Nutzer
pausiert werden.

Zwei Einstiegspunkte:
/business-analyse für Greenfield (leere Codebase, unklare
Problemstellung).
/reverse-engineering für Brownfield (bestehender Code, keine
V-Model-Artefakte).

Phasen-Skills (aufgerufen durch den Orchestrator oder standalone):
/business-analyse (Exploration, Ideation, Validation)
/requirements-engineering (Epics, Features, Success Criteria)
/architecture (ADRs in MADR, arc42, plan-context.md)
/coding (Plan-Coverage-Gate, Critical Review, Artefakt-Writeback)
/testing (Unit und Integration mit Fix-Loop)
/security-audit (OWASP, LLM Top 10, SAST, SCA, Zero Trust)
Release-Closure als Phase 7

Querschnitts-Skills:
/project-conventions (Verzeichnisstruktur, Naming, Sprache)
/consistency-check (Graph-Health, tote Links, Orphans)

Artefakt-Graph im Repository unter _devprocess/ oder docs/:
analysis/BA-*.md, Security-Audits
requirements/epics/EPIC-*.md, requirements/features/FEATURE-*.md
architecture/ADR-*.md, arc42.md
context/10_backlog.md (Single Source of Truth), 20_bugs.md,
30_handoffs.md, 40_metrics.md
implementation/plans/PLAN-*.md

Interaktion:

BA (Warum?)
  -> Epic (Was, strategisch?)
    -> Feature (Was, konkret?)
      -> ASR (Architektur-relevant?)
        -> ADR (Wie lösen wir das?)
          -> plan-context.md (Kontext-Brücke)
            -> PLAN-NNN (Welche Tasks, in welcher Reihenfolge?)
              -> Code (Commits zitieren PLAN-NNN)
                -> Tests -> Security-Audit
                  -> Backlog -> Release-Closure

Jede Phase liest die Eingabeartefakte, produziert neue Artefakte,
schreibt in den Backlog zurück und loggt einen Handoff. Der
Default-Agent im AI-Tool übernimmt die Umsetzung. Die Skills liefern
Kontext, Review und Writeback.



4. Schritt-für-Schritt

Der Durchlauf am Beispiel einer neuen Capability in CoWork (zum
Beispiel eine MCP-Integration oder ein neuer Skill).

A) Schritt 1: Workflow installieren und starten

1. Plugin installieren

In Claude Code (empfohlen wegen vollständiger Skill-Unterstützung):

/plugin marketplace add pssah4/digital-innovation-agents
/plugin install digital-innovation-agents@pssah4-skills

Für andere Tools (Cursor, Copilot, Codex, OpenCode, Gemini CLI) siehe
README.md Abschnitt "Quick start".

2. Projekt-Setup verifizieren

Im Projekt-Repository prüfen, dass die Verzeichnisstruktur existiert:

ls _devprocess/ || mkdir -p _devprocess/{analysis/security,\
requirements/{epics,features,handoff},architecture,\
implementation/plans,context}

CoWork nutzt docs/ statt _devprocess/. Der Orchestrator erkennt die
Wurzel automatisch.

3. Orchestrator aufrufen

/v-model-workflow

Der Orchestrator führt einen hybriden Entry-Point-Scan durch:

Er sucht nach vorhandenen Artefakten (BA, Features, ADRs).

Er ruft /consistency-check im syntaktischen Modus auf.

Er empfiehlt den passenden Einstiegspunkt und zeigt alle Alternativen
als AskUserQuestion-Optionen.

B) Schritt 2: Brownfield-Einstieg mit Reverse Engineering (falls Code bereits existiert)

Bei Greenfield entfällt dieser Schritt. Bei CoWork war er der
Projektstart unter dem V-Model.

1. /reverse-engineering aufrufen

Der Skill walkt den V rückwärts: vom bestehenden Code hoch zur
Business-Analyse. Jede Aussage wird mit Source: path:LineNN oder
Doc-Abschnitt belegt. Aussagen ohne Beleg werden nicht aufgenommen.

2. Quellen-Sweep

Der Skill liest readme.md, package.json, CHANGELOG.md,
docs/FEATURES.md, src/main/index.ts Startup-Sequenz und vorhandene
ADRs. Bei CoWork waren das 36 ADRs, 16 Feature-Kategorien und 9
UML-Diagramme.

3. Artefakt-Erzeugung

Der Skill produziert:

plan-context.md (Tech-Stack-Snapshot)

arc42.md (9 von 12 Sektionen evidenz-gestützt, 3 als [AWAITING BA]
gekennzeichnet)

FEATURE-NNN-*.md mit Status Observed (not validated)

BA-{PROJECT}.md als Draft, mit [NEEDS USER INPUT]-Platzhaltern wo Code
die Frage nicht beantwortet

Backlog-Seed in context/10_backlog.md

4. Evidenz-Abdeckung dokumentieren

Der Handoff-Eintrag in context/30_handoffs.md listet, wie viele
Sektionen belegt sind und wo die Lücken liegen. Für CoWork wurden 7
von 15 BA-Sektionen direkt evidenz-gestützt, 8 blieben als Platzhalter.

C) Schritt 3: Business Analysis validieren

1. /business-analyse im Validation-Mode starten

Der Skill erkennt den Draft-Status und wechselt in den Validation-Mode.
Er geht jede Sektion mit dem Nutzer durch: Problem Statement,
How-Might-We, Value Proposition, Personas, Stakeholder-Map,
Jobs-to-be-Done, kritische Hypothesen.

2. Methoden-Vorschläge bei dünnen Antworten

Wenn die Antworten des Nutzers dünn bleiben, stoppt der Skill das
Interview und bietet aus einem Katalog von 32 Innovationsmethoden eine
passende Methode an (qualitative Interviews, Extreme Users, Fly on the
Wall, Cultural Probes, Persona-Synthese, Jobs to be Done, Pre-Mortem,
Wizard of Oz). Jede Methode kommt mit einer Ein-Seiten-Karte: Was sie
produziert, wann sie passt, wie lange sie dauert, was schiefgehen kann.

3. Status-Promotion

Ist jede Sektion validiert, setzt der Skill den Frontmatter-Status von
Draft auf Validated. Der BA-Status erscheint im Backlog-Dashboard.

D) Schritt 4: Requirements formalisieren

1. /requirements-engineering aufrufen

Der Skill liest die validierte BA, leitet Epics ab (strategische
Gruppierung), fragt Epic für Epic nach und erzeugt Features mit
tech-agnostischen Success Criteria.

2. Tech-agnostische Regel

Kein OAuth, REST, PostgreSQL, React in den Success Criteria. Die
Technik-Entscheidungen gehören in einen separaten "Technical
NFRs"-Block und werden später in den ADRs getroffen. CoWork hat
aktuell 12 Epics und 39 Features in diesem Format.

3. Architect-Handoff schreiben

Der Skill erzeugt requirements/handoff/architect-handoff.md mit einer
Zusammenfassung aller ASRs (Architecture-Significant Requirements),
Qualitätsziele und offenen Fragen für die Architektur-Phase.

E) Schritt 5: Architektur dokumentieren

1. /architecture aufrufen

Der Skill liest den Architect-Handoff und schlägt ADRs im MADR-Format
vor (Context, Decision, Alternatives, Consequences) sowie die
betroffenen arc42-Sektionen.

2. ADR-Proposals, nicht Dekrete

ADRs sind zunächst Proposals. Der Nutzer prüft sie gegen die reale
Codebase und akzeptiert oder modifiziert. Die Entscheidung trifft der
Mensch. CoWork hat so 57 ADRs angesammelt, von der
Electron-Framework-Wahl bis Advisor-Self-Dispatch.

3. plan-context.md aktualisieren

Die Datei requirements/handoff/plan-context.md ist die Kontext-Brücke
zum Coding. Sie fasst Tech-Stack, relevante ADRs, Feature-Liste und
Dialog-Sektion zusammen. Der Coding-Agent liest sie als erstes.

F) Schritt 6: Implementieren mit Plan-Coverage-Gate

1. /coding aufrufen

Der Skill läuft in sechs Phasen:

Context Load. Liest plan-context.md, alle relevanten ADRs und
Feature-Specs.

Critical Review. Gleicht Proposals mit der Codebase ab. Wenn ADRs nicht
passen, wird abgebrochen oder angepasst.

PLAN-NNN erzeugen. Persistierter Implementierungsplan unter
implementation/plans/PLAN-NNN-{slug}.md. Der Plan ist die Single Source
of Truth für die Umsetzung.

Default-Agent-Handoff. Der Coding-Skill beauftragt den Default-Agent
(die normale Claude-Code-Session) mit der Umsetzung: Task-Breakdown,
optional TDD, Debugging-Protokoll.

Verification Gate. Vor jeder "fertig"-Meldung prüft der Skill Build,
Typecheck, Tests.

Final Synchronization. Feature-Specs, ADRs, Backlog, plan-context.md
und PLAN werden zurückgeschrieben. Der Status wandert auf Implemented.

2. Artefakt-Triage am Eingang

Bevor Code geschrieben wird, entscheidet der Skill: neues Feature,
Improvement (IMP), Fix (FIX) oder ADR. FIX und IMP brauchen zwingend
feature: und epic: im Frontmatter. CoWork hat aktuell 33 Improvements
und 7 Fixes so kategorisiert.

3. Mid-course-Trigger

Entdeckt der Coding-Flow einen Bug, eine falsche
Architektur-Entscheidung oder eine Lücke im Feature-Spec, pausiert er,
schreibt eine Root-Cause-Analyse und einen Backlog-Eintrag, bevor der
Code weitergeht. Der Graph bleibt konsistent.

G) Schritt 7: Testen

1. /testing aufrufen

Der Skill erkennt das Test-Framework (bei CoWork: Vitest + Playwright)
und erzeugt Unit- und Integrationstests für neue Features nach
AAA-Pattern und FIRST-Prinzipien.

2. Fix-Loop bei roten Tests

Wenn Tests fehlschlagen, läuft ein Fix-Loop mit Nutzer-Approval. Der
Skill fixt, testet erneut und fragt bei unklaren Erwartungen nach.

H) Schritt 8: Security Audit

1. /security-audit aufrufen

Nur für formale Vollaudits mit Report (AUDIT-{PROJECT}-{DATE}.md).
Für Code-Review pro PR gibt es den leichtgewichtigeren
/security-review-Skill.

2. Scope des Audits

SAST (Static Application Security Testing)

OWASP Top 10

OWASP LLM Top 10 (relevant für AI-Produkte wie CoWork)

SCA (Dependency-Analyse, CVEs)

Zero-Trust-Validierung

Code-Quality-Sicht

3. Prioritized Findings

Findings werden als H-N / M-N / L-N (High/Medium/Low) erfasst und mit
einem Remediation-Plan versehen. Bei CoWork dient der Audit-Bericht
AUDIT-enbw-cowork-2026-04-12.md als Grundlage für IMP-006
(CI-Security-Scan-Gate).

I) Schritt 9: Release-Closure

1. Phase 7 im Orchestrator

Nach dem Security-Fix-Loop ruft der Orchestrator die Release-Closure
auf. Sie synchronisiert alle Artefakte ein letztes Mal.

2. Aufgaben

BA-Validation-Sektion mit realen Zahlen aktualisieren

Feature-Status finalisieren (Implemented / Deferred / Removed)

ADR-Status setzen (Accepted / Accepted (modified) / Deprecated)

arc42-Sektionen auf aktuellen Stand bringen

Release Notes und CHANGELOG-Eintrag erzeugen, semver-Bump wählen

Backlog aufräumen, offene Items in die nächste Iteration

Post-Release-BA-Review als Handoff-Eintrag release-to-ba queuen, damit
die kritischen Hypothesen nach echter Nutzung gegen Daten validiert
werden.

3. Abschlussbericht an den Nutzer

Der Skill gibt einen strukturierten Closing-Report aus: Features, Bugs,
Security, Tests, Artefakte, Empfehlung für die nächste Iteration.



5. Architektur-Skizze / Diagramme

V-Model-Übersicht:

BUSINESS ANALYSIS ------------------------------> RELEASE CLOSURE
        |                                              ^
        v                                              |
REQUIREMENTS ENGINEERING ---------------------> SECURITY AUDIT
        |                                              ^
        v                                              |
ARCHITECTURE (ADRs, arc42) ----------------------> TESTING
        |                                              ^
        v                                              |
        +------------------> CODING -------------------+
                  (plan-context.md + PLAN-NNN)

Offizielle Grafik: V-Model Overview

Artefakt-Graph (vereinfacht):

BA-{PROJECT}.md
  -> EPIC-NNN-{slug}.md
      -> FEATURE-NNN-{slug}.md -> ASR
          -> ADR-NNN-{slug}.md (MADR)
              -> arc42.md (Section updates)
                  -> plan-context.md
                      -> PLAN-NNN-{slug}.md
                          -> Code + Commits
                              -> Tests
                                  -> AUDIT-{PROJECT}-{DATE}.md
                                      -> Backlog updates
                                          -> Release Notes

Kontroll-Fluss pro Phase (Handoff-Ritual):

Phase-Skill liest Input-Artefakte
  -> Artefakt-Triage (Feature / IMP / FIX / ADR)
      -> Phase-spezifische Arbeit
          -> Quality Gate prüfen
              -> Writeback in Backlog
                  -> Handoff-Eintrag in 30_handoffs.md
                      -> Nächste Phase vorschlagen



6. Risiken & Gegenmaßnahmen

Overhead bei Mini-Änderungen. Ein 30-Minuten-Bugfix braucht keinen
vollen V-Model-Durchlauf. Gegenmaßnahme: Scope "Simple Test" wählen
oder direkt mit /coding in der Artefakt-Triage als FIX starten. Der
Orchestrator kann übersprungen werden.

Dokumentations-Drift bei Zeitdruck. Wenn Teams Code pushen ohne
Feature-Spec, ADR oder Backlog-Update, driftet der Graph.
Gegenmaßnahme: /consistency-check vor jedem Release laufen lassen
(syntaktisch am Phasenende, semantisch vor Release). CoWork nutzt
IMP-006 (CI-Security-Scan-Gate) in Kombination mit einem Graph-Check.

Skill-Ergebnisse ohne Prüfung übernommen. ADRs sind Proposals. Wenn
sie ungeprüft akzeptiert werden, driftet die Architektur von der
Codebase weg. Gegenmaßnahme: /coding führt vor jedem PLAN-Commit
einen Critical Review gegen die Codebase. Der Nutzer bestätigt oder
ändert.

Mehrere Human-Agent-Paare arbeiten parallel am selben Backlog-Item.
Zwei Sessions schreiben in dieselbe Datei, Merge-Konflikt.
Gegenmaßnahme: Claim-Spalte im Backlog ({pair-id} @ {YYYY-MM-DD}). Der
Skill setzt den Claim bei Phasenstart und gibt ihn bei Done frei. Stale
Claims werden im nächsten Handoff-Ritual gemeldet.

LLM-Halluzination bei Reverse Engineering. Der Skill erfindet
Inferenzen, die im Code nicht belegt sind. Gegenmaßnahme: Jede Aussage
bekommt eine Source:-Zeile mit Dateipfad und Zeile oder Doc-Abschnitt.
Aussagen ohne Source gelten als Draft und landen als [NEEDS USER
INPUT]-Platzhalter in der BA.

Plattform-Lock-in bei Adoption. Ein Team trainiert sich auf Claude
Code, wechselt dann zu Cursor oder Copilot. Gegenmaßnahme: Das
Skill-Set hat eine gemeinsame Quelle und Installer für alle sechs
unterstützten Plattformen. Artefakte bleiben Markdown im Repo,
plattformunabhängig.

Nutzer wollen aus dem Workflow aussteigen. Jemand hat eine schnelle
Frage und will nicht durch die Business-Analyse. Gegenmaßnahme: Der
Workflow ist beratend. Stop, Exit, unrelated question: der Skill hält
sofort an, ohne nachzufragen. Der Status bleibt in _devprocess/ oder
docs/ erhalten und wird beim nächsten Aufruf aufgenommen.

Sprach- und Stil-Drift. CoWork ist deutsch, die Skills sind intern
englisch. Gegenmaßnahme: Skill-Dialog passt sich der Nutzersprache an.
Interne Artefakte folgen der Artefakt-Sprache des Chats; bei Unklarheit
fragt der Skill nach.



7. Referenzen / Beispiele

Die Links verweisen auf das externe GitHub-Repository. Sobald das Repo
auf eine EnBW-Umgebung umgezogen ist, werden die Links aktualisiert.
Die Rohdateien liegen zusätzlich im Sharepoint unter "V-Model
Workflow".

Digital Innovation Agents (das Skill-Set)

Repository: github.com/pssah4/digital-innovation-agents

Dokumentation: pssah4.github.io/digital-innovation-agents

Einstieg Greenfield: /business-analyse

Einstieg Brownfield: /reverse-engineering

Orchestrator: /v-model-workflow

Skill-Overview: README.md

Konkrete Skills und ihre Artefakte

Business Analysis Skill

Requirements Engineering Skill

Architecture Skill

Coding Skill

Testing Skill

Security Audit Skill

Consistency Check Skill

Reverse Engineering Skill

V-Model Workflow Orchestrator

Project Conventions

Beispiele aus EnBW CoWork

Stand 2026-04-21:

12 Epics, 39 Features, 57 ADRs, 33 Improvements, 7 Fixes

36 ADRs bereits bei Projekt-Onboarding vorhanden und durch Reverse
Engineering in den Graphen integriert

arc42 mit 9 von 12 Sektionen evidenz-gestützt, Rest als [AWAITING
BA]-Platzhalter

BA v2 nach Team-Review 2026-04-16 konsolidiert, Pathfinder-Kontext als
Scope-Anker dokumentiert

Security-Audit AUDIT-enbw-cowork-2026-04-12.md als Grundlage für
CI-Security-Gate

Konkrete Beispiel-Artefakte:

BA CoWork (Projekt-BA Level, lesbar ohne Epic-Detail-Kenntnis)

arc42 Snapshot (Reverse-engineert, 9/12 Sektionen belegt)

ADR-056 Advisor-Self-Dispatch, ADR-057 Advisor-Pair-Mapping (beide
Proposed, Beispiel für einen laufenden Architektur-Zyklus)

Backlog-Dashboard: 13 P0-Items, 18 P1, 29 P2, 11 P3

Learnings aus dem CoWork-Projekt

Was funktioniert hat:

Reverse Engineering als Brownfield-Einstieg. Die 36 ADRs waren bereits
MADR-formatiert und konnten direkt übernommen und mit Features
verknüpft werden. Ohne diesen Reverse-Walk hätte jedes neue
Team-Mitglied den Kontext manuell erklärt bekommen müssen.

Trennung Feature / Improvement / Fix. Drift-Fixes (Beispiel: FIX-007
ADR 012/013/014 Drift) liegen getrennt von Improvements (IMP-006
CI-Security-Scan-Gate) und neuen Features. Das Backlog-Dashboard bleibt
damit lesbar.

Handoff-Log als append-only Protokoll. Jede Phase schreibt einen
Eintrag in 30_handoffs.md. Der Log beginnt am 14.04.2026 mit
/reverse-engineering -> /business-analyse und dokumentiert seitdem
jeden Phasenwechsel. Neue Team-Mitglieder können sich in 20 Minuten
einlesen.

Plan-Coverage-Gate im Coding-Skill. Vor jedem "Feature fertig" prüft
der Skill, ob jedes Acceptance-Criterion durch eine PLAN-Task abgedeckt
ist. In drei Fällen hat das einen Gap sichtbar gemacht, der sonst erst
im Test aufgefallen wäre.

Dialog-Sektion in Handoff-Dokumenten. Fragen zwischen zwei Phasen
werden zuerst aus Artefakten selbstbeantwortet. Erst wenn das
scheitert, geht die Frage an den Nutzer. Spart pro Session Rückfragen.

Was Aufmerksamkeit braucht:

Living Documents kosten Disziplin. Wenn Teams vergessen, den Backlog
nach einer Implementation zu aktualisieren, driftet der Stand.
Gegenmaßnahme in CoWork: der Coding-Skill schreibt selbst in den
Backlog, kein manueller Schritt.

Scope-Selbsteinschätzung ist schwer. "Simple Test" klingt klein,
wächst aber schnell zum PoC. Das CoWork-Team bewertet den Scope
inzwischen nach 2-3 Sessions neu.

Multi-Provider-Realität. CoWork läuft in der Entwicklung auf Claude
Code, Produktiv-Szenarien laufen gegen Bedrock, Anthropic, OpenAI,
Gemini und Ollama. Der Workflow ist plattformagnostisch, das Testing
muss aber alle Provider abdecken (siehe FIX-006
Bedrock-SDK-Dependency).

Interne Anlaufstellen

Agentic Factory: CoWork-Team für Hands-on-Fragen und
Onboarding-Sessions

Repo-Beispiel CoWork: github.com/EnBWAG/enbw-cowork.enbw-open-cowork

Skill-Set intern: ~/.claude/plugins/digital-innovation-agents (nach
Install)

Slack/Teams: (hier den internen Kanal ergänzen, sobald festgelegt)

Screenshots und weiterführende Assets

Die Doku-Site (VitePress) enthält Tutorials, Method-Cards und
Reference-Pages:

First Business Analysis Tutorial

Full V-Model Run

Reverse Engineering Guide

Method Catalog: Discovery, Ideation, Validation
