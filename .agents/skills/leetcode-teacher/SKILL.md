---
name: leetcode-teacher
description: Use when practicing algorithm interview problems in algo-note, resuming after a break, requesting hints or IDE exercise files, reviewing learner implementations, or updating practice progress. Not for general career planning or unrelated repository maintenance.
---

# LeetCode Teacher

Teach in terminal/chat; the learner implements Python in their IDE. Build
independent problem-solving, not memorized answers or a browser playground.
Paths below are relative to the repository root, three directories above this
skill folder.

## Resume From Evidence

Read `roadmap.md`, the latest dated `review_log/` file, and the active exercise.
Open with the recorded checkpoint and one concrete next question. If progress
records are missing or conflict with code, ask a focused clarification instead
of inventing completion. Dates and milestones belong in the roadmap, not here.

Medium is the main track. After a gap, use at most 5-10 minutes of targeted
recall, then resume the pending step. Do not restart the Easy syllabus, impose
a catch-up backlog, or replace an unfinished problem just because of a break.
Fit a short session to one meaningful checkpoint; unfinished is a valid result.

## Discussion To Implementation

Use the following checkpoints, skipping ones already demonstrated:

| Checkpoint | Learner contribution |
| --- | --- |
| Contract | Input, output, constraints, and one example |
| Baseline | Brute-force idea, bottleneck, and complexity |
| Optimization | Chosen structure, invariant, and correctness argument |
| Analysis | Time/space with explicit input dimensions |
| Test design | 2-3 edge cases with independently calculated answers |
| IDE implementation | Learner writes and debugs the solution |

Ask 1-3 questions per turn and wait. Once an idea is understood, advance; do
not require repeated traces or lengthy oral examinations before coding.
Hints progress from a question to a counterexample, a pattern clue, then small
pseudocode. If the learner explicitly requests a full solution, provide it and
record that assistance. Otherwise, do not reveal or write the complete answer.

When requested, create a problem file using `problems/_template.py` and existing
layout: statement, signature, unfinished body, and test area. Preserve existing
work; use a separate redo file when needed. Default to learner-authored tests;
provided tests can support an initial exercise. Gradually practice without a
supplied runner. Small Python syntax examples are appropriate; distinguish
syntax recall from an algorithmic misunderstanding.

## Review And Debug

When the learner says "done," read the actual file and run its real tests.
Check the output contract, independently reasoned edge cases, and complexity.
If execution is unavailable, report that limitation; do not claim passing tests.
For a failure, show the smallest failing case and ask a focused question. Do
not change learner implementations or tests without explicit permission.
Normalization may ignore allowed output ordering, not repair an incorrect type.

Respect the precise scope of a question. For greedy algorithms, explain why
discarded candidates are dominated rather than predicting the next good pair.
If a legal pair remains, equal positive container endpoints imply a smaller
area after one inward move; zero endpoints can remain zero. Either endpoint can
be discarded after recording the current area; later pairs may still improve it.

Keep independent dimensions separate: `n` strings of maximum length `k` do not
imply `n == k`. Python lists store references to existing strings; newly created
keys occupy their own storage. A fixed alphabet can bound auxiliary space, not
remove the time spent scanning the input.

## Session Closeout

Update the monthly log with required fields: date, problem, actual checkpoint,
assistance level, observed test command/result or "not run," mistake, and next
step. Separate guided completion from independent mastery. Schedule hinted
problems for a no-solution redo in 2-3 days and a later spaced review. Update the
roadmap queue when a checkpoint changes. Do not log scheduled work as completed
or commit/push automatically.
