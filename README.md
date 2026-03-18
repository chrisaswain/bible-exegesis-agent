# Bible Exegesis Agent

A rigorous Bible exegesis assistant using the historical-grammatical method. Works across Claude Code, ChatGPT, GitHub Copilot, Cursor, Grok, and Kiro.

Prioritizes **textual fidelity** over interpretive creativity. Serves as an assistant, not an authority.

## Quick Start

### Option A: Download the installer

1. Download the latest release zip from [Releases](https://github.com/chrisaswain/bible-exegesis-agent/releases)
2. Unzip and run the installer for your OS:

   **macOS / Linux:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

   **Windows (PowerShell):**
   ```powershell
   .\install.ps1
   ```

3. Pick your platform and target directory. Done.

### Option B: Build from source

```bash
git clone https://github.com/chrisaswain/bible-exegesis-agent.git
cd bible-exegesis-agent
python build.py
```

The build generates platform-specific bundles in `dist/` and a distributable zip.

## Supported Platforms

| Platform | What gets installed | External API access |
|----------|--------------------|--------------------|
| **Claude Code** (full) | CLAUDE.md + agents/ + skills/ + references/ | Yes (WebFetch) |
| **Claude Code** (single file) | One combined CLAUDE.md | Yes (WebFetch) |
| **ChatGPT** | System prompt + OpenAI function schema + setup script | Yes (function calling) |
| **GitHub Copilot** | `.github/copilot-instructions.md` | No |
| **Cursor** | `.cursor/rules/bible-exegesis.mdc` | Yes (terminal) |
| **Grok** | System prompt + API code examples | Yes (code interpreter) |
| **Kiro** | `.kiro/steering/bible-exegesis.md` | Varies |

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Text retrieval** | Fetch passages in Hebrew/Greek + English (public-domain and licensed via API) |
| **Lexical analysis** | Word studies with lemma, Strong's numbers, semantic range, concordance |
| **Grammar & syntax** | Verb parsing, clause relationships, discourse flow |
| **Literary analysis** | Genre, chiasm, parallelism, narrative technique, rhetoric |
| **Textual criticism** | Manuscript variants, text-critical evidence and criteria |

## Example Queries

- "Exegete Romans 8:28-30"
- "What does *hesed* mean in Psalm 136?"
- "Parse the Greek verbs in Philippians 2:5-11"
- "Compare translations of Isaiah 7:14"
- "What are the textual variants in Mark 16:9-20?"
- "Identify the chiastic structure of Genesis 6-9"

## Design Principles

1. **Textual fidelity** — meaning comes from the text, not imposed on it
2. **Historical-grammatical method** — grammar, syntax, literary context, historical context
3. **Confidence signaling** — every interpretive claim is tagged (high / plausible / ambiguous / disputed)
4. **No theological imposition** — no frameworks, no premature harmonization, no eisegesis
5. **Observation first** — what it says, how it functions, what it means, then implications
6. **Preserve tension** — where Scripture preserves tension, the agent does too
7. **Copyright compliance** — public-domain texts freely used; licensed texts via API only

## Project Structure

```
bible-exegesis-agent/
├── agents/bible-exegesis/AGENT.md       # Core agent definition + system prompt
├── skills/
│   ├── text-retrieval-expert/           # Bible text sources and retrieval
│   ├── lexical-analysis-expert/         # Word studies, lemmas, concordance
│   ├── grammatical-analysis-expert/     # Morphology, syntax, clause analysis
│   ├── literary-analysis-expert/        # Genre, structure, rhetorical devices
│   └── textual-criticism-expert/        # Manuscript variants, apparatus
├── references/
│   ├── hermeneutical-method.md          # Historical-grammatical method guide
│   ├── confidence-levels.md             # Confidence tagging definitions
│   ├── prohibited-patterns.md           # Interpretive fallacies to avoid
│   └── book-abbreviations.md           # Bible book name normalization
├── build.py                             # Build script for platform bundles
├── install.sh                           # Interactive installer (macOS/Linux)
└── install.ps1                          # Interactive installer (Windows)
```

## License

[MIT](LICENSE)
