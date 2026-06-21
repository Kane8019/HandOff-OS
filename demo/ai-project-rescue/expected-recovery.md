# Expected recovery

A good resume from the recovery prompt looks like this. It's grounded entirely in
the two state files — no invented details, no re-litigating settled decisions.

---

**Where the project stands**

You're adding a weekly digest email to a demo app. The feature is **scoped and
drafted but not live**: there's a `send_weekly_digests()` job and a
`build_digest()` helper, gated behind `WEEKLY_DIGEST_ENABLED` (default off) and
pointed at a local fake mailer. v1 is plain-text only.

**The single next action**

Review the existing draft and decide whether to test it in staging. Before that
can be useful, the open **double-send guard** needs a plan — the job currently
has no protection against re-running in the same week, so a re-run would email
users twice.

**Active boundaries and high-consequence items**

- Stay in scope: build digest → render plain text → send via the mailer **in
  dev**. HTML, per-user send times, and production sends are out of scope for v1.
- No real recipients, credentials, or external services.
- **High-consequence:** enabling production email sends requires **owner
  approval**, which has not been requested. Do not enable it.

I'll wait for your go-ahead before proposing changes.

---

## Why this counts as a successful rescue

- The new chat recovered the project from **durable state**, not a transcript.
- It correctly carried forward the **decisions** (plain-text v1, flag-off,
  fake mailer), the **next action**, and the **open question** (double-send).
- It respected the **boundary** that production is not approved — the single most
  important thing not to get wrong.
- It did **not** hallucinate company names, recipients, or commitments that were
  never in the state files.

That's the whole value: a couple of screens of Markdown let any chat, any model,
resume the work correctly in about a minute.
