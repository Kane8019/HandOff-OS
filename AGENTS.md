# AGENTS.md

This repository is a public, clean-room edition of HandOff-OS.

Use this file as the default instruction layer for AI coding agents working in this repo.

## Product contract

HandOff-OS is a lightweight project-memory and handoff layer for AI-assisted work.

The core rule is:

> Chat is scratch. Durable state lives outside the chat.

The product should remain small, local-first, and easy to understand. Do not turn it into a full project-management system, hosted SaaS, or autonomous approval framework without an explicit proposal.

## Public-safety boundary

Do not add real private material to this repository.

Never include:

- private Notion exports
- real legal facts, case numbers, party names, or court strategy
- real lab, sample, server, dataset, or customer identifiers
- financial, tax, banking, or credit material
- private emails or communications
- credentials, tokens, secrets, or private links
- approval strings or internal workflow details from private projects

Use synthetic examples only. If an example needs realism, make it fictional and non-reconstructable.

## Naming rules

Use these names consistently:

- Product and repository display name: `HandOff-OS`
- Python package and CLI command: `handoffos`

Do not reintroduce the old display spelling unless documenting history.

## Architecture boundaries

The v0.1 product is intentionally local-only:

- no network calls
- no Notion API
- no Google Drive API
- no Gmail API
- no GitHub write automation
- no background agents
- no autonomous approval or merge flow

The CLI should copy and inspect local Markdown state. Optional integrations belong in future proposals, not casual drive-by edits.

## When changing code

Before editing, read:

- `README.md`
- `templates/`
- `handoffos/cli.py`
- `tests/`

When CLI behavior changes:

- update tests
- update README examples if user-facing commands change
- keep the standard-library path working
- avoid new runtime dependencies unless the proposal explicitly justifies them

Run at least:

```bash
python -m unittest discover -s tests -t .
```

If pytest-specific behavior is changed, also run:

```bash
python -m pytest
```

## When changing docs or examples

Docs should help a new user understand the product in minutes.

Prefer:

- short explanations
- copyable templates
- concrete synthetic examples
- clear boundaries
- source pointers instead of payloads

Avoid:

- long philosophy before the demo
- transcript dumps
- private or realistic sensitive facts
- over-engineered governance language
- vague claims that the tool "solves memory" without explaining the state contract

## Review standard

A useful change should preserve at least one of these outcomes:

- a fresh chat can recover a project without guessing
- a user knows what to save and what not to save
- an AI agent knows the scope and boundaries before drafting
- a human owner remains the only approver
- private payloads stay outside public/shared HandOff-OS files

If a change adds complexity without improving one of those outcomes, push back.
