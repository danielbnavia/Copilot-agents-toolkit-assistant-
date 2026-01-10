#!/bin/bash

# Setup script for M365 Agent Toolkit Assistant
# This script installs all required Microsoft 365, Teams, and Agent SDKs

echo "============================================================================"
echo "🚀 M365 Agent Toolkit Assistant - Setup Script"
echo "============================================================================"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
REQUIRED_VERSION="3.8"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "❌ Python 3.8 or higher is required. Please install Python first."
    exit 1
fi

echo "✅ Python version OK: $(python3 --version)"
echo ""

# Install Python packages
echo "📦 Installing Python packages..."
echo "   This may take a few minutes..."
echo ""

pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install Python packages. Please check the error messages above."
    exit 1
fi

echo ""
echo "✅ Python packages installed successfully!"
echo ""

# Check Node.js
echo "🔍 Checking Node.js installation..."

if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js is not installed."
    echo "   Node.js is needed for Teams Toolkit and Teams development."
    echo "   Install from: https://nodejs.org/"
    echo ""
    NODE_INSTALLED=false
else
    NODE_VERSION=$(node --version)
    echo "✅ Node.js is installed: $NODE_VERSION"
    NODE_INSTALLED=true
    echo ""
fi

# Check npm
if [ "$NODE_INSTALLED" = true ]; then
    echo "🔍 Checking npm installation..."
    
    if ! command -v npm &> /dev/null; then
        echo "⚠️  npm is not installed (should come with Node.js)"
        NPM_INSTALLED=false
    else
        NPM_VERSION=$(npm --version)
        echo "✅ npm is installed: $NPM_VERSION"
        NPM_INSTALLED=true
        echo ""
    fi
fi

# Install Teams Toolkit CLI
if [ "$NPM_INSTALLED" = true ]; then
    echo "📦 Installing Microsoft Teams Toolkit CLI..."
    echo "   (This is optional but recommended for Teams development)"
    echo ""
    
    read -p "   Install Teams Toolkit CLI? (y/n) " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        npm install -g @microsoft/teamsfx-cli
        
        if [ $? -eq 0 ]; then
            echo "✅ Teams Toolkit CLI installed successfully!"
        else
            echo "⚠️  Failed to install Teams Toolkit CLI (you can install it later)"
        fi
    else
        echo "⏭️  Skipping Teams Toolkit CLI installation"
    fi
    echo ""
fi

# Verify installation
echo "🔍 Verifying installation..."
echo ""

python3 setup_verify.py

if [ $? -eq 0 ]; then
    echo ""
    echo "============================================================================"
    echo "🎉 Setup completed successfully!"
    echo "============================================================================"
    echo ""
    echo "Next steps:"
    echo "  1. Run the assistant: python3 assistant.py"
    echo "  2. Read the documentation: docs/getting-started.md"
    echo "  3. Try the examples: examples/"
    echo ""
    echo "For help, type 'help' in the interactive assistant"
    echo ""
else
    echo ""
    echo "============================================================================"
    echo "⚠️  Setup completed with warnings"
    echo "============================================================================"
    echo ""
    echo "Some optional packages are missing, but you can still use the assistant."
    echo "Review the messages above and install missing packages if needed."
    echo ""
fi
