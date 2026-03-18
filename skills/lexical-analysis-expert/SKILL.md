---
name: lexical-analysis-expert
description: >
  Performs lexical analysis of biblical Hebrew, Aramaic, and Greek terms.
  Use when the user requests a word study, needs a semantic range, wants
  concordance data, or asks about the meaning of an original-language term.
  Guards against root-word fallacies, theological loading, and semantic
  range collapse.
version: "1.0.0"
author: AIAdvance
keywords:
  - lexical-analysis
  - word-study
  - hebrew
  - greek
  - strongs
  - concordance
  - semantic-range
  - lemma
---

# Lexical Analysis Expert

## Word study workflow

1. **Identify the term** — surface form in the passage
2. **Lemma identification** — root/dictionary form + Strong's number
3. **Morphological parsing** — part of speech, inflection details
4. **Semantic range** — full range of attested meanings
5. **Concordance survey** — usage across Scripture, grouped by corpus
6. **Contextual determination** — meaning in the immediate passage

## Lemma identification

For every term analyzed, provide:
- **Surface form** — the word as it appears in the text (transliterated)
- **Lemma** — dictionary form (transliterated + original script)
- **Strong's number** — H#### for Hebrew/Aramaic, G#### for Greek
- **Morphological code** — using standard parsing notation

### Hebrew morphology notation
```
Verb:    Stem (Qal/Niphal/Piel/etc.) + Conjugation (Perfect/Imperfect/etc.) + PGN
Noun:    Gender + Number + State (absolute/construct) + Suffix
Adj:     Gender + Number + State
```

### Greek morphology notation
```
Verb:    Tense + Voice + Mood + Person + Number
Noun:    Case + Number + Gender
Adj:     Case + Number + Gender + Degree
Part:    Tense + Voice + Case + Number + Gender
```

## Semantic range rules

Present the **full attested range** of meanings, then narrow to context:

1. List all major glosses from standard lexica (BDB for Hebrew, BDAG for Greek)
2. Group by semantic domain where helpful
3. Note frequency — how common is each sense?
4. **Immediate context determines meaning** — prioritize the passage over distant usage
5. Present the contextual meaning with a confidence tag

## Concordance data

When surveying usage across Scripture:
- Group occurrences by corpus (Torah, Prophets, Writings, Gospels, Pauline, etc.)
- Note total frequency (approximate is acceptable)
- Highlight passages where the same author uses the term
- Identify any semantic shifts across corpora

## Prohibited patterns

| Fallacy | Description | Example to avoid |
|---------|-------------|------------------|
| **Root-word fallacy** | Deriving meaning from etymological roots rather than usage | "ekklesia means 'called out ones' because ek + kaleo" |
| **Theological loading** | Importing systematic theology into a lexical entry | "pistis always means 'saving faith'" |
| **Semantic range collapse** | Reducing multiple meanings to one "true" meaning | "agape only means unconditional love" |
| **Illegitimate totality transfer** | Loading the total semantic range into every occurrence | "logos in John 1:1 carries all meanings of logos" |
| **Etymological fallacy** | Assuming original meaning persists unchanged | "hypocrite means 'actor' because that's the Greek origin" |

## Reference lexica (for grounding, not quotation)

### Hebrew / Aramaic
- BDB — Brown-Driver-Briggs Hebrew and English Lexicon
- HALOT — Hebrew and Aramaic Lexicon of the Old Testament
- TWOT — Theological Wordbook of the Old Testament

### Greek
- BDAG — Bauer-Danker-Arndt-Gingrich Greek-English Lexicon
- LSJ — Liddell-Scott-Jones (classical Greek, for background)
- TDNT — Theological Dictionary of the New Testament (use cautiously — prone to theological loading)

## Output format

```
### Word Study: [transliterated term]

**Surface form:** [form as it appears]
**Lemma:** [dictionary form] ([original script]) — Strong's [number]
**Morphology:** [parsed form]

**Semantic range:**
- [gloss 1] — [frequency/domain note]
- [gloss 2] — [frequency/domain note]
- [gloss 3] — ...

**Usage in context:**
- [corpus 1]: [key references]
- [corpus 2]: [key references]

**Contextual meaning:** [meaning in this passage] — **[confidence level]**
```
