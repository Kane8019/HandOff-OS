# Risk tiers: match the process to the action

Not all work needs the same care. The mistake most "process" makes is applying
heavy review to an entire *project* when only a few *actions* in it are actually
risky.

> **Risk belongs to an action, not an entire project.**

So HandOff-OS doesn't grade projects. It grades actions, and it keeps the grading
to two practical tiers.

## LOW consequence

An action is **low consequence** when it is easy to reverse and cheap to get
wrong. Just do it. Don't ask for review. Don't write a proposal.

Signals of low consequence:

- Easily reversible (you can undo it in seconds or minutes).
- Local and private (nothing leaves your machine or your draft).
- No outside party sees it.
- A mistake costs a little time and nothing else.

Public-safe examples:

- Drafting an internal note or outline.
- Renaming a local file.
- Refactoring code you haven't shipped.
- Sketching three options before picking one.

For low-consequence work, the right amount of process is **none**. Move.

## HIGH consequence

An action is **high consequence** when it is hard to reverse, visible to
others, or expensive to get wrong. These deserve a proposal, a review, and an
explicit owner approval before they happen.

Signals of high consequence:

- Hard or impossible to reverse.
- Outward-facing (publishing, sending, deploying, filing).
- Touches money, legal matters, or other people's data.
- A mistake is costly, public, or both.

Public-safe examples:

- Publishing to a public repository or website.
- Sending an external email on someone's behalf.
- Deploying to production.
- Submitting a document to an outside party.
- Deleting or overwriting something you didn't create.

For high-consequence work, use [`proposal.md`](../templates/proposal.md) and
[`review.md`](../templates/review.md), and get the owner's approval first.

## How to tell, fast

Ask two questions about the **action** (not the project):

1. **Can I undo this easily?**
2. **Does anyone outside this workspace see the result?**

If you can undo it and nobody outside sees it â†’ LOW. Otherwise â†’ treat it as HIGH.

## This is not fear-based bureaucracy

The point isn't to slow everything down. It's the opposite: by reserving
ceremony for the handful of actions that are genuinely consequential, you get to
move fast on everything else with a clear conscience.

- Don't write a proposal to rename a variable.
- Do write one before you publish.

Add review **only when the action is high-consequence**. The rest of the time,
the shortest useful workflow wins.
