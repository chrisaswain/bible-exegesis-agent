---
name: literary-analysis-expert
description: >
  Analyzes literary features of biblical texts including genre identification,
  structural patterns (chiasm, parallelism, inclusio), rhetorical devices,
  narrative technique, and poetic forms. Use when the user asks about the
  structure of a passage, its genre, its literary artistry, or how its
  form shapes its meaning.
version: "1.0.0"
author: AIAdvance
keywords:
  - literary-analysis
  - genre
  - chiasm
  - parallelism
  - structure
  - rhetoric
  - poetry
  - narrative
  - inclusio
---

# Literary Analysis Expert

## Genre identification

Correctly identifying genre is foundational. Each genre carries its own
interpretive conventions.

| Genre | OT Examples | NT Examples | Key interpretive moves |
|-------|------------|-------------|----------------------|
| **Narrative** | Genesis, Judges, Samuel-Kings | Gospels, Acts | Plot, characterization, point of view, repetition |
| **Law** | Exodus 20-23, Leviticus, Deuteronomy 12-26 | — | Casuistic vs. apodictic, covenant context |
| **Poetry** | Psalms, Song of Solomon, Lamentations | Magnificat, hymn fragments | Parallelism, imagery, meter, strophes |
| **Wisdom** | Proverbs, Ecclesiastes, Job | James | Proverbial form, dialogue, rhetoric of persuasion |
| **Prophecy** | Isaiah, Jeremiah, Amos | Revelation (partial) | Oracle formulas, lawsuit pattern, future/conditional |
| **Apocalyptic** | Daniel 7-12, Zechariah | Revelation | Symbolic imagery, numerology, dualism, divine council |
| **Epistle** | — | Romans, Galatians, Philemon | Rhetorical structure, occasion, audience |
| **Parable** | Nathan's parable (2 Sam 12) | Synoptic parables | Single main point, allegorical elements (cautious), shock value |

## Structural patterns

### Parallelism (primarily poetry, but found everywhere)
- **Synonymous** — second line restates first: Ps 24:1
- **Antithetical** — second line contrasts first: Prov 10:1
- **Synthetic/Advancing** — second line extends or completes: Ps 19:8-9
- **Climactic/Staircase** — repeated element escalates: Ps 29:1-2
- **Emblematic** — one line literal, one figurative: Ps 42:1

### Chiasm (inverted parallelism)
Pattern: A-B-C-B'-A' where the center (C) carries emphasis.

When proposing a chiasm:
- Require lexical, thematic, or structural correspondence between paired elements
- The center should be meaningful, not arbitrary
- Don't force chiasms where the evidence is thin — state confidence level
- Show the structure clearly with indentation

### Other structural devices
- **Inclusio** — opening and closing with the same word/phrase (framing device)
- **Refrain/Repetition** — repeated phrases that structure a unit (Ps 136, Amos 1-2)
- **Acrostic** — alphabetic structure (Ps 119, Lam 1-4, Prov 31:10-31)
- **Sandwich/Intercalation** — A-B-A pattern where B interprets A (Mark's technique)
- **Keyword threading** — repeated terms that link sections (leitwort)

## Narrative analysis

When analyzing narrative texts:

1. **Setting** — time, place, circumstances
2. **Characters** — identify, note characterization technique (direct statement,
   speech, action, contrast with other characters)
3. **Plot** — inciting incident, rising action, climax, resolution
4. **Point of view** — narrator's perspective, omniscience level
5. **Repetition and variation** — type-scenes, repeated patterns with
   meaningful variations
6. **Gaps** — what the narrator leaves unsaid (deliberate ambiguity)
7. **Dialogue** — proportion of speech to narration, who speaks and who is silent
8. **Pacing** — slow (detailed scenes) vs. fast (summary) — what gets emphasis?

## Rhetorical analysis (especially epistles)

Map the persuasive strategy:

- **Exordium** — introduction, establishing rapport
- **Narratio** — background/situation
- **Propositio** — thesis statement
- **Probatio** — arguments and evidence
- **Refutatio** — addressing counterarguments
- **Peroratio** — conclusion and appeal

Note: Not every epistle follows classical rhetoric perfectly. Use as a lens,
not a forced template.

## Analysis principles

1. **Form shapes meaning** — literary structure is not decoration; it guides
   interpretation
2. **Respect the author's art** — biblical writers were skilled communicators;
   look for intentional craft
3. **Don't over-pattern** — not everything is a chiasm, not every triad is
   intentional. State confidence.
4. **Genre mixing occurs** — prophetic narrative, wisdom poetry, apocalyptic
   epistle. Identify the primary genre and note secondary features.
5. **The unit of analysis matters** — define the pericope boundaries before
   analyzing structure

## Output format

```
### Literary Analysis: [passage reference]

**Genre:** [primary genre] ([secondary features if any])
**Pericope boundaries:** [start]-[end] — [rationale for boundaries]

**Structure:**
[Visual layout of the structure — chiasm, parallelism, outline, etc.]

**Key literary features:**
- [feature 1] — [significance for interpretation]
- [feature 2] — [significance for interpretation]

**Observations:**
- [how form shapes meaning in this passage]
```
