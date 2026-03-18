#!/usr/bin/env bash
#
# Bible Exegesis Agent — Interactive Installer
# Copies platform-specific config files to your project directory.
#
set -euo pipefail

VERSION="1.0.0"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Colors (skip if not a terminal)
if [ -t 1 ]; then
    BOLD='\033[1m'
    DIM='\033[2m'
    GREEN='\033[0;32m'
    CYAN='\033[0;36m'
    YELLOW='\033[0;33m'
    RED='\033[0;31m'
    RESET='\033[0m'
else
    BOLD='' DIM='' GREEN='' CYAN='' YELLOW='' RED='' RESET=''
fi

echo -e "${BOLD}Bible Exegesis Agent v${VERSION} — Installer${RESET}"
echo ""

# ── Platform selection ──────────────────────────────────────────────

echo -e "Select your AI platform:\n"
echo -e "  ${CYAN}1${RESET})  Claude Code       ${DIM}(CLAUDE.md + skill tree)${RESET}"
echo -e "  ${CYAN}2${RESET})  Claude Code       ${DIM}(single-file mode)${RESET}"
echo -e "  ${CYAN}3${RESET})  ChatGPT           ${DIM}(Custom GPT / Assistants API)${RESET}"
echo -e "  ${CYAN}4${RESET})  GitHub Copilot    ${DIM}(.github/copilot-instructions.md)${RESET}"
echo -e "  ${CYAN}5${RESET})  Cursor            ${DIM}(.cursor/rules/)${RESET}"
echo -e "  ${CYAN}6${RESET})  Grok              ${DIM}(paste-in system prompt)${RESET}"
echo -e "  ${CYAN}7${RESET})  Kiro              ${DIM}(.kiro/steering/)${RESET}"
echo ""
read -rp "Enter choice [1-7]: " choice

# ── Target directory ────────────────────────────────────────────────

echo ""
read -rp "Target project directory [$(pwd)]: " target_dir
target_dir="${target_dir:-$(pwd)}"
target_dir="${target_dir/#\~/$HOME}"

if [ ! -d "$target_dir" ]; then
    echo -e "${YELLOW}Directory does not exist. Create it? [Y/n]${RESET}"
    read -rp "" create_dir
    if [[ "${create_dir:-Y}" =~ ^[Yy] ]]; then
        mkdir -p "$target_dir"
    else
        echo -e "${RED}Aborted.${RESET}"
        exit 1
    fi
fi

# ── Resolve source directories ──────────────────────────────────────

# The installer may be run from the dist/ directory (after build.py)
# or from the zip extraction root. Detect which layout we're in.
if [ -d "$SCRIPT_DIR/claude" ]; then
    # We're in the dist/ or zip root
    SRC="$SCRIPT_DIR"
elif [ -d "$SCRIPT_DIR/dist/claude" ]; then
    # We're in the repo root
    SRC="$SCRIPT_DIR/dist"
else
    echo -e "${RED}Error: Cannot find platform bundles.${RESET}"
    echo "Run build.py first, or run this script from the dist/ directory."
    exit 1
fi

# ── Install ─────────────────────────────────────────────────────────

install_count=0

copy_with_report() {
    local src="$1" dst="$2"
    local dst_dir
    dst_dir="$(dirname "$dst")"
    mkdir -p "$dst_dir"
    cp -r "$src" "$dst"
    echo -e "  ${GREEN}+${RESET} $(echo "$dst" | sed "s|^$target_dir/||")"
    install_count=$((install_count + 1))
}

case "$choice" in
    1)
        echo -e "\n${BOLD}Installing Claude Code (full skill tree)...${RESET}\n"
        copy_with_report "$SRC/claude/CLAUDE.md" "$target_dir/bible-exegesis-agent/CLAUDE.md"
        copy_with_report "$SRC/claude/agents" "$target_dir/bible-exegesis-agent/agents"
        copy_with_report "$SRC/claude/skills" "$target_dir/bible-exegesis-agent/skills"
        copy_with_report "$SRC/claude/references" "$target_dir/bible-exegesis-agent/references"
        ;;
    2)
        echo -e "\n${BOLD}Installing Claude Code (single-file mode)...${RESET}\n"
        if [ -f "$target_dir/CLAUDE.md" ]; then
            echo -e "${YELLOW}Warning: CLAUDE.md already exists at target.${RESET}"
            read -rp "Overwrite? [y/N]: " overwrite
            if [[ ! "${overwrite:-N}" =~ ^[Yy] ]]; then
                echo -e "${RED}Aborted.${RESET}"
                exit 1
            fi
        fi
        copy_with_report "$SRC/claude/system-prompt-full.md" "$target_dir/CLAUDE.md"
        ;;
    3)
        echo -e "\n${BOLD}Installing ChatGPT config...${RESET}\n"
        mkdir -p "$target_dir/bible-exegesis-agent"
        copy_with_report "$SRC/chatgpt/system-prompt.md" "$target_dir/bible-exegesis-agent/system-prompt.md"
        copy_with_report "$SRC/chatgpt/openai-config.json" "$target_dir/bible-exegesis-agent/openai-config.json"
        copy_with_report "$SRC/chatgpt/create-assistant.py" "$target_dir/bible-exegesis-agent/create-assistant.py"
        copy_with_report "$SRC/chatgpt/SETUP.md" "$target_dir/bible-exegesis-agent/SETUP.md"
        echo ""
        echo -e "${CYAN}Next steps:${RESET}"
        echo "  1. Open https://chat.openai.com/gpts/editor"
        echo "  2. Paste system-prompt.md as the GPT instructions"
        echo "  3. Import tools from openai-config.json"
        echo "  4. See SETUP.md for full details"
        ;;
    4)
        echo -e "\n${BOLD}Installing GitHub Copilot config...${RESET}\n"
        copy_with_report "$SRC/copilot/.github/copilot-instructions.md" "$target_dir/.github/copilot-instructions.md"
        ;;
    5)
        echo -e "\n${BOLD}Installing Cursor rules...${RESET}\n"
        copy_with_report "$SRC/cursor/.cursor/rules/bible-exegesis.mdc" "$target_dir/.cursor/rules/bible-exegesis.mdc"
        ;;
    6)
        echo -e "\n${BOLD}Installing Grok config...${RESET}\n"
        mkdir -p "$target_dir/bible-exegesis-agent"
        copy_with_report "$SRC/grok/system-prompt.md" "$target_dir/bible-exegesis-agent/system-prompt.md"
        copy_with_report "$SRC/grok/api-examples.md" "$target_dir/bible-exegesis-agent/api-examples.md"
        echo ""
        echo -e "${CYAN}Next steps:${RESET}"
        echo "  1. Open a Grok conversation"
        echo "  2. Paste system-prompt.md as your first message"
        echo "  3. See api-examples.md for Bible API code snippets"
        ;;
    7)
        echo -e "\n${BOLD}Installing Kiro steering document...${RESET}\n"
        copy_with_report "$SRC/kiro/.kiro/steering/bible-exegesis.md" "$target_dir/.kiro/steering/bible-exegesis.md"
        ;;
    *)
        echo -e "${RED}Invalid choice: $choice${RESET}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}Done!${RESET} Installed ${install_count} item(s) to ${target_dir}"
