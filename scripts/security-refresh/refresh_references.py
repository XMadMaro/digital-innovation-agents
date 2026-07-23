#!/usr/bin/env python3
"""Auto-refresh the security-audit reference checklists from official sources.

D3 Ebene 2: a frontier model regenerates the bundled OWASP/CWE/LLM
checklists from the CURRENT published editions, restricted to official
domains, then a second adversarial model verifies the diff before anything
is committed (verify_refresh.py + the workflow enforce fail-closed).

This script produces CANDIDATE files into an output dir; it does not touch
the live references and does not commit. The workflow wires:
  refresh_references.py refresh  --out <dir>    (this: model writes candidates)
  refresh_references.py verify   --candidate-dir <dir> --out <verdict.json>
  verify_refresh.py  (deterministic fail-closed gate + verdict)
  bump_version.py    (only if the gate passes)

stdlib + the `anthropic` SDK. If the SDK or the API key is unavailable,
the script exits non-zero WITHOUT writing candidates (fail-closed: a
refresh that cannot verify must not proceed). Model: claude-opus-4-8,
adaptive thinking, web_search restricted to official domains.

Usage:
    refresh_references.py refresh --out DIR [--refs-dir DIR]
    refresh_references.py verify  --candidate-dir DIR --refs-dir DIR --out FILE
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path

# Official-source allowlist. The web_search tool is restricted to these;
# anything the model cites outside them is rejected by the verifier.
ALLOWED_DOMAINS = [
    "owasp.org",
    "genai.owasp.org",
    "cwe.mitre.org",
    "nvd.nist.gov",
    "github.com",  # github.com/advisories
    "osv.dev",
]

MODEL = "claude-opus-4-8"

# The reference files the refresh regenerates (checklists only; procedures
# like desktop-runtime.md are not auto-rewritten -- they change rarely and
# are not edition-pinned).
REFRESH_TARGETS = ["owasp-checklist.md", "owasp-llm-checklist.md", "cwe-patterns.md"]


def _load_sdk():
    """Import the anthropic SDK, or exit fail-closed if unavailable."""
    try:
        import anthropic  # noqa: F401
        return anthropic
    except Exception:
        print("ERROR: anthropic SDK not available; refresh cannot verify -> "
              "aborting (fail-closed).", file=sys.stderr)
        sys.exit(2)


def _client(anthropic):
    # Zero-arg client resolves ANTHROPIC_API_KEY / auth profile itself.
    try:
        return anthropic.Anthropic()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: cannot construct Anthropic client: {exc}", file=sys.stderr)
        sys.exit(2)


def _web_search_tool():
    # Domain-restricted web search: the Quell-Whitelist, enforced at the tool.
    return {
        "type": "web_search_20260209",
        "name": "web_search",
        "allowed_domains": ALLOWED_DOMAINS,
        "max_uses": 12,
    }


def _text(response) -> str:
    out = []
    for block in response.content:
        if getattr(block, "type", None) == "text":
            out.append(block.text)
    return "\n".join(out)


REFRESH_PROMPT = """You are refreshing the OFFLINE BASELINE security checklists \
that ship with an automated security-audit skill. Regenerate the file `{fname}` \
from the CURRENT published edition, using web_search restricted to official \
sources only ({domains}).

Current bundled content (the baseline you are updating):
---
{current}
---

Rules:
- Only add or change a category if you can cite an OFFICIAL source for it \
(one of the allowed domains). Note the source URL inline as an HTML comment \
after any changed line.
- Keep the file's existing structure, frontmatter, and style. Keep the \
`edition:`/`cwe-basis:` frontmatter and update the year/edition to what the \
official source currently publishes.
- Do NOT invent categories, CVE numbers, or codes. If unsure, keep the \
baseline line unchanged.
- Preserve every cross-reference to other files (e.g. desktop-runtime.md, \
agent-approval-gate.md) exactly.
- Output ONLY the complete new file content, no preamble, no code fences.

Return the full updated `{fname}`."""


def cmd_refresh(args) -> int:
    anthropic = _load_sdk()
    client = _client(anthropic)
    refs = Path(args.refs_dir)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    wrote = []
    for fname in REFRESH_TARGETS:
        src = refs / fname
        current = src.read_text(encoding="utf-8") if src.exists() else ""
        prompt = REFRESH_PROMPT.format(
            fname=fname, domains=", ".join(ALLOWED_DOMAINS), current=current)
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=16000,
                thinking={"type": "adaptive"},
                tools=[_web_search_tool()],
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: refresh model call failed for {fname}: {exc}",
                  file=sys.stderr)
            return 2
        content = _text(resp).strip()
        if len(content) < 200:
            print(f"ERROR: refresh produced empty/short {fname}; aborting.",
                  file=sys.stderr)
            return 2
        (out / fname).write_text(content + "\n", encoding="utf-8")
        wrote.append(fname)

    print(json.dumps({"refreshed": wrote, "out": str(out)},
                     indent=2, ensure_ascii=False))
    return 0


VERIFY_PROMPT = """You are an ADVERSARIAL verifier. A model rewrote the \
security checklist `{fname}` from official sources. Your job is to REFUTE the \
changes, not confirm them. Assume each changed line is HALLUCINATED until you \
prove otherwise from an official source ({domains}). Default to rejecting on \
any doubt.

Baseline (before):
---
{before}
---

Candidate (after):
---
{after}
---

For every ADDED or CHANGED category/code:
- Re-fetch the official source yourself with web_search (do not trust the \
candidate's inline citation). If you cannot find it on an allowed domain, \
that change is REJECTED.
- Also check whether the candidate DROPPED anything that should still exist.

Respond with STRICT JSON only:
{{"passed": <true|false>, "reasons": ["<one line per rejected or suspect change>"]}}
`passed` is true only if every change is backed by an official source and no \
core category was wrongly dropped."""


def cmd_verify(args) -> int:
    anthropic = _load_sdk()
    client = _client(anthropic)
    refs = Path(args.refs_dir)
    cand = Path(args.candidate_dir)

    all_reasons = []
    passed = True
    for fname in REFRESH_TARGETS:
        after_path = cand / fname
        if not after_path.exists():
            continue
        before = (refs / fname).read_text(encoding="utf-8") if (refs / fname).exists() else ""
        after = after_path.read_text(encoding="utf-8")
        prompt = VERIFY_PROMPT.format(
            fname=fname, domains=", ".join(ALLOWED_DOMAINS),
            before=before, after=after)
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=8000,
                thinking={"type": "adaptive"},
                tools=[_web_search_tool()],
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:  # noqa: BLE001
            # Fail-closed: a verifier that cannot run rejects the change.
            print(json.dumps({"passed": False,
                              "reasons": [f"verifier call failed for {fname}: {exc}"]}))
            _write_verdict(args.out, False, [f"verifier call failed for {fname}"])
            return 1
        verdict = _parse_verdict(_text(resp))
        if not verdict.get("passed", False):
            passed = False
            all_reasons.extend([f"{fname}: {r}" for r in verdict.get("reasons", [])])

    _write_verdict(args.out, passed, all_reasons)
    print(json.dumps({"passed": passed, "reasons": all_reasons},
                     indent=2, ensure_ascii=False))
    return 0 if passed else 1


def _parse_verdict(text: str) -> dict:
    """Extract the strict-JSON verdict. Fail-closed on unparseable output."""
    text = text.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        return {"passed": False, "reasons": ["verifier returned no JSON verdict"]}
    try:
        return json.loads(text[start:end + 1])
    except Exception:
        return {"passed": False, "reasons": ["verifier verdict was not valid JSON"]}


def _write_verdict(out_path, passed: bool, reasons: list) -> None:
    if not out_path:
        return
    Path(out_path).write_text(
        json.dumps({"passed": passed, "reasons": reasons}, indent=2, ensure_ascii=False),
        encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Auto-refresh security-audit references.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    default_refs = str(Path(__file__).resolve().parents[2]
                       / "skills" / "security-audit" / "references")

    p_refresh = sub.add_parser("refresh")
    p_refresh.add_argument("--out", required=True)
    p_refresh.add_argument("--refs-dir", default=default_refs)

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("--candidate-dir", required=True)
    p_verify.add_argument("--refs-dir", default=default_refs)
    p_verify.add_argument("--out", default=None)

    args = ap.parse_args(argv)
    if args.cmd == "refresh":
        return cmd_refresh(args)
    if args.cmd == "verify":
        return cmd_verify(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
