# Contributing to HandoffOS

Thanks for your interest. HandoffOS aims to stay small, useful, and safe to
share. A few ground rules keep it that way.

## Public-safe contributions only

This is a public project. Everything you add must be safe for anyone to read.

- **No private data** in issues, pull requests, examples, screenshots, or commit messages.
- **Examples must be synthetic or heavily redacted.** Use fictional names,
  fictional companies, and made-up identifiers (e.g. `demo_batch_A.csv`,
  `Alice Example`).
- **No real** legal facts, case numbers, lab/sample/server/customer IDs,
  financial documents, credentials, tokens, or private links.

If you're not sure whether something is safe to include, leave it out or ask
first.

## Keep it lightweight

HandoffOS is documentation-first with a tiny CLI. Please help it stay that way.

- **Prefer useful templates and docs over automation.** A clear template beats
  a clever script.
- **No new external integrations.** No network calls, no third-party APIs, no
  credential handling.
- **Stick to the standard library** in the CLI unless there is a compelling reason.
- Small, focused pull requests are easier to review and merge.

## How to propose a change

1. Open an issue or a short proposal describing the change and why it helps.
2. For docs/templates: edit the Markdown directly.
3. For the CLI: keep it minimal and add a note in the pull request about how
   you tested it locally.
4. Make sure nothing private slipped into your diff before you submit.

## Local checks

```bash
python -m compileall handoffos
python -m unittest discover -s tests -t .      # tests, no extra installs needed
python -m handoffos.cli init ./scratch-demo
```

Inspect the generated files, then delete the scratch folder before committing.

The tests use the standard-library `unittest` framework, so they run without any
dependencies. If you prefer pytest, install the optional dev extra and run it:

```bash
pip install -e ".[dev]"
python -m pytest
```

Before opening a public release, also run through
[`docs/publication-review-checklist.md`](docs/publication-review-checklist.md).
