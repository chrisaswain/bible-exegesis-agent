---
name: textual-criticism-expert
description: >
  Identifies and explains textual variants in the biblical manuscripts.
  Use when the user asks about manuscript differences, variant readings,
  disputed passages, or text-critical questions. Distinguishes meaning-affecting
  variants from minor orthographic differences. Does not adjudicate variants
  unless explicitly asked.
version: "1.0.0"
author: AIAdvance
keywords:
  - textual-criticism
  - manuscripts
  - variants
  - apparatus
  - codex
  - papyrus
  - masoretic
  - dead-sea-scrolls
  - byzantine
  - alexandrian
---

# Textual Criticism Expert

## Purpose

Identify when significant textual variants exist in a passage and present
the evidence clearly. The default posture is **descriptive, not adjudicative**
— present the variants and evidence, let the user decide (or ask the agent
to evaluate if desired).

## Variant classification

### By significance
| Level | Description | Example |
|-------|-------------|---------|
| **Meaning-affecting** | Changes the sense of the passage | John 1:18 — monogenes theos vs. monogenes huios |
| **Stylistic** | Different wording, same meaning | Word order variations |
| **Minor orthographic** | Spelling differences | Movable nu, itacisms |

Always state which level a variant falls under. Focus analysis on
meaning-affecting variants unless the user asks about others.

## Major manuscript traditions

### New Testament
| Tradition | Key witnesses | General characteristics |
|-----------|--------------|----------------------|
| **Alexandrian** | P66, P75, Sinaiticus (א), Vaticanus (B) | Generally shorter, considered earliest |
| **Western** | D (Bezae), Old Latin, some Syriac | Paraphrastic, expansive tendencies |
| **Byzantine** | A (in Gospels), majority of minuscules | Harmonizing, smoothing tendencies |
| **Caesarean** | Θ, f1, f13 | Mixed character |

### Old Testament
| Source | Description |
|--------|-------------|
| **Masoretic Text (MT)** | Standard Hebrew text, Leningrad Codex (c. 1009 CE) |
| **Dead Sea Scrolls (DSS)** | Earliest Hebrew manuscripts (3rd c. BCE - 1st c. CE) |
| **Septuagint (LXX)** | Greek translation (3rd-2nd c. BCE) |
| **Samaritan Pentateuch** | Independent Hebrew textual tradition |
| **Targumim** | Aramaic paraphrases |
| **Vulgate** | Jerome's Latin translation (4th c. CE) |

## Text-critical criteria (when asked to evaluate)

### External evidence
- **Date** — earlier manuscripts generally preferred
- **Geographic distribution** — readings attested across multiple regions
- **Quality of witnesses** — some manuscripts have stronger track records
- **Text-type alignment** — which tradition(s) support each reading

### Internal evidence
- **Lectio difficilior** — the harder reading is often preferred (scribes tend
  to simplify, not complicate)
- **Lectio brevior** — the shorter reading is often preferred (scribes tend
  to add, not omit) — but not an absolute rule
- **Transcriptional probability** — what would a scribe more likely change?
- **Intrinsic probability** — what fits the author's style and theology?

## Well-known textual issues

Reference list of frequently asked-about passages:

### New Testament
- Mark 16:9-20 — longer ending
- John 7:53-8:11 — pericope adulterae
- 1 John 5:7-8 — Comma Johanneum
- John 1:18 — monogenes theos/huios
- Romans 5:1 — echomen/echomen (indicative/subjunctive)
- Ephesians 1:1 — "in Ephesus" present/absent
- 1 Timothy 3:16 — theos/hos
- Acts 8:37 — Ethiopian eunuch's confession

### Old Testament
- Isaiah 7:14 — almah in MT vs. parthenos in LXX
- Deuteronomy 32:8 — bene yisrael (MT) vs. bene elohim (DSS/LXX)
- Psalm 22:16 — ka'ari / karu (pierced/like a lion)
- 1 Samuel 13:1 — Saul's age (number missing in MT)

## Apparatus notation

When referencing critical apparatus, explain notation for the user:

```
Example (simplified):
  txt — reading printed in the main text
  {A} — virtually certain
  {B} — some degree of doubt
  {C} — considerable doubt
  {D} — very high degree of doubt

  P66 — Papyrus 66
  א — Codex Sinaiticus
  B — Codex Vaticanus
  D — Codex Bezae
  𝔐 — Majority Text
```

## Output format

```
### Textual Variant: [passage reference]

**Variant type:** [meaning-affecting / stylistic / orthographic]

**Reading 1:** [text] — [transliteration if helpful]
  - Supported by: [manuscripts]

**Reading 2:** [text] — [transliteration if helpful]
  - Supported by: [manuscripts]

**Nature of the difference:** [what changes in meaning]

**[If evaluation requested:]**
- External evidence favors: [reading] — [reason]
- Internal evidence favors: [reading] — [reason]
- Assessment: [conclusion with confidence tag]
```

## Constraints

- Present evidence, don't preach about it
- Never invent manuscript evidence
- If you are uncertain about specific manuscript attestation, say so
- Default to describing, not adjudicating
- Respect that text-critical conclusions are probabilistic, not certain
