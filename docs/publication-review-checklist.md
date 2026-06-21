# Publication Review Checklist

Run through this before HandoffOS is made public. The goal is a clean, safe,
credible v0.1. Nothing here authorizes publication on its own — see the final
item.

## 1. Private-data check

- [ ] No real legal facts, case numbers, party names, or court materials.
- [ ] No real lab, sample, server, dataset, database, or customer identifiers.
- [ ] No financial, tax, banking, or credit documents.
- [ ] No private emails, communications, or private links (e.g. Drive URLs).
- [ ] No credentials, tokens, or secrets anywhere in the repo or git history.
- [ ] No private documents reproduced or reconstructable from examples.

## 2. Synthetic examples check

- [ ] Every example is fictional (e.g. `Alice Example`, `Bob Example`).
- [ ] Dataset names are synthetic (e.g. `demo_batch_A.csv`).
- [ ] No real company names, domains, or systems.
- [ ] The legal example is clearly labeled fictional and contains no real
      strategy or facts.

## 3. No-external-integration check

- [ ] CLI makes no network calls and connects to no external service.
- [ ] No API clients, SDKs, or credential handling (Notion, Gmail, Drive,
      GitHub, etc.).
- [ ] `dependencies` in `pyproject.toml` is empty (only optional dev tooling).

## 4. README first-60-seconds check

- [ ] README opens with the name, tagline, and one-liner.
- [ ] The problem, the solution, and the role split are clear within a screen.
- [ ] Setup is presented as a 10-minute path.
- [ ] "What this is not" section is present and honest.
- [ ] The "Repository layout" tree in the README matches the actual repo layout.

## 5. CLI smoke test

- [ ] `python -m compileall handoffos` succeeds.
- [ ] `python -m unittest discover -s tests -t .` (or `python -m pytest`) passes.
- [ ] `python -m handoffos.cli init <tmp>` creates the four files.
- [ ] Installed entry point works: `handoffos init <tmp>`.
- [ ] Re-running without `--force` fails safely; `--force` overwrites only the
      four known files and leaves unrelated files intact.

## 6. Owner approval required before public release

- [ ] A human owner has reviewed this checklist and the diff.
- [ ] The owner explicitly approves publication.

Publishing is a high-consequence, outward-facing action. The human owner is the
only approver. Do not push, upload, or make the repository public until this box
is checked.
