# Two-Remote Setup: digital-innovation-agents-dev und digital-innovation-agents

## Konzept

| Remote | Repo | Sichtbarkeit | Inhalt |
|--------|------|--------------|--------|
| `origin` | `github.com/pssah4/digital-innovation-agents-dev` | Privat | Alle Branches, inklusive `main` mit `_devprocess/`, `CLAUDE.md`, `scripts/` |
| `public` | `github.com/pssah4/digital-innovation-agents` | Oeffentlich | Nur `main`, gespiegelt von `origin/main` ohne interne Dateien |

**Was nie in public landet:**

- `CLAUDE.md`
- `_devprocess/` (V-Model Artefakte, AI-lesbares Wissensarchiv)
- `scripts/` (Helper-Skripte und diese Doku)
- `.github/` ausser `deploy-docs.yml` (GitHub Pages bleibt im public)

**Was gitignored ist und in keinem Remote landet:**

- `backup/`, `spike/`, `node_modules/`, `.DS_Store`
- `.claude/settings*.json`
- `docs/.vitepress/cache/` und `docs/.vitepress/dist/`
- `__pycache__/` und `*.pyc`

## Automatischer Sync via GitHub Actions

**Trigger:** Jeder Push auf `origin/main` (inklusive Merges via Pull Request).

**Workflow:** `.github/workflows/sync-public.yml`

Ablauf:

1. Checkout `origin/main`
2. `deploy-docs.yml` zwischenspeichern
3. `_devprocess/`, `.github/`, `scripts/`, `CLAUDE.md` aus dem Index und vom Filesystem entfernen
4. `deploy-docs.yml` wieder hinzufuegen
5. Gefilterten State committen
6. Force-Push zu `public/main`

## Einmaliges Setup

Bereits eingerichtet (Stand 2026-05-06):

- Privates dev-Repo `pssah4/digital-innovation-agents-dev`
- PAT mit `repo` Scope
- Secret `DIA_PUBLIC_TOKEN` im dev-Repo

Falls der PAT abgelaufen ist:

1. https://github.com/settings/tokens
2. Tab "Tokens (classic)", **Generate new token (classic)**
3. Note `dia public sync`, Expiration nach Bedarf, Scope `repo`
4. https://github.com/pssah4/digital-innovation-agents-dev/settings/secrets/actions
5. Secret `DIA_PUBLIC_TOKEN` aktualisieren

## Workflow fuer taegliche Arbeit

```
Feature entwickeln (feature/xyz)
        |
        v
   git push origin feature/xyz   landet nur im dev-Repo
        |
        v
PR auf GitHub: feature/xyz -> main im dev-Repo
        |
        v
   Merge
        |
        v (automatisch)
GitHub Actions: sync-public.yml
        |
        v
public/main aktuell, ohne interne Dateien
```

## Lokale Remote-Konfiguration

```bash
git remote -v
# enbw    https://github.com/EnBWAG/skill-registry.digital-innovation-agents.git (fetch/push)
# origin  https://github.com/pssah4/digital-innovation-agents-dev.git (fetch/push)
# public  https://github.com/pssah4/digital-innovation-agents.git (fetch/push)
```

`public` als Remote dient nur dem manuellen Fallback. Der regulaere Sync laeuft via GitHub Actions.

## Manueller Fallback

Falls Actions ausfallen oder ein Hotfix noetig ist, kann der gefilterte State manuell gepusht werden:

```bash
# 1. Auf einen tempraeren Branch, der spaeter weggeworfen wird
git checkout -b tmp-public-sync main

# 2. Interne Pfade entfernen
cp .github/workflows/deploy-docs.yml /tmp/deploy-docs.yml
git rm -rf .github _devprocess scripts CLAUDE.md
mkdir -p .github/workflows
cp /tmp/deploy-docs.yml .github/workflows/deploy-docs.yml
git add .github/workflows/deploy-docs.yml
git commit -m "chore: strip internal files for public mirror"

# 3. Force-Push zu public/main
git push public HEAD:main --force

# 4. Zurueck und tempraeren Branch loeschen
git checkout main
git branch -D tmp-public-sync
```

## Troubleshooting

**Actions-Workflow schlaegt fehl mit "Permission denied":**

- PAT abgelaufen oder ohne `repo` Scope, neu erstellen und Secret aktualisieren

**`CLAUDE.md` erscheint im public Repo:**

- Pruefen ob Workflow-Run in Actions-Tab erfolgreich war
- Sicherstellen, dass `CLAUDE.md` in `origin/main` getrackt ist (`git ls-files CLAUDE.md`)

**public hat anderen Inhalt als `origin/main`:**

- Erwartet: public hat einen extra Commit "chore: strip internal files for public mirror"
- Commit-History unterscheidet sich leicht zwischen dev und public, das ist akzeptabel

## GitHub Pages

GitHub Pages laeuft auf `pssah4/digital-innovation-agents`:

- Branch: `main`, Workflow `deploy-docs.yml`
- URL: `https://pssah4.github.io/digital-innovation-agents`

`deploy-docs.yml` bleibt im public Repo, weil GitHub Pages den Workflow dort braucht. Im dev-Repo ist die Datei ebenfalls vorhanden, dort hat sie keinen Effekt (kein Pages-Setup).
