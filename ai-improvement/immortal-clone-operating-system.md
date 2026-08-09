---
date: 2026-07-05
tags: [claude, fable-5, jarvis, prompt, source-pdf]
status: ready-for-you
source: Aprendio — "The Immortal Clone" (AI Operating System, Method No. 03)
---

# The Immortal Clone — Operating System Interview

> From the PDF at `~/Downloads/The_Immortal_Clone.pdf`. Prep done up to the
> point where **you** open a new chat with Fable 5 and run the interview —
> that part is yours to do live, since it's asking for your actual judgment,
> not something to fabricate on your behalf.

## The idea

Two ingredients for a useful AI clone:
1. **What you've already written down** — the vault, SOPs, docs. You have this.
2. **Everything that never made it into a document** — tiebreakers, instincts,
   values, voice. This interview extracts *that*.

## Prerequisite check (done)

The guide wants an agent already pointed at a knowledge vault before this
hooks into anything. That's already true here: Claude Code is pointed at
this mega-vault (`~/Documents/Obsidian`), and Jarvis (`~/code/jarvis`) reads
`memory/identity.md` + `memory/facts.md` as its grounding layer. ✓

## What to do

1. Open a **new chat with Fable 5** (`/model claude-fable-5` in Claude Code,
   or pick Fable 5 in claude.ai).
2. Paste the prompt below — both parts, as **one message**, exactly as-is.
3. Answer honestly. Vague in, vague out. Let it push back on shallow answers;
   that's the design, not a bug.
4. When it hands you the **OPERATING SYSTEM** doc at the end, save it — see
   Integration steps below.

## The pasteable prompt (verbatim, both parts as one message)

```
You are conducting a deep-context interview with me. Your goal isn't to collect facts about my life — it's to
extract how I actually think and decide, so the transcript can become the foundation for an AI agent that
reasons and communicates the way I do.

Run this as a real interview, not a form. Ask one question at a time. Wait for my full answer before moving on.
If an answer is generic, surface-level, or sounds like something anyone could say, push back with a specific
follow-up — ask for a real example, a number, a name, a moment — before you move to the next question. Depth on
fewer questions beats shallow coverage of all of them. Follow interesting threads even if they pull you off the
list below.

Work through these nine areas, in this order, adapting the exact questions to what I've already told you:

1. ORIGIN & FORMATION — the experiences, people, and reversals that shaped how I operate now.
2. DECISION-MAKING — my actual tiebreakers and rules when good options conflict, illustrated with a real recent
decision.
3. DOMAIN EDGE — what I know cold, where my expertise genuinely ends, and what beginners in my field always get
wrong.
4. VALUES & NON-NEGOTIABLES — what I won't do for money, what I optimize for when no one's watching, what it
takes to lose or earn my trust.
5. FAILURE & RECOVERY — the failure that taught me the most, what specifically changed after it, and how I tell
the difference between pushing through and cutting losses.
6. VOICE — the phrases I actually use, how I deliver bad news, what tone or style I can't stand.
7. TRUST & DELEGATION — how I decide who to trust with something important, what I delegate immediately, what I
never let go of.
8. VISION — what "done" looks like for what I'm building, and what I want said about how I operated once I'm
not in the room.
9. TEXTURE — the quirks, particularities, and stories that make me recognizable as me, not a generic executive.

Pacing: this should feel like a long conversation with someone genuinely trying to understand how I think, not
an intake form. Take as long as it takes — there's no question count to hit. If I give you a boring or vague
answer, don't accept it and move on; that's exactly where the real signal is hiding.

When we've gone deep enough on all nine areas — and only then — write me a structured document called my
OPERATING SYSTEM. Format it in markdown with one section per area above, written so it can be pasted directly
into another AI agent's system prompt or dropped into a knowledge vault as a grounding document. For each
section:

— State my actual decision rules and heuristics as reusable principles, not a biography of me.
— Preserve my real phrasing and voice wherever I said something distinctive — quote it.
— Flag anything you're inferring versus something I said directly, so I can correct it.
— Keep it honest to what I actually said. Don't smooth me into someone more impressive or more consistent than
I actually am — the contradictions are data too.

Start now. Ask me the first question.
```

## Integration (after Fable 5 hands you the doc — your move, not automatic)

1. **Save the doc.** Drop it into this vault — `ai-improvement/` fits, next to
   this note — or straight into `~/code/jarvis/memory/` alongside `identity.md`
   given the fold-into-Jarvis-memory decision above.
2. **Re-point the agent.** Re-index / restart Jarvis so it picks up the new
   file (or, if Claude Code, just make sure it's somewhere in the vault it
   already reads).
3. **Test it.** Ask a judgment call you never explicitly answered in the
   interview. If it reasons the way you would, ingredient two worked. If not,
   that's exactly what to add next round.
4. **Re-run it quarterly.** You change; the clone should too.

## Related

- [[fable-5-launch-prep]] — where this connects to Jarvis's `memory/identity.md`
- [[claude-improvement-notes]] — the "AI Second Brain Prompt" is a lighter
  cousin of this same idea
