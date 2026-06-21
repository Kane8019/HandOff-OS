# Draft release notes: HandOff-OS v0.1.0

## Title

HandOff-OS v0.1.0 — durable project memory for AI-assisted work

## Summary

This first public release introduces HandOff-OS as a lightweight project-memory and handoff layer for long-running work across ChatGPT, Claude Code, Cursor, Codex, and other AI tools.

The core idea is simple:

> Chat is scratch. Durable state lives outside the chat.

HandOff-OS keeps the state that matters in small Markdown files so a fresh AI chat can resume without guessing, rereading transcripts, or mixing projects.

## What's included

- A strong README with a 30-second rescue demo.
- A local-only Python CLI:

```bash
handoffos init my-project
handoffos status my-project
```

- Four bundled Markdown templates:
  - `project-context.md`
  - `history-log.md`
  - `proposal.md`
  - `review.md`
- Synthetic examples for software, research, and redacted legal-style workflows.
- A demo showing how a fresh chat can recover project state from durable files.
- Documentation for risk tiers, dual-AI workflow, Notion setup, GitHub workflow, and publication review.
- `AGENTS.md` instructions for AI coding tools working inside the repo.

## What is intentionally not included

This release is intentionally small and local-first.

It does not include:

- hosted accounts
- network calls
- Notion API automation
- Google Drive integration
- Gmail integration
- GitHub write automation
- autonomous approval or merge flows
- multi-user permissions
- transcript archiving

## Why this matters

AI coding and writing agents are getting better at doing tasks, but long projects still break when state lives only in a chat.

HandOff-OS gives the user a small state contract:

- what is true now
- what was decided
- what is next
- what must not be touched
- where the real source material lives

That is enough for a fresh model or agent to resume without pretending it remembers.

## Try it

```bash
git clone https://github.com/Kane8019/HandOff-OS.git
cd HandOff-OS
pip install -e .
handoffos init my-project
handoffos status my-project
```

Or copy the templates manually from `templates/`.

## Feedback wanted

Open an issue if you use AI tools across long-running projects and have feedback on:

- what durable state you actually need
- what should not be saved
- how ChatGPT, Claude Code, Cursor, or Codex handoffs break in practice
- whether the templates are too light, too heavy, or missing a key field

## Public-safety note

This is a public clean-room edition. Do not put private payloads, secrets, legal facts, customer data, lab identifiers, or internal documents into shared HandOff-OS files. Use source pointers instead.
