# Teams Agents Guide

Complete guide to building Microsoft Teams agents using the M365 Agent Toolkit Assistant.

## Table of Contents

1. [Introduction to Teams Agents](#introduction-to-teams-agents)
2. [Types of Teams Agents](#types-of-teams-agents)
3. [Getting Started](#getting-started)
4. [Building Your First Bot](#building-your-first-bot)
5. [Advanced Features](#advanced-features)
6. [Deployment](#deployment)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

## Introduction to Teams Agents

Teams agents are intelligent bots that interact with users in Microsoft Teams. They can:

- **Respond to messages** - Answer questions and provide information
- **Proactively notify** - Send updates and alerts
- **Execute commands** - Perform actions based on user requests
- **Integrate with services** - Connect to external APIs and systems
- **Use AI capabilities** - Leverage natural language understanding

## Types of Teams Agents

### 1. Conversational Bots

Simple bots that respond to user messages in chats.

**Use Cases:**
- FAQ bots
- Help desk assistants
- Information retrieval

**Example:**
```python
from src.teams_agents import TeamsAgentHelper

helper = TeamsAgentHelper()
bot = helper.create_bot(
    name="FAQ Bot",
    features=["basic_messaging"]
)
```

### 2. Command Bots

Bots that execute specific commands.

**Use Cases:**
- Meeting scheduling
- Task creation
- Data lookup

**Example:**
```python
bot = helper.create_bot(
    name="Task Manager Bot",
    features=["task_management", "notifications"]
)
```

### 3. Notification Bots

Bots that send proactive messages to users or channels.

**Use Cases:**
- Alert systems
- Status updates
- Workflow notifications

**Example:**
```python
bot = helper.create_bot(
    name="Alert Bot",
    features=["notifications"]
)
```

### 4. Meeting Bots

Bots that participate in Teams meetings.

**Use Cases:**
- Meeting transcription
- Note-taking
- Meeting assistance

**Example:**
```python
bot = helper.create_bot(
    name="Meeting Assistant",
    features=["meeting_scheduling", "notes_taking"]
)
```

## Getting Started

### Prerequisites

1. Microsoft 365 account
2. Teams Toolkit installed
3. Python 3.8+ with Bot Framework SDK
4. Azure subscription (for deployment)

### Quick Start

1. **Start the assistant:**
```bash
python assistant.py --mode teams-agent
```

2. **Create a new bot:**
- Select option 1: "Create new bot"
- Enter bot name
- Choose features
- Bot project is created

3. **Test locally:**
```bash
cd your-bot-name
python bot.py
```

4. **Connect with Bot Framework Emulator**

## Building Your First Bot

### Step 1: Interactive Creation

```bash
$ python assistant.py --mode teams-agent

👥 Teams Agent Mode

Teams Agent Commands:
  1. Create new bot
  2. Add feature to bot
  3. Test bot locally
  4. Back to main menu

Select option (1-4): 1

👥 Create New Teams Bot

Bot name: Hello Bot

Available features:
  1. meeting_scheduling - Schedule and manage meetings
  2. notes_taking - Take and share meeting notes
  3. task_management - Create and track tasks
  4. notifications - Send proactive notifications

Select features (comma-separated, e.g., 1,2): 3,4

✅ Teams bot created successfully!
📁 Location: hello-bot/
```

### Step 2: Understanding the Generated Code

The assistant creates:

**manifest.json** - Teams app manifest
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.16/MicrosoftTeams.schema.json",
  "manifestVersion": "1.16",
  "name": {
    "short": "Hello Bot"
  },
  "bots": [{
    "botId": "${BOT_ID}",
    "scopes": ["personal", "team", "groupchat"]
  }]
}
```

**bot.py** - Bot implementation
```python
class HelloBotBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Handle incoming messages
        text = turn_context.activity.text
        await turn_context.send_activity(f"You said: {text}")
```

**requirements.txt** - Dependencies
```
botbuilder-core>=4.15.0
botbuilder-schema>=4.15.0
aiohttp>=3.9.0
```

### Step 3: Customize Your Bot

Edit `bot.py` to add your logic:

```python
async def on_message_activity(self, turn_context: TurnContext):
    text = turn_context.activity.text.strip().lower()
    
    # Task management
    if text.startswith("create task"):
        task_name = text.replace("create task", "").strip()
        await self.create_task(turn_context, task_name)
    
    # Notifications
    elif text == "notify":
        await self.send_notification(turn_context)
    
    # Help
    elif text == "help":
        await self.send_help(turn_context)
    
    else:
        await turn_context.send_activity(
            f"I received: {text}. Type 'help' for commands."
        )

async def create_task(self, turn_context: TurnContext, task_name: str):
    # Your task creation logic here
    await turn_context.send_activity(f"✅ Created task: {task_name}")

async def send_notification(self, turn_context: TurnContext):
    # Send a notification
    await turn_context.send_activity("🔔 This is a notification!")
```

### Step 4: Test Locally

1. **Set environment variables:**
```bash
export MICROSOFT_APP_ID="your-app-id"
export MICROSOFT_APP_PASSWORD="your-app-password"
```

2. **Run the bot:**
```bash
python bot.py
```

3. **Use Bot Framework Emulator:**
   - Download from [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator)
   - Connect to `http://localhost:3978/api/messages`
   - Start chatting!

## Advanced Features

### Using Adaptive Cards

Send rich, interactive cards:

```python
from botbuilder.schema import Attachment
import json

async def send_card(self, turn_context: TurnContext):
    card = {
        "type": "AdaptiveCard",
        "version": "1.5",
        "body": [
            {
                "type": "TextBlock",
                "text": "Task Created",
                "weight": "Bolder",
                "size": "Large"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "View Task",
                "data": {"action": "view"}
            }
        ]
    }
    
    attachment = Attachment(
        content_type="application/vnd.microsoft.card.adaptive",
        content=card
    )
    
    await turn_context.send_activity(
        Activity(attachments=[attachment])
    )
```

### Handling Card Actions

```python
async def on_teams_card_action_invoke(self, turn_context: TurnContext):
    action_data = turn_context.activity.value
    action = action_data.get("action")
    
    if action == "view":
        await turn_context.send_activity("Opening task...")
```

### Proactive Messaging

Send messages outside of a conversation context:

```python
from botbuilder.core import ConversationReference
from botbuilder.schema import Activity

# Save conversation reference when user first messages
async def on_message_activity(self, turn_context: TurnContext):
    # Save reference for later
    conv_ref = TurnContext.get_conversation_reference(
        turn_context.activity
    )
    # Store conv_ref in your database
    
# Later, send proactive message
async def send_proactive_message(conv_ref, message):
    await adapter.continue_conversation(
        conv_ref,
        lambda tc: tc.send_activity(message),
        app_id
    )
```

### Teams-Specific Features

**Get team members:**
```python
from botbuilder.core import TeamsInfo

async def on_message_activity(self, turn_context: TurnContext):
    members = await TeamsInfo.get_team_members(turn_context)
    
    for member in members:
        print(f"Member: {member.name}")
```

**Send to specific channel:**
```python
from botbuilder.schema.teams import TeamInfo

async def send_to_channel(self, turn_context: TurnContext, message: str):
    team_id = turn_context.activity.teams_get_team_info().id
    channel_id = "specific-channel-id"
    
    await turn_context.adapter.create_conversation(
        ConversationParameters(
            channel_data={"channel": {"id": channel_id}},
            bot=turn_context.activity.recipient,
            tenant_id=turn_context.activity.conversation.tenant_id
        ),
        lambda tc: tc.send_activity(message)
    )
```

### Using Microsoft Graph

Access M365 data from your bot:

```python
from msgraph import GraphServiceClient
from azure.identity import ClientSecretCredential

credential = ClientSecretCredential(
    tenant_id="your-tenant-id",
    client_id="your-client-id",
    client_secret="your-secret"
)

graph_client = GraphServiceClient(credentials=credential)

# Get user info
user = await graph_client.users.by_user_id(user_id).get()
print(f"User: {user.display_name}")

# Send email
message = {
    "subject": "From Teams Bot",
    "body": {
        "contentType": "Text",
        "content": "Hello from bot!"
    },
    "toRecipients": [
        {
            "emailAddress": {
                "address": "user@example.com"
            }
        }
    ]
}

await graph_client.users.by_user_id(user_id).send_mail.post(message)
```

## Deployment

### Deploy to Azure

1. **Create Azure resources:**
```bash
# Using Azure CLI
az group create --name MyBotResourceGroup --location eastus
az bot create --resource-group MyBotResourceGroup --name MyBot --kind webapp
```

2. **Deploy code:**
```bash
# Using Teams Toolkit
teamsfx provision
teamsfx deploy
```

3. **Configure app settings:**
```bash
az webapp config appsettings set \
  --resource-group MyBotResourceGroup \
  --name MyBot \
  --settings MICROSOFT_APP_ID=your-app-id MICROSOFT_APP_PASSWORD=your-password
```

### Deploy with Teams Toolkit

1. **Open in VS Code with Teams Toolkit extension**
2. **Click "Provision in the Cloud"**
3. **Click "Deploy to the Cloud"**
4. **Publish to Teams**

## Best Practices

### 1. Error Handling

Always handle errors gracefully:

```python
async def on_message_activity(self, turn_context: TurnContext):
    try:
        # Your bot logic
        await self.process_message(turn_context)
    except Exception as e:
        logging.error(f"Error: {e}")
        await turn_context.send_activity(
            "Sorry, something went wrong. Please try again."
        )
```

### 2. Conversation State

Use state management for multi-turn conversations:

```python
from botbuilder.core import ConversationState, UserState

class MyBot(ActivityHandler):
    def __init__(self, conversation_state: ConversationState):
        self.conversation_state = conversation_state
        self.state_accessor = conversation_state.create_property("DialogState")
```

### 3. Security

- Never hardcode credentials
- Use Azure Key Vault for secrets
- Validate all user input
- Implement authentication when needed

### 4. Performance

- Use async/await properly
- Cache frequently accessed data
- Implement retry logic for external calls
- Monitor bot performance

### 5. User Experience

- Provide clear help messages
- Use typing indicators for long operations
- Send progress updates
- Handle interruptions gracefully

## Troubleshooting

### Bot doesn't respond

**Check:**
1. Bot is running: `ps aux | grep python`
2. Correct endpoint: `http://localhost:3978/api/messages`
3. Valid credentials in environment variables
4. Firewall/network settings

### Authentication errors

**Solution:**
```bash
# Verify credentials
echo $MICROSOFT_APP_ID
echo $MICROSOFT_APP_PASSWORD

# Test with Bot Framework Emulator
# Leave credentials empty for local testing
```

### Deployment fails

**Check:**
1. Azure subscription is active
2. Resource group exists
3. Bot name is unique
4. All required services are enabled

### Cards not displaying

**Ensure:**
1. Using correct Adaptive Card schema version
2. Card JSON is valid
3. Content type is set correctly
4. Teams client is up to date

## Additional Resources

- [Bot Framework Documentation](https://docs.microsoft.com/en-us/azure/bot-service/)
- [Teams Platform Documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/)
- [Bot Framework Samples](https://github.com/microsoft/BotBuilder-Samples)
- [Teams Toolkit](https://docs.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals)
- [Adaptive Cards Designer](https://adaptivecards.io/designer)

## Getting Help

Use the interactive assistant for help:

```bash
python assistant.py --mode teams-agent
```

Or access help within the assistant:
```
M365 Assistant> bot help
```

---

Happy building Teams agents! 👥🤖
