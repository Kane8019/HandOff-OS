# The dual-AI workflow

HandOff-OS works well with two AI roles plus one human. The roles can be played
by any tools; the names below are just a common pairing.

```text
ChatGPT scopes  →  Claude drafts/builds  →  ChatGPT reviews  →  Human approves
                                                                      │
                                                       durable state checkpointed
```

## The four steps

1. **ChatGPT scopes the task and boundaries.**
   Before any building happens, frame the work: the goal, what's in scope,
   what's explicitly out, and what "done" looks like. Capture the result in
   `project-context.md` (boundaries, next action) or, for a specific action, in
   `proposal.md`.

2. **Claude drafts or builds within that scope.**
   The builder produces the artifact — text, code, a plan — staying inside the
   boundaries that were set. If the boundaries turn out to be wrong, that's a
   signal to go back to step 1, not to quietly expand scope.

3. **ChatGPT reviews the result.**
   A reviewer checks the artifact against the scope using
   [`review.md`](../templates/review.md): is it in scope, are the load-bearing
   claims sound, are sources present, what should change? The verdict is one of
   `PASS / REVISE / BLOCKED / OUT_OF_SCOPE`.

4. **The human owner approves execution or publication.**
   Review is advice. Approval is a decision, and it belongs to a person.

5. **Durable state is checkpointed outside the chat.**
   Update `project-context.md` and add a line to `history-log.md`. Now the work
   is recoverable regardless of what happens to the chats.

## When to skip review

Skip the review step for **low-consequence actions** (see
[risk-tiers.md](risk-tiers.md)). If the action is easily reversible and nobody
outside the workspace sees it, a review is just friction. Draft it, do it, and
note anything worth keeping.

## When review is useful

Add a review when the action is **high-consequence**: hard to reverse,
outward-facing, or touching money, legal matters, or other people's data. There,
a second perspective before the human approves catches expensive mistakes
cheaply.

## Why repeated AI-checks-AI loops are usually bad

It's tempting to wire the builder and reviewer together so they iterate
automatically until they "agree." Resist this.

- **Agreement isn't correctness.** Two models can converge confidently on
  something wrong. A loop that runs until they agree optimizes for agreement,
  not truth.
- **It hides the decision.** The whole point is that a *human* owns the call.
  An automatic loop quietly removes the human from the only step that needs them.
- **It burns effort without adding signal.** After the first good review, extra
  rounds mostly reword. One sharp review beats five polite ones.

So: one AI may draft and another may review, but **do not create automatic
AI-checks-AI loops**. Use a single review pass when it's warranted, then bring
it to the human.

> The human owner is the only approver.
