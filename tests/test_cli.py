"""Tests for the HandoffOS CLI.

Written with the standard-library ``unittest`` framework so they run with no
extra installs (no network required):

    python -m unittest discover -s tests -t .

They are also collectable by pytest if you install the dev extra:

    pip install -e ".[dev]"
    python -m pytest
"""

import sys
import tempfile
import unittest
from pathlib import Path

# Make the repo importable when this file is run directly (python tests/test_cli.py).
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from handoffos import cli  # noqa: E402

EXPECTED_FILES = {
    "project-context.md",
    "history-log.md",
    "proposal.md",
    "review.md",
}


class InitTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_init_creates_exactly_the_four_files(self):
        target = self.tmp / "proj"
        rc = cli.main(["init", str(target)])
        self.assertEqual(rc, 0)
        created = {p.name for p in target.iterdir()}
        self.assertEqual(created, EXPECTED_FILES)

    def test_generated_files_are_non_empty(self):
        target = self.tmp / "proj"
        cli.main(["init", str(target)])
        for name in EXPECTED_FILES:
            content = (target / name).read_text(encoding="utf-8")
            self.assertTrue(content.strip(), f"{name} should be non-empty")

    def test_rerun_without_force_fails_safely(self):
        target = self.tmp / "proj"
        self.assertEqual(cli.main(["init", str(target)]), 0)

        # Mark the file so we can prove it was NOT overwritten on the failed run.
        marked = target / "project-context.md"
        marked.write_text("EDITED BY USER", encoding="utf-8")

        rc = cli.main(["init", str(target)])
        self.assertEqual(rc, 1, "re-run without --force should fail")
        self.assertEqual(
            marked.read_text(encoding="utf-8"),
            "EDITED BY USER",
            "failed re-run must not overwrite existing files",
        )

    def test_force_overwrites_known_files_only_and_keeps_unrelated(self):
        target = self.tmp / "proj"
        cli.main(["init", str(target)])

        # An edited known file (should be overwritten) ...
        known = target / "review.md"
        known.write_text("EDITED", encoding="utf-8")
        # ... and an unrelated file plus a subfolder (must be left untouched).
        unrelated = target / "notes.md"
        unrelated.write_text("KEEP ME", encoding="utf-8")
        subdir = target / "attachments"
        subdir.mkdir()
        sub_file = subdir / "data.txt"
        sub_file.write_text("KEEP ME TOO", encoding="utf-8")

        rc = cli.main(["init", str(target), "--force"])
        self.assertEqual(rc, 0)

        # The known file was regenerated from the template (no longer "EDITED").
        self.assertNotEqual(known.read_text(encoding="utf-8"), "EDITED")
        self.assertTrue(known.read_text(encoding="utf-8").startswith("# Review"))

        # Unrelated content is preserved.
        self.assertTrue(unrelated.exists())
        self.assertEqual(unrelated.read_text(encoding="utf-8"), "KEEP ME")
        self.assertTrue(sub_file.exists())
        self.assertEqual(sub_file.read_text(encoding="utf-8"), "KEEP ME TOO")

    def test_target_that_is_a_file_fails(self):
        target = self.tmp / "afile"
        target.write_text("i am a file", encoding="utf-8")
        rc = cli.main(["init", str(target)])
        self.assertEqual(rc, 1)


class TemplateParityTests(unittest.TestCase):
    """The packaged templates must match the human-facing repo-root copies."""

    def test_packaged_templates_match_repo_root(self):
        repo_templates = REPO_ROOT / "templates"
        if not repo_templates.is_dir():
            self.skipTest("repo-root templates/ not present (installed package?)")
        for name in EXPECTED_FILES:
            packaged = cli._read_template(name)
            on_disk = (repo_templates / name).read_text(encoding="utf-8")
            self.assertEqual(
                packaged,
                on_disk,
                f"{name}: packaged template differs from templates/{name}",
            )


if __name__ == "__main__":
    unittest.main()
