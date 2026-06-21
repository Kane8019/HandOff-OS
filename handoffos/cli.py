"""HandoffOS command-line interface.

A minimal, standard-library-only CLI. It is local-only: it makes no network
calls and connects to no external service. It only reads packaged templates and
writes Markdown files on your machine.

Usage:
    handoffos init <project-dir> [--force]
"""

import argparse
import sys
from importlib import resources
from pathlib import Path

# The four files a workspace is made of. The CLI reads their contents from the
# packaged ``handoffos.templates`` source (single source of truth) so there is
# no duplicated template text inside this module.
WORKSPACE_FILES = (
    "project-context.md",
    "history-log.md",
    "proposal.md",
    "review.md",
)


def _read_template(name: str) -> str:
    """Return the packaged template text for *name*."""
    return resources.files("handoffos.templates").joinpath(name).read_text(
        encoding="utf-8"
    )


def init_project(target: Path, force: bool = False) -> int:
    """Create a HandoffOS workspace at *target*.

    Writes exactly the four files in ``WORKSPACE_FILES``. ``--force`` only
    overwrites those four known files; it never deletes or touches any other
    file in the directory.

    Returns a process exit code (0 = success).
    """
    if target.exists():
        if not target.is_dir():
            print(
                f"error: {target} exists and is not a directory.",
                file=sys.stderr,
            )
            return 1
        # Directory exists. Refuse to clobber existing HandoffOS files unless
        # --force is given.
        existing = [name for name in WORKSPACE_FILES if (target / name).exists()]
        if existing and not force:
            print(
                f"error: {target} already contains HandoffOS files "
                f"({', '.join(existing)}).",
                file=sys.stderr,
            )
            print(
                "Use --force to overwrite those four files, or choose another "
                "directory.",
                file=sys.stderr,
            )
            return 1

    try:
        target.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: could not create {target}: {exc}", file=sys.stderr)
        return 1

    for name in WORKSPACE_FILES:
        path = target / name
        try:
            path.write_text(_read_template(name), encoding="utf-8")
        except OSError as exc:
            print(f"error: could not write {path}: {exc}", file=sys.stderr)
            return 1
        print(f"created {path}")

    print()
    print(f"HandoffOS workspace ready at {target}")
    print("Next: open project-context.md and fill in Status, Purpose, and Next action.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="handoffos",
        description=(
            "Keep AI-assisted work recoverable across chats, tools, and models. "
            "Local-only: makes no network calls."
        ),
    )
    sub = parser.add_subparsers(dest="command")

    init = sub.add_parser(
        "init",
        help="Create a new HandoffOS workspace (four Markdown files).",
        description=(
            "Create a HandoffOS workspace: project-context.md, history-log.md, "
            "proposal.md, and review.md."
        ),
    )
    init.add_argument(
        "project_dir",
        help="Directory to create the workspace in (created if it doesn't exist).",
    )
    init.add_argument(
        "--force",
        action="store_true",
        help=(
            "Overwrite the four HandoffOS files (project-context.md, "
            "history-log.md, proposal.md, review.md) if they already exist. "
            "Does NOT delete or modify any other file in the directory."
        ),
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "init":
        return init_project(Path(args.project_dir), force=args.force)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
