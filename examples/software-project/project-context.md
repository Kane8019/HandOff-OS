# Project Context

Status: In progress
Sensitivity: Low (public-safe demo, no real systems)
Project purpose: Add a booking-confirmation email to a small web app so users
get a receipt after they reserve a slot.
Current state: Feature drafted on a branch. Email template and send logic exist
behind a feature flag; not yet enabled in production.
Next action: Review the draft against scope, then have the owner approve
enabling the flag in staging.

## Active decisions

- Send the confirmation **synchronously** for v1 (small volume); revisit a queue
  later if volume grows.
- Use a plain-text email body for v1; HTML formatting is out of scope.
- Confirmation includes booking id, date/time, and a cancel link. No marketing
  content.

## Boundaries

- In scope: confirmation email on successful booking.
- Out of scope: reminder emails, cancellation emails, HTML templates, retries.
- No real provider credentials in the repo — use a local fake mailer in dev.

## Source pointers

- Feature branch: `feature/booking-confirmation-email`
- Draft template: `app/emails/booking_confirmation.txt` (fictional path)
- Booking flow: `app/bookings/create.py` (fictional path)

## Open questions

- Should the cancel link expire? (Leaning yes, but out of scope for v1.)
- What from-name should production use? Owner to decide before enabling.

## Unresolved high-consequence items

- Enabling the flag in production is high-consequence (outward-facing email to
  real users). Requires owner approval — not yet given.
