# Proposal

## Goal

Send a booking-confirmation email to users after a successful reservation so they
have a receipt and a way to cancel.

## Decision needed

Approval to enable the confirmation-email feature flag in **staging** for a test
run, ahead of a later production decision.

## Scope

- Plain-text confirmation email on successful booking.
- Contents: booking id, date/time, cancel link.
- Behind a feature flag; enabled in staging only.

## Out of scope

- Reminder and cancellation emails.
- HTML email templates.
- Retry/queue infrastructure.
- Enabling in production (separate, later approval).

## Reversibility

High in staging — the flag can be turned off instantly and staging sends only to
test addresses. No real users affected.

## Risks

- Misformatted email or wrong link → low impact in staging, caught before prod.
- Accidentally pointing staging at a real mailer → mitigated by using the local
  fake mailer / test addresses only.

## Requested approval

Owner approval to enable the flag in staging and run one end-to-end test booking.

## Execution notes

After approval: enable flag in staging config, make one test booking, confirm
the email renders correctly, then disable the flag and log the result. Production
enablement is a separate proposal.
