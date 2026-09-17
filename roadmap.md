# Google Application And Interview Practice Roadmap

Updated: 2026-09-17. This replaces the earlier six-month practice schedule.

Career source of truth:
[big-tech-18mo-roadmap.md](../plans/OKR/big-tech-18mo-roadmap.md), current decision.
Submit the Google application on **2026-10-15**; target interview readiness by
**2026-12-17**, three calendar months from this update. An invitation and its
timing depend on recruitment. If an interview is scheduled earlier, prioritize
that date and reassess gaps immediately. Do not wait for full syllabus mastery
to prepare or submit the resume.

## Operating Rules

- Medium is the main track; targeted Easy recall takes at most 5-10 minutes.
- Discuss in terminal/chat, implement in the IDE, and use progressive hints.
- Advance after understanding; avoid repeatedly restarting familiar topics.
- Record assistance and real test evidence, not just a solved counter.
- Redo guided problems without the solution in 2-3 days, then about a week later.
- Treat the topic sequence as an adjustable coverage plan, not a hiring rubric.

Teaching details live in [.agents/skills/leetcode-teacher/SKILL.md](.agents/skills/leetcode-teacher/SKILL.md).

## Weekly Rhythm

Target **6-8 focused algorithm hours**. Resume and career work are separate.

| Session | Work |
| --- | --- |
| Three weekday blocks, 60 minutes each | New Medium or complete a pending implementation; include a short due review |
| One weekday block, 45-60 minutes | Timed Medium attempt or spoken walkthrough, followed by a retrospective |
| One weekend block, 2-3 hours | Another Medium, weak-pattern practice, and remaining spaced review |
| Weekly closeout, 15-30 minutes | Inspect evidence, update queue, choose next week's weak point |

Expected throughput: **3-4 new Medium problems, two reviews, and one timed
walkthrough** per week. A timed problem can count as a new problem; do not stack
these as separate quotas. Unfinished attempts carry forward. From November,
replace some new-problem blocks with a second mock rather than adding hours.

Busy-week floor: two 30-45 minute blocks, one pending/new Medium checkpoint and
one review. This preserves continuity, but is not equivalent to the accelerated
target. After two low-time weeks, reduce coverage or reassess the readiness
date. Do not create a catch-up backlog.

## Phase 1: September 17 - October 14

Recover implementation fluency while extending known patterns. Complete the
current Two Pointers problem, then cover Sliding Window, Stack, Binary Search,
and introductory Tree DFS/BFS. Use Hash Map reviews only where needed.

Suggested next problems: Container With Most Water, Longest Substring Without
Repeating Characters, 3Sum, Daily Temperatures, and a binary-search variation.
Add one lightweight timed walkthrough weekly starting now, without expecting
immediate independent success.

Career checkpoints run in parallel: resume draft by October 1, review and
role/referral route by October 8, application on October 15. Existing resume
work should be refined rather than restarted.

## Phase 2: October 15 - November 11

Continue practice after applying. Cover Tree DFS/BFS, Heap / Top K, Intervals,
Linked Lists, and Graph BFS/DFS. Include basic topological ordering if graph
fundamentals are stable. Reuse patterns across different statements and track
which steps still require hints. Keep weekly timed practice and due reviews.

## Phase 3: November 12 - December 17

Focus on Backtracking, basic Dynamic Programming, and remaining graph gaps.
Example DP progression: House Robber, Coin Change, then a sequence problem if
ready. Hard problems and exhaustive catalog completion are not prerequisites.

Use two timed/mock blocks weekly, replacing part of new-topic work. Rehearse
clarifications, correctness arguments, complexity, and hand-calculated edge
cases. Review misses before opening additional advanced topics.

## Readiness Check

During the final two weeks, attempt at least four previously unseen Medium
problems across different covered patterns in 35-45 minute sessions. Record
hint level and results for each. Look for repeated evidence of independent
pattern selection, a sound correctness argument, executable code, correct
TC/SC, and self-designed tests. This is a local diagnostic, not a guarantee of
passing Google's interviews. Repeated dependence on major hints remains a gap.

Broader readiness also includes resume/project storytelling and role-appropriate
design preparation, owned by the career plan rather than this algorithm repo.

## Current Queue

1. **Container With Most Water: active.** Reasoning discussion complete;
   `problems/medium/container_with_most_water.py` is still a skeleton. Next:
   design three cases with expected answers, then implement in the IDE.
2. **Group Anagrams: spaced review due 2026-09-20.** September 17 redo passed
   after guided recall; independent mastery remains to be demonstrated. Do not
   repeat the entire discussion before finishing the active problem.
3. Longest Substring Without Repeating Characters.
4. 3Sum.
5. Daily Temperatures, then Binary Search / Tree basics as coverage requires.

Actual attempts and evidence: [2026-09 practice log](review_log/2026-09.md).
