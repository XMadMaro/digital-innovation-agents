#!/usr/bin/env python3
"""Bump the plugin patch version in BOTH manifests, consistently.

A Claude Code plugin pinned to a `version` string in plugin.json does NOT
propagate new commits to users until that string changes. This script is
the D3 refresh's propagation step: after the verifier confirms a
reference update, bump the patch version so `/plugin update` (and
marketplace auto-update) actually pull the change.

Both .claude-plugin/plugin.json and .claude-plugin/marketplace.json carry
the version (plugin.json:version, marketplace.json:metadata.version and
plugins[].version). They must move together, or the marketplace and the
plugin disagree. This script refuses to bump if they are already out of
sync (that is a pre-existing bug to fix by hand, not to paper over).

stdlib-only. Usage:
    bump_version.py [repo_root]     # bumps patch, prints the new version
Exit 0 on success, 2 on error.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

_SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def bump_patch(version: str) -> str:
    m = _SEMVER.match(version.strip())
    if not m:
        raise ValueError(f"not a MAJOR.MINOR.PATCH version: {version!r}")
    major, minor, patch = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return f"{major}.{minor}.{patch + 1}"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write(path: Path, data: dict) -> None:
    # Preserve 2-space indent + trailing newline, the repo's manifest style.
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bump_files(repo_root: Path) -> str:
    pj_path = repo_root / ".claude-plugin" / "plugin.json"
    mk_path = repo_root / ".claude-plugin" / "marketplace.json"
    pj = _read(pj_path)
    mk = _read(mk_path)

    cur = pj.get("version")
    if cur is None:
        raise ValueError("plugin.json has no version field")

    # All three version slots must already agree before we bump.
    mk_meta = mk.get("metadata", {}).get("version")
    mk_plugin = mk.get("plugins", [{}])[0].get("version") if mk.get("plugins") else None
    for label, val in (("marketplace.metadata", mk_meta), ("marketplace.plugins[0]", mk_plugin)):
        if val is not None and val != cur:
            raise ValueError(
                f"version mismatch: plugin.json={cur} but {label}={val}; "
                f"fix by hand before auto-bumping"
            )

    new = bump_patch(cur)
    pj["version"] = new
    _write(pj_path, pj)

    if "metadata" in mk and "version" in mk["metadata"]:
        mk["metadata"]["version"] = new
    if mk.get("plugins"):
        for p in mk["plugins"]:
            if p.get("name") == pj.get("name") or "version" in p:
                p["version"] = new
    _write(mk_path, mk)
    return new


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    root = Path(argv[0]).resolve() if argv else Path.cwd()
    try:
        new = bump_files(root)
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
