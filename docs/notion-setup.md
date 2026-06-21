# Notion setup (manual, no API)

You can keep HandoffOS state anywhere plain text lives. Notion is a comfortable
home for it. This setup is **fully manual** — no API, no integration, no
automation, no network calls from HandoffOS. You copy and paste.

## The minimal structure

Create one Notion page per project, with four sub-pages (or four toggles, if you
prefer everything on one page):

```text
📁 My Project                ← top-level project page
   📄 Project Context        ← from templates/project-context.md
   📄 History Log            ← from templates/history-log.md
   📄 Proposals              ← one entry per proposal, from templates/proposal.md
   📄 Reviews                ← one entry per review, from templates/review.md
```

## How to build it

1. Create a new page in Notion named for your project.
2. Open [`templates/project-context.md`](../templates/project-context.md), copy
   its contents, and paste into a sub-page called **Project Context**. Notion
   will render the Markdown headings and fields.
3. Repeat for **History Log**, using
   [`templates/history-log.md`](../templates/history-log.md). The Markdown table
   pastes in as a Notion table.
4. Create **Proposals** and **Reviews** pages. Each new proposal or review is a
   new entry pasted from the matching template.

## Working rhythm

- **Project Context is the living briefing.** Edit it in place. It should always
  reflect *current* status, next action, and active boundaries.
- **History Log is append-only.** Add a row when something durable changes; never
  rewrite old rows. The "what it replaced/superseded" column is what makes the
  history readable later.
- **Proposals and Reviews are per-action.** Only create them for high-consequence
  actions (see [risk-tiers.md](risk-tiers.md)).

## What to keep out of Notion

HandoffOS stores **pointers, not payloads**. In a shared or syncable Notion
workspace, do not paste private source material — real legal facts, personal
data, identifiers, credentials, or private documents. Instead, write a pointer:

```text
Source pointer: "Lease draft v3 — in the owner's private drive, not linked here."
```

That keeps the state recoverable without turning your notes into a copy of the
sensitive original.

## Why no API?

By design. HandoffOS v0.1 is deliberately offline and integration-free. A manual
copy/paste workflow is auditable, has no credentials to leak, and works
identically whether your "Notion" is Notion, Obsidian, a wiki, or a folder of
Markdown files.
