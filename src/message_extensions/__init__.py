"""Message Extensions helper module"""

import json
import os
from typing import Dict, Any, List, Optional


class MessageExtensionHelper:
    """Helper class for creating and managing Message Extensions."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the message extension helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def create_search_extension(self, name: str, description: str) -> Dict[str, Any]:
        """Create a search-based message extension.
        
        Args:
            name: Extension name
            description: Extension description
            
        Returns:
            Message extension configuration
        """
        return {
            "botId": "${BOT_ID}",
            "commands": [
                {
                    "id": "searchCmd",
                    "type": "query",
                    "title": name,
                    "description": description,
                    "initialRun": False,
                    "parameters": [
                        {
                            "name": "searchQuery",
                            "title": "Search",
                            "description": "Enter search terms"
                        }
                    ]
                }
            ]
        }
    
    def interactive_mode(self):
        """Run in interactive mode for message extensions."""
        print("\n📬 Message Extensions Mode\n")
        print("Message extensions allow users to interact with external services")
        print("directly from Teams conversations.\n")
        
        print("Learn more in docs/all-scenarios.md - Message Extension Scenarios section")
