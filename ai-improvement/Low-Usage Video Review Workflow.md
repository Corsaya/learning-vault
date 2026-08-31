---
tags: [ai-improvement, workflow, video-review, usage-efficiency]
---

# Low-Usage Video Review Workflow

Use this process when asking an AI to review gameplay or another long video. The goal is to keep visual analysis focused without repeatedly sending the full recording or a growing collection of frames through the conversation.

## Principle

Video clipping and frame extraction happen locally and do not require model usage. Usage grows when the model must repeatedly process a long conversation, many images, or densely sampled footage.

Treat review as a funnel:

`full recording -> sparse overview -> candidate moments -> dense inspection -> short reference clips`

## Workflow

1. Start a fresh conversation for each recording or tightly related batch.
2. Provide:
   - the local video path;
   - your character or subject;
   - the opponent or context;
   - one primary review goal.
3. Run a sparse first pass locally:
   - sample one frame every 5–10 seconds;
   - combine the frames into 3–5 contact sheets;
   - identify match boundaries and large momentum swings.
4. Select approximately 3–6 important exchanges:
   - stock losses;
   - successful adaptations;
   - repeated neutral situations;
   - recovery or edgeguard decisions;
   - obvious execution failures.
5. Inspect only those exchanges more densely, usually around one frame per second. Use full-rate playback only when exact sequencing or inputs matter.
6. Cut short, silent reference clips locally with `ffmpeg`.
7. Save the clips with descriptive names and index them in an Obsidian note with:
   - original timestamp;
   - situation;
   - one question to study;
   - the preferred alternative.
8. End with no more than three priorities for the next session.
9. Record again and compare the same situations instead of requesting another unrestricted full-video review.

## Copy-paste request

> Review this recording without audio: `[VIDEO PATH]`. I am `[CHARACTER / PLAYER]` against `[OPPONENT / CONTEXT]`. My primary goal is `[ONE GOAL]`. Use the low-usage review funnel: sparse contact sheets first, then densely inspect only the most instructive exchanges. Give me short clip timestamps, cut silent reference clips locally, and finish with no more than three priorities.

## Clip guidelines

- Prefer 10–30 second clips centered on one decision.
- Include 2–4 seconds before the decision so the available information is visible.
- Keep both successful and unsuccessful examples for comparison.
- Preserve 60 FPS when controller inputs or fast interactions matter.
- Use compact H.264 MP4 for Obsidian playback; 960×540 is usually sufficient.
- Do not embed the full source recording in the vault unless it has durable value.

## Review questions

1. What information was available before the commitment?
2. Was the follow-up guaranteed, or should the player have reset position?
3. In disadvantage, was the player trying to escape or immediately retaliate?
4. Did positioning cover more options than chasing would have?
5. Is the mistake strategic, or did execution prevent the intended decision?

## Usage monitoring

For local ChatGPT/Codex usage:

```bash
cd ~/code/usage-monitor
python -m ccdash --chatgpt
python -m ccdash --chatgpt --brief
python -m ccdash --chatgpt --json
```

The monitor reads local Codex rollout logs under `~/.codex/sessions`. It reports per-request token usage plus the latest locally recorded 5-hour and 7-day Codex utilization. It does not include unrelated browser conversations on chatgpt.com.

## Efficiency rules

- Start a new thread when changing recordings or review goals.
- Do not carry dozens of old contact sheets into later reviews.
- Ask for one primary analytical objective at a time.
- Reuse saved reference clips instead of reopening the full recording.
- Prefer timestamps and compact notes over repeated visual re-analysis.
- Track uncached input separately from cached context; raw token traffic alone does not equal plan utilization.

## Related

- [[Home|AI Improvement]]
- [[../Entertainment/Video Games/Super Smash Bros. Melee/Gameplay Reviews/Home|Melee Gameplay Reviews]]
