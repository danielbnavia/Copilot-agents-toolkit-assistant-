"""Teams Agents helper module"""

import json
import os
from typing import Dict, Any, List, Optional


class TeamsAgentHelper:
    """Helper class for creating and managing Teams agents and bots."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Teams agent helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def create_bot(self, name: str, features: List[str]) -> Dict[str, Any]:
        """Create a new Teams bot configuration.
        
        Args:
            name: Bot name
            features: List of bot features
            
        Returns:
            Bot configuration dictionary
        """
        bot_config = {
            "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.16/MicrosoftTeams.schema.json",
            "manifestVersion": "1.16",
            "version": "1.0.0",
            "id": "${TEAMS_APP_ID}",
            "packageName": f"com.teams.{name.lower().replace(' ', '')}",
            "developer": {
                "name": "Teams Developer",
                "websiteUrl": "https://www.example.com",
                "privacyUrl": "https://www.example.com/privacy",
                "termsOfUseUrl": "https://www.example.com/terms"
            },
            "icons": {
                "color": "color.png",
                "outline": "outline.png"
            },
            "name": {
                "short": name,
                "full": name
            },
            "description": {
                "short": f"{name} - A Teams bot",
                "full": f"{name} is a bot for Microsoft Teams with advanced features"
            },
            "accentColor": "#FFFFFF",
            "bots": [
                {
                    "botId": "${BOT_ID}",
                    "scopes": ["personal", "team", "groupchat"],
                    "supportsFiles": "meeting_scheduling" in features,
                    "isNotificationOnly": False,
                    "commandLists": self._build_command_list(features)
                }
            ],
            "permissions": ["identity", "messageTeamMembers"],
            "validDomains": []
        }
        
        return bot_config
        
    def _build_command_list(self, features: List[str]) -> List[Dict[str, Any]]:
        """Build command list based on features.
        
        Args:
            features: List of bot features
            
        Returns:
            List of command configurations
        """
        commands = []
        
        if "meeting_scheduling" in features:
            commands.append({
                "scopes": ["personal", "team", "groupchat"],
                "commands": [
                    {
                        "title": "Schedule Meeting",
                        "description": "Schedule a new meeting"
                    }
                ]
            })
            
        if "notes_taking" in features:
            commands.append({
                "scopes": ["personal", "team", "groupchat"],
                "commands": [
                    {
                        "title": "Take Notes",
                        "description": "Start taking meeting notes"
                    }
                ]
            })
            
        return commands if commands else [{"scopes": ["personal", "team", "groupchat"], "commands": []}]
        
    def create_new_bot(self):
        """Interactive bot creation."""
        print("\n👥 Create New Teams Bot\n")
        
        name = input("Bot name: ").strip()
        
        print("\nAvailable features:")
        print("  1. meeting_scheduling - Schedule and manage meetings")
        print("  2. notes_taking - Take and share meeting notes")
        print("  3. task_management - Create and track tasks")
        print("  4. notifications - Send proactive notifications")
        
        feature_input = input("\nSelect features (comma-separated, e.g., 1,2): ").strip()
        
        feature_map = {
            "1": "meeting_scheduling",
            "2": "notes_taking",
            "3": "task_management",
            "4": "notifications"
        }
        
        features = [feature_map[f.strip()] for f in feature_input.split(",") if f.strip() in feature_map]
        
        bot = self.create_bot(name, features)
        
        # Create bot project structure
        bot_dir = name.lower().replace(' ', '-')
        os.makedirs(bot_dir, exist_ok=True)
        
        # Save manifest
        manifest_path = os.path.join(bot_dir, "manifest.json")
        try:
            with open(manifest_path, 'w') as f:
                json.dump(bot, f, indent=2)
        except OSError as e:
            print(f"❌ Failed to save manifest: {e}")
            return
            
        # Create basic bot code
        self._create_bot_code(bot_dir, name, features)
        
        print(f"\n✅ Teams bot created successfully!")
        print(f"📁 Location: {bot_dir}/")
        print(f"\nFiles created:")
        print(f"  • manifest.json - Teams app manifest")
        print(f"  • bot.py - Bot implementation")
        print(f"  • requirements.txt - Python dependencies")
        print(f"\nNext steps:")
        print(f"  1. cd {bot_dir}")
        print(f"  2. pip install -r requirements.txt")
        print(f"  3. Configure your bot credentials")
        print(f"  4. Run: python bot.py")
        
    def _create_bot_code(self, bot_dir: str, name: str, features: List[str]):
        """Create basic bot implementation code.
        
        Args:
            bot_dir: Bot directory
            name: Bot name
            features: List of features
        """
        bot_code = f'''"""
{name} - Teams Bot Implementation
"""

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class {name.replace(' ', '')}Bot(ActivityHandler):
    """Teams bot implementation for {name}."""
    
    async def on_message_activity(self, turn_context: TurnContext):
        """Handle incoming messages."""
        text = turn_context.activity.text.strip().lower()
        
        if text == "hello" or text == "hi":
            await turn_context.send_activity(f"Hello! I'm {name}. How can I help you today?")
        elif text == "help":
            await self.send_help(turn_context)
        else:
            await turn_context.send_activity(f"You said: {{turn_context.activity.text}}")
    
    async def on_members_added_activity(
        self, members_added: list[ChannelAccount], turn_context: TurnContext
    ):
        """Handle new members being added to the conversation."""
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    f"Welcome to {name}! Type 'help' to see what I can do."
                )
    
    async def send_help(self, turn_context: TurnContext):
        """Send help information."""
        help_text = "**Available Commands:**\\n\\n"
'''
        
        if "meeting_scheduling" in features:
            bot_code += '''        help_text += "• `schedule meeting` - Schedule a new meeting\\n"
'''
        if "notes_taking" in features:
            bot_code += '''        help_text += "• `take notes` - Start taking notes\\n"
'''
        if "task_management" in features:
            bot_code += '''        help_text += "• `create task` - Create a new task\\n"
'''
        
        bot_code += '''        
        await turn_context.send_activity(help_text)


# Bot startup code
if __name__ == "__main__":
    import os
    from aiohttp import web
    from botbuilder.core import BotFrameworkAdapterSettings, BotFrameworkAdapter
    from botbuilder.schema import Activity
    
    # Create adapter
    settings = BotFrameworkAdapterSettings(
        os.getenv("MICROSOFT_APP_ID", ""),
        os.getenv("MICROSOFT_APP_PASSWORD", "")
    )
    adapter = BotFrameworkAdapter(settings)
    
    # Create bot
    bot = ''' + name.replace(' ', '') + '''Bot()
    
    # Listen for incoming requests
    async def messages(req: web.Request) -> web.Response:
        """Handle incoming messages."""
        if "application/json" in req.headers["Content-Type"]:
            body = await req.json()
        else:
            return web.Response(status=415)
        
        activity = Activity().deserialize(body)
        auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""
        
        response = await adapter.process_activity(activity, auth_header, bot.on_turn)
        if response:
            return web.json_response(data=response.body, status=response.status)
        return web.Response(status=201)
    
    app = web.Application()
    app.router.add_post("/api/messages", messages)
    
    print(f"Starting {name}...")
    print("Bot is listening on http://localhost:3978/api/messages")
    web.run_app(app, host="localhost", port=3978)
'''
        
        try:
            with open(os.path.join(bot_dir, "bot.py"), 'w') as f:
                f.write(bot_code)
        except OSError as e:
            print(f"❌ Failed to write bot.py: {e}")
            return
            
        # Create requirements.txt
        requirements = """botbuilder-core>=4.14.0
botbuilder-schema>=4.14.0
aiohttp>=3.8.0
"""
        try:
            with open(os.path.join(bot_dir, "requirements.txt"), 'w') as f:
                f.write(requirements)
        except OSError as e:
            print(f"❌ Failed to write requirements.txt: {e}")
            
    def add_feature(self):
        """Add a feature to an existing bot."""
        print("\n➕ Add Feature to Bot\n")
        print("This feature is coming soon!")
        
    def test_bot(self):
        """Test bot locally."""
        print("\n🧪 Test Bot Locally\n")
        print("To test your bot:")
        print("  1. Install Bot Framework Emulator")
        print("  2. Run your bot: python bot.py")
        print("  3. Connect emulator to http://localhost:3978/api/messages")
        print("  4. Start chatting with your bot!")
        
    def show_help(self):
        """Display comprehensive help for Teams agents."""
        help_text = """
╔══════════════════════════════════════════════════════════════════════╗
║                     TEAMS AGENTS HELP                                ║
╚══════════════════════════════════════════════════════════════════════╝

📚 WHAT ARE TEAMS AGENTS?

Teams agents are intelligent bots that interact with users in Microsoft Teams.
They can respond to messages, send notifications, execute commands, and more.

🎯 TYPES OF TEAMS AGENTS:

  1. Conversational Bots
     - Simple Q&A bots
     - Help desk assistants
     - Information retrieval
     
  2. Command Bots
     - Execute specific tasks
     - Meeting scheduling
     - Task management
     
  3. Notification Bots
     - Send proactive alerts
     - Status updates
     - Workflow notifications
     
  4. Meeting Bots
     - Join Teams meetings
     - Take notes
     - Provide meeting assistance

🚀 GETTING STARTED:

  Step 1: Create a new bot
          → Select option 1 from the menu
          → Choose a descriptive name
          → Select features you need
          
  Step 2: Test locally
          → Navigate to the bot directory
          → Run: python bot.py
          → Use Bot Framework Emulator
          
  Step 3: Deploy to Azure
          → Use Teams Toolkit
          → Or deploy manually via Azure Portal
          
  Step 4: Publish to Teams
          → Upload to Teams Admin Center
          → Install in your organization

📦 AVAILABLE FEATURES:

  • meeting_scheduling - Schedule and manage meetings
  • notes_taking - Take and share meeting notes
  • task_management - Create and track tasks
  • notifications - Send proactive notifications

🛠️ BOT STRUCTURE:

Your bot project includes:
  
  manifest.json         - Teams app manifest (defines bot metadata)
  bot.py               - Bot implementation (handles messages)
  requirements.txt     - Python dependencies
  README.md            - Setup and deployment guide

💡 SAMPLE BOT CODE:

  class MyBot(ActivityHandler):
      async def on_message_activity(self, turn_context):
          text = turn_context.activity.text
          
          if text.lower() == "hello":
              await turn_context.send_activity("Hi there!")
          elif text.lower() == "help":
              await self.send_help(turn_context)
          else:
              await turn_context.send_activity(f"You said: {text}")

🎨 USING ADAPTIVE CARDS:

Send rich, interactive cards in your bot:

  card = {
      "type": "AdaptiveCard",
      "version": "1.5",
      "body": [
          {"type": "TextBlock", "text": "Hello from bot!"}
      ],
      "actions": [
          {"type": "Action.Submit", "title": "Click me"}
      ]
  }

🔐 AUTHENTICATION:

For production deployment, you'll need:
  
  • MICROSOFT_APP_ID - Your bot's app ID
  • MICROSOFT_APP_PASSWORD - Your bot's password
  • Register at: https://dev.botframework.com/

📚 LEARNING RESOURCES:

  • Full Guide: docs/teams-agents.md
  • Bot Framework: https://dev.botframework.com/
  • Teams Platform: https://docs.microsoft.com/en-us/microsoftteams/platform/
  • Samples: https://github.com/microsoft/BotBuilder-Samples

❓ COMMON TASKS:

  Q: How do I send a message to a specific channel?
  A: Use TeamsInfo and conversation references
  
  Q: How do I handle button clicks on Adaptive Cards?
  A: Implement on_teams_card_action_invoke method
  
  Q: How do I access user information?
  A: Use Microsoft Graph API with proper permissions
  
  Q: How do I debug my bot?
  A: Use Bot Framework Emulator for local testing

💬 NEED MORE HELP?

  • Type 'tutorial' for a step-by-step tutorial
  • Type 'examples' to see code examples
  • Type 'tips' for best practices and tips
  • Read the full guide in docs/teams-agents.md

Press Enter to continue...
"""
        print(help_text)
        input()
        
    def show_tutorial(self):
        """Show interactive tutorial for building Teams agents."""
        print("\n" + "="*70)
        print("🎓 TEAMS AGENTS TUTORIAL")
        print("="*70)
        
        print("\n📖 LESSON 1: Understanding Teams Bots\n")
        print("Teams bots are applications that interact with users through")
        print("conversation. They can:")
        print("  • Answer questions")
        print("  • Execute commands")
        print("  • Send notifications")
        print("  • Integrate with other services")
        
        input("\nPress Enter to continue...")
        
        print("\n📖 LESSON 2: Bot Framework Basics\n")
        print("Your bot uses the Microsoft Bot Framework, which provides:")
        print("  • ActivityHandler - Base class for your bot")
        print("  • TurnContext - Information about the current conversation")
        print("  • Activity - Messages and events")
        
        print("\nKey methods to override:")
        print("  • on_message_activity - Handle user messages")
        print("  • on_members_added_activity - Welcome new users")
        print("  • on_teams_card_action_invoke - Handle card button clicks")
        
        input("\nPress Enter to continue...")
        
        print("\n📖 LESSON 3: Creating Your First Bot\n")
        print("Let's create a simple 'Hello World' bot:")
        
        print("\nStep 1: Create the bot")
        print("  → Select option 1 from the main menu")
        print("  → Name: 'Hello Bot'")
        print("  → Features: Leave blank for basic bot")
        
        print("\nStep 2: Understand the generated code")
        print("  → bot.py contains your bot logic")
        print("  → manifest.json defines your Teams app")
        
        print("\nStep 3: Test locally")
        print("  → Run: python bot.py")
        print("  → Connect Bot Framework Emulator")
        print("  → Send a message!")
        
        input("\nPress Enter to continue...")
        
        print("\n📖 LESSON 4: Adding Features\n")
        print("Enhance your bot with features:")
        
        print("\n1. Respond to specific commands:")
        print('''
  async def on_message_activity(self, turn_context):
      text = turn_context.activity.text.lower()
      
      if text == "help":
          await turn_context.send_activity("I can help you!")
      elif text.startswith("create task"):
          await self.create_task(turn_context, text)
''')
        
        print("\n2. Send Adaptive Cards:")
        print('''
  card = {
      "type": "AdaptiveCard",
      "body": [{"type": "TextBlock", "text": "Hello!"}]
  }
  attachment = Attachment(content_type="application/vnd.microsoft.card.adaptive",
                         content=card)
  await turn_context.send_activity(Activity(attachments=[attachment]))
''')
        
        input("\nPress Enter to continue...")
        
        print("\n📖 LESSON 5: Deployment\n")
        print("Deploy your bot to Azure:")
        
        print("\nOption A: Using Teams Toolkit (Recommended)")
        print("  1. Open in VS Code with Teams Toolkit extension")
        print("  2. Click 'Provision in the Cloud'")
        print("  3. Click 'Deploy to the Cloud'")
        print("  4. Click 'Publish to Teams'")
        
        print("\nOption B: Manual Azure Deployment")
        print("  1. Create Azure Bot resource")
        print("  2. Create Azure App Service")
        print("  3. Deploy your code")
        print("  4. Configure bot endpoint")
        print("  5. Upload manifest to Teams")
        
        input("\nPress Enter to continue...")
        
        print("\n✅ Tutorial Complete!\n")
        print("You now know the basics of Teams bots. Next steps:")
        print("  • Create your first bot using option 1")
        print("  • Read the full guide: docs/teams-agents.md")
        print("  • Explore examples in the examples/ directory")
        print("  • Join the Bot Framework community")
        
        input("\nPress Enter to return to menu...")
        
    def show_examples(self):
        """Show code examples for common scenarios."""
        print("\n" + "="*70)
        print("💡 TEAMS AGENTS CODE EXAMPLES")
        print("="*70)
        
        examples = [
            {
                "title": "Basic Message Handler",
                "code": '''
async def on_message_activity(self, turn_context: TurnContext):
    text = turn_context.activity.text.strip().lower()
    
    if text == "hello":
        await turn_context.send_activity("👋 Hello! How can I help?")
    elif text == "help":
        await self.send_help(turn_context)
    else:
        await turn_context.send_activity(f"You said: {text}")
'''
            },
            {
                "title": "Send Adaptive Card",
                "code": '''
from botbuilder.schema import Attachment, Activity

async def send_task_card(self, turn_context: TurnContext, task_name: str):
    card = {
        "type": "AdaptiveCard",
        "version": "1.5",
        "body": [
            {
                "type": "TextBlock",
                "text": "New Task Created",
                "weight": "Bolder",
                "size": "Large"
            },
            {
                "type": "TextBlock",
                "text": f"Task: {task_name}"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "View Task",
                "data": {"action": "view", "taskName": task_name}
            }
        ]
    }
    
    attachment = Attachment(
        content_type="application/vnd.microsoft.card.adaptive",
        content=card
    )
    
    await turn_context.send_activity(Activity(attachments=[attachment]))
'''
            },
            {
                "title": "Handle Card Actions",
                "code": '''
async def on_teams_card_action_invoke(self, turn_context: TurnContext):
    action_data = turn_context.activity.value
    action = action_data.get("action")
    
    if action == "view":
        task_name = action_data.get("taskName")
        await turn_context.send_activity(f"Opening task: {task_name}")
    elif action == "delete":
        await turn_context.send_activity("Task deleted")
    
    return {"statusCode": 200}
'''
            },
            {
                "title": "Proactive Messaging",
                "code": '''
# Save conversation reference when user messages
async def on_message_activity(self, turn_context: TurnContext):
    conv_ref = TurnContext.get_conversation_reference(turn_context.activity)
    # Store conv_ref in your database for later use
    
# Send proactive message later
async def send_notification(self, conv_ref, message: str):
    async def callback(turn_context: TurnContext):
        await turn_context.send_activity(message)
    
    await self.adapter.continue_conversation(
        conv_ref,
        callback,
        self.app_id
    )
'''
            },
            {
                "title": "Access Microsoft Graph",
                "code": '''
from msgraph import GraphServiceClient
from azure.identity import ClientSecretCredential

async def get_user_info(self, user_id: str):
    credential = ClientSecretCredential(
        tenant_id=os.getenv("TENANT_ID"),
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET")
    )
    
    graph_client = GraphServiceClient(credentials=credential)
    user = await graph_client.users.by_user_id(user_id).get()
    
    return f"User: {user.display_name}, Email: {user.mail}"
'''
            },
            {
                "title": "Get Team Members",
                "code": '''
from botbuilder.core import TeamsInfo

async def list_team_members(self, turn_context: TurnContext):
    try:
        members = await TeamsInfo.get_team_members(turn_context)
        
        member_list = "Team Members:\\n"
        for member in members:
            member_list += f"• {member.name}\\n"
        
        await turn_context.send_activity(member_list)
    except Exception as e:
        await turn_context.send_activity("Error getting team members")
'''
            }
        ]
        
        for i, example in enumerate(examples, 1):
            print(f"\n{'='*70}")
            print(f"Example {i}: {example['title']}")
            print('='*70)
            print(example['code'])
            
            if i < len(examples):
                input("\nPress Enter for next example...")
        
        input("\n\nPress Enter to return to menu...")
        
    def show_tips(self):
        """Show best practices and tips."""
        print("\n" + "="*70)
        print("💡 TEAMS AGENTS TIPS & BEST PRACTICES")
        print("="*70)
        
        tips = [
            {
                "category": "🎯 Design Tips",
                "items": [
                    "Keep bot responses concise and actionable",
                    "Use Adaptive Cards for rich, interactive content",
                    "Provide clear help and command documentation",
                    "Handle 'help' and 'start' commands gracefully",
                    "Use typing indicators for operations taking >2 seconds"
                ]
            },
            {
                "category": "🔒 Security",
                "items": [
                    "Never hardcode credentials - use environment variables",
                    "Validate all user input before processing",
                    "Use Azure Key Vault for secrets in production",
                    "Implement proper authentication for sensitive operations",
                    "Follow principle of least privilege for permissions"
                ]
            },
            {
                "category": "⚡ Performance",
                "items": [
                    "Use async/await properly - don't block the event loop",
                    "Cache frequently accessed data",
                    "Implement retry logic for external API calls",
                    "Use connection pooling for database connections",
                    "Monitor bot performance with Application Insights"
                ]
            },
            {
                "category": "🐛 Error Handling",
                "items": [
                    "Always wrap bot logic in try-except blocks",
                    "Provide user-friendly error messages",
                    "Log errors with context for debugging",
                    "Implement graceful degradation",
                    "Test edge cases and error scenarios"
                ]
            },
            {
                "category": "📱 User Experience",
                "items": [
                    "Respond within 3 seconds or show typing indicator",
                    "Use emojis sparingly for better readability",
                    "Provide progress updates for long operations",
                    "Support both text commands and card actions",
                    "Make conversations feel natural, not robotic"
                ]
            },
            {
                "category": "🧪 Testing",
                "items": [
                    "Test locally with Bot Framework Emulator first",
                    "Test all features in actual Teams environment",
                    "Test on multiple devices (desktop, mobile, web)",
                    "Verify all card layouts render correctly",
                    "Test with different user permissions and roles"
                ]
            }
        ]
        
        for tip_group in tips:
            print(f"\n{tip_group['category']}\n")
            for item in tip_group['items']:
                print(f"  ✓ {item}")
        
        input("\n\nPress Enter to return to menu...")
    
    def interactive_mode(self):
        """Run in interactive mode for Teams agents."""
        print("Starting Teams Agent interactive mode...")
        print("Type 'back' to return to main menu\n")
        
        while True:
            print("\n" + "="*70)
            print("TEAMS AGENT ASSISTANT")
            print("="*70)
            print("\nMain Commands:")
            print("  1. Create new bot")
            print("  2. Add feature to bot")
            print("  3. Test bot locally")
            print("  4. View help and documentation")
            print("  5. Interactive tutorial")
            print("  6. Code examples")
            print("  7. Tips & best practices")
            print("  8. Back to main menu")
            
            choice = input("\nSelect option (1-8): ").strip()
            
            if choice == "1":
                self.create_new_bot()
            elif choice == "2":
                self.add_feature()
            elif choice == "3":
                self.test_bot()
            elif choice == "4":
                self.show_help()
            elif choice == "5":
                self.show_tutorial()
            elif choice == "6":
                self.show_examples()
            elif choice == "7":
                self.show_tips()
            elif choice == "8" or choice.lower() == "back":
                break
            else:
                print("Invalid option. Please try again.")
