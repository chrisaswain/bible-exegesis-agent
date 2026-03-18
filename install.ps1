#Requires -Version 5.1
<#
.SYNOPSIS
    Bible Exegesis Agent - Interactive Installer (Windows)
.DESCRIPTION
    Copies platform-specific config files to your project directory.
.PARAMETER Platform
    Platform choice (1-7). If omitted, prompts interactively.
.PARAMETER TargetDir
    Target directory. If omitted, prompts interactively.
.PARAMETER Force
    Skip confirmation prompts (create dirs, overwrite files).
#>
param(
    [string]$Platform,
    [string]$TargetDir,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$Version = "1.0.0"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host "Bible Exegesis Agent v$Version - Installer" -ForegroundColor White
Write-Host ""

# -- Platform selection --

if ([string]::IsNullOrWhiteSpace($Platform)) {
    Write-Host "Select your AI platform:" -ForegroundColor White
    Write-Host ""
    Write-Host "  1)  Claude Code       (CLAUDE.md + skill tree)" -ForegroundColor Cyan
    Write-Host "  2)  Claude Code       (single-file mode)" -ForegroundColor Cyan
    Write-Host "  3)  ChatGPT           (Custom GPT / Assistants API)" -ForegroundColor Cyan
    Write-Host "  4)  GitHub Copilot    (.github/copilot-instructions.md)" -ForegroundColor Cyan
    Write-Host "  5)  Cursor            (.cursor/rules/)" -ForegroundColor Cyan
    Write-Host "  6)  Grok              (paste-in system prompt)" -ForegroundColor Cyan
    Write-Host "  7)  Kiro              (.kiro/steering/)" -ForegroundColor Cyan
    Write-Host ""
    $Platform = Read-Host "Enter choice [1-7]"
}
$choice = $Platform

# -- Target directory --

if ([string]::IsNullOrWhiteSpace($TargetDir)) {
    Write-Host ""
    $defaultDir = Get-Location
    $TargetDir = Read-Host "Target project directory [$defaultDir]"
    if ([string]::IsNullOrWhiteSpace($TargetDir)) { $TargetDir = $defaultDir }
}
$targetDir = [System.IO.Path]::GetFullPath($TargetDir)

if (-not (Test-Path $targetDir -PathType Container)) {
    if ($Force) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    } else {
        $create = Read-Host "Directory does not exist. Create it? [Y/n]"
        if ($create -match '^[Yy]?$') {
            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        } else {
            Write-Host "Aborted." -ForegroundColor Red
            exit 1
        }
    }
}

# -- Resolve source directory --

$Src = $null
if (Test-Path (Join-Path $ScriptDir "claude")) {
    $Src = $ScriptDir
} elseif (Test-Path (Join-Path $ScriptDir "dist\claude")) {
    $Src = Join-Path $ScriptDir "dist"
} else {
    Write-Host "Error: Cannot find platform bundles." -ForegroundColor Red
    Write-Host "Run build.py first, or run this script from the dist/ directory."
    exit 1
}

# -- Helper --

$installCount = 0

function Copy-WithReport {
    param([string]$Source, [string]$Destination)
    $destDir = Split-Path -Parent $Destination
    if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
    if (Test-Path $Source -PathType Container) {
        Copy-Item -Path $Source -Destination $Destination -Recurse -Force
    } else {
        Copy-Item -Path $Source -Destination $Destination -Force
    }
    $relative = $Destination.Replace("$targetDir\", "").Replace("$targetDir/", "")
    Write-Host "  + $relative" -ForegroundColor Green
    $script:installCount++
}

# -- Install --

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Installing Claude Code (full skill tree)..." -ForegroundColor White
        Write-Host ""
        $base = Join-Path $targetDir "bible-exegesis-agent"
        Copy-WithReport (Join-Path $Src "claude\CLAUDE.md") (Join-Path $base "CLAUDE.md")
        Copy-WithReport (Join-Path $Src "claude\agents") (Join-Path $base "agents")
        Copy-WithReport (Join-Path $Src "claude\skills") (Join-Path $base "skills")
        Copy-WithReport (Join-Path $Src "claude\references") (Join-Path $base "references")
    }
    "2" {
        Write-Host ""
        Write-Host "Installing Claude Code (single-file mode)..." -ForegroundColor White
        Write-Host ""
        $dest = Join-Path $targetDir "CLAUDE.md"
        if ((Test-Path $dest) -and -not $Force) {
            $overwrite = Read-Host "Warning: CLAUDE.md already exists. Overwrite? [y/N]"
            if ($overwrite -notmatch '^[Yy]$') {
                Write-Host "Aborted." -ForegroundColor Red
                exit 1
            }
        }
        Copy-WithReport (Join-Path $Src "claude\system-prompt-full.md") $dest
    }
    "3" {
        Write-Host ""
        Write-Host "Installing ChatGPT config..." -ForegroundColor White
        Write-Host ""
        $base = Join-Path $targetDir "bible-exegesis-agent"
        Copy-WithReport (Join-Path $Src "chatgpt\system-prompt.md") (Join-Path $base "system-prompt.md")
        Copy-WithReport (Join-Path $Src "chatgpt\openai-config.json") (Join-Path $base "openai-config.json")
        Copy-WithReport (Join-Path $Src "chatgpt\create-assistant.py") (Join-Path $base "create-assistant.py")
        Copy-WithReport (Join-Path $Src "chatgpt\SETUP.md") (Join-Path $base "SETUP.md")
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Cyan
        Write-Host "  1. Open https://chat.openai.com/gpts/editor"
        Write-Host "  2. Paste system-prompt.md as the GPT instructions"
        Write-Host "  3. Import tools from openai-config.json"
        Write-Host "  4. See SETUP.md for full details"
    }
    "4" {
        Write-Host ""
        Write-Host "Installing GitHub Copilot config..." -ForegroundColor White
        Write-Host ""
        Copy-WithReport (Join-Path $Src "copilot\.github\copilot-instructions.md") (Join-Path $targetDir ".github\copilot-instructions.md")
    }
    "5" {
        Write-Host ""
        Write-Host "Installing Cursor rules..." -ForegroundColor White
        Write-Host ""
        Copy-WithReport (Join-Path $Src "cursor\.cursor\rules\bible-exegesis.mdc") (Join-Path $targetDir ".cursor\rules\bible-exegesis.mdc")
    }
    "6" {
        Write-Host ""
        Write-Host "Installing Grok config..." -ForegroundColor White
        Write-Host ""
        $base = Join-Path $targetDir "bible-exegesis-agent"
        Copy-WithReport (Join-Path $Src "grok\system-prompt.md") (Join-Path $base "system-prompt.md")
        Copy-WithReport (Join-Path $Src "grok\api-examples.md") (Join-Path $base "api-examples.md")
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Cyan
        Write-Host "  1. Open a Grok conversation"
        Write-Host "  2. Paste system-prompt.md as your first message"
        Write-Host "  3. See api-examples.md for Bible API code snippets"
    }
    "7" {
        Write-Host ""
        Write-Host "Installing Kiro steering document..." -ForegroundColor White
        Write-Host ""
        Copy-WithReport (Join-Path $Src "kiro\.kiro\steering\bible-exegesis.md") (Join-Path $targetDir ".kiro\steering\bible-exegesis.md")
    }
    default {
        Write-Host "Invalid choice: $choice" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "Done! Installed $installCount item(s) to $targetDir" -ForegroundColor Green
