# History Log

| Date | Event | What changed | What it replaced/superseded | Source pointer |
|---|---|---|---|---|
| 2026-06-10 | Scoped feature | Defined booking-confirmation email scope and boundaries | Replaced vague "send emails" idea | Issue #42 (demo) |
| 2026-06-12 | Drafted email template | Added plain-text confirmation body | — | `app/emails/booking_confirmation.txt` |
| 2026-06-15 | Wired send logic behind flag | Confirmation sends on successful booking when flag on | Replaced no-confirmation behavior | `feature/booking-confirmation-email` |
| 2026-06-18 | Decision: sync send for v1 | Chose synchronous send over a queue | Superseded earlier "use a job queue" assumption | This file |
