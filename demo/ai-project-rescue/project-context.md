# Project Context

Status: In progress
Sensitivity: Low
Project purpose: Add weekly digest emails to a fictional demo app.
Current state: Feature scoped; draft exists; production send not approved.
Next action: Review draft and decide whether to test in staging.

## Active decisions

- Plain-text digest for v1; HTML is out of scope.
- Send once per week per active user via the existing mailer abstraction.
- Gated behind a `WEEKLY_DIGEST_ENABLED` flag, default off.
- Develop against a local fake mailer only — no real recipients.

## Boundaries

- In scope: build the digest, render plain text, send via the mailer in dev.
- Out of scope: HTML templates, per-user send-time preferences, production sends.
- No real recipients, credentials, or external services.

## Source pointers

- Draft job: `app/jobs/weekly_digest.py` (fictional path)
- Digest builder: `app/digests/build_digest.py` (fictional path)
- Feature flag: `WEEKLY_DIGEST_ENABLED` (default off)

## Open questions

- How do we guard against double-sending if the weekly job re-runs in the same
  week? (Needs a "last sent" marker per user.)
- One combined digest vs. per-section digests? Leaning combined for v1.

## Unresolved high-consequence items

- Production email enablement requires owner approval. Not requested yet.
