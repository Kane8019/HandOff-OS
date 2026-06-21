# Demo: AI project rescue

A 2-minute walkthrough of the one thing HandoffOS is for: **resuming a project
in a fresh chat after the old chat is gone** — without re-explaining everything.

The scenario is fictional. A solo builder is adding a `weekly-digest-email`
feature to a small demo app. Chat 1 scopes the work and Claude drafts it. Then
the chat is "lost." Chat 2 recovers the project from two small files —
`project-context.md` and `history-log.md` — not from a transcript.

> The point: HandoffOS does **not** store the conversation. It stores only the
> durable state needed to pick the work back up.

## Run the demo (under 2 minutes)

1. **Read [`chat-1-scope.md`](chat-1-scope.md).**
   See how the work was scoped (ChatGPT) and drafted (Claude) in the first chat.

2. **Read [`project-context.md`](project-context.md) and
   [`history-log.md`](history-log.md).**
   This is everything that was checkpointed out of that chat. Notice how little
   it is — a living briefing plus a short change log.

3. **Pretend the chat was lost.**
   The window is closed. The transcript is gone. All you have is the two files
   from step 2.

4. **Use [`chat-2-recovery-prompt.md`](chat-2-recovery-prompt.md).**
   This is the prompt you'd paste into a brand-new chat (any model) to resume.
   It hands over only the durable state.

5. **Compare with [`expected-recovery.md`](expected-recovery.md).**
   This is the kind of grounded, accurate resume you should get back. No
   guessing, no re-litigating settled decisions, no inventing facts.

## What to notice

- The recovery prompt contains the **two state files**, not the chat history.
- The new chat knows the **decisions**, the **next action**, and the **active
  boundaries** — including that production sending is **not approved**.
- Total state is a couple of screens of plain Markdown. That's the handoff.

Everything here is synthetic: no real company, domain, user data, credentials,
or links.
