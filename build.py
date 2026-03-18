#!/usr/bin/env python3
"""
Build script for Bible Exegesis Agent installer package.

Flattens all agent markdown (system prompt, skills, references) into
platform-specific bundles under dist/, then packages everything into
a distributable zip file.

Usage:
    python build.py          # Build all platforms
    python build.py claude   # Build only Claude platform
    python build.py --clean  # Remove dist/ and rebuild
"""

import json
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path

VERSION = "1.0.0"
AGENT_NAME = "bible-exegesis-agent"
ROOT = Path(__file__).parent
DIST = ROOT / "dist"
AGENT_MD = ROOT / "agents" / "bible-exegesis" / "AGENT.md"

SKILLS = [
    ROOT / "skills" / "text-retrieval-expert" / "SKILL.md",
    ROOT / "skills" / "lexical-analysis-expert" / "SKILL.md",
    ROOT / "skills" / "grammatical-analysis-expert" / "SKILL.md",
    ROOT / "skills" / "literary-analysis-expert" / "SKILL.md",
    ROOT / "skills" / "textual-criticism-expert" / "SKILL.md",
]

REFERENCES = [
    ROOT / "references" / "hermeneutical-method.md",
    ROOT / "references" / "confidence-levels.md",
    ROOT / "references" / "prohibited-patterns.md",
    ROOT / "references" / "book-abbreviations.md",
]

PLATFORMS = ["claude", "chatgpt", "copilot", "cursor", "grok", "kiro"]


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter (--- ... ---) from markdown."""
    match = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    if match:
        return text[match.end():]
    return text


def read_and_strip(path: Path) -> str:
    """Read a file and strip its YAML frontmatter."""
    return strip_frontmatter(path.read_text(encoding="utf-8"))


def build_flattened_prompt() -> str:
    """Build a single flattened system prompt with all skills and references."""
    parts = []

    # Core agent prompt
    parts.append("# Bible Exegesis Agent — Complete System Prompt\n")
    parts.append(f"# Version: {VERSION}\n")
    parts.append("# https://github.com/AIAdvance/bible-exegesis-agent\n\n")
    parts.append(read_and_strip(AGENT_MD))

    # Skills
    parts.append("\n\n---\n\n# COMPANION SKILLS\n")
    parts.append("# The following sections provide domain expertise for each capability.\n\n")
    for skill_path in SKILLS:
        parts.append(read_and_strip(skill_path))
        parts.append("\n\n---\n\n")

    # References
    parts.append("# REFERENCE DOCUMENTS\n")
    parts.append("# Methodology, confidence levels, prohibited patterns, abbreviations.\n\n")
    for ref_path in REFERENCES:
        parts.append(ref_path.read_text(encoding="utf-8"))
        parts.append("\n\n---\n\n")

    return "".join(parts).rstrip("\n -") + "\n"


def build_claude(dest: Path, flattened: str):
    """Build Claude Code bundle — CLAUDE.md + original skill/reference tree."""
    dest.mkdir(parents=True, exist_ok=True)

    # CLAUDE.md (the config version, not flattened)
    claude_md = (ROOT / "config" / "claude.md").read_text(encoding="utf-8")
    (dest / "CLAUDE.md").write_text(claude_md, encoding="utf-8")

    # Agent definition
    agent_dir = dest / "agents" / "bible-exegesis"
    agent_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(AGENT_MD, agent_dir / "AGENT.md")

    # Skills
    for skill_path in SKILLS:
        skill_name = skill_path.parent.name
        skill_dir = dest / "skills" / skill_name
        skill_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_path, skill_dir / "SKILL.md")

    # References
    ref_dir = dest / "references"
    ref_dir.mkdir(parents=True, exist_ok=True)
    for ref_path in REFERENCES:
        shutil.copy2(ref_path, ref_dir / ref_path.name)

    # Also include the flattened prompt for convenience
    (dest / "system-prompt-full.md").write_text(flattened, encoding="utf-8")

    # Setup instructions
    (dest / "SETUP.md").write_text(
        "# Claude Code Setup\n\n"
        "## Option A: Full skill tree (recommended)\n\n"
        "Copy this entire directory into your project root:\n\n"
        "```bash\n"
        "cp -r claude/ ~/my-project/bible-exegesis-agent/\n"
        "```\n\n"
        "Claude Code will automatically read the CLAUDE.md and load skills as needed.\n\n"
        "## Option B: Single-file mode\n\n"
        "Copy `system-prompt-full.md` into your project as `CLAUDE.md`:\n\n"
        "```bash\n"
        "cp claude/system-prompt-full.md ~/my-project/CLAUDE.md\n"
        "```\n\n"
        "This gives you the full agent in one file, no skill loading needed.\n",
        encoding="utf-8",
    )


def build_chatgpt(dest: Path, flattened: str):
    """Build ChatGPT bundle — Custom GPT config + flattened prompt."""
    dest.mkdir(parents=True, exist_ok=True)

    # Flattened system prompt for pasting into Custom GPT builder
    (dest / "system-prompt.md").write_text(flattened, encoding="utf-8")

    # OpenAI function-calling schema
    openai_json = (ROOT / "config" / "openai.json").read_text(encoding="utf-8")
    (dest / "openai-config.json").write_text(openai_json, encoding="utf-8")

    # Custom GPT creation guide
    (dest / "SETUP.md").write_text(
        "# ChatGPT Setup\n\n"
        "## Option A: Custom GPT (shareable link)\n\n"
        "1. Go to https://chat.openai.com/gpts/editor\n"
        "2. Click **Create a GPT**\n"
        "3. In the **Configure** tab:\n"
        "   - **Name:** Bible Exegesis Agent\n"
        "   - **Description:** Rigorous Bible exegesis using the historical-grammatical method\n"
        "   - **Instructions:** Paste the entire contents of `system-prompt.md`\n"
        "4. Under **Actions**, import the tools from `openai-config.json`\n"
        "   (or manually add each function)\n"
        "5. Optionally upload the reference documents as **Knowledge** files\n"
        "6. Click **Save** and choose visibility (Only me / Anyone with link / Public)\n"
        "7. Share the link with others\n\n"
        "## Option B: OpenAI Assistants API\n\n"
        "Use the provided `create-assistant.py` script:\n\n"
        "```bash\n"
        "pip install openai\n"
        "export OPENAI_API_KEY=sk-...\n"
        "python create-assistant.py\n"
        "```\n\n"
        "## Option C: Paste into any ChatGPT conversation\n\n"
        "Start a new conversation, paste the system prompt, and ask your question.\n"
        "You won't get tool/function access, but the agent's reasoning and method\n"
        "will still apply.\n",
        encoding="utf-8",
    )

    # Assistants API creation script
    openai_config = json.loads(openai_json)
    tools_json = json.dumps(openai_config.get("tools", []), indent=2)
    (dest / "create-assistant.py").write_text(
        '#!/usr/bin/env python3\n'
        '"""Create a Bible Exegesis Agent via the OpenAI Assistants API."""\n\n'
        'from openai import OpenAI\n'
        'from pathlib import Path\n\n'
        'client = OpenAI()  # Uses OPENAI_API_KEY env var\n\n'
        'instructions = Path("system-prompt.md").read_text(encoding="utf-8")\n\n'
        f'tools = {tools_json}\n\n'
        'assistant = client.beta.assistants.create(\n'
        '    name="Bible Exegesis Agent",\n'
        '    description="Rigorous Bible exegesis using the historical-grammatical method.",\n'
        '    instructions=instructions,\n'
        '    tools=tools,\n'
        '    model="gpt-4o",\n'
        ')\n\n'
        'print(f"Assistant created: {assistant.id}")\n'
        'print(f"Name: {assistant.name}")\n'
        'print("Use this ID in your application to start threads with this assistant.")\n',
        encoding="utf-8",
    )


def build_copilot(dest: Path, flattened: str):
    """Build GitHub Copilot bundle."""
    dest.mkdir(parents=True, exist_ok=True)

    # .github/copilot-instructions.md
    github_dir = dest / ".github"
    github_dir.mkdir(parents=True, exist_ok=True)
    (github_dir / "copilot-instructions.md").write_text(flattened, encoding="utf-8")

    (dest / "SETUP.md").write_text(
        "# GitHub Copilot Setup\n\n"
        "Copy the `.github/` directory into your repository root:\n\n"
        "```bash\n"
        "cp -r copilot/.github/ ~/my-repo/.github/\n"
        "```\n\n"
        "Copilot will use the instructions in `.github/copilot-instructions.md`\n"
        "when answering questions in your repo.\n\n"
        "## Limitations\n\n"
        "- No external API access — the agent works from model knowledge only\n"
        "- No MCP server support — Bible text retrieval APIs are not available\n"
        "- Best for: exegetical analysis, grammatical explanation, literary structure\n"
        "- Not suited for: dynamic text retrieval, live translation comparison\n",
        encoding="utf-8",
    )


def build_cursor(dest: Path, flattened: str):
    """Build Cursor bundle."""
    dest.mkdir(parents=True, exist_ok=True)

    # .cursor/rules/bible-exegesis.mdc
    cursor_dir = dest / ".cursor" / "rules"
    cursor_dir.mkdir(parents=True, exist_ok=True)
    (cursor_dir / "bible-exegesis.mdc").write_text(flattened, encoding="utf-8")

    (dest / "SETUP.md").write_text(
        "# Cursor Setup\n\n"
        "Copy the `.cursor/` directory into your project root:\n\n"
        "```bash\n"
        "cp -r cursor/.cursor/ ~/my-project/.cursor/\n"
        "```\n\n"
        "Cursor will load the rules from `.cursor/rules/bible-exegesis.mdc`.\n\n"
        "## Tool access\n\n"
        "Cursor supports terminal commands. You can call Bible APIs via curl:\n\n"
        "```bash\n"
        'curl -s "https://bolls.life/get-text/KJV/43/3/16-17/" | python -m json.tool\n'
        "```\n",
        encoding="utf-8",
    )


def build_grok(dest: Path, flattened: str):
    """Build Grok bundle."""
    dest.mkdir(parents=True, exist_ok=True)

    (dest / "system-prompt.md").write_text(flattened, encoding="utf-8")

    grok_config = (ROOT / "config" / "grok.md").read_text(encoding="utf-8")
    (dest / "api-examples.md").write_text(grok_config, encoding="utf-8")

    (dest / "SETUP.md").write_text(
        "# Grok Setup\n\n"
        "Grok does not have a persistent agent/instructions mechanism.\n"
        "Use one of these approaches:\n\n"
        "## Option A: Paste system prompt\n\n"
        "1. Open a new Grok conversation\n"
        "2. Paste the contents of `system-prompt.md` as your first message\n"
        "3. Follow with your exegesis question\n\n"
        "## Option B: Use Grok's code interpreter for API calls\n\n"
        "See `api-examples.md` for Python snippets that call Bible text APIs.\n"
        "Grok's code interpreter can execute these directly.\n\n"
        "## Limitations\n\n"
        "- No persistent file system — prompt must be re-pasted each session\n"
        "- No MCP server connections\n"
        "- Large system prompts may hit token limits — consider using a\n"
        "  trimmed version with only the skills you need\n",
        encoding="utf-8",
    )


def build_kiro(dest: Path, flattened: str):
    """Build AWS Kiro bundle."""
    dest.mkdir(parents=True, exist_ok=True)

    # .kiro/steering/bible-exegesis.md
    kiro_dir = dest / ".kiro" / "steering"
    kiro_dir.mkdir(parents=True, exist_ok=True)
    (kiro_dir / "bible-exegesis.md").write_text(flattened, encoding="utf-8")

    (dest / "SETUP.md").write_text(
        "# Kiro Setup\n\n"
        "Copy the `.kiro/` directory into your project root:\n\n"
        "```bash\n"
        "cp -r kiro/.kiro/ ~/my-project/.kiro/\n"
        "```\n\n"
        "Kiro will load steering documents from `.kiro/steering/bible-exegesis.md`.\n\n"
        "## Limitations\n\n"
        "- Kiro steering docs influence code generation context\n"
        "- No external API access for Bible text retrieval\n"
        "- Best for: embedding exegetical methodology into AI-assisted coding projects\n",
        encoding="utf-8",
    )


BUILDERS = {
    "claude": build_claude,
    "chatgpt": build_chatgpt,
    "copilot": build_copilot,
    "cursor": build_cursor,
    "grok": build_grok,
    "kiro": build_kiro,
}


def create_zip(dist_dir: Path) -> Path:
    """Create a distributable zip from the dist directory."""
    zip_name = f"{AGENT_NAME}-v{VERSION}"
    zip_path = ROOT / f"{zip_name}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(dist_dir.rglob("*")):
            if file.is_file():
                arcname = f"{zip_name}/{file.relative_to(dist_dir)}"
                zf.write(file, arcname)

    return zip_path


def build_dist_readme(dest: Path):
    """Write the top-level README for the distribution package."""
    (dest / "README.md").write_text(
        f"# Bible Exegesis Agent v{VERSION}\n\n"
        "A rigorous Bible exegesis assistant using the historical-grammatical method.\n"
        "Works across multiple AI platforms.\n\n"
        "## Quick Start\n\n"
        "### Interactive installer\n\n"
        "```bash\n"
        "# macOS / Linux\n"
        "chmod +x install.sh\n"
        "./install.sh\n\n"
        "# Windows (PowerShell)\n"
        ".\\install.ps1\n"
        "```\n\n"
        "### Manual setup\n\n"
        "Each platform directory contains a `SETUP.md` with detailed instructions:\n\n"
        "| Platform | Directory | Config format |\n"
        "|----------|-----------|---------------|\n"
        "| **Claude Code** | `claude/` | CLAUDE.md + skill tree |\n"
        "| **ChatGPT** | `chatgpt/` | Custom GPT config + system prompt |\n"
        "| **GitHub Copilot** | `copilot/` | `.github/copilot-instructions.md` |\n"
        "| **Cursor** | `cursor/` | `.cursor/rules/bible-exegesis.mdc` |\n"
        "| **Grok** | `grok/` | System prompt for paste-in |\n"
        "| **Kiro** | `kiro/` | `.kiro/steering/bible-exegesis.md` |\n\n"
        "## What's included\n\n"
        "- **System prompt** — the complete agent definition with all skills and references\n"
        "- **5 companion skills** — text retrieval, lexical analysis, grammatical analysis,\n"
        "  literary analysis, textual criticism\n"
        "- **4 reference documents** — hermeneutical method, confidence levels, prohibited\n"
        "  patterns, book abbreviations\n"
        "- **Platform-specific configs** — ready to copy into each AI system\n"
        "- **OpenAI function-calling schema** — for ChatGPT Custom GPTs and Assistants API\n\n"
        "## Capabilities\n\n"
        "- Passage exegesis (observation, structure, interpretation)\n"
        "- Word studies (Hebrew/Greek lemma, semantic range, concordance)\n"
        "- Grammar and syntax analysis (verb parsing, clause relationships)\n"
        "- Literary analysis (genre, chiasm, parallelism, narrative technique)\n"
        "- Textual criticism (manuscript variants, apparatus reading)\n"
        "- Translation comparison (public-domain + licensed via API)\n"
        "- Canonical cross-referencing (intertextual connections)\n\n"
        "## Design principles\n\n"
        "1. **Textual fidelity** — meaning comes from the text, not imposed on it\n"
        "2. **Historical-grammatical method** — grammar, syntax, literary context, historical context\n"
        "3. **Confidence signaling** — every claim tagged (high / plausible / ambiguous / disputed)\n"
        "4. **No theological imposition** — no frameworks, no premature harmonization\n"
        "5. **Observation first** — what it says, how it functions, what it means, then implications\n\n"
        "## License\n\n"
        "MIT License. See individual Bible translation licenses for text usage restrictions.\n",
        encoding="utf-8",
    )


def main():
    targets = PLATFORMS
    if "--clean" in sys.argv:
        if DIST.exists():
            shutil.rmtree(DIST)
        print("Cleaned dist/")
        sys.argv.remove("--clean")

    # Filter to specific platforms if requested
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        targets = [a for a in args if a in BUILDERS]
        if not targets:
            print(f"Unknown platform(s): {args}")
            print(f"Available: {', '.join(PLATFORMS)}")
            sys.exit(1)

    print(f"Building Bible Exegesis Agent v{VERSION}")
    print(f"Platforms: {', '.join(targets)}\n")

    # Build flattened prompt (used by all platforms)
    print("  Flattening system prompt + skills + references...")
    flattened = build_flattened_prompt()
    print(f"  Flattened prompt: {len(flattened):,} characters\n")

    # Build each platform
    for platform in targets:
        dest = DIST / platform
        print(f"  Building {platform}/ ...")
        BUILDERS[platform](dest, flattened)

    # Copy installers
    print("\n  Copying installers...")
    for installer in ["install.sh", "install.ps1"]:
        src = ROOT / installer
        if src.exists():
            shutil.copy2(src, DIST / installer)

    # Write distribution README
    build_dist_readme(DIST)

    # Create zip
    print("  Creating zip archive...")
    zip_path = create_zip(DIST)
    zip_size_mb = zip_path.stat().st_size / (1024 * 1024)

    print(f"\nBuild complete!")
    print(f"  Distribution: {DIST}")
    print(f"  Archive:      {zip_path} ({zip_size_mb:.1f} MB)")
    print(f"  Platforms:    {len(targets)}")


if __name__ == "__main__":
    main()
