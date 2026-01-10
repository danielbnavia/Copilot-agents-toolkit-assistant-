# Getting Started with M365 Agent Toolkit Assistant

Welcome to the Microsoft 365 Agent Toolkit Assistant! This guide will help you get started with building agents, apps, and workflows for Microsoft 365.

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.8 or higher** installed
2. **Node.js 16 or higher** (for Teams development)
3. **Microsoft 365 Developer Account** - Get one at [Microsoft 365 Developer Program](https://developer.microsoft.com/microsoft-365/dev-program)
4. **Azure Subscription** (for deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/danielbnavia/Copilot-agents-toolkit-assistant-.git
cd Copilot-agents-toolkit-assistant-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the assistant executable:
```bash
chmod +x assistant.py
```

## Quick Start

### Interactive Mode

Start the assistant in interactive mode:

```bash
python assistant.py
```

You'll see a welcome message and can type commands like:
- `help` - Show available commands
- `create myproject` - Create a new project
- `agent new` - Create a declarative agent
- `bot new` - Create a Teams bot
- `card new` - Create an adaptive card
- `workflow new` - Create a workflow

### Specific Mode

Launch directly into a specific mode:

```bash
# Declarative Agent mode
python assistant.py --mode declarative-agent

# Teams Agent mode
python assistant.py --mode teams-agent

# Adaptive Cards mode
python assistant.py --mode adaptive-cards

# Workflows mode
python assistant.py --mode workflows
```

### Quick Project Creation

Create a project with a template:

```bash
# Create a basic declarative agent
python assistant.py --create my-agent --template basic-declarative-agent

# Create a Teams bot
python assistant.py --create my-bot --template basic-teams-bot

# Create a workflow
python assistant.py --create my-workflow --template basic-workflow
```

## Your First Declarative Agent

Let's create a simple customer support agent:

1. Start the assistant:
```bash
python assistant.py
```

2. Create a new agent:
```
M365 Assistant> agent new
```

3. Follow the prompts:
- Agent name: **Customer Support Agent**
- Description: **AI agent for handling customer inquiries**
- Capabilities: **1,3** (answer_questions and graph_api)

4. The assistant will create a `customer-support-agent.json` file with your agent configuration.

5. Test and deploy your agent using Teams Toolkit!

## Your First Teams Bot

Create a simple meeting assistant bot:

1. Run:
```bash
python assistant.py --mode teams-agent
```

2. Select option 1 (Create new bot)

3. Follow the prompts:
- Bot name: **Meeting Assistant**
- Features: **1,2** (meeting_scheduling and notes_taking)

4. Navigate to the created directory and follow the README for testing and deployment.

## Your First Adaptive Card

Create an approval card:

1. Run:
```bash
python assistant.py --mode adaptive-cards
```

2. Select option 1 (Create new card)

3. Follow the prompts:
- Card type: **2** (Approval)
- Title: **Expense Approval**
- Fill in the details

4. Test your card at [Adaptive Cards Designer](https://adaptivecards.io/designer)

## Your First Workflow

Create a document approval workflow:

1. Run:
```bash
python assistant.py --mode workflows
```

2. Select option 1 (Create new workflow)

3. Follow the prompts:
- Workflow name: **Document Approval**
- Triggers: **1** (document_uploaded)
- Actions: **1,2** (send_notification, request_approval)

4. Import the workflow into Power Automate!

## Next Steps

- Explore the [examples](../examples/) directory for more samples
- Read the detailed guides for each module:
  - [Declarative Agents Guide](declarative-agents.md)
  - [Teams Agents Guide](teams-agents.md)
  - [Adaptive Cards Guide](adaptive-cards.md)
  - [Workflows Guide](workflows.md)
- Check out [Best Practices](best-practices.md)
- Review the [FAQ](faq.md)

## Getting Help

If you encounter issues:

1. Type `help` in the interactive assistant
2. Check the documentation in the `docs/` directory
3. Review the examples in the `examples/` directory
4. Open an issue on GitHub

## Configuration

The assistant creates a configuration file at `~/.m365-assistant-config.json`. You can customize:

- Default template
- Output directory
- Azure settings
- M365 settings

Edit the file directly or use the configuration commands in the assistant.

Happy building! 🚀
