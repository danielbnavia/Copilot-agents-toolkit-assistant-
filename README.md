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

- 🤖 **Expert AI Assistant** for M365 agent development with complete Microsoft 365 Agents Toolkit knowledge
- 📝 **Code generation** following official Microsoft schemas and best practices
- 🎨 **Adaptive Cards designer** with official schema templates
- 🔄 **Workflow automation** helpers with proper configuration
- 📚 **Comprehensive knowledge base** of M365 declarative agents, API plugins, and connectors
- 🛠️ **Official template library** for quick starts using Microsoft standards
- ✅ **Validation and testing** utilities with schema compliance checking
- 🔍 **Expert guidance** on capabilities, authentication, and deployment

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher (for Teams Toolkit integration)
- Microsoft 365 Developer account
- Azure subscription (for deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/danielbnavia/Copilot-agents-toolkit-assistant-.git
cd Copilot-agents-toolkit-assistant-

# Install dependencies
pip install -r requirements.txt
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
```

## Project Structure

```
.
├── assistant.py              # Main assistant entry point
├── src/
│   ├── core/                # Core assistant functionality
│   │   ├── assistant.py     # Main assistant logic
│   │   └── config.py        # Configuration management
│   ├── declarative_agents/  # Declarative Agents module
│   ├── teams_agents/        # Teams Agents module
│   ├── adaptive_cards/      # Adaptive Cards module
│   ├── workflows/           # Workflows module
│   └── utils/               # Utility functions
├── templates/               # Project templates
├── examples/                # Example projects
└── docs/                    # Documentation
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

See the `examples/` directory for complete sample projects:

- **Customer Support Agent**: Declarative agent for handling customer inquiries
- **Meeting Bot**: Teams bot for managing meetings
- **Approval Cards**: Adaptive cards for approval workflows
- **Onboarding Workflow**: Automated employee onboarding process

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- [Getting Started Guide](docs/getting-started.md)
- [Declarative Agents Guide](docs/declarative-agents.md)
- [Teams Agents Guide](docs/teams-agents.md)
- [Adaptive Cards Guide](docs/adaptive-cards.md)
- [Workflows Guide](docs/workflows.md)
- [Best Practices](docs/best-practices.md)

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