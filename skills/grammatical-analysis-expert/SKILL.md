---
name: grammatical-analysis-expert
description: >
  Performs grammatical and syntactical analysis of biblical Hebrew, Aramaic,
  and Greek texts. Use when the user needs verb parsing, clause analysis,
  conditional construction identification, discourse flow mapping, or
  syntactical explanation. Distinguishes grammatical fact from interpretive
  inference.
version: "1.0.0"
author: AIAdvance
keywords:
  - grammar
  - syntax
  - morphology
  - verb-parsing
  - clause-analysis
  - discourse-analysis
  - hebrew-grammar
  - greek-grammar
---

# Grammatical Analysis Expert

## Analysis domains

### 1. Verb analysis
For every significant verb, identify:

**Hebrew verbs:**
- Stem (binyan): Qal, Niphal, Piel, Pual, Hithpael, Hiphil, Hophal
- Conjugation: Perfect (qatal), Imperfect (yiqtol), Wayyiqtol, Weqatal, Imperative, Jussive, Cohortative, Infinitive (construct/absolute), Participle
- Person, gender, number
- Aspect/function in context (completed action, habitual, stative, etc.)

**Greek verbs:**
- Tense-form: Present, Imperfect, Aorist, Perfect, Pluperfect, Future
- Voice: Active, Middle, Passive, Middle/Passive (deponent considerations)
- Mood: Indicative, Subjunctive, Optative, Imperative, Infinitive, Participle
- Person and number
- Aspect: imperfective (present/imperfect), perfective (aorist), stative (perfect)

**Critical distinction:** Tense-form does not always equal time. Greek verbal
aspect (Aktionsart) is primarily about the author's perspective on the action,
not temporal reference. Be precise about this.

### 2. Clause relationships

Identify and label clause connections:

| Relationship | Greek markers | Hebrew markers |
|-------------|---------------|----------------|
| Coordinate | kai, de, alla | waw-conjunction |
| Subordinate (causal) | hoti, gar, dio | ki |
| Subordinate (temporal) | hote, hotan, prin | ka'asher, be- + infinitive |
| Subordinate (conditional) | ei, ean | im, lu |
| Subordinate (purpose) | hina, hopos | lema'an, le- + infinitive |
| Subordinate (result) | hoste | — |
| Concessive | ei kai, kaipper | gam ki |
| Comparative | hos, kathaper | ka'asher, kemo |

### 3. Conditional constructions

**Greek conditions:**
| Class | Protasis | Apodosis | Assumption |
|-------|----------|----------|------------|
| First (simple) | ei + indicative | any mood | Assumed true for argument |
| Second (contrary-to-fact) | ei + past indicative | an + past indicative | Assumed false |
| Third (more probable future) | ean + subjunctive | any mood | Probable/possible |
| Fourth (less probable future) | ei + optative | an + optative | Remote possibility |

**Hebrew conditions:**
- im + perfect/imperfect — standard conditional
- lu / lule — counterfactual
- ki — sometimes conditional ("if/when")
- Context determines force more than form in Hebrew

### 4. Participles and infinitives

**Greek participles** — identify function:
- Adverbial: temporal, causal, concessive, conditional, means, manner, purpose
- Adjectival: attributive, predicate, substantival
- Attendant circumstance
- Periphrastic (with eimi)
- Genitive absolute

**Greek infinitives** — identify function:
- Substantival (subject, object, apposition)
- Complementary (completing a verb)
- Purpose (tou + infinitive, eis to + infinitive)
- Result (hoste + infinitive)
- Temporal (prin, en to, meta to)
- Causal (dia to + infinitive)

**Hebrew infinitives:**
- Construct: often functions as gerund or with prepositions (le-, be-, ke-)
- Absolute: emphasis, continuation, or substitute for finite verb

### 5. Discourse analysis

Map the flow of argument or narrative:

- **Epistolary:** thesis -> support -> counter -> conclusion
- **Narrative:** setting -> inciting event -> rising action -> climax -> resolution
- **Poetry:** line structure, strophe breaks, shifts in speaker/addressee
- **Prophetic:** oracle formula -> accusation -> judgment -> restoration

Mark discourse markers:
- Transition indicators (oun, de, alla, tote, kai egeneto)
- Logical connectors (gar, dio, hoste, ara)
- Emphasis markers (amen, idou, hinne)

## Analysis principles

1. **Descriptive, not speculative** — state what the grammar shows, not what
   you wish it showed
2. **Distinguish fact from inference** — parsing is fact; interpretive weight
   is inference. Label both clearly.
3. **Grammar constrains meaning but rarely determines it alone** — always pair
   grammatical observations with contextual analysis
4. **Avoid grammatical maximalism** — not every aorist is "once for all," not
   every present is "continuous." Report the range of possibilities.

## Output format

```
### Grammatical Analysis: [passage reference]

**Clause structure:**
- [Main clause] — [verb parse] — [function]
  - [Subordinate clause] — [relationship] — [verb parse]
  - [Subordinate clause] — [relationship] — [verb parse]

**Key verbal forms:**
- [verb form] ([transliterated]) — [full parse] — [aspect/function note]

**Syntactical observations:**
- [observation 1] — **[fact/inference]**
- [observation 2] — **[fact/inference]**

**Discourse flow:**
- [step 1 in the argument/narrative]
- [step 2]
- ...
```
