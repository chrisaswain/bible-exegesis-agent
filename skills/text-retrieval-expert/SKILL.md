---
name: text-retrieval-expert
description: >
  Retrieves biblical texts in original languages and English translations.
  Use when the user needs a passage displayed, wants to compare translations,
  or needs original-language text (Hebrew, Aramaic, Greek). Handles public-domain
  and licensed text sources with proper attribution and copyright compliance.
version: "1.0.0"
author: AIAdvance
keywords:
  - bible
  - text-retrieval
  - translation
  - hebrew
  - greek
  - kjv
  - asv
  - web
  - septuagint
---

# Text Retrieval Expert

## Public-domain sources

The following sources may be freely quoted and displayed:

### Original languages
| Text | Language | Notes |
|------|----------|-------|
| Westminster Leningrad Codex (WLC) | Hebrew/Aramaic | Masoretic Text, BHS base |
| SBL Greek New Testament (SBLGNT) | Greek | Free-use license with attribution |
| Nestle 1904 | Greek | Public domain |
| Rahlfs Septuagint (LXX) | Greek | OT in Greek translation |

### English translations
| Translation | Abbreviation | Status |
|-------------|-------------|--------|
| King James Version | KJV | Public domain |
| American Standard Version | ASV | Public domain |
| Young's Literal Translation | YLT | Public domain |
| World English Bible | WEB | Public domain |
| Darby Translation | DBY | Public domain |
| Webster's Bible Translation | WBT | Public domain |

## API sources for text retrieval

### Primary: API.Bible
- Base URL: `https://api.scripture.api.bible/v1/`
- Requires API key (free tier available)
- Supports multiple translations including ESV, NIV (with usage limits)
- Rate limits apply; respect quotation length restrictions

### Fallback: public REST endpoints
- **getbible.net** — KJV, WEB, YLT and others (JSON API)
- **bolls.life** — multiple translations (free API, no key required)

## Retrieval workflow

1. **Identify the passage** — Parse book, chapter, verse(s) from user input
2. **Select source(s)** — Default to WEB (modern English, public domain) + original language
3. **Retrieve text** — Use WebFetch or cached reference data
4. **Label clearly:**
   - Translation name and abbreviation
   - License status (public domain or licensed)
   - Any truncation or omission
5. **Display** — Original language first (if requested), then English, side-by-side when helpful

## Book name normalization

Accept all common forms and normalize:
- Full names: "Genesis", "1 Corinthians", "Song of Solomon"
- Abbreviations: "Gen", "1 Cor", "Song", "SoS"
- Numbered books: "1 Sam", "I Samuel", "First Samuel"

## Copyright compliance rules

- **Public-domain texts**: quote freely, no restrictions
- **Licensed translations** (ESV, NIV, NASB, CSB, NLT, etc.):
  - Retrieve dynamically via API only
  - Display proper attribution as required by the license
  - Do not cache beyond session
  - If the license prohibits full quotation: summarize the passage and state the limitation
- **Never** reproduce licensed text from training data — always retrieve via API

## Error handling

- If an API is unreachable: state the limitation, fall back to public-domain text
- If a book/chapter/verse is invalid: ask the user to clarify
- If a translation is unavailable: list available alternatives
