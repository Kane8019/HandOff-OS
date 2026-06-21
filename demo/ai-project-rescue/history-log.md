# History Log

| Date | Event | What changed | What it replaced/superseded | Source pointer |
|---|---|---|---|---|
| 2026-06-15 | Scoped weekly digest | Defined v1 scope and boundaries for the digest email | Replaced vague "send weekly emails" idea | chat-1-scope.md |
| 2026-06-15 | Decision: plain text v1 | Chose plain-text body over HTML for the first version | Superseded "start with HTML" assumption | This file |
| 2026-06-15 | Drafted job + builder | Added `send_weekly_digests()` and `build_digest()` behind a flag | Replaced no-digest behavior | `app/jobs/weekly_digest.py` |
| 2026-06-15 | Flagged double-send risk | Noted missing guard against re-running the job in one week | — | project-context.md (open questions) |
