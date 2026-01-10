#!/usr/bin/env python3
"""
Microsoft 365 Agent Toolkit Assistant
Main entry point for the interactive AI assistant
"""

import argparse
import sys
from src.core.assistant import M365Assistant


def main():
    """Main entry point for the M365 Agent Toolkit Assistant."""
    parser = argparse.ArgumentParser(
        description="Microsoft 365 Agent Toolkit Assistant - Your guide to building M365 agents, apps, and workflows"
    )
    
    parser.add_argument(
        "--mode",
        choices=["interactive", "declarative-agent", "teams-agent", "adaptive-cards", 
                 "workflows", "message-extensions", "api-plugins", "graph-connectors",
                 "copilot-studio", "power-platform", "azure-integration",
                 "template-manager", "test-framework", "cicd-helper"],
        default="interactive",
        help="Specify the mode of operation"
    )
    
    parser.add_argument(
        "--create",
        type=str,
        help="Create a new project (provide project name)"
    )
    
    parser.add_argument(
        "--template",
        type=str,
        help="Specify a template to use (e.g., 'basic-bot', 'declarative-agent', 'approval-workflow')"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Initialize the assistant
    assistant = M365Assistant(verbose=args.verbose)
    
    # Display welcome message
    assistant.display_welcome()
    
    # Handle project creation
    if args.create:
        assistant.create_project(args.create, args.template, args.mode)
        return 0
    
    # Run in specified mode
    if args.mode == "interactive":
        assistant.run_interactive()
    elif args.mode == "declarative-agent":
        assistant.run_declarative_agent_mode()
    elif args.mode == "teams-agent":
        assistant.run_teams_agent_mode()
    elif args.mode == "adaptive-cards":
        assistant.run_adaptive_cards_mode()
    elif args.mode == "workflows":
        assistant.run_workflows_mode()
    elif args.mode == "message-extensions":
        assistant.run_message_extensions_mode()
    elif args.mode == "api-plugins":
        assistant.run_api_plugins_mode()
    elif args.mode == "graph-connectors":
        assistant.run_graph_connectors_mode()
    elif args.mode == "copilot-studio":
        assistant.run_copilot_studio_mode()
    elif args.mode == "power-platform":
        assistant.run_power_platform_mode()
    elif args.mode == "azure-integration":
        assistant.run_azure_integration_mode()
    elif args.mode == "template-manager":
        assistant.run_template_manager_mode()
    elif args.mode == "test-framework":
        assistant.run_test_framework_mode()
    elif args.mode == "cicd-helper":
        assistant.run_cicd_helper_mode()
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nAssistant interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)
