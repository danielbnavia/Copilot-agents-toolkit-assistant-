@echo off
REM Setup script for M365 Agent Toolkit Assistant (Windows)
REM This script installs all required Microsoft 365, Teams, and Agent SDKs

echo ============================================================================
echo 🚀 M365 Agent Toolkit Assistant - Setup Script
echo ============================================================================
echo.

REM Check Python version
echo 🔍 Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo    Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

python --version
echo.

REM Install Python packages
echo 📦 Installing Python packages...
echo    This may take a few minutes...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install Python packages. Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo ✅ Python packages installed successfully!
echo.

REM Check Node.js
echo 🔍 Checking Node.js installation...

node --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Node.js is not installed.
    echo    Node.js is needed for Teams Toolkit and Teams development.
    echo    Install from: https://nodejs.org/
    echo.
    set NODE_INSTALLED=false
) else (
    node --version
    echo ✅ Node.js is installed
    set NODE_INSTALLED=true
    echo.
)

REM Check npm
if "%NODE_INSTALLED%"=="true" (
    echo 🔍 Checking npm installation...
    
    npm --version >nul 2>&1
    if errorlevel 1 (
        echo ⚠️  npm is not installed (should come with Node.js)
        set NPM_INSTALLED=false
    ) else (
        npm --version
        echo ✅ npm is installed
        set NPM_INSTALLED=true
        echo.
    )
)

REM Install Teams Toolkit CLI
if "%NPM_INSTALLED%"=="true" (
    echo 📦 Installing Microsoft Teams Toolkit CLI...
    echo    (This is optional but recommended for Teams development)
    echo.
    
    set /p INSTALL_TT="   Install Teams Toolkit CLI? (y/n): "
    
    if /i "%INSTALL_TT%"=="y" (
        npm install -g @microsoft/teamsfx-cli
        
        if errorlevel 1 (
            echo ⚠️  Failed to install Teams Toolkit CLI (you can install it later)
        ) else (
            echo ✅ Teams Toolkit CLI installed successfully!
        )
    ) else (
        echo ⏭️  Skipping Teams Toolkit CLI installation
    )
    echo.
)

REM Verify installation
echo 🔍 Verifying installation...
echo.

python setup_verify.py

if errorlevel 1 (
    echo.
    echo ============================================================================
    echo ⚠️  Setup completed with warnings
    echo ============================================================================
    echo.
    echo Some optional packages are missing, but you can still use the assistant.
    echo Review the messages above and install missing packages if needed.
    echo.
) else (
    echo.
    echo ============================================================================
    echo 🎉 Setup completed successfully!
    echo ============================================================================
    echo.
    echo Next steps:
    echo   1. Run the assistant: python assistant.py
    echo   2. Read the documentation: docs\getting-started.md
    echo   3. Try the examples: examples\
    echo.
    echo For help, type 'help' in the interactive assistant
    echo.
)

pause
