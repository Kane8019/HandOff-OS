# GitHub workflow

A simple, manual GitHub rhythm that fits the HandoffOS roles. No automation, no
bots, no AI with write access. The human owner merges.

```text
issue / proposal  →  branch  →  local draft/build  →  review  →  owner approval  →  merge
```

## The steps

1. **Open an issue or write a proposal.**
   State the goal, the decision needed, and what's in and out of scope. For
   anything high-consequence, fill in
   [`proposal.md`](../templates/proposal.md) and attach or paste it into the
   issue.

2. **Create a branch.**
   One branch per unit of work. Name it for the change, e.g.
   `feature/booking-confirmation-email`.

   ```bash
   git switch -c feature/booking-confirmation-email
   ```

3. **Draft or build locally.**
   This is the builder's step. Produce the change on the branch. Keep commits
   small and described in plain language.

4. **Review.**
   Open a pull request and review it against the scope using
   [`review.md`](../templates/review.md). The verdict is one of
   `PASS / REVISE / BLOCKED / OUT_OF_SCOPE`. Reviewers comment; they do not merge.

5. **Owner approval.**
   The human owner reads the review and decides. Approval is explicit — a comment
   like `Approved to merge` or a formal PR approval. This is the only step that
   authorizes the change to land.

6. **Merge.**
   After approval, merge the branch and delete it. Then **checkpoint durable
   state**: add a line to [`history-log.md`](../templates/history-log.md) and
   update [`project-context.md`](../templates/project-context.md) so the next
   chat knows where things stand.

## Authority model

- **Builder** writes code on a branch. No direct pushes to the main branch.
- **Reviewer** comments and gives a verdict. No merge rights needed.
- **Owner** approves and merges. The owner is the only approver.

This mirrors the dual-AI workflow: an AI can draft on the branch, another can
review the PR, but the human owner is the one who approves and merges. There is
**no automatic AI-checks-AI loop** and no AI with merge authority.

## Keeping it public-safe

- Don't put private data in issues, PR descriptions, commit messages, or
  screenshots.
- Use source pointers for sensitive material instead of pasting it.
- Examples committed to a public repo must be synthetic or heavily redacted.
