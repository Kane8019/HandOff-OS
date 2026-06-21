# Philosophy: chat is scratch, state is durable

HandOff-OS rests on one idea:

> **Chat is scratch. Durable state lives outside the chat.**

A chat window is a fantastic place to think. It is a terrible place to keep
anything you can't afford to lose. The moment a project depends on something
that only exists inside a transcript, that project is one closed tab, one
context-window overflow, or one model switch away from amnesia.

## Why this matters more with multiple tools

If you only ever used one AI in one window forever, you might get away with
treating the chat as your memory. Almost nobody works that way.

In practice you bounce between:

- one model that's good at scoping and critique,
- another that's good at drafting and building,
- a notes tool, a code host, a file store,
- and a new chat every time the old one gets unwieldy.

Each hop loses context. The reasoning that justified a decision stays in the
window where it happened. The next tool starts cold.

HandOff-OS fixes this by moving the **few load-bearing facts** out of any single
chat and into plain documents that every tool — and every future you — can read.

## What "durable state" actually is

Durable state is small. It is the answer to: *if I lost this chat right now,
what would make tomorrow's work wrong, blocked, or duplicated?*

That usually comes down to four things:

1. **Decisions** — what we settled, and what it replaced.
2. **Next action** — the single most useful thing to do next.
3. **Source pointers** — where the real material lives.
4. **Active boundaries** — what's in and out of scope right now.

Everything else is scratch. The long exploration, the rejected options, the
phrasing you iterated on — none of it needs to survive. If it changed a
decision, the decision survives; the deliberation doesn't.

## Why not just save the whole transcript?

Because a transcript is the opposite of memory. It's high-volume, low-signal,
and it grows without bound. To find the one decision that matters, you'd have to
re-read everything — which is exactly the problem you were trying to escape.

Durable state is a **summary you maintain on the way**, not an archive you mine
later. You pay a few seconds at the end of a session so future-you pays zero.

## The discipline

- Write down a fact **when it becomes load-bearing**, not "eventually."
- Record what a decision **replaced or superseded**, so the history makes sense.
- Keep pointers, not payloads — especially for anything private.
- Use the **shortest workflow that produces usable progress**. Ceremony is not
  the goal; recoverability is.

The payoff: any chat, any tool, any model can pick the project up from the
state file and be useful in the first minute.
