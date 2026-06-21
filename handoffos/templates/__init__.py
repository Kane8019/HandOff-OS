"""Packaged HandOff-OS templates.

These four Markdown files are the single source the CLI reads (via
importlib.resources) when scaffolding a workspace. They are kept byte-identical
to the human-facing copies in the repo-root ``templates/`` directory; a test
(``tests/test_cli.py``) enforces that they do not drift.
"""
