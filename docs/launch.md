# HandOff-OS launch page copy

## Hero

# Stop losing AI project context.

HandOff-OS is a lightweight project-memory and handoff layer for long-running work across ChatGPT, Claude Code, Cursor, Codex, and other AI tools.

Your AI can help you think, draft, and build. But the chat should not be the source of truth.

HandOff-OS keeps durable project state in small Markdown files so a fresh chat or coding agent can resume without guessing, rereading transcripts, or mixing projects.

## 30-second demo

A long AI project fails when the original chat disappears or becomes too stale.

HandOff-OS keeps two core files alive:

```text
project-context.md + history-log.md
```

A fresh chat reads those files and recovers:

- current state
- settled decisions
- next action
- active boundaries
- source pointers

No full transcript. No private payload. No guessing.

## Try it in two minutes

```bash
pip install -e .
handoffos init my-project
handoffos status my-project
```

Or skip the CLI and copy the templates manually.

HandOff-OS is local-first and makes no network calls.

## Who it is for

HandOff-OS is for people running serious AI-assisted projects across multiple tools:

- solo founders using ChatGPT and Claude Code
- developers using Cursor, Codex, or other coding agents
- researchers and operators who need decisions and source pointers to survive new chats
- technical PMs coordinating AI-generated drafts and human approval
- consultants working on high-consequence deliverables where context drift is expensive

It is not necessary for one-off questions or disposable prompts.

## The core rule

> Chat is scratch. Durable state lives outside the chat.

Save only what would make future work wrong, blocked, or duplicated if lost.

That usually means:

- current state
- next action
- active decisions
- source pointers
- boundaries
- unresolved high-consequence items

It does not mean saving full transcripts.

## Why not just use chat memory?

Chat memory is convenient, but it is not a reliable canonical state layer for long-running, multi-tool, or high-consequence work.

HandOff-OS keeps the state contract outside any single model so ChatGPT, Claude, Cursor, Codex, or a future AI can recover the project the same way.

## Role split

HandOff-OS assumes a simple workflow:

1. ChatGPT or another reasoning model scopes the task.
2. Claude Code, Cursor, Codex, or another building tool drafts within scope.
3. A reviewer checks the result against the durable state.
4. The human owner approves execution, publication, or high-consequence changes.
5. Durable state is checkpointed outside the chat.

## What this is not

HandOff-OS is not:

- a full project-management system
- a transcript archive
- a prompt collection
- an autonomous approval system
- a replacement for Notion, GitHub, Drive, Linear, Jira, or local files

It is a small memory and handoff layer that points to the real source material.

## Call to action

Try the rescue demo, clone the repo, and initialize one project.

If it helps a fresh AI chat recover your project without guessing, star the repo and open an issue with your workflow.

If your team or solo workflow keeps breaking across ChatGPT, Claude Code, Cursor, or Codex, use HandOff-OS as the first lightweight state layer before adding heavier tooling.
