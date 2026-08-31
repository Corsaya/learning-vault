---
title: Codex Usage and Context Protocol
date: 2026-08-31
tags: [ai-improvement, codex, usage, context, workflow]
status: active
sources:
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/reference/java/resources/responses/methods/compact
  - local: /home/donovan/code/usage-monitor
---

# Codex Usage and Context Protocol

## What the monitor showed

Snapshot taken 2026-08-31 around 15:53 EDT with:

```bash
cd ~/code/usage-monitor
python -m ccdash --chatgpt --json
```

| Window | Requests | Input | Cached input | Output | Total tokens | Recorded plan use |
|---|---:|---:|---:|---:|---:|---:|
| Current five-hour block / today | 53 | 121,995 | 3,092,224 | 18,704 | 3,232,923 | 13% |
| Last seven days | 480 | 1,534,323 | 46,416,128 | 200,039 | 48,150,490 | 2% |

These are local Codex rollout-log counts plus the newest plan-limit snapshot the client recorded. They do not include ordinary ChatGPT web conversations. Raw token totals are not equivalent to plan percentage: model, task complexity, reasoning, tools, execution location, and cached context all affect usage.

Quick check:

```bash
cd ~/code/usage-monitor
python -m ccdash --chatgpt --brief
```

Use the monitor at the start and end of a substantive session or when usage changes unexpectedly. Running it after every response adds noise without improving decisions.

## Operating protocol

### 1. One objective per thread

Keep closely related follow-ups together, but start a new thread when the objective changes materially. Do not make one permanent conversation carry unrelated Git repair, school planning, product research, and code implementation indefinitely.

### 2. Close major milestones with a handoff

Before leaving a long thread, ask for a compact continuation note containing only:

```text
Objective:
Completed:
Verified state (commits, branches, tests, paths):
Decisions and constraints:
Unfinished work:
Exact next action:
Files to read first:
```

Save the handoff in the owning vault when it has durable value. Start the next thread with the handoff and the new request. Do not paste the full conversation unless exact wording is required.

### 3. Understand what clearing does

Deleting, clearing, or hiding a conversation does **not** refund usage already consumed in the current plan window. Starting a fresh conversation from a compact handoff can reduce future carried context. The benefit is prospective, not retroactive.

Codex/API compaction is designed for long, tool-heavy workflows. Official guidance recommends compaction after meaningful milestones rather than after every turn. A human-readable handoff is still valuable because it is auditable and portable even when product-managed compaction is opaque.

### 4. Match model and reasoning to the work

- Use GPT-5.6 Sol for complex architecture, risky migrations, difficult debugging, and work where mistakes are expensive.
- Use GPT-5.6 Terra for ordinary implementation and analysis when available.
- Use GPT-5.6 Luna for inventories, formatting, extraction, simple lookups, and other high-volume routine work when available.
- Start routine work at low or medium reasoning. Increase reasoning only when the task demonstrates a quality need.
- Reserve `max` or pro-style work for genuinely difficult cases; they explicitly trade more usage and latency for quality.

This is a routing rule, not a claim that the cheapest model is always adequate. Compare outputs on representative tasks before making a default permanent.

### 5. Reduce irrelevant context before reducing useful context

- Point to the smallest relevant folder or set of files.
- Ask for read-only diagnosis before implementation when the cause is unknown.
- Batch related questions and approvals.
- Keep generated logs, large exports, and binary files out of prompts unless the task needs them.
- Give success criteria and boundaries once, concretely.
- Reuse durable summaries instead of repeatedly re-deriving the same architecture.

## Plugins and tooling

The existing local `ccdash --chatgpt` mode is the verified measurement tool. It reads local Codex session logs and recorded limit snapshots without sending credentials or telemetry.

No usage-reduction plugin was verified in the available plugin catalog during this review because plugin search was not exposed to the session. Do not install a plugin merely because it advertises “context optimization.” Verify its permissions, what data it reads, whether it makes extra model calls, and whether measured plan usage actually falls on representative work.

A plugin does not reduce usage merely by existing. Plugins and connectors can increase tool calls and returned context. Adopt one only if it measurably prevents larger repeated reads or manual rework.

## Review trigger

Re-run a seven-day comparison after one week of using milestone handoffs. Record:

- requests;
- uncached input;
- cached input;
- output;
- five-hour and seven-day plan percentages;
- number of completed substantive objectives.

Token reduction without completed work is not an improvement. The useful measure is plan usage per completed objective.
