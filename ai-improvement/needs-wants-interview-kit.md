---
date: 2026-07-08
tags: [ai-improvement, interview, jarvis, memory]
---

# Needs & Wants Interview Kit

Reusable methods for any Claude/Jarvis session to learn what Donovan actually
needs, wants, and prefers — extending the Immortal Clone interview
([[immortal-clone-operating-system]]) from a one-time extraction into a
standing system. Every method ends with answers landing somewhere durable;
an interview whose output only lives in a chat is wasted.

## Where answers go (the memory map)

| Kind of answer | Destination | Why |
|---|---|---|
| Identity, values, standing directives | `~/code/jarvis/memory/identity.md` (**you write it**, nothing else may) | First content in every Jarvis prompt, forever |
| Facts, preferences, current context | `/remember <fact>` in Jarvis → `memory/facts.md` | Injected every session, timestamped, prunable |
| Decision heuristics + voice | [[donny-operating-system]] | The clone-grounding doc |
| Weekly deltas | `jarvis/Surveys/YYYY-Www.md` (auto-created weekly) | Steers the self-improvement loop |
| Project-specific answers | The project's own vault note / blueprint | Context where builders look |

## Method 1 — The deep interview (yearly, or after a life change)

Already run once (2026-07-06 → donny-operating-system.md). Re-run when
something structural changes (senior year starts, first real income, new
sport season). Paste-able:

```
Interview me to update my operating-system document. Read
ai-improvement/donny-operating-system.md first. Then ask me questions ONE AT
A TIME, adapting to my answers, across: current priorities, what changed
since the doc was written, decision heuristics that proved wrong, new
non-negotiables, and anything I keep having to re-explain to AI sessions.
Don't flatter me, don't accept vague answers — push for the concrete version
("efficient" is not an answer; "under 20 min/day" is). When done, show me a
diff-style list of proposed doc updates and wait for approval.
```

## Method 2 — Project kickoff discovery (before any new build/plan)

The QUESTIONS-FIRST gate from the Blueprint Vault, generalized. Paste at the
start of any project planning session:

```
Before proposing anything: interview me about this project. Ask only
questions whose answers change what gets built — scope, what "done" means,
constraints (time/money/skill), what I've already tried, and what I'd do
with the result. One round, grouped, max 8 questions. Open with the line
QUESTIONS FIRST, then stop and wait. If a later answer contradicts an
earlier assumption, flag it instead of silently adapting.
```

## Method 3 — Taste calibration (when outputs keep missing)

For "technically right but not what I wanted" problems:

```
Generate 3 deliberately DIFFERENT versions of [the thing] — different in
approach, not wording. Label them A/B/C. Ask me to rank them and say one
sentence about why the winner won. Then state, in one paragraph, the taste
rule you learned ("Donovan prefers X over Y when Z") and give me the exact
/remember line to save it.
```

This is the highest-value-per-minute method: each round converts a vague
preference into a stored, reusable rule.

## Method 4 — The weekly delta (automated)

The Briefing component now writes `Surveys/YYYY-Www.md` on the first launch
of each week. Five questions, two minutes. Q2 ("what did you do by hand that
Jarvis should have done") and Q4 ("one capability to add") are the standing
needs-discovery channel — they feed the self-improvement loop directly
(`~/code/jarvis/SELF-IMPROVEMENT.md` §4).

## Method 5 — Contradiction audit (quarterly)

```
Read ai-improvement/donny-operating-system.md, ai-improvement/North Star.md,
and ~/code/jarvis/memory/facts.md. List every place they contradict each
other or contradict what I've actually done recently (check claude-mem for
the last month). For each contradiction: which side do I probably mean, and
what update resolves it? Don't fix anything — show the list and wait.
```

Memory that's never audited drifts into fiction; this keeps the stored
Donovan matching the real one.

## Ground rules for every method

- **One question at a time in interviews** — batch-dumping 20 questions gets
  shallow answers.
- **Concrete beats vague** — the interviewer's job is to refuse "better/
  faster/efficient" until it becomes a number, an example, or a comparison.
- **No flattery, no leading questions** (standing directive from the
  operating-system doc).
- **Always end with the write** — the last step of any interview is putting
  answers into the memory map above, or it never happened.
