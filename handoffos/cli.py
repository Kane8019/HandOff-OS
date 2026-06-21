"""HandOff-OS command-line interface.

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
    """Create a HandOff-OS workspace at *target*.

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
        # Directory exists. Refuse to clobber existing HandOff-OS files unless
        # --force is given.
        existing = [name for name in WORKSPACE_FILES if (target / name).exists()]
        if existing and not force:
            print(
                f"error: {target} already contains HandOff-OS files "
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
    print(f"HandOff-OS workspace ready at {target}")
    print("Next: open project-context.md and fill in Status, Purpose, and Next action.")
    return 0


# Fields shown by `status`, in display order. Parsing is intentionally simple
# (line-prefix matching) — this is not a Markdown parser.
STATUS_FIELDS = (
    "Status",
    "Sensitivity",
    "Project purpose",
    "Current state",
    "Next action",
)

_HIGH_CONSEQUENCE_HEADING = "## Unresolved high-consequence items"


def _parse_context(text: str):
    """Pull the status fields and high-consequence items out of *text*.

    Returns ``(fields, high_consequence)`` where ``fields`` maps each known
    field name to its value (empty string if blank) and ``high_consequence`` is
    a list of the bullet lines under that section.
    """
    fields = {name: "" for name in STATUS_FIELDS}
    lines = text.splitlines()

    for line in lines:
        for name in STATUS_FIELDS:
            prefix = name + ":"
            if line.startswith(prefix):
                fields[name] = line[len(prefix):].strip()

    high_consequence = []
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped == _HIGH_CONSEQUENCE_HEADING:
            in_section = True
            continue
        if in_section:
            if stripped.startswith("## ") or stripped.startswith("# "):
                break  # next section
            if stripped:
                high_consequence.append(stripped)

    return fields, high_consequence


def status_project(target: Path) -> int:
    """Print a compact status summary from ``project-context.md``.

    Returns a process exit code (0 = success, 1 = file missing/unreadable).
    """
    context = target / "project-context.md"
    if not context.is_file():
        print(
            f"error: no project-context.md found in {target}. "
            "Is this a HandOff-OS workspace? Try `handoffos init`.",
            file=sys.stderr,
        )
        return 1

    try:
        text = context.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: could not read {context}: {exc}", file=sys.stderr)
        return 1

    fields, high_consequence = _parse_context(text)

    print(f"HandOff-OS status: {target.name}")
    print()
    for name in STATUS_FIELDS:
        print(f"{name}: {fields[name]}".rstrip())

    if high_consequence:
        print()
        print("Unresolved high-consequence items:")
        for item in high_consequence:
            # Items already start with "- " in the template; keep as written.
            print(item if item.startswith("-") else f"- {item}")

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
        help="Create a new HandOff-OS workspace (four Markdown files).",
        description=(
            "Create a HandOff-OS workspace: project-context.md, history-log.md, "
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
            "Overwrite the four HandOff-OS files (project-context.md, "
            "history-log.md, proposal.md, review.md) if they already exist. "
            "Does NOT delete or modify any other file in the directory."
        ),
    )

    status = sub.add_parser(
        "status",
        help="Print a compact status summary from a workspace's project-context.md.",
        description=(
            "Read project-context.md in the given workspace and print Status, "
            "Sensitivity, Project purpose, Current state, Next action, and any "
            "unresolved high-consequence items."
        ),
    )
    status.add_argument(
        "project_dir",
        help="Directory of an existing HandOff-OS workspace.",
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "init":
        return init_project(Path(args.project_dir), force=args.force)

    if args.command == "status":
        return status_project(Path(args.project_dir))

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
