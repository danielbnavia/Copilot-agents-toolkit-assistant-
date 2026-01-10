"""API Plugins helper module"""

import json
from typing import Dict, Any, List, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.knowledge import M365AgentsKnowledge


class APIPluginHelper:
    """Helper class for creating and managing API Plugins."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the API plugin helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.knowledge = M365AgentsKnowledge()
        
    def create_plugin(self, name: str, description_human: str, 
                     description_model: str) -> Dict[str, Any]:
        """Create a new API plugin configuration.
        
        Args:
            name: Plugin name
            description_human: Human-readable description
            description_model: Description for AI model understanding
            
        Returns:
            API plugin configuration following official schema
        """
        return self.knowledge.get_api_plugin_template()
    
    def interactive_mode(self):
        """Run in interactive mode for API plugins."""
        print("\n🔌 API Plugins Mode\n")
        print("API plugins enable declarative agents to interact with external services")
        print("using OpenAPI specifications.\n")
        
        print("Key Concepts:")
        print("  • OpenAPI 3.0 specification required")
        print("  • description_for_model is critical for AI understanding")
        print("  • Supports OAuth 2.0 and API Key authentication")
        print("  • Response semantics guide data presentation\n")
        
        print("Common Plugin Types:")
        print("  1. CRUD Operations (Create, Read, Update, Delete)")
        print("  2. Search & Filter")
        print("  3. Notifications & Alerts")
        print("  4. File Management")
        print("  5. Scheduling & Calendar")
        print("  6. Analytics & Metrics\n")
        
        print("📚 Complete guide: docs/m365-agents-knowledge-base.md - API Plugins section")
        print("📚 All scenarios: docs/all-scenarios.md - API Plugin Scenarios section")
