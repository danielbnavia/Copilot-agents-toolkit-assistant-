"""
Core assistant functionality for M365 Agent Toolkit
"""

import json
import os
from typing import Optional, Dict, Any, List
from .config import AssistantConfig


class M365Assistant:
    """Main assistant class for Microsoft 365 Agent Toolkit."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the M365 Assistant.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.config = AssistantConfig()
        self.current_project = None
        
    def display_welcome(self):
        """Display welcome message and available options."""
        welcome_message = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║    Microsoft 365 Agent Toolkit Assistant                            ║
║    Your AI-powered guide to building M365 agents and apps           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

Welcome! I'm here to help you build with Microsoft 365 Agent Toolkit.

I can assist you with:
  🤖 Declarative Agents - AI-powered agents with declarative configs
  👥 Teams Agents - Custom bots and agents for Microsoft Teams
  🎨 Adaptive Cards - Rich, interactive cards for M365 apps
  🔄 Workflows - Automated business processes
  📱 Apps - Full Microsoft 365 applications
  📬 Message Extensions - Search and actions in Teams conversations
  🔌 API Plugins - OpenAPI-based service integrations
  🔗 Graph Connectors - Index external data sources
  🎨 Copilot Studio - Low-code agent building (NEW 2025)
  ⚡ Power Platform - Power Automate, Dataverse integration (NEW 2025)
  ☁️  Azure AI - OpenAI GPT-4/GPT-5, AI Search, RAG (NEW 2025)
  🏪 Template Manager - Agent Store browser and template importer (CLI)
  🧪 Test Framework - Automated testing with scenarios (CLI)
  🔧 CI/CD Helper - Generate pipeline configurations (CLI)

Type 'help' for available commands or 'exit' to quit.
        """
        print(welcome_message)
        
    def run_interactive(self):
        """Run the assistant in interactive mode."""
        print("\n🚀 Starting interactive mode...\n")
        
        while True:
            try:
                user_input = input("M365 Assistant> ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Goodbye! Happy building!")
                    break
                    
                if user_input.lower() == 'help':
                    self.display_help()
                    continue
                    
                # Process the command
                self.process_command(user_input)
                
            except EOFError:
                break
                
    def display_help(self):
        """Display help information."""
        help_text = """
Available Commands:
  
  Project Management:
    create <name>           - Create a new project
    list templates          - List available templates
    open <project>          - Open an existing project
    
  Declarative Agents:
    agent new               - Create a new declarative agent
    agent list              - List agent capabilities
    agent validate          - Validate agent configuration
    
  Teams Agents:
    bot new                 - Create a new Teams bot
    bot add-feature         - Add feature to Teams bot
    bot test                - Test bot locally
    
  Adaptive Cards:
    card new                - Create a new adaptive card
    card templates          - List card templates
    card preview            - Preview card design
    
  Workflows:
    workflow new            - Create a new workflow
    workflow add-action     - Add action to workflow
    workflow test           - Test workflow
    
  General:
    help                    - Show this help message
    status                  - Show current project status
    exit                    - Exit the assistant
        """
        print(help_text)
        
    def process_command(self, command: str):
        """Process a user command.
        
        Args:
            command: The command to process
        """
        parts = command.split()
        
        if not parts:
            return
            
        cmd = parts[0].lower()
        
        if cmd == "create" and len(parts) > 1:
            project_name = parts[1]
            self.create_project(project_name)
        elif cmd == "list" and len(parts) > 1 and parts[1] == "templates":
            self.list_templates()
        elif cmd == "agent":
            self.handle_agent_command(parts[1:] if len(parts) > 1 else [])
        elif cmd == "bot":
            self.handle_bot_command(parts[1:] if len(parts) > 1 else [])
        elif cmd == "card":
            self.handle_card_command(parts[1:] if len(parts) > 1 else [])
        elif cmd == "workflow":
            self.handle_workflow_command(parts[1:] if len(parts) > 1 else [])
        elif cmd == "status":
            self.show_status()
        else:
            print(f"Unknown command: {cmd}. Type 'help' for available commands.")
            
    def create_project(self, name: str, template: Optional[str] = None, mode: Optional[str] = None):
        """Create a new project.
        
        Args:
            name: Project name
            template: Template to use
            mode: Project mode/type
        """
        print(f"\n✨ Creating project '{name}'...")
        
        # Determine template based on mode or explicit template
        if template:
            selected_template = template
        elif mode:
            template_map = {
                "declarative-agent": "basic-declarative-agent",
                "teams-agent": "basic-teams-bot",
                "adaptive-cards": "adaptive-cards-showcase",
                "workflows": "basic-workflow"
            }
            selected_template = template_map.get(mode, "basic-project")
        else:
            selected_template = "basic-project"
            
        # Create project directory
        project_path = os.path.join(os.getcwd(), name)
        
        if os.path.exists(project_path):
            print(f"❌ Error: Project directory '{name}' already exists.")
            return
            
        os.makedirs(project_path)
        self.current_project = name
        
        print(f"✅ Project '{name}' created successfully!")
        print(f"📁 Location: {project_path}")
        print(f"📋 Template: {selected_template}")
        print(f"\nNext steps:")
        print(f"  1. cd {name}")
        print(f"  2. Follow the README.md for setup instructions")
        
    def list_templates(self):
        """List available project templates."""
        print("\n📋 Available Templates:\n")
        
        templates = [
            {
                "name": "basic-declarative-agent",
                "description": "Basic declarative agent with AI capabilities",
                "category": "Declarative Agents"
            },
            {
                "name": "basic-teams-bot",
                "description": "Simple Teams bot with messaging",
                "category": "Teams Agents"
            },
            {
                "name": "adaptive-cards-showcase",
                "description": "Collection of adaptive card examples",
                "category": "Adaptive Cards"
            },
            {
                "name": "basic-workflow",
                "description": "Basic workflow automation template",
                "category": "Workflows"
            },
            {
                "name": "full-teams-app",
                "description": "Complete Teams app with tabs, bots, and cards",
                "category": "Apps"
            }
        ]
        
        for template in templates:
            print(f"  • {template['name']}")
            print(f"    Category: {template['category']}")
            print(f"    {template['description']}\n")
            
    def handle_agent_command(self, args: List[str]):
        """Handle declarative agent commands."""
        from ..declarative_agents import DeclarativeAgentHelper
        
        helper = DeclarativeAgentHelper(verbose=self.verbose)
        
        if not args:
            print("Usage: agent <new|list|validate>")
            return
            
        if args[0] == "new":
            helper.create_new_agent()
        elif args[0] == "list":
            helper.list_capabilities()
        elif args[0] == "validate":
            helper.validate_agent()
            
    def handle_bot_command(self, args: List[str]):
        """Handle Teams bot commands."""
        from ..teams_agents import TeamsAgentHelper
        
        helper = TeamsAgentHelper(verbose=self.verbose)
        
        if not args:
            print("Usage: bot <new|add-feature|test>")
            return
            
        if args[0] == "new":
            helper.create_new_bot()
        elif args[0] == "add-feature":
            helper.add_feature()
        elif args[0] == "test":
            helper.test_bot()
            
    def handle_card_command(self, args: List[str]):
        """Handle adaptive card commands."""
        from ..adaptive_cards import AdaptiveCardHelper
        
        helper = AdaptiveCardHelper(verbose=self.verbose)
        
        if not args:
            print("Usage: card <new|templates|preview>")
            return
            
        if args[0] == "new":
            helper.create_new_card()
        elif args[0] == "templates":
            helper.list_templates()
        elif args[0] == "preview":
            helper.preview_card()
            
    def handle_workflow_command(self, args: List[str]):
        """Handle workflow commands."""
        from ..workflows import WorkflowHelper
        
        helper = WorkflowHelper(verbose=self.verbose)
        
        if not args:
            print("Usage: workflow <new|add-action|test>")
            return
            
        if args[0] == "new":
            helper.create_new_workflow()
        elif args[0] == "add-action":
            helper.add_action()
        elif args[0] == "test":
            helper.test_workflow()
            
    def show_status(self):
        """Show current project status."""
        print("\n📊 Current Status:\n")
        
        if self.current_project:
            print(f"  Project: {self.current_project}")
        else:
            print("  No project currently open")
            
        print(f"  Verbose mode: {'Enabled' if self.verbose else 'Disabled'}")
        
    def run_declarative_agent_mode(self):
        """Run in declarative agent mode."""
        print("\n🤖 Declarative Agent Mode\n")
        from ..declarative_agents import DeclarativeAgentHelper
        
        helper = DeclarativeAgentHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_teams_agent_mode(self):
        """Run in Teams agent mode."""
        print("\n👥 Teams Agent Mode\n")
        from ..teams_agents import TeamsAgentHelper
        
        helper = TeamsAgentHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_adaptive_cards_mode(self):
        """Run in adaptive cards mode."""
        print("\n🎨 Adaptive Cards Mode\n")
        from ..adaptive_cards import AdaptiveCardHelper
        
        helper = AdaptiveCardHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_workflows_mode(self):
        """Run in workflows mode."""
        print("\n🔄 Workflows Mode\n")
        from ..workflows import WorkflowHelper
        
        helper = WorkflowHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_message_extensions_mode(self):
        """Run in message extensions mode."""
        print("\n📬 Message Extensions Mode\n")
        from ..message_extensions import MessageExtensionHelper
        
        helper = MessageExtensionHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_api_plugins_mode(self):
        """Run in API plugins mode."""
        print("\n🔌 API Plugins Mode\n")
        from ..api_plugins import APIPluginHelper
        
        helper = APIPluginHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_graph_connectors_mode(self):
        """Run in Graph connectors mode."""
        print("\n🔗 Graph Connectors Mode\n")
        from ..graph_connectors import GraphConnectorHelper
        
        helper = GraphConnectorHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_copilot_studio_mode(self):
        """Run in Copilot Studio mode."""
        print("\n🎨 Copilot Studio Integration Mode\n")
        from ..copilot_studio import CopilotStudioHelper
        
        helper = CopilotStudioHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_power_platform_mode(self):
        """Run in Power Platform mode."""
        print("\n⚡ Power Platform Integration Mode\n")
        from ..power_platform import PowerPlatformHelper
        
        helper = PowerPlatformHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_azure_integration_mode(self):
        """Run in Azure AI Services mode."""
        print("\n☁️  Azure AI Services Integration Mode\n")
        from ..azure_integration import AzureIntegrationHelper
        
        helper = AzureIntegrationHelper(verbose=self.verbose)
        helper.interactive_mode()
        
    def run_template_manager_mode(self):
        """Run in Template Manager mode."""
        print("\n🏪 Template Manager Mode\n")
        from ..cli_tools import TemplateManager
        
        manager = TemplateManager(verbose=self.verbose)
        manager.interactive_mode()
        
    def run_test_framework_mode(self):
        """Run in Test Framework mode."""
        print("\n🧪 Test Framework Mode\n")
        from ..cli_tools import TestFramework
        
        framework = TestFramework(verbose=self.verbose)
        framework.interactive_mode()
        
    def run_cicd_helper_mode(self):
        """Run in CI/CD Helper mode."""
        print("\n🔧 CI/CD Helper Mode\n")
        from ..cli_tools import CICDHelper
        
        helper = CICDHelper(verbose=self.verbose)
        helper.interactive_mode()
