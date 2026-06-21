# Chat 2 — recovery prompt

The original chat is gone. Open a brand-new chat (any model) and paste the prompt
below. Notice what you're handing over: the **two state files**, not a
transcript.

---

```text
You are resuming an in-progress project. I lost the original chat. Below is the
durable state I kept outside the chat. Do not invent facts that aren't here.

Read it, then tell me:
1. Where the project stands right now.
2. The single next action.
3. Any active boundaries or high-consequence items I must respect.
Then wait for me before doing anything.

--- project-context.md ---
# Project Context

Status: In progress
Sensitivity: Low
Project purpose: Add weekly digest emails to a fictional demo app.
Current state: Feature scoped; draft exists; production send not approved.
Next action: Review draft and decide whether to test in staging.

## Active decisions
- Plain-text digest for v1; HTML is out of scope.
- Send once per week per active user via the existing mailer abstraction.
- Gated behind a WEEKLY_DIGEST_ENABLED flag, default off.
- Develop against a local fake mailer only — no real recipients.

## Boundaries
- In scope: build the digest, render plain text, send via the mailer in dev.
- Out of scope: HTML templates, per-user send-time preferences, production sends.
- No real recipients, credentials, or external services.

## Open questions
- Guard against double-sending if the weekly job re-runs in the same week.
- One combined digest vs. per-section digests? Leaning combined for v1.

## Unresolved high-consequence items
- Production email enablement requires owner approval. Not requested yet.

--- history-log.md ---
2026-06-15  Scoped weekly digest — defined v1 scope and boundaries
2026-06-15  Decision: plain text v1 — chose plain text over HTML
2026-06-15  Drafted job + builder — added send_weekly_digests() behind a flag
2026-06-15  Flagged double-send risk — missing guard if job re-runs in one week
```

---

That's the whole handoff. Compare the model's response to
[`expected-recovery.md`](expected-recovery.md).
