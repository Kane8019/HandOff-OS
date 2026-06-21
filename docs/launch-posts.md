# HandOff-OS launch post drafts

These are draft launch posts for public distribution. Adjust links and screenshots before posting.

## X / Twitter short post

I built HandOff-OS because long AI projects kept breaking across chats.

The rule is simple:

Chat is scratch. Durable state lives outside the chat.

HandOff-OS keeps project context, decisions, next actions, boundaries, and source pointers in small Markdown files so ChatGPT, Claude Code, Cursor, or Codex can resume without guessing.

Repo: https://github.com/Kane8019/HandOff-OS

## X / Twitter thread

**Post 1**

Your AI can help you write, code, and plan.

But the chat should not be the source of truth.

I built HandOff-OS: a lightweight project-memory and handoff layer for long-running work across ChatGPT, Claude Code, Cursor, Codex, and other AI tools.

**Post 2**

The problem:

- the chat gets too long
- the next model starts cold
- yesterday's decisions become a bad summary
- Claude and ChatGPT disagree because neither owns the project state
- people either save full transcripts or lose the facts that matter

**Post 3**

HandOff-OS keeps only durable state:

- current state
- next action
- active decisions
- boundaries
- source pointers
- unresolved high-consequence items

No full transcript. No private payload. No guessing.

**Post 4**

The workflow:

1. ChatGPT scopes.
2. Claude Code / Cursor / Codex drafts.
3. A reviewer checks the result.
4. Human approves execution.
5. Durable state is checkpointed outside the chat.

**Post 5**

The v0.1 CLI is intentionally tiny and local-only:

```bash
handoffos init my-project
handoffos status my-project
```

No accounts. No network calls. No service integration.

**Post 6**

This is not a project-management system, prompt collection, or transcript archive.

It is a small state contract for AI-assisted projects.

If a fresh chat can resume without guessing, the system is working.

Repo: https://github.com/Kane8019/HandOff-OS

## LinkedIn post

Long AI projects fail when the project state only lives inside a chat.

The chat gets too long, a new model starts cold, and important decisions turn into a bad summary. This gets worse when the work moves across ChatGPT, Claude Code, Cursor, Codex, GitHub, Notion, and local files.

I built HandOff-OS to solve the smallest useful version of that problem.

HandOff-OS is a lightweight project-memory and handoff layer for AI-assisted work. It keeps durable state in small Markdown files so a fresh AI chat or coding agent can resume without guessing, rereading transcripts, or mixing projects.

The core rule:

Chat is scratch. Durable state lives outside the chat.

It saves the things that actually matter:

- current state
- next action
- active decisions
- boundaries
- source pointers
- unresolved high-consequence items

It does not save full transcripts or private payloads.

The v0.1 release is intentionally local-first and small: templates, synthetic examples, docs, and a tiny CLI.

```bash
handoffos init my-project
handoffos status my-project
```

The goal is not to replace Notion, GitHub, Drive, or Jira. It is to create a lightweight state contract that lets AI tools hand off work without pretending they remember.

Repo: https://github.com/Kane8019/HandOff-OS

Feedback welcome, especially from people using ChatGPT with Claude Code, Cursor, Codex, or other coding agents on long-running projects.

## Hacker News / Show HN draft

**Title option A**

Show HN: HandOff-OS – keep AI projects recoverable across chats and agents

**Title option B**

Show HN: A tiny protocol so AI projects survive new chats

**Post body**

I built HandOff-OS after repeatedly hitting the same problem in long AI-assisted projects: the chat gets too long, the next model starts cold, and important decisions become an unreliable summary.

The core rule is: chat is scratch; durable state lives outside the chat.

HandOff-OS keeps four small Markdown files:

- project context
- history log
- proposal
- review

The source material stays in GitHub, Notion, Drive, tickets, or local files. HandOff-OS stores source pointers and the state that would make future work wrong, blocked, or duplicated if lost.

The v0.1 CLI is local-only and has no network calls:

```bash
handoffos init my-project
handoffos status my-project
```

The repo includes a small demo where a fresh AI chat recovers a fictional lost project from durable state instead of a transcript.

I would especially like feedback from people using ChatGPT plus Claude Code, Cursor, Codex, or other coding agents across long-running projects.

Repo: https://github.com/Kane8019/HandOff-OS

## Reddit feedback post

**Title**

I made a small local-first workflow so AI projects survive new chats — would this solve a real problem for you?

**Body**

I kept running into the same issue with long AI-assisted projects: after enough ChatGPT / Claude / Cursor / Codex sessions, the actual project state was scattered across chat history, local files, GitHub, and half-remembered decisions.

So I built a small open-source workflow called HandOff-OS.

The core rule is:

Chat is scratch. Durable state lives outside the chat.

It keeps four Markdown files:

- project-context.md
- history-log.md
- proposal.md
- review.md

The idea is not to archive transcripts. The idea is to save only what would make future work wrong, blocked, or duplicated if lost: current state, next action, decisions, boundaries, and source pointers.

The CLI is local-only and makes no network calls:

```bash
handoffos init my-project
handoffos status my-project
```

I am looking for feedback from people who run long AI-assisted coding, research, writing, or operations projects.

Repo: https://github.com/Kane8019/HandOff-OS

Questions:

- Do your AI projects actually break from lost context?
- Would Markdown durable state be enough?
- What would you add or remove from the templates?
- Would you use this with ChatGPT + Claude Code / Cursor / Codex?

## Product Hunt draft

**Tagline**

Durable project memory for ChatGPT, Claude Code, Cursor, and Codex workflows.

**Description**

HandOff-OS is a lightweight, local-first project-memory and handoff layer for long-running AI-assisted work. It keeps the state that matters in small Markdown files so fresh AI chats and coding agents can resume without guessing, rereading transcripts, or mixing projects.

**Maker comment**

I built HandOff-OS after long AI projects kept breaking across chats and tools. The core idea is simple: chat is scratch, durable state lives outside the chat.

The v0.1 release is intentionally small: Markdown templates, synthetic examples, docs, and a tiny local CLI. No accounts, no network calls, no integrations.

I would love feedback from people using ChatGPT with Claude Code, Cursor, Codex, or other AI agents on multi-session projects.
