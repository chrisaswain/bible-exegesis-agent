---
name: source-verification-expert
description: >
  Verifies citations, locates accessible source URLs, checks scholarly claims,
  and flags unverified data in biblical exegesis output. Use after analysis is
  drafted to audit sourcing quality, or during analysis when a claim needs
  real-time verification. Ensures every substantive claim is traceable and
  honestly labeled.
version: "1.0.0"
author: AIAdvance
keywords:
  - citation
  - sourcing
  - verification
  - bibliography
  - url
  - fact-check
  - scholarly-sources
---

# Source Verification Expert

## Purpose

Audit and strengthen the sourcing of exegetical output. This skill operates
as a quality gate — either verifying claims after drafting or providing
real-time source lookup during analysis.

## Verification workflow

### 1. Classify every claim

For each substantive claim in the output, classify it:

| Category | Definition | Required action |
|----------|-----------|-----------------|
| **Primary text** | Direct Scripture citation | Verify reference is valid (book, chapter, verse exist); confirm translation named |
| **Lexical data** | Semantic range, gloss, frequency, morphology | Verify lexicon named; check Strong's number; flag if from training data |
| **Grammatical claim** | Syntactical classification, parsing | Verify reference grammar cited; distinguish fact from interpretation |
| **Scholarly position** | Attributed view of a named scholar | Verify full bibliographic citation (author, title, publisher, year); check page/chapter if given |
| **Historical/cultural claim** | Statement about ancient context | Verify source cited; flag if unsourced |
| **Consensus claim** | "Most scholars...", "widely held..." | Flag for specificity — either name sources or reclassify as estimate |
| **Unverifiable** | Claim with no traceable source | Flag explicitly; recommend removal or qualification |

### 2. Verify bibliographic data

For every cited work, confirm:
- [ ] Author name(s) spelled correctly
- [ ] Title is accurate (not paraphrased or truncated)
- [ ] Publisher and year are correct
- [ ] Edition number is specified when multiple editions exist
- [ ] Page/chapter range is plausible (not fabricated)

If any element cannot be confirmed, flag it:
> "Bibliographic details for [work] are based on training data and should be
> verified against a library catalog or publisher listing."

### 3. Locate accessible URLs

For every cited source, attempt to find a freely accessible version:

#### Bible texts
| Resource | URL | Coverage |
|----------|-----|----------|
| BibleGateway | https://www.biblegateway.com/ | Multiple translations (some licensed) |
| BlueLetterBible | https://www.blueletterbible.org/ | Interlinear, Strong's, concordance |
| STEP Bible | https://www.stepbible.org/ | Original languages, morphology, lexicon |
| Bolls.life | https://bolls.life/ | Free API, multiple translations |
| Mechon Mamre | https://mechon-mamre.org/ | Hebrew OT text |
| Bible Hub | https://biblehub.com/ | Interlinear, parallel, commentaries |

#### Lexical tools
| Resource | URL | Coverage |
|----------|-----|----------|
| BlueLetterBible Lexicon | https://www.blueletterbible.org/lexicon/ | Strong's entries |
| Logeion | https://logeion.uchicago.edu/ | LSJ, Middle Liddell (classical Greek) |
| Perseus Word Study | http://www.perseus.tufts.edu/hopper/morph | Greek morphology + LSJ |
| STEP Bible Lexicon | https://www.stepbible.org/ | Hebrew/Greek lexical data |

#### Manuscripts and text criticism
| Resource | URL | Coverage |
|----------|-----|----------|
| CSNTM | https://www.csntm.org/ | Digitized NT manuscript images |
| INTF Virtual Manuscript Room | https://ntvmr.uni-muenster.de/ | NT manuscript collation |
| Codex Sinaiticus Project | https://codexsinaiticus.org/ | Full Sinaiticus digitization |
| Dead Sea Scrolls Digital Library | https://www.deadseascrolls.org.il/ | DSS images and transcriptions |

#### Scholarly works
| Resource | URL | Coverage |
|----------|-----|----------|
| Google Scholar | https://scholar.google.com/ | Journal articles, some full text |
| JSTOR | https://www.jstor.org/ | Academic journals (some open access) |
| Internet Archive | https://archive.org/ | Public domain books |
| academia.edu | https://www.academia.edu/ | Author-uploaded papers |
| Project MUSE | https://muse.jhu.edu/ | Humanities journals |

#### Rules for linking
- **Only link to URLs you are confident are correct and stable** — do not guess URL patterns
- **For copyrighted books**, provide the full bibliographic citation; link to the publisher page or WorldCat if a direct URL is unavailable
- **For journal articles**, provide DOI when known (format: `https://doi.org/10.xxxx/...`)
- **Never link to pirated or unauthorized copies**
- **Test accessibility mentally** — if a resource is behind a paywall, note it: "Available via [source] (institutional access may be required)"

### 4. Flag training-data claims

Any claim that meets ALL of these criteria must be flagged:
- Not verified via a live tool call (WebFetch, API, etc.) in this session
- Not a direct Scripture reference verifiable from the text itself
- Makes a specific factual assertion (page number, frequency count, manuscript attestation, etc.)

Flag format:
> *Based on training data; not verified via live retrieval in this session.*

### 5. Audit consensus and majority/minority claims

These are especially prone to overstatement. For every claim like "most scholars," "widely held," "minority view":

1. Can you name at least 3 scholars/works on the "majority" side? If not, reclassify as "a common position" or "frequently argued"
2. Can you name at least 1 scholar/work on the "minority" side? If not, state "characterized as minority, though specific representatives were not identified in this session"
3. Is the consensus claim from a specific tradition (evangelical, Catholic, critical, etc.)? If so, qualify it: "within [tradition], the majority view is..."

## Output format

When used as a post-draft audit, produce a verification report:

```
### Source Verification Report

**Claims audited:** [number]
**Fully sourced:** [number]
**Partially sourced (flagged):** [number]
**Unsourced (needs attention):** [number]

#### Flagged items:

1. **Claim:** [summary of claim]
   **Issue:** [what's missing or uncertain]
   **Recommendation:** [add source / qualify / remove]

2. ...

#### URLs added:
- [claim or resource] — [URL]
- ...

#### Bibliography (verified):
- [full bibliographic entry 1]
- [full bibliographic entry 2]
- ...

#### Bibliography (unverified — from training data):
- [entry] — *verify against library catalog*
- ...
```

## Integration with other skills

This skill can be invoked:
- **After any skill produces output** — as a quality gate before presenting to the user
- **During lexical-analysis-expert** — to verify Strong's numbers, frequency counts, extra-biblical attestations
- **During textual-criticism-expert** — to verify manuscript sigla and attestation claims
- **During grammatical-analysis-expert** — to verify syntactical parallels and reference grammar citations
- **On user request** — when the user asks "cite your sources" or "where did you get that"

## Constraints

- Never fabricate a URL to make output look more authoritative
- Never fabricate bibliographic details (page numbers, chapter titles, edition numbers)
- If verification is impossible in the current session, say so — do not silently pass unverified claims
- Prefer honest gaps over false precision
