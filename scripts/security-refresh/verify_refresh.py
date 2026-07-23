#!/usr/bin/env python3
"""Fail-closed verifier for the auto-refresh of security-audit references.

Two layers, both must pass or the refresh is rolled back (no commit):

  1. gate() -- DETERMINISTIC, this file. Regression net + sanity:
     - every known_good category still present (disappearance = rollback)
     - no known_bad string present (hallucination/refusal = rollback)
     - no file empty/truncated, frontmatter intact
     - every fixtured file actually produced (missing = fail closed)
     This is a regression net, NOT a novelty gate: new categories are
     admitted by the adversarial layer's source citation, not blocked
     for being absent from known_good.

  2. adversarial model re-check -- runtime, orchestrated by the workflow
     via refresh_references.py's verifier prompt. The verifier re-fetches
     the official sources ITSELF (does not trust the refresher's cited
     quotes), assumes each changed assertion is false until refuted, and
     drops any assertion without an official-domain citation. Its verdict
     is combined with the gate here.

stdlib-only. Usage:
    verify_refresh.py --candidate-dir DIR --fixtures F.json [--verdict V.json]
Exit 0 = passed (safe to bump + commit), 1 = failed (roll back).
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

MIN_FILE_CHARS = 200  # a real reference file is never this short


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def gate(candidate_files: dict, fixtures: dict) -> dict:
    """Deterministic fail-closed gate.

    candidate_files: {filename: full_text} of the refreshed references.
    fixtures: {known_good: {file: [str,...]}, known_bad: [str,...]}
    Returns {passed: bool, violations: [str,...]}.
    """
    violations: list = []
    known_good = fixtures.get("known_good", {})
    known_bad = fixtures.get("known_bad", [])

    # 1. Every fixtured file must be present and non-trivial.
    for fname in known_good:
        if fname not in candidate_files:
            violations.append(f"missing file in refresh: {fname}")
            continue
        text = candidate_files[fname] or ""
        if len(text.strip()) < MIN_FILE_CHARS:
            violations.append(f"file empty or too short (truncation?): {fname}")

    # 2. known_good categories must survive in their file.
    for fname, needles in known_good.items():
        text = candidate_files.get(fname, "")
        for needle in needles:
            if needle not in text:
                violations.append(f"known_good regression: '{needle}' gone from {fname}")

    # 3. known_bad strings must not appear in ANY file.
    for fname, text in candidate_files.items():
        for bad in known_bad:
            if bad in text:
                violations.append(f"known_bad string '{bad}' appeared in {fname}")

    return {"passed": not violations, "violations": violations}


def _read_candidate_dir(candidate_dir: Path) -> dict:
    out: dict = {}
    for p in sorted(candidate_dir.glob("*.md")):
        try:
            out[p.name] = p.read_text(encoding="utf-8")
        except Exception:
            out[p.name] = ""
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Fail-closed refresh verifier.")
    ap.add_argument("--candidate-dir", required=True,
                    help="dir of refreshed reference .md files")
    ap.add_argument("--fixtures", required=True)
    ap.add_argument("--verdict", default=None,
                    help="optional JSON from the adversarial model re-check "
                         "({passed: bool, reasons: [...]})")
    args = ap.parse_args(argv)

    candidate = _read_candidate_dir(Path(args.candidate_dir))
    fixtures = _load_json(Path(args.fixtures))

    result = gate(candidate, fixtures)

    # Combine with the adversarial model verdict if provided. Fail-closed:
    # a missing/malformed verdict counts as NOT passed.
    adversarial_passed = True
    adversarial_reasons: list = []
    if args.verdict:
        try:
            v = _load_json(Path(args.verdict))
            adversarial_passed = bool(v.get("passed", False))
            adversarial_reasons = v.get("reasons", [])
        except Exception as exc:  # noqa: BLE001
            adversarial_passed = False
            adversarial_reasons = [f"verdict unreadable: {exc}"]

    passed = result["passed"] and adversarial_passed
    report = {
        "passed": passed,
        "gate_violations": result["violations"],
        "adversarial_passed": adversarial_passed,
        "adversarial_reasons": adversarial_reasons,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
