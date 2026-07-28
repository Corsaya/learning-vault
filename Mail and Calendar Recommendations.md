# Mail & Calendar — recommendations (2026-07-28)

Requirements Donovan gave: works on **phone + computer**, handles **Zoho
Mail + Gmail**, currently uses **Thunderbird** on desktop; calendar must
**sync to the cloud or auto-push to GitHub on every change**.

## Mail — recommendation: keep Thunderbird, add Thunderbird for Android

The genuinely universal option is Thunderbird itself. Thunderbird for
Android (the rebuilt K-9 Mail) shipped in late 2024 and is the same
project, so it's one client on both devices, free, open source, no
subscription, and handles Zoho + Gmail together as ordinary IMAP/SMTP
accounts.

| Option | Phone | Desktop | Notes |
|---|---|---|---|
| **Thunderbird + TB for Android** | ✅ | ✅ (already yours) | Same project both ends; unified inbox; free. **Recommended.** |
| FairEmail | ✅ | ❌ | Best-in-class Android privacy client, but Android only |
| Bluemail | ✅ | ✅ | Truly cross-platform incl. Linux, but closed source, ads in free tier |
| Zoho Mail app + Gmail app | ✅ | ~ | What you'd avoid: two apps, no unified inbox |

Caveat: TB for Android does **not** sync settings from desktop — accounts
are configured once per device (app passwords, same as Pytheas uses).

**Pytheas already covers the "read + draft + confirmed send" path** over
plain IMAP/SMTP, so it works with Zoho and Gmail simultaneously without
depending on whichever client you pick.

## Calendar — recommendation: Radicale (self-hosted CalDAV) or Zoho Calendar

The "auto-push to GitHub on change" idea is workable but the wrong tool:
git has no conflict resolution for concurrent edits and no push
mechanism from a phone calendar app. **CalDAV is the protocol that
actually does what you want** — it syncs both ways, from any device,
instantly.

Two good paths:

1. **Zoho Calendar (easiest).** You already have Zoho. It's CalDAV +
   has iOS/Android apps, and Thunderbird speaks CalDAV natively. Zero
   infrastructure. Pytheas can read it today via its ICS "secret
   address".
2. **Radicale (self-hosted, full control).** ~50 MB Python server on this
   machine or a Pi; every device syncs over CalDAV; storage is plain
   `.ics` files in a folder — which means **you can point git at that
   folder** and get the versioned/auto-push behavior you wanted as a
   *backup*, not as the sync mechanism. A post-commit cron or inotify
   hook pushes on change.

Recommended phone apps for either: **DAVx⁵** (CalDAV sync adapter,
makes any CalDAV server appear as a native Android calendar) + your
existing calendar app.

**Do not use:** Google Calendar as the primary if you want out of the
cloud; ICS-file-in-git as the primary sync (read-only in practice,
merge conflicts, no phone write path).

## What Pytheas supports today
- Calendar: **read-only ICS feeds** (works with Zoho, Google, Radicale).
- Mail: IMAP read + drafts + confirmed send (works with Zoho + Gmail app
  passwords).
- Not yet built: two-way CalDAV write. If you pick Radicale or Zoho
  CalDAV, adding event *creation* from Pytheas is a small follow-up.
