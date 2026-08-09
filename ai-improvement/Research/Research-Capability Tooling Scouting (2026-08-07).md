---
tags: [mega-prompt, research, tooling]
date: 2026-08-07
---

# Research-Capability Tooling Scouting — 2026-08-07

Scouting pass (no installs done) triggered while researching SAT prep content for
`pytheas/Courses/SAT/`, when the `yt-analysis` MCP server hit a daily quota wall mid-task.
Goal: find tools/repos that would sharpen Claude's own research capability generally, and
specifically for sourcing structured educational content.

## Deep-research agent frameworks (open source, MCP-friendly)

- **Open Deep Research** (LangChain/LangGraph) — configurable open-source deep-research
  agent, #6 on Deep Research Bench, 12.5k stars, MCP-compatible for search tools, multi-model.
  Most mature/active option found. https://github.com/langchain-ai/open_deep_research
- **RivalSearchMCP** — single MCP connection: 5 web search engines, 9 social platforms, 5 news
  aggregators, 5 academic DBs (arXiv, PubMed, OpenAlex, CrossRef, Europe PMC), 4 dataset hubs.
  Built-in quality scoring + **cross-source conflict detection** (numeric/date/polarity
  disagreements), structured JSON output. No API keys, MIT, actively committed (117 stars).
  Directly useful for "don't treat one source as fact" verification.
  https://github.com/damionrashford/RivalSearchMCP
- **AutoSearch** — MCP-native, ~40 channels (academic/code/community/Chinese-language),
  deduplicated + source-attributed, usable as Claude Code plugin/CLI/MCP server.
- **Gigaxity Deep Research** — MCP server: multi-source search → RRF fusion → synthesis with
  citation binding, 6 tools, works with Claude Code/Codex/Cursor.
  https://github.com/yoloshii/gigaxity-deep-research
- **Awesome-Deep-Research** — curated survey list, good future jumping-off point.
  https://github.com/DavidZWZ/Awesome-Deep-Research

## MCP servers for research/search

- **mcp-open-webresearch** — aggregates Bing/DuckDuckGo/Brave, built-in multi-round "Deep
  Research" mode with citation extraction. https://github.com/rinaldowouterson/mcp-open-webresearch
- **Firecrawl MCP** — official scrape/crawl-to-markdown server, useful fetch backend for sites
  WebFetch struggles with. https://github.com/firecrawl/firecrawl-mcp-server
- **Exa MCP server** — semantic web/code/company search. https://github.com/exa-labs/exa-mcp-server
- **awesome-mcp-servers** — general curated directory (includes Perplexity Sonar MCP, others),
  worth periodic browsing. https://github.com/wong2/awesome-mcp-servers

**YouTube MCP alternatives (backups for `yt-analysis` quota outages, like today's):**
- **ZeroPointRepo/youtube-mcp** — transcripts + search + channel browsing + playlist
  extraction + new-upload polling, 6 tools. https://github.com/ZeroPointRepo/youtube-mcp
- **kimtaeyoon83/mcp-server-youtube-transcript** — transcripts, optional TwelveLabs Pegasus
  integration for *visual* (non-speech) understanding — closest like-for-like backup if
  yt-analysis's value is frame/screenshot analysis, not just transcript summarization.
  https://github.com/kimtaeyoon83/mcp-server-youtube-transcript
- **sinco-lab/mcp-youtube-transcript**, **jkawamoto/mcp-youtube-transcript** — lightweight
  transcript-only fallbacks.

Note: 40+ YouTube MCP servers exist as of 2026; most are transcript-only, fine as an outage
fallback but won't replace yt-analysis's frame/screenshot features.

## SAT/educational-content sourcing — legitimacy flagged

- College Board's **official API is shut down** — no legitimate direct API access exists.
- **OpenSAT** (github.com/Anas099X/OpenSAT, 46★) — community question bank + AI generator,
  Reading/Writing/Math, public API. **Provenance unclear — treat as unverified, not confirmed
  official content.**
- **VG-Fish/College-Board** (6★, GPL-3.0) — Selenium scraper pulling directly from College
  Board's own public Question Bank site. **Real ToS risk** — no disclaimer addresses scraping
  restrictions; don't redistribute scraped content.
- **mdn522/sat-question-bank** (23★) — Flask app + question data, source/license undisclosed.
  Same caution.
- **Recommended instead: SAT Suite Educator Question Bank**
  (https://satsuiteeducatorquestionbank.collegeboard.org/) — 3,500+ real released questions,
  exportable, educator-tier access. Cleanest ToS-safe official source.

## Cross-verification methodology (technique, not just tooling)

- **Claim-extraction → evidence-retrieval → verify → explain** pipeline (per "TRUST Agents"
  framework, arXiv 2604.12184): decompose content into atomic factual claims, retrieve
  evidence per claim independently, score confidence per claim, cite inline — rather than
  verifying a whole document at once.
- **Corroboration/conflict scoring** — RivalSearchMCP's built-in pattern: score sources by
  freshness/tier, auto-flag numeric/date/polarity disagreements instead of manual eyeballing.
  Usable as a methodology even without adopting the server.
- **Structured-summary-before-synthesis** — normalize each source into a structured summary
  before passing to a synthesis step, rather than dumping raw text into one context; reduces
  hallucination vs. naive RAG (per FinVet framework, arXiv 2510.11654).

## Bottom line / near-term recommendation

1. **RivalSearchMCP** — most directly actionable addition: multi-source academic/web/news
   search + built-in conflict detection, no API keys, low setup cost.
2. Keep **kimtaeyoon83/mcp-server-youtube-transcript** or **ZeroPointRepo/youtube-mcp** as
   noted fallbacks for `yt-analysis` quota outages (relevant immediately — today's SAT video
   research hit exactly this wall).
3. For SAT content specifically: prioritize the **official Educator Question Bank** over any
   scraper repo — OpenSAT and VG-Fish/College-Board both have unresolved provenance/ToS
   concerns.

Nothing here was installed or adopted — this is a scouting pass for a future decision.
