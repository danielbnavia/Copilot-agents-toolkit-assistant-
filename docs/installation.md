# Installation Guide - Microsoft 365 Agent Toolkit Assistant

This guide covers the complete installation of all required Microsoft 365, Teams, and Agent SDKs.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Automated Installation](#automated-installation)
3. [Manual Installation](#manual-installation)
4. [SDK Overview](#sdk-overview)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

Before installing the M365 Agent Toolkit Assistant, ensure you have:

### Required
- **Python 3.8 or higher** - [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Internet connection** (for package downloads)

### Recommended
- **Node.js 16 or higher** - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** - [Download](https://git-scm.com/)

### For Development/Deployment
- **Microsoft 365 Developer Account** - [Get one free](https://developer.microsoft.com/microsoft-365/dev-program)
- **Azure Subscription** - [Free trial available](https://azure.microsoft.com/free/)

## Automated Installation

The easiest way to install all dependencies is using the provided setup scripts.

### On Linux/macOS:

```bash
# Make the setup script executable
chmod +x setup.sh

# Run the setup script
./setup.sh
```

### On Windows:

```cmd
# Run the setup script
setup.bat
```

The setup script will:
1. ✅ Verify Python installation
2. 📦 Install all Python packages from requirements.txt
3. 🔍 Check for Node.js and npm
4. 📦 Optionally install Teams Toolkit CLI
5. ✅ Verify all installations

## Manual Installation

If you prefer to install manually or the automated script fails:

### Step 1: Install Python Packages

```bash
pip install -r requirements.txt
```

This installs:

**Microsoft Bot Framework SDK:**
- `botbuilder-core>=4.15.0` - Core bot framework
- `botbuilder-schema>=4.15.0` - Schema definitions
- `botbuilder-dialogs>=4.15.0` - Dialog management
- `botbuilder-ai>=4.15.0` - AI capabilities
- `botbuilder-applicationinsights>=4.15.0` - Telemetry
- `botframework-connector>=4.15.0` - Bot connector

**Microsoft Teams SDK:**
- `msal>=1.24.0` - Microsoft Authentication Library
- `msal-extensions>=1.0.0` - MSAL extensions

**Microsoft Graph SDK:**
- `msgraph-core>=0.2.2` - Graph core library
- `msgraph-sdk>=1.0.0` - Graph SDK
- `azure-identity>=1.15.0` - Azure authentication

**Azure SDK:**
- `azure-mgmt-resource>=23.0.0` - Resource management
- `azure-mgmt-botservice>=2.0.0` - Bot service management
- `azure-mgmt-web>=7.0.0` - Web app management
- `azure-storage-blob>=12.19.0` - Blob storage

**Additional Libraries:**
- `adaptivecards>=1.0.0` - Adaptive Cards support
- `aiohttp>=3.9.0` - Async HTTP
- `requests>=2.31.0` - HTTP requests
- `python-dotenv>=1.0.0` - Environment variables
- `pyyaml>=6.0.1` - YAML support
- `jsonschema>=4.20.0` - JSON validation
- `rich>=13.7.0` - Pretty terminal output
- `click>=8.1.7` - CLI framework

### Step 2: Install Node.js (Optional but Recommended)

Download and install Node.js from [nodejs.org](https://nodejs.org/)

Verify installation:
```bash
node --version
npm --version
```

### Step 3: Install Teams Toolkit CLI (Optional)

If you have npm installed:

```bash
npm install -g @microsoft/teamsfx-cli
```

Verify installation:
```bash
teamsfx --version
```

## SDK Overview

### Microsoft Bot Framework SDK

The Bot Framework SDK enables building conversational AI for Teams and other channels.

**Key Components:**
- **botbuilder-core** - Activity handlers, middleware, state management
- **botbuilder-dialogs** - Conversation flows and prompts
- **botbuilder-ai** - LUIS, QnA Maker integration

**Use Cases:**
- Teams chatbots
- Conversational agents
- Interactive notifications

### Microsoft Graph SDK

Access Microsoft 365 data and services through a unified API.

**Capabilities:**
- User and group management
- Mail, calendar, contacts
- OneDrive files
- Teams messages and channels
- SharePoint lists

**Example:**
```python
from msgraph import GraphServiceClient
from azure.identity import DeviceCodeCredential

credential = DeviceCodeCredential()
client = GraphServiceClient(credentials=credential)
```

### Azure Identity

Handles authentication for Azure services and Microsoft Graph.

**Authentication Methods:**
- Device code flow
- Client credentials
- Managed identity
- Interactive browser

### MSAL (Microsoft Authentication Library)

Modern authentication library for acquiring tokens.

**Features:**
- OAuth 2.0 and OpenID Connect
- Token caching
- Single sign-on (SSO)

### Adaptive Cards

Framework for creating rich, platform-agnostic UI cards.

**Supported Platforms:**
- Microsoft Teams
- Outlook
- Bot Framework

### Azure Management SDKs

Programmatically manage Azure resources.

**Capabilities:**
- Deploy bot services
- Manage app services
- Configure resources
- Monitor deployments

## Verification

After installation, verify everything is set up correctly:

```bash
python setup_verify.py
```

This will check:
- ✅ Python version (3.8+)
- ✅ All Microsoft SDKs
- ✅ Azure SDKs
- ✅ Utility packages
- ⚠️  Node.js (optional)
- ⚠️  Teams Toolkit CLI (optional)

Expected output:
```
============================================================================
🚀 M365 AGENT TOOLKIT ASSISTANT - SETUP VERIFICATION
============================================================================

🔍 Checking Python version...
🔍 Checking Microsoft SDKs...
🔍 Checking Azure SDKs...
🔍 Checking utility packages...
🔍 Checking Node.js and npm...
🔍 Checking Teams Toolkit...

📊 SETUP VERIFICATION SUMMARY
============================================================================

✅ All required packages are installed!

✅ You're ready to use the M365 Agent Toolkit Assistant!
   Run: python assistant.py
```

## Troubleshooting

### Common Issues

#### 1. "pip: command not found"

**Solution:**
```bash
# On Linux/macOS
python3 -m pip install -r requirements.txt

# On Windows
python -m pip install -r requirements.txt
```

#### 2. "Permission denied" on Linux/macOS

**Solution:**
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 3. "Microsoft Visual C++ required" on Windows

Some packages require Visual C++ Build Tools.

**Solution:**
Download and install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

#### 4. SSL Certificate errors

**Solution:**
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

#### 5. Slow installation

**Solution:**
Use a faster mirror:
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

#### 6. Import errors after installation

**Solution:**
```bash
# Verify package installation
pip list | grep botbuilder
pip list | grep msgraph
pip list | grep azure

# Reinstall specific package
pip uninstall botbuilder-core
pip install botbuilder-core
```

### Package Conflicts

If you encounter version conflicts:

1. **Create a virtual environment:**
```bash
python3 -m venv m365-env
source m365-env/bin/activate  # On Linux/macOS
# or
m365-env\Scripts\activate  # On Windows
```

2. **Install packages in the clean environment:**
```bash
pip install -r requirements.txt
```

### Getting Help

If you still have issues:

1. **Check the setup verification output:**
   ```bash
   python setup_verify.py
   ```

2. **Review package versions:**
   ```bash
   pip list
   ```

3. **Check Python version:**
   ```bash
   python --version
   ```

4. **Open an issue on GitHub** with:
   - Your operating system
   - Python version
   - Error messages
   - Output of `pip list`

## Next Steps

After successful installation:

1. **Run the assistant:**
   ```bash
   python assistant.py
   ```

2. **Read the Getting Started guide:**
   ```bash
   cat docs/getting-started.md
   ```

3. **Try creating your first agent:**
   ```bash
   python assistant.py --mode declarative-agent
   ```

4. **Explore examples:**
   ```bash
   ls examples/
   ```

## Additional Resources

- [Python Package Index (PyPI)](https://pypi.org/)
- [Microsoft Bot Framework Documentation](https://docs.microsoft.com/en-us/azure/bot-service/)
- [Microsoft Graph Documentation](https://docs.microsoft.com/en-us/graph/)
- [Teams Toolkit Documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals)
- [Adaptive Cards Documentation](https://adaptivecards.io/)
- [Azure SDK for Python](https://docs.microsoft.com/en-us/azure/developer/python/)

---

Happy building with M365 Agent Toolkit Assistant! 🚀
