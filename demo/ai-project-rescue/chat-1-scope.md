# Chat 1 — scope and draft

This is a trimmed, fictional record of the *first* chat. You would not save this
file in real life — it's shown here only so you can see what the durable state
was distilled *from*. The transcript is scratch; the checkpoint is what matters.

---

**Builder:** I want to add a weekly digest email to my little side app. Once a
week, send each user a summary of what happened in their account that week.

**ChatGPT (scoping):** Let's bound this before any code.

- Goal: a once-a-week digest email per active user.
- In scope for v1: assemble the digest, render a plain-text email, send via the
  app's existing mailer abstraction.
- Out of scope for v1: HTML templates, per-user send-time preferences,
  unsubscribe management beyond the existing global opt-out, and **enabling real
  sends in production**.
- Boundary: develop against a local fake mailer only. No real recipients.
- "Done" for this chat: a reviewed draft that runs against the fake mailer in
  dev. Production is a separate, owner-approved decision.

**Builder:** Agreed. Keep it boring and reversible.

**Claude (drafting):** Here's a first draft.

- A `build_digest(user, since)` function that gathers the week's events and
  returns a plain-text body.
- A `send_weekly_digests()` job that loops active users and calls the mailer.
- Wired behind a `WEEKLY_DIGEST_ENABLED` flag, default **off**.
- In dev it points at the fake mailer; it has no production credentials.

**ChatGPT (quick review):** In scope. One gap: the draft has no guard against
sending twice if the job is re-run in the same week. Note it as an open question,
not a blocker for the draft.

**Builder:** Good catch. Let's checkpoint and stop here for today.

---

At this point the builder updates `project-context.md` and adds a row to
`history-log.md`, then closes the chat. Those two files are the entire handoff.
