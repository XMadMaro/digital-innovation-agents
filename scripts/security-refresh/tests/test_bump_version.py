"""Tests for scripts/security-refresh/bump_version.py.

    python3 scripts/security-refresh/tests/test_bump_version.py
"""
from __future__ import annotations
import importlib.util
import json
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "bump_version.py"


def _load():
    spec = importlib.util.spec_from_file_location("bump_version", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["bump_version"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_bump_patch() -> None:
    m = _load()
    assert m.bump_patch("3.6.0") == "3.6.1"
    assert m.bump_patch("3.6.9") == "3.6.10"
    assert m.bump_patch("0.0.0") == "0.0.1"
    print("OK: bump_patch")


def test_bump_patch_rejects_bad() -> None:
    m = _load()
    for bad in ("3.6", "abc", "3.x.0", ""):
        try:
            m.bump_patch(bad)
        except ValueError:
            continue
        assert False, f"expected ValueError for {bad!r}"
    print("OK: bump_patch rejects malformed")


def test_bump_files_updates_both_consistently() -> None:
    m = _load()
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        pj = tmp / ".claude-plugin" / "plugin.json"
        mk = tmp / ".claude-plugin" / "marketplace.json"
        pj.parent.mkdir(parents=True)
        pj.write_text(json.dumps({"name": "x", "version": "3.6.0"}), encoding="utf-8")
        mk.write_text(json.dumps({
            "metadata": {"version": "3.6.0"},
            "plugins": [{"name": "x", "version": "3.6.0"}],
        }), encoding="utf-8")
        new = m.bump_files(tmp)
        assert new == "3.6.1", new
        pj_after = json.loads(pj.read_text(encoding="utf-8"))
        mk_after = json.loads(mk.read_text(encoding="utf-8"))
        assert pj_after["version"] == "3.6.1", pj_after
        assert mk_after["metadata"]["version"] == "3.6.1", mk_after
        assert mk_after["plugins"][0]["version"] == "3.6.1", mk_after
        # other fields untouched
        assert pj_after["name"] == "x"
        print("OK: bump_files updates plugin.json + marketplace.json consistently")


def test_bump_files_refuses_version_mismatch() -> None:
    m = _load()
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        pj = tmp / ".claude-plugin" / "plugin.json"
        mk = tmp / ".claude-plugin" / "marketplace.json"
        pj.parent.mkdir(parents=True)
        pj.write_text(json.dumps({"version": "3.6.0"}), encoding="utf-8")
        mk.write_text(json.dumps({
            "metadata": {"version": "3.5.0"},  # mismatch
            "plugins": [{"version": "3.6.0"}],
        }), encoding="utf-8")
        try:
            m.bump_files(tmp)
        except ValueError:
            print("OK: bump_files refuses version mismatch")
            return
        assert False, "expected ValueError on version mismatch"


ALL_TESTS = [
    test_bump_patch,
    test_bump_patch_rejects_bad,
    test_bump_files_updates_both_consistently,
    test_bump_files_refuses_version_mismatch,
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
    print("\nAll bump_version tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
