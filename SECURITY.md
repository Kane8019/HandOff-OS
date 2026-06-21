# Security

HandOff-OS is a documentation-first project with a small, local-only CLI.

## What HandOff-OS does and doesn't do

- It does **not** process credentials, tokens, or secrets.
- It does **not** connect to any external service.
- It makes **no network calls**.
- The CLI only creates local Markdown files from bundled templates.

Because of this, the main "security" concern for HandOff-OS is **not leaking
private data into a public repository**.

## Do not submit private data

Please do not put private or sensitive information into public issues, pull
requests, examples, or screenshots. This includes real legal facts, personal
data, lab/sample/server/customer identifiers, financial documents,
credentials, tokens, or private links.

All examples in this project must be synthetic or heavily redacted.

## Reporting a private-data exposure concern

If you believe private data has been committed to this repository, or you find
a security-relevant issue, report it through the most private channel available,
in this order:

1. **GitHub private vulnerability reporting**, if it is enabled for this
   repository (repository **Security** tab → **Report a vulnerability**). This
   keeps the report confidential.
2. **If no private channel is available,** open a **minimal public issue**
   without any sensitive details — for example, "possible private-data exposure
   in file X." Do **not** paste the sensitive content into the issue; naming the
   file is enough to start the conversation without making the exposure worse.

Until a dedicated security contact is published, the steps above are the
supported reporting path.
