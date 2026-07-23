"""Tests for scripts/security-refresh/verify_refresh.py (deterministic gate).

The adversarial model re-fetch is a runtime step; here we test the
fail-closed deterministic gate: known_good must survive, known_bad must
never appear, structural sanity must hold.

    python3 scripts/security-refresh/tests/test_verify_refresh.py
"""
from __future__ import annotations
import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "verify_refresh.py"


def _load():
    spec = importlib.util.spec_from_file_location("verify_refresh", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["verify_refresh"] = mod
    spec.loader.exec_module(mod)
    return mod


FIXTURES = {
    "known_good": {
        "owasp-checklist.md": ["Broken Access Control", "Injection"],
        "cwe-patterns.md": ["CWE-79", "CWE-918"],
    },
    "known_bad": ["A11:", "lorem ipsum", "as an AI language model"],
}


def _pad(text: str) -> str:
    """Pad to above the MIN_FILE_CHARS truncation threshold with a comment
    so a legitimately structured file is not mistaken for truncated."""
    filler = "\n<!-- reference body: real files carry full prose per category -->" * 6
    return text + filler


def test_gate_passes_clean_update() -> None:
    m = _load()
    new = {
        "owasp-checklist.md": _pad("---\nedition: \"2025\"\n---\n# X\n- Broken Access Control\n- Injection\n"),
        "cwe-patterns.md": _pad("---\ncwe-basis: top25\n---\n## CWE-79\n## CWE-918\n"),
    }
    res = m.gate(new, FIXTURES)
    assert res["passed"] is True, res
    assert res["violations"] == [], res
    print("OK: gate passes a clean update")


def test_gate_fails_on_known_good_regression() -> None:
    m = _load()
    new = {
        "owasp-checklist.md": "---\nedition: \"2025\"\n---\n# X\n- Injection\n",  # dropped Broken Access Control
        "cwe-patterns.md": "---\nx: y\n---\n## CWE-79\n## CWE-918\n",
    }
    res = m.gate(new, FIXTURES)
    assert res["passed"] is False, res
    assert any("Broken Access Control" in v for v in res["violations"]), res
    print("OK: gate fails when a known_good category disappears")


def test_gate_fails_on_known_bad_appearance() -> None:
    m = _load()
    new = {
        "owasp-checklist.md": "---\nedition: \"2025\"\n---\n# X\n- Broken Access Control\n- Injection\n- A11: made up\n",
        "cwe-patterns.md": "---\nx: y\n---\n## CWE-79\n## CWE-918\n",
    }
    res = m.gate(new, FIXTURES)
    assert res["passed"] is False, res
    assert any("A11:" in v for v in res["violations"]), res
    print("OK: gate fails when a known_bad string appears")


def test_gate_fails_on_hallucination_marker() -> None:
    m = _load()
    new = {
        "owasp-checklist.md": "---\nedition: \"2025\"\n---\n- Broken Access Control\n- Injection\nas an AI language model I cannot\n",
        "cwe-patterns.md": "---\nx: y\n---\n## CWE-79\n## CWE-918\n",
    }
    res = m.gate(new, FIXTURES)
    assert res["passed"] is False, res
    assert any("as an AI language model" in v for v in res["violations"]), res
    print("OK: gate catches model-refusal / hallucination markers")


def test_gate_fails_on_empty_or_truncated() -> None:
    m = _load()
    new = {
        "owasp-checklist.md": "",  # empty = truncation/failure
        "cwe-patterns.md": "---\nx: y\n---\n## CWE-79\n## CWE-918\n",
    }
    res = m.gate(new, FIXTURES)
    assert res["passed"] is False, res
    assert any("empty" in v.lower() or "short" in v.lower() for v in res["violations"]), res
    print("OK: gate fails on empty/truncated file")


def test_gate_fail_closed_on_missing_file() -> None:
    m = _load()
    # A fixture references cwe-patterns.md but the refresh produced only one file.
    new = {
        "owasp-checklist.md": "---\ne: 1\n---\n- Broken Access Control\n- Injection\n",
    }
    res = m.gate(new, FIXTURES)
    assert res["passed"] is False, res
    assert any("cwe-patterns.md" in v for v in res["violations"]), res
    print("OK: gate fails closed when a fixtured file is missing from the refresh")


ALL_TESTS = [
    test_gate_passes_clean_update,
    test_gate_fails_on_known_good_regression,
    test_gate_fails_on_known_bad_appearance,
    test_gate_fails_on_hallucination_marker,
    test_gate_fails_on_empty_or_truncated,
    test_gate_fail_closed_on_missing_file,
]


def main() -> int:
    failed = 0
    for t in ALL_TESTS:
        try:
            t()
        except AssertionError as exc:
            print(f"FAIL: {t.__name__}: {exc}", file=sys.stderr)
            failed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: {t.__name__}: {exc!r}", file=sys.stderr)
            failed += 1
    if failed:
        print(f"\n{failed} test(s) failed.", file=sys.stderr)
        return 1
    print("\nAll verify_refresh tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
