# Microsoft 365 Agent Toolkit Assistant

An AI-powered assistant designed to help you build with Microsoft 365 Agent Toolkit, including Declarative Agents, Teams Agents, Apps, Adaptive Cards, and Workflows.

## Overview

This assistant provides intelligent guidance, code generation, and best practices for working with:

- **Declarative Agents**: Build AI-powered agents using declarative configurations
- **Teams Agents**: Create custom agents for Microsoft Teams
- **Apps**: Develop Microsoft 365 applications
- **Adaptive Cards**: Design rich, interactive cards for Teams and other Microsoft 365 apps
- **Workflows**: Automate business processes with Power Automate integration

## Features

### Core Capabilities
- 🤖 **Expert AI Assistant** for M365 agent development with complete Microsoft 365 Agents Toolkit knowledge
- 📝 **Code generation** following official Microsoft schemas and best practices
- 🎨 **Adaptive Cards designer** with official schema templates
- 🔄 **Workflow automation** helpers with proper configuration
- 📚 **Comprehensive knowledge base** of M365 declarative agents, API plugins, and connectors
- 🛠️ **Official template library** for quick starts using Microsoft standards
- ✅ **Validation and testing** utilities with schema compliance checking
- 🔍 **Expert guidance** on capabilities, authentication, and deployment

### CLI Tools
- 🏪 **Template Manager** - Browse and import from Agent Store
- 🧪 **Test Framework** - Automated testing with scenarios
- 🔧 **CI/CD Helper** - Generate pipeline configurations

### Web UI (NEW!)
- 🎯 **Visual Workflow Designer** - Drag-and-drop workflow builder
- 🏗️ **Agent Builder** - Form-based declarative agent creator
- 🛒 **Template Gallery** - Community marketplace with 50+ templates

### Marketplace API (NEW!)
- 🌐 **RESTful API** - Backend for template marketplace
- 📦 **Template Management** - Browse, search, filter, and import
- 📊 **Analytics** - Download tracking, ratings, featured templates

### Video Tutorials (NEW!)
- 🎥 **12-Video Series** - Beginner to professional level
- 📜 **Production Scripts** - Ready-to-record tutorial scripts
- 🎬 **Production Guide** - Equipment, editing, publishing strategies

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 18 or higher (for Teams Toolkit and Web UI)
- Microsoft 365 Developer account
- Azure subscription (for deployment)
- npm or yarn (for Web UI)

### Installation

```bash
# Clone the repository
git clone https://github.com/danielbnavia/Copilot-agents-toolkit-assistant-.git
cd Copilot-agents-toolkit-assistant-

# Install Python dependencies
pip install -r requirements.txt

# Optional: Install Web UI dependencies
cd web-ui
npm install
cd ..

# Optional: Install API dependencies
cd api
pip install -r requirements.txt
cd ..
```

### Usage

```bash
# Start the interactive assistant
python assistant.py

# Use specific modules
python assistant.py --mode declarative-agent
python assistant.py --mode teams-agent
python assistant.py --mode adaptive-cards
python assistant.py --mode workflows

# Use CLI tools
python assistant.py --mode template-manager    # Browse and import templates
python assistant.py --mode test-framework      # Generate and run tests
python assistant.py --mode cicd-helper         # Create CI/CD pipelines

# Start Web UI (NEW!)
cd web-ui
npm run dev
# Open http://localhost:3000

# Start Marketplace API (NEW!)
cd api
python main.py
# API available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

## Project Structure

```
.
├── assistant.py              # Main assistant entry point
├── src/
│   ├── core/                # Core assistant functionality
│   ├── declarative_agents/  # Declarative Agents module
│   ├── teams_agents/        # Teams Agents module
│   ├── adaptive_cards/      # Adaptive Cards module
│   ├── workflows/           # Workflows module
│   ├── api_plugins/         # API Plugins module
│   ├── message_extensions/  # Message Extensions module
│   ├── graph_connectors/    # Graph Connectors module
│   ├── copilot_studio/      # Copilot Studio integration
│   ├── power_platform/      # Power Platform integration
│   ├── azure_integration/   # Azure AI Services integration
│   ├── cli_tools/           # CLI Tools
│   │   ├── template_manager.py  # Agent Store browser
│   │   ├── test_framework.py    # Testing framework
│   │   └── cicd_helper.py       # CI/CD generator
│   └── utils/               # Utility functions
├── web-ui/                  # Visual Workflow Designer (NEW!)
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── WorkflowDesigner.jsx
│   │   │   ├── AgentBuilder.jsx
│   │   │   └── TemplateGallery.jsx
│   │   └── styles/          # CSS files
│   ├── package.json
│   └── vite.config.js
├── api/                     # Marketplace API (NEW!)
│   ├── main.py             # FastAPI application
│   ├── requirements.txt    # API dependencies
│   └── README.md
├── video-tutorials/         # Video Tutorial Infrastructure (NEW!)
│   ├── scripts/            # Tutorial scripts
│   └── README.md           # Production guide
├── templates/              # Project templates
├── examples/               # Example projects (5 complete examples)
│   ├── customer-support-agent/
│   ├── sales-assistant/    # NEW!
│   ├── hr-bot/            # NEW!
│   ├── analytics-agent/   # NEW!
│   └── meeting-bot/       # NEW!
└── docs/                   # Documentation (8 comprehensive guides)
    ├── getting-started.md
    ├── declarative-agents.md
    ├── teams-agents.md
    ├── cli-tools.md
    ├── all-scenarios.md
    └── integration-recommendations.md
```

## Modules

### Declarative Agents

Create AI-powered agents using declarative JSON configurations:

```python
from src.declarative_agents import DeclarativeAgentHelper

helper = DeclarativeAgentHelper()
agent = helper.create_agent(
    name="Customer Support Agent",
    description="AI agent for customer support",
    capabilities=["answer_questions", "ticket_creation"]
)
```

### Teams Agents

Build custom agents for Microsoft Teams:

```python
from src.teams_agents import TeamsAgentHelper

helper = TeamsAgentHelper()
bot = helper.create_bot(
    name="Meeting Assistant",
    features=["meeting_scheduling", "notes_taking"]
)
```

### Adaptive Cards

Design and generate Adaptive Cards:

```python
from src.adaptive_cards import AdaptiveCardHelper

helper = AdaptiveCardHelper()
card = helper.create_card(
    card_type="approval",
    title="Request Approval",
    data={"requestor": "John Doe", "amount": "$500"}
)
```

### Workflows

Create and manage automated workflows:

```python
from src.workflows import WorkflowHelper

helper = WorkflowHelper()
workflow = helper.create_workflow(
    name="Document Approval",
    triggers=["document_uploaded"],
    actions=["send_notification", "request_approval"]
)
```

## Examples

See the `examples/` directory for 5 complete sample projects:

- **Customer Support Agent**: Declarative agent for handling customer inquiries with ticket management
- **Sales Assistant** (NEW!): Lead qualification, CRM integration, and pipeline management
- **HR Onboarding Bot** (NEW!): Automated employee onboarding with document distribution
- **Data Analytics Agent** (NEW!): Natural language queries and business intelligence
- **Meeting Insights Bot** (NEW!): Extract action items and summaries from Teams meetings

Each example includes:
- `declarativeAgent.json` - Complete agent manifest
- `instructions.txt` - Detailed behavior instructions
- `README.md` - Setup and usage guide

## Documentation

Comprehensive documentation is available in the `docs/` directory:

### Getting Started
- [Getting Started Guide](docs/getting-started.md)
- [Installation Guide](docs/installation.md)

### Core Modules
- [Declarative Agents Guide](docs/declarative-agents.md)
- [Teams Agents Guide](docs/teams-agents.md)
- [M365 Agents Knowledge Base](docs/m365-agents-knowledge-base.md)

### Advanced Features
- [All Scenarios Coverage](docs/all-scenarios.md)
- [Integration Recommendations](docs/integration-recommendations.md)
- [CLI Tools Guide](docs/cli-tools.md)

### Web UI & API
- [Web UI README](web-ui/README.md) - Visual workflow designer documentation
- [API README](api/README.md) - Marketplace API documentation
- [Video Tutorials Guide](video-tutorials/README.md) - Tutorial production guide
- [Future Enhancements](FUTURE-ENHANCEMENTS.md) - Implementation status

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Microsoft 365 Developer Documentation](https://docs.microsoft.com/en-us/microsoft-365/)
- [Teams Toolkit Documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals)
- [Adaptive Cards Documentation](https://adaptivecards.io/)
- [Power Automate Documentation](https://docs.microsoft.com/en-us/power-automate/)

## Support

For questions and support, please:
- Open an issue on GitHub
- Check the [FAQ](docs/faq.md)
- Review existing discussions

---

Built with ❤️ for the Microsoft 365 developer community