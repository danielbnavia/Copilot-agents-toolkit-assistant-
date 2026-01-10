"""Declarative Agents helper module"""

import json
from typing import Dict, Any, List, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.knowledge import M365AgentsKnowledge


class DeclarativeAgentHelper:
    """Helper class for creating and managing declarative agents with expert knowledge."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the declarative agent helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.knowledge = M365AgentsKnowledge()
        
    def create_agent(self, name: str, description: str, capabilities: List[str], 
                    instructions: Optional[str] = None) -> Dict[str, Any]:
        """Create a new declarative agent configuration using official schema.
        
        Args:
            name: Agent name (max 100 characters)
            description: Agent description (max 1000 characters)
            capabilities: List of capabilities
            instructions: Optional custom instructions
            
        Returns:
            Agent configuration dictionary following Microsoft schema
        """
        # Start with official template
        agent_config = self.knowledge.get_declarative_agent_template()
        
        # Set basic info
        agent_config["name"] = name[:100]  # Enforce limit
        agent_config["description"] = description[:1000]  # Enforce limit
        
        # Set instructions
        if instructions:
            agent_config["instructions"] = instructions[:8000]  # Enforce limit
        else:
            agent_config["instructions"] = f"You are {name}. {description}"
        
        # Build capabilities using expert knowledge
        agent_config["capabilities"] = self._build_capabilities(capabilities)
        
        return agent_config
        
    def _build_capabilities(self, capabilities: List[str]) -> List[Dict[str, Any]]:
        """Build capabilities configuration using expert knowledge.
        
        Args:
            capabilities: List of capability identifiers
            
        Returns:
            List of capability configurations following official schema
        """
        capability_configs = []
        capabilities_info = self.knowledge.get_capabilities_info()
        
        capability_map = {
            "web_search": "WebSearch",
            "answer_questions": "WebSearch",
            "graph_connectors": "GraphConnectors",
            "onedrive_sharepoint": "OneDriveAndSharePoint",
            "microsoft_graph": "MicrosoftGraph",
            "graph_api": "MicrosoftGraph"
        }
        
        for cap in capabilities:
            cap_name = capability_map.get(cap, cap)
            
            if cap_name in capabilities_info:
                # Use official schema from knowledge base
                capability_configs.append(capabilities_info[cap_name]["schema"].copy())
                
        return capability_configs
        
    def create_new_agent(self):
        """Interactive agent creation with expert guidance."""
        print("\n🤖 Create New Declarative Agent\n")
        print("Using official Microsoft 365 Agents Toolkit schema v1.0\n")
        
        name = input("Agent name (max 100 chars): ").strip()
        if len(name) > 100:
            print("⚠️  Name truncated to 100 characters")
            name = name[:100]
            
        description = input("Agent description (max 1000 chars): ").strip()
        if len(description) > 1000:
            print("⚠️  Description truncated to 1000 characters")
            description = description[:1000]
        
        # Show available capabilities from knowledge base
        print("\n📋 Available Capabilities (from Microsoft 365 Agents Toolkit):\n")
        capabilities_info = self.knowledge.get_capabilities_info()
        
        cap_options = {
            "1": ("web_search", "WebSearch - Enable web search for current information"),
            "2": ("graph_connectors", "GraphConnectors - Access custom data sources"),
            "3": ("onedrive_sharepoint", "OneDriveAndSharePoint - Search documents"),
            "4": ("microsoft_graph", "MicrosoftGraph - Access M365 data (users, mail, calendar)")
        }
        
        for key, (_, desc) in cap_options.items():
            print(f"  {key}. {desc}")
        
        cap_input = input("\nSelect capabilities (comma-separated, e.g., 1,4): ").strip()
        
        selected_capabilities = []
        for c in cap_input.split(","):
            c = c.strip()
            if c in cap_options:
                selected_capabilities.append(cap_options[c][0])
        
        # Offer to add custom instructions
        print("\n📝 Instructions define your agent's behavior (max 8000 chars)")
        print("   You can provide instructions now or press Enter to use default")
        
        custom_instructions = input("\nCustom instructions (or press Enter): ").strip()
        
        if not custom_instructions:
            # Show guidelines from knowledge base
            guidelines = self.knowledge.get_instructions_guidelines()
            custom_instructions = f"""You are {name}, an AI agent specialized in your domain.

{description}

## Your Capabilities
You have been configured with the following capabilities to assist users effectively.

## Response Guidelines
- Be helpful, accurate, and professional
- Ask clarifying questions when needed
- Provide specific, actionable information
- Cite sources when using web search or documents

## How to Help Users
Listen to user requests carefully and use your configured capabilities to provide the best possible assistance."""
        
        agent = self.create_agent(name, description, selected_capabilities, custom_instructions)
        
        # Validate using expert knowledge
        is_valid, messages = self.knowledge.validate_agent_manifest(agent)
        
        output_file = f"{name.lower().replace(' ', '-')}-agent.json"
        with open(output_file, 'w') as f:
            json.dump(agent, f, indent=2)
        
        print(f"\n✅ Agent configuration created: {output_file}")
        
        if not is_valid:
            print("\n⚠️  Validation warnings:")
            for msg in messages:
                print(f"   {msg}")
        
        print(f"\n📊 Agent Summary:")
        print(f"   Name: {agent['name']}")
        print(f"   Description: {agent['description'][:80]}...")
        print(f"   Capabilities: {len(agent.get('capabilities', []))}")
        print(f"   Schema: Official Microsoft v1.0")
        
        print(f"\n📚 Next Steps:")
        print(f"   1. Review and customize {output_file}")
        print(f"   2. Add conversation starters (recommended)")
        print(f"   3. Test with Teams Toolkit")
        print(f"   4. Deploy to Microsoft Teams")
        print(f"\n💡 Tip: Read docs/m365-agents-knowledge-base.md for complete guidance")
        
    def list_capabilities(self):
        """List available agent capabilities from expert knowledge base."""
        print("\n📋 Microsoft 365 Declarative Agent Capabilities\n")
        print("Based on official Microsoft 365 Agents Toolkit documentation:\n")
        
        capabilities_info = self.knowledge.get_capabilities_info()
        
        for cap_name, cap_info in capabilities_info.items():
            print(f"{'='*70}")
            print(f"📦 {cap_name}")
            print(f"{'='*70}")
            print(f"\n{cap_info['description']}\n")
            
            print("Use Cases:")
            for use_case in cap_info['use_cases']:
                print(f"  • {use_case}")
            
            print(f"\nConfiguration:")
            print(f"  {json.dumps(cap_info['schema'], indent=2)}")
            
            if cap_info['requirements']:
                print(f"\nRequirements:")
                for req in cap_info['requirements']:
                    print(f"  ⚠️  {req}")
            
            print()
        
        print(f"\n💡 For complete details, see: docs/m365-agents-knowledge-base.md")
        input("\nPress Enter to continue...")
            
    def validate_agent(self):
        """Validate an agent configuration file using expert knowledge."""
        print("\n✅ Validate Declarative Agent Configuration\n")
        print("Using official Microsoft 365 Agents Toolkit schema validation\n")
        
        file_path = input("Enter agent config file path: ").strip()
        
        try:
            with open(file_path, 'r') as f:
                config = json.load(f)
            
            # Use expert knowledge for validation
            is_valid, messages = self.knowledge.validate_agent_manifest(config)
            
            print(f"\n{'='*70}")
            print(f"VALIDATION RESULTS")
            print(f"{'='*70}\n")
            
            if is_valid:
                print("✅ Configuration is VALID!\n")
            else:
                print("❌ Configuration has issues:\n")
            
            # Show all messages
            for msg in messages:
                print(f"  {msg}")
            
            print(f"\n{'='*70}")
            print(f"AGENT SUMMARY")
            print(f"{'='*70}\n")
            print(f"  Name: {config.get('name', 'N/A')}")
            print(f"  Description: {config.get('description', 'N/A')[:80]}...")
            print(f"  Version: {config.get('version', 'N/A')}")
            print(f"  Schema: {config.get('$schema', 'N/A')}")
            
            if 'capabilities' in config:
                print(f"  Capabilities: {len(config['capabilities'])} configured")
                for cap in config['capabilities']:
                    print(f"    • {cap.get('name', 'Unknown')}")
            
            if 'conversation_starters' in config:
                print(f"  Conversation Starters: {len(config['conversation_starters'])}")
            
            if 'actions' in config:
                print(f"  Actions: {len(config['actions'])} API plugins")
            
            print(f"\n💡 See docs/m365-agents-knowledge-base.md for detailed specifications")
                    
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in file: {file_path}")
            print(f"   Error: {e}")
        
        input("\nPress Enter to continue...")
            
    def interactive_mode(self):
        """Run in interactive mode for declarative agents."""
        print("Starting Declarative Agent interactive mode...")
        print("Type 'back' to return to main menu\n")
        
        while True:
            print("\nDeclarative Agent Commands:")
            print("  1. Create new agent")
            print("  2. List capabilities")
            print("  3. Validate agent config")
            print("  4. Back to main menu")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == "1":
                self.create_new_agent()
            elif choice == "2":
                self.list_capabilities()
            elif choice == "3":
                self.validate_agent()
            elif choice == "4" or choice.lower() == "back":
                break
            else:
                print("Invalid option. Please try again.")
