# =====================================
# RAM.py Installer
# Version 1.0.0
# =====================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "====================================="
Write-Host "🚀 Welcome to RAM.py"
Write-Host "Modern Python Development Toolkit"
Write-Host "====================================="
Write-Host ""

Write-Host "RAM.py will:"
Write-Host "✓ Copy RAM.py files"
Write-Host "✓ Create configuration files"
Write-Host "✓ Create install metadata"
Write-Host "✓ Verify installation"
Write-Host ""

$answer = Read-Host "Install RAM.py now? (Y/N)"

if ($answer -ne "Y" -and $answer -ne "y") {
    Write-Host "Installation cancelled."
    exit
}

# Directories

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

$InstallDir = Join-Path $HOME ".ramtools"

$BinDir = Join-Path $HOME ".local\bin"

$PackageDir = Join-Path $ScriptDir "Application\Download Package"

New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
New-Item -ItemType Directory -Force -Path $BinDir | Out-Null
New-Item -ItemType Directory -Force -Path $PackageDir | Out-Null

Write-Host "Creating manifest..."

$manifest = @{
    name = "RAM.py"
    version = "1.0.0"
    description = "Modern Python Development Toolkit"

    modules = @(
        "ramtools"
        "filetools"
        "speed"
        "debug"
        "data"
        "utils"
    )

    features = @(
        "Fast processing utilities"
        "Cleaner file management"
        "Built-in debugging helpers"
        "RAM-efficient data tools"
        "Seamless Library Integration"
    )
}

$manifest | ConvertTo-Json -Depth 10 |
Set-Content "$PackageDir\manifest.json"

Write-Host "Creating install info..."

$installInfo = @{
    installed_at = (Get-Date).ToString("o")
    version = "1.0.0"
    status = "installed"
}

$installInfo | ConvertTo-Json |
Set-Content "$InstallDir\install_info.json"

Write-Host "Creating config..."

$config = @{
    version = "1.0.0"

    features = @{
        filetools = $true
        speed = $true
        debug = $true
        data = $true
        utils = $true
    }
}

$config | ConvertTo-Json -Depth 5 |
Set-Content "$InstallDir\config.json"

Write-Host "Creating package ID..."

"550e8400-e29b-41d4-a716-446655440000" |
Set-Content "$InstallDir\package_id.txt"

# Copy ramtools

$ramtoolsSource = Join-Path $ScriptDir "RAM LIB\ramtools"

if (Test-Path $ramtoolsSource) {

    $ramtoolsDest = Join-Path $PackageDir "ramtools"

    if (Test-Path $ramtoolsDest) {
        Remove-Item $ramtoolsDest -Recurse -Force
    }

    Copy-Item $ramtoolsSource `
        -Destination $ramtoolsDest `
        -Recurse
}

# Copy RAM CLI

$ramCli = Join-Path $ScriptDir "ram"

if (Test-Path $ramCli) {

    Copy-Item $ramCli `
        -Destination "$PackageDir\ram"

    Copy-Item $ramCli `
        -Destination "$BinDir\ram"
}

# Create README

@"
RAM.py Installation Package v1.0.0

Usage:

from ramtools import *

python -m ramtools

ram --version
"@ | Set-Content "$PackageDir\README.txt"

# Create QUICKSTART

@"
RAM.py Quick Start

from ramtools import *

start()

organize("./Downloads")

superboost([1,2,3])

log_info("Hello World")

ram --version

ram organize ./Downloads

ram boost data.json

ram getpkg_id
"@ | Set-Content "$PackageDir\QUICKSTART.txt"

Write-Host ""
Write-Host "====================================="
Write-Host "✅ Installation Complete"
Write-Host "====================================="
Write-Host ""

Write-Host "Install Directory:"
Write-Host $InstallDir

Write-Host ""
Write-Host "Package Directory:"
Write-Host $PackageDir

Write-Host ""
Write-Host "Commands:"
Write-Host "python -m ramtools"
Write-Host "from ramtools import *"
Write-Host "ram --version"

Write-Host ""

if ($env:PATH -notlike "*$HOME\.local\bin*") {

    Write-Host "Add this folder to PATH:"
    Write-Host "$HOME\.local\bin"
}

Write-Host ""
Write-Host "🎉 RAM.py installed successfully."
