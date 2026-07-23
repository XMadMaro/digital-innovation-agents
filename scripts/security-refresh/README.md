# scripts/security-refresh/

D3 of the security-audit rework: the **auto-refresh** that keeps the
bundled threat checklists current without manual editing. A scheduled
GitHub Actions job regenerates the OWASP/CWE/LLM checklists from official
sources, verifies them adversarially, and only commits (with a version
bump) when a fail-closed gate passes.

This directory is dev-internal tooling. `sync-public.yml` strips
`scripts/` and `.github/` from the public mirror, so the refresh
machinery never ships to installers. Only the regenerated
`skills/security-audit/references/*.md` and the version bump propagate.

## Why a version bump is mandatory

A Claude Code plugin pinned to a `version` string in `plugin.json` does
NOT propagate new commits to installed copies until that string changes
(the marketplace sees "same version" and keeps the cache). So the refresh
MUST bump the patch version, or nothing reaches any project. `bump_version.py`
does that, moving `plugin.json` and `marketplace.json` together.

## The pipeline (fail-closed at every step)

```
refresh_references.py refresh   model regenerates candidates (web_search
                                restricted to official domains only)
        |
refresh_references.py verify    adversarial 2nd pass: re-fetches official
                                sources itself, assumes each change is
                                hallucinated until proven, writes verdict
        |
verify_refresh.py               deterministic gate: known-good survive,
                                known-bad absent, no truncation, verdict OK
        |  (only if BOTH pass)
bump_version.py                 patch bump in both manifests
        |
git commit + push (develop)     auto-commit with source-cited message
```

Any failure (model error, unverifiable change, dropped core category,
known-bad string, empty file, missing API key) aborts before the commit.
A refresh that cannot be verified never lands.

## Files

| File | Role |
|------|------|
| `refresh_references.py` | `refresh` (model writes candidates) + `verify` (adversarial re-fetch verdict). anthropic SDK; fails closed if SDK/key absent. |
| `verify_refresh.py` | Deterministic fixture gate + combines the adversarial verdict. Exit 1 = roll back. |
| `bump_version.py` | Patch-bump `plugin.json` + `marketplace.json` consistently. |
| `currency_fixtures.json` | known-good (must survive) / known-bad (must never appear) regression seed. |
| `tests/` | Assertion-based tests for the gate and the bump. |

## Model and source policy

- Model: `claude-opus-4-8`, adaptive thinking.
- Web search restricted to `owasp.org`, `genai.owasp.org`, `cwe.mitre.org`,
  `nvd.nist.gov`, `github.com` (advisories), `osv.dev`. Anything cited
  outside these is rejected by the verifier.
- The fixture list is a **regression net, not a novelty gate**: genuinely
  new categories are admitted via official-source citation, not blocked
  for being absent from known-good. Grow known-good/known-bad over time as
  the verifier confirms/catches entries.

## One-time setup (required before the schedule does anything)

1. **API key secret.** In the GitHub repo: Settings -> Secrets and
   variables -> Actions -> New repository secret named `ANTHROPIC_API_KEY`.
   Without it, the refresh step fails closed (no commit).

2. **Marketplace auto-update (on your machine).** Third-party marketplaces
   have auto-update OFF by default. Turn it on so the version-bumped
   refresh reaches your projects without a manual `/plugin update`:
   run `/plugin` -> Marketplaces -> `pssah4-skills` -> enable auto-update.
   Claude Code then pulls the new version ~10 min after session start; you
   confirm with `/reload-plugins` (or it loads on next launch).

3. **The last mile (develop -> main) stays manual, by design.** The
   workflow pushes to `develop`, honouring the repo's `feature -> develop
   -> main` flow and the "never auto-commit to main" rule. The public
   mirror (which the marketplace serves) is synced from `origin/main` by
   `sync-public.yml`, so a refresh reaches installers only after
   `develop -> main` is promoted. If you want the refresh fully
   hands-off, change the workflow's checkout `ref` and push target from
   `develop` to `main`, but that bypasses safe-merge, so it is opt-in,
   not the default.

## Running it by hand

Actions tab -> "Security reference auto-refresh" -> Run workflow. Or
locally with `ANTHROPIC_API_KEY` set:

```bash
python3 scripts/security-refresh/refresh_references.py refresh --out /tmp/cand
python3 scripts/security-refresh/refresh_references.py verify --candidate-dir /tmp/cand --out /tmp/verdict.json
python3 scripts/security-refresh/verify_refresh.py --candidate-dir /tmp/cand \
    --fixtures scripts/security-refresh/currency_fixtures.json --verdict /tmp/verdict.json
# only if the gate exits 0:
python3 scripts/security-refresh/bump_version.py
```

## Residual risk (honest)

Two models can agree and both be wrong. The domain whitelist, the
adversarial re-fetch, and the fixture net make that unlikely, and every
auto-commit cites its sources so a bad change is traceable and revertible.
If the residual risk proves too high in practice, switch the workflow's
commit step to open a PR instead of pushing (one human glance per cycle),
leaving the rest of the pipeline unchanged.
