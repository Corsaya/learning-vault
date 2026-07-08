---
date: 2026-07-07
tags: [capability-scouting, fable-5, monetization, content, ab-test-output]
---

# Side A output — real Fable 5, faceless content brand plan

Captured 2026-07-07 from a real `claude-fable-5` Claude Code session,
responding to the verbatim Main Task Prompt in
[[2026-07-07-fable5-clone-content-brand-test-prompt]]. Planning pass only —
no accounts, handles, or content created, per the prompt.

---

## The response

Before the five sections, one framing call that shapes all of them: **your
two content sources are not equal.** "AI/Claude Code tips" is a commodity
niche — thousands of accounts, mostly adults with credibility signals you
can't use while anonymous. But "watch an anonymous student build a
1,000-player Minecraft permadeath event with an AI workflow" is a *story*,
and short-form rewards serialized stories far more than tips. So the plan
inverts your assumed order: the Minecraft event build is the growth engine,
and the AI-workflow material is the *lead magnet layer* extracted from it.
Tips accounts have to earn every view from scratch; devlog serials get
followers who want episode 12 because they saw episode 11.

### 1. Brand name and niche strategy

**Niche: "AI-built Minecraft engineering" devlog** — the intersection, not
either half alone. Content pillars:

- **P1 — The event build serial (60–70% of posts).** "Day N of building a
  1,000-player permadeath event": one problem per video (how do you stop
  1,000 players from crashing one server tick? how does a fragment reveal
  work?), the AI-assisted solution, screen capture of it working. Minecraft
  is one of the largest content audiences alive; "I coded/built X" is a
  proven faceless format there; and the event gives you a built-in season
  arc with a finale.
- **P2 — Workflow extraction (20–30%).** "The exact prompt/setup I used to
  do that" — Claude Code patterns, the Obsidian second brain, the blueprint
  technique. This pillar exists mainly to *be gateable* (see §2) and to
  catch the AI-tools audience.
- **P3 — occasional TCG-automation or Jarvis clips as tests, only if P1/P2
  data says the audience wants more "AI lab" breadth. Don't start here.**

**Name:** pick something that reads as a *place/lab*, not a person, since
there's no face to brand. Three candidates meeting the criteria (sayable,
spellable from hearing it, no existing-handle collision risk, works even if
you later drop Minecraft): **"Fragment Labs"** (nods to the event's nine
fragments without leaking specifics), **"The Anvil Room"**, **"Redstone &
Reason"**. My pick is **Fragment Labs** — it makes the event serial feel
native and still fits generic AI-build content. Check handle availability on
all three platforms before committing, and — anonymity rule — it must share
zero tokens with any existing username, email, or gamertag you've ever used.

### 2. The gated lead-magnet funnel, end to end

**What to gate:** rotate 2–3 magnets, all things you already have or produce
as exhaust: (a) the **Blueprint prompt pack** (mining prompt + template +
loop, once you've dogfooded it), (b) a **Claude Code starter config** (a
sanitized CLAUDE.md + hooks + 3 skills), (c) later, an **event-tech
breakdown doc** for the Minecraft audience. One magnet live at a time;
retire and swap when comment rates fade.

**The funnel, concretely:**
1. Video ends: "comment BLUEPRINT and follow — I'll DM you the pack."
2. **Instagram:** ManyChat free tier auto-DMs the link on keyword comment —
   this is the standard mechanic and why IG is your *primary* platform for
   the gate. **TikTok:** no reliable auto-DM at small scale — route TikTok
   viewers to "link in bio" instead (Beacons free tier), same destination.
   At <50 comments/day you can also just DM manually; that's 10 min/day and
   it converts *better* (people reply to a human-feeling DM).
3. The DM/bio link lands on a **free-tier landing page (Beacons or
   Carrd-free) that asks for an email to deliver the file.** This step is
   the whole business: followers are platform-hostage, an email list is
   yours. Deliver via an automated welcome email (MailerLite free tier,
   ≤1,000 subs).
4. **End goal — corrected from your framing:** the audience is not the
   asset; the *email list* is. Path to money: once the list clears ~100–200
   subs, offer a $5–15 paid pack (expanded blueprint library, the "full"
   config, an event-tech deep dive). Four sales a month clears $20. Later,
   the same list is the launch audience for anything else you build.

**Two honest warnings:** (a) "comment X for the link" sits close to
engagement-bait under platform ToS; it's tolerated at massive scale daily,
but keep the magnet genuinely load-bearing so it survives as "value" not
"bait". (b) **You're a minor — Gumroad/Stripe/most payment rails require
18+.** The monetization leg needs a parent-held account or waiting until
the list is built. Build the list now, solve payments when there's something
to pay for; do not fake an age on a payment processor.

### 3. Posting cadence you can actually sustain

Assume school + crew + restaurant shifts + the event project itself. The
event project is the trick: **the content is a byproduct of work you're
already doing** — a devlog costs you capture + assembly, not ideation.

- **Floor (school weeks): 2 shorts/week** (one P1, one P2), batch-produced
  in a single ~2-hour weekend block: script both with Claude from the
  week's build notes, record captures, assemble.
- **Ceiling (summer/breaks): 4/week.** Never promise daily anywhere.
- **YouTube: 1 long-form/month**, a compilation cut of that month's shorts
  plus connective narration — archive layer, near-zero extra footage.
- Post the same short to TikTok + Reels + YT Shorts (native uploads, not
  cross-watermarked). Rule of thumb: if a week collapses, post one P1 and
  skip P2 — the serial must never break two weeks in a row, because the
  serial is the retention engine.

### 4. What to set up and learn

**Accounts (all free):** new email address for the brand (nothing linked to
existing identities) → TikTok, Instagram, YouTube, Beacons, MailerLite,
ManyChat free tier. **Tools:** OBS (free, screen/gameplay capture — you're
on Linux, it's native), **CapCut desktop or Kdenlive** for assembly +
auto-captions (free; captions are non-negotiable, most shorts play muted),
TTS for narration — you can run local TTS on your box (Kokoro/Piper) for a
consistent synthetic voice at $0, which doubles as an anonymity layer.
Thumbnails/title cards from your existing AI stack.

**Pipeline (idea → posted):** build-log note in Obsidian → Claude turns the
week's log into 2 hook-first 45-second scripts → OBS captures while you do
the real work → TTS the narration → CapCut: assemble, captions, hook in
first 1.5s → export 9:16 → native upload ×3 platforms → log performance in
a vault note (views/follows/comments-per-post) for the weekly review.

**To learn (in order, ~2 weeks of doing not studying):** (1) short-form
grammar — hooks, pacing, cut every 2–3s: learn by deconstructing 20 top
devlog/AI shorts, write down their first sentence; (2) CapCut basics — one
evening; (3) OBS scene setup — one evening. Skip color grading, motion
graphics, and gear entirely.

**Anonymity checklist:** fresh email; VO is synthetic only; never screen-
record the vault with real-name files visible (use a demo profile or crop);
strip metadata from uploads; never mention school, city, restaurant, or the
event's private details before they're public.

**Total cost: $0/month** (all free tiers) — optional later: ~$12/yr domain.
Nothing in this plan spends money before money comes in.

### 5. Timeline to first $20/month + kill criteria

Honest numbers, not hype: faceless accounts that work usually show a pulse
fast but pay slow. **Realistic first-$20 month: month 3–5**, via the $5–15
pack to the email list — not platform ad programs (TikTok's rewards program
needs 10k followers; don't plan around it).

- **Weeks 1–4 (16 posts in):** *working* = at least one post >2–3k views,
  follower count converting at all (>1 follow per 100 views), comment
  keyword getting used. *Not working* = flat <200 views across 16 posts →
  that's a hook/format problem, not a niche problem yet; iterate hooks
  first (change the first 1.5 seconds before changing anything else).
- **Month 2–3:** *working* = 500–1,000 followers on the best platform,
  50–150 emails captured, one magnet with >30% comment→email conversion.
  *Not working* = views fine but nobody comments/converts → the magnet is
  wrong, swap it (the audience is telling you what they want gated).
- **Month 3–4:** first paid offer to the list. $20/mo = 2–4 sales. *Working*
  = any sales at all from <200 subs (unusually good). *Not working after
  month 5* = engaged views but zero conversion after two magnet swaps and
  one price test → pivot the *monetization* (e.g., a Ko-fi tip layer or a
  bigger product later), keep the audience engine.
- **Hard kill:** if after ~40 posts and two format overhauls nothing has
  ever broken 1k views, the P1 bet is wrong — fall back to pure Minecraft
  event content (biggest raw audience) and drop the AI framing, rather than
  quitting entirely; the event finale is a guaranteed content spike you'll
  want an account existing for.

**Assumptions I made (flag any):** the Minecraft event details are okay to
show publicly at devlog granularity once the event is announced; your crew
is fine with the event being content; "AI generates video" in your setup
means captures + TTS + assembly, not full text-to-video (the plan doesn't
need it).

That's the full plan and reasoning. Ready for your go-ahead — first
concrete step when you give it: check the three handle candidates for
availability, then set up the brand email + OBS + CapCut, before touching
any account creation.

---

## Notes for the A/B comparison (meta, not part of the response)

- Held at planning stage: yes — no accounts/assets created.
- Distinctive choices to compare vs Side B: inverted the niche assumption
  (Minecraft devlog serial as engine, AI tips demoted to lead-magnet
  layer); email list framed as the real asset over follower count; platform
  asymmetry handled (ManyChat on IG vs link-in-bio on TikTok); flagged the
  minor/payment-processor blocker; $0 hard budget with local TTS as both
  cost and anonymity play; kill criteria separate hook-failure from
  niche-failure from magnet-failure.
- Over/under-scope check: cadence floor is 2/week batch-produced; no paid
  tools anywhere; learning path is 3 concrete items, two evenings + one
  deconstruction exercise.
