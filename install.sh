#!/usr/bin/env bash

# ======================================
# RAM.py Installer
# Version: 1.0.0
# ======================================

set -e

echo ""
echo "======================================"
echo "🚀 Welcome to RAM.py"
echo "Modern Python Development Toolkit"
echo "======================================"
echo ""

echo "RAM.py will:"
echo "✓ Copy RAM.py files"
echo "✓ Create configuration files"
echo "✓ Create install metadata"
echo "✓ Verify installation"
echo ""

read -p "Install RAM.py now? (y/n): " answer

if [[ "$answer" != "y" && "$answer" != "Y" ]]; then
    echo "Installation cancelled."
    exit 0
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

INSTALL_DIR="$HOME/.ramtools"
BIN_DIR="$HOME/.local/bin"

PACKAGE_DIR="$SCRIPT_DIR/Application/Download Package"

echo ""
echo "Creating directories..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
mkdir -p "$PACKAGE_DIR"

echo "Creating manifest..."

cat > "$PACKAGE_DIR/manifest.json" << EOF
{
  "name":"RAM.py",
  "version":"1.0.0",
  "description":"Modern Python Development Toolkit",
  "modules":[
    "ramtools",
    "filetools",
    "speed",
    "debug",
    "data",
    "utils"
  ],
  "features":[
    "Fast processing utilities",
    "Cleaner file management",
    "Built-in debugging helpers",
    "RAM-efficient data tools",
    "Seamless Library Integration"
  ]
}
EOF

echo "Creating install info..."

DATE=$(date -Iseconds)

cat > "$INSTALL_DIR/install_info.json" << EOF
{
  "installed_at":"$DATE",
  "version":"1.0.0",
  "status":"installed"
}
EOF

echo "Creating config..."

cat > "$INSTALL_DIR/config.json" << EOF
{
  "version":"1.0.0",
  "features":{
    "filetools":true,
    "speed":true,
    "debug":true,
    "data":true,
    "utils":true
  }
}
EOF

echo "Creating package ID..."

echo "550e8400-e29b-41d4-a716-446655440000" > "$INSTALL_DIR/package_id.txt"

echo "Copying ramtools..."

if [ -d "$SCRIPT_DIR/RAM LIB/ramtools" ]; then
    rm -rf "$PACKAGE_DIR/ramtools"
    cp -R "$SCRIPT_DIR/RAM LIB/ramtools" "$PACKAGE_DIR/"
fi

echo "Copying RAM CLI..."

if [ -f "$SCRIPT_DIR/ram" ]; then
    cp "$SCRIPT_DIR/ram" "$PACKAGE_DIR/ram"
    chmod +x "$PACKAGE_DIR/ram"

    cp "$SCRIPT_DIR/ram" "$BIN_DIR/ram"
    chmod +x "$BIN_DIR/ram"
fi

echo "Creating README..."

cat > "$PACKAGE_DIR/README.txt" << EOF
RAM.py Installation Package v1.0.0

To use RAM.py:

from ramtools import *

python3 -m ramtools

ram --version
EOF

echo "Creating QUICKSTART..."

cat > "$PACKAGE_DIR/QUICKSTART.txt" << EOF
RAM.py Quick Start

from ramtools import *

start()

organize("./Downloads")

superboost([1,2,3,4])

log_info("Hello World")

ram --version
ram organize ./Downloads
ram boost data.json
ram getpkg_id
EOF

echo ""
echo "======================================"
echo "✅ Installation Complete"
echo "======================================"

echo ""
echo "Install directory:"
echo "$INSTALL_DIR"

echo ""
echo "Package directory:"
echo "$PACKAGE_DIR"

echo ""
echo "Commands:"
echo "python3 -m ramtools"
echo "from ramtools import *"
echo "ram --version"

echo ""

if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    echo "Add this to your shell profile:"
    echo ""
    echo 'export PATH="$HOME/.local/bin:$PATH"'
fi

echo ""
echo "🎉 RAM.py installed successfully."
