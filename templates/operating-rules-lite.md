# Operating Rules (Lite)

A short, copyable rule sheet for running AI-assisted work with HandOff-OS. Paste
it into a project, a README, or a system prompt.

## Purpose

Keep AI-assisted work recoverable across chats, tools, and models by keeping the
few load-bearing facts outside any single chat.

## What lives where

- **Chat** is scratch â€” thinking, drafting, exploring. Disposable.
- **Durable state** lives outside the chat: decisions, next action, source
  pointers, and active boundaries.
- Save **pointers, not payloads**. Point to where sensitive material lives;
  don't paste it in.

## Shortest useful workflow

Use the shortest workflow that produces usable progress. Don't add steps that
don't change the outcome.

1. Scope the task and its boundaries.
2. Draft or build within that scope.
3. Review **only if** the action is high-consequence.
4. Get owner approval for execution or publication.
5. Checkpoint durable state.

## Low vs high consequence work

- **Low consequence:** easily reversible, private, nobody outside sees it. Just
  do it â€” no proposal, no review.
- **High consequence:** hard to reverse, outward-facing, or touching money,
  legal matters, or others' data. Write a proposal, get a review, then approval.

Risk belongs to an **action**, not an entire project.

## Owner approval

The human owner is the only approver. AI may draft and review; AI does not
approve, publish, or execute on its own.

## Dual-AI review

One AI may draft and another may review. Do **not** create automatic
AI-checks-AI loops â€” they optimize for agreement, not correctness, and they
hide the human's decision. Use a single review pass when warranted, then bring
it to the owner.

## Project boundaries

Write down what's in scope and what's explicitly out. If the work pushes against
a boundary, re-scope deliberately â€” don't drift.

## Checkpointing durable state

Before closing a chat or finishing a session:

- Update **Project Context** (status, current state, next action, boundaries).
- Append a row to the **History Log** (what changed, what it replaced).

Save only what would make future work **wrong, blocked, or duplicated** if lost.
Do not copy transcripts.

## Writes and execution

Any action that writes to the outside world â€” publishing, sending, deploying,
filing, deleting something you didn't create â€” requires explicit owner approval
first. When in doubt, treat it as high-consequence.
