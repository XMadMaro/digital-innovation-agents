# `_devprocess/` in the plugin repo

This directory is the standard location where the V-Model workflow
stores project artifacts: BA documents, Epics, Features, ADRs,
arc42, PLANs, backlog, bug log, etc.

In **user projects** that install this plugin, real artifacts live
here and are tracked in git alongside the code.

In **this plugin repo**, the directory should stay empty. The repo
is public and hosts the skill set itself, not a concrete product.
Drafts, internal notes, wiki articles, and migration plans do not
belong here. If you need a private scratchpad, keep it outside the
repo or add a path to `.gitignore` first.

Empty subdirectories (`plans/`, `requirements/features/`) are kept
as a structural hint for contributors and can be ignored.
