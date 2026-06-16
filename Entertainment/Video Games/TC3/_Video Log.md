# TC3 Video Log

> Every TC3 video processed (or queued), so we never re-fetch the same one. **Method** = how content was extracted.
> Stat-currency legend: 🟢 recent (≥2024) · 🟠 old (2020–2023) · 🔴 very old (≤2019).

| Video | Uploaded | Len | Method | Status | Note |
|---|---|---|---|---|---|
| [Win in 30 Minutes (PI)](https://www.youtube.com/watch?v=ymJqbdNUFWc) | 2020-04-02 | 27:10 | Captions | ✅ Done → [[Guide - Win in 30 Minutes Rush (PI)]] | 🟠 |
| [Beginner Tips (Mike)](https://www.youtube.com/watch?v=K6HQZJz-Nc4) | 2019-07-30 | 11:22 | Captions | ✅ Done → [[Guide - Beginner Tips (Mike, 2019)]] | 🔴 oldest |
| [Basics Tutorial](https://www.youtube.com/watch?v=T5-E5dJqnz0) | 2021-01-16 | 13:27 | Captions | ✅ Done → [[Guide - Basics Tutorial (2021)]] | 🟠 price-drift goldmine |
| [Fighting the unbeatable duo (woof1977)](https://www.youtube.com/watch?v=URiNtrLAfcc) | 2024-09-12 | 30:23 | Frames (HUD) | ✅ Done → [[Match - woof1977 2v2 naval (URiNtrLAfcc)]] | 🟢 most current |
| [Survival Guide](https://www.youtube.com/watch?v=7Mm3IHSObjo) | 2020-12-27 | 9:56 | — | ⛔ No usable captions (music only) | needs frames |
| [TIPS to Get Better](https://www.youtube.com/watch?v=ZrssoUb2Tik) | 2021-12-06 | 8:09 | — | ⛔ No captions available | needs frames |
| [Ultimate Germany Strategy](https://www.youtube.com/watch?v=SigeOoviB-U) | 2023-06-29 | 2:39 | — | ⏳ No captions (text/music vid) | queued for frames |
| [April 2020 Tournament R2 M1](https://www.youtube.com/watch?v=G1jeWzTuC2A) | 2020-05-19 | 42:42 | — | ⏳ Queued | 🟠 frame-only, long; competitive play |

## Method guide
- **Narrated guide** → captions via `yt-dlp --write-auto-sub` (cheap, accurate to narrator's words).
- **Silent match/replay** → `extract_frames` at full res, read HUD directly (cash/CPM/caps/buy-menu = ground truth).
- **Never** rely on `summarize_video`/`ask_about_video` as primary — it paraphrases frames and mislabels TC3 units/counts.
- **Always** confirm any number against `TC3_Reference.md` before trusting it, especially from pre-2024 videos.
