"""Graph Connectors helper module"""

import json
from typing import Dict, Any, List, Optional


class GraphConnectorHelper:
    """Helper class for creating and managing Graph Connectors."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the Graph connector helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def create_connector_schema(self, name: str, properties: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create a Graph connector schema.
        
        Args:
            name: Connector name
            properties: List of property definitions
            
        Returns:
            Connector schema configuration
        """
        return {
            "baseType": "microsoft.graph.externalItem",
            "properties": properties
        }
    
    def interactive_mode(self):
        """Run in interactive mode for Graph connectors."""
        print("\n🔗 Graph Connectors Mode\n")
        print("Graph connectors enable indexing external data sources for")
        print("Microsoft Search and declarative agents.\n")
        
        print("Connector Types:")
        print("  1. Custom Data Source Connectors")
        print("  2. File Share Connectors")
        print("  3. Web Content Connectors")
        print("  4. API-based Connectors\n")
        
        print("Key Capabilities:")
        print("  • Full-text search across custom data")
        print("  • ACL (Access Control List) support")
        print("  • Incremental updates")
        print("  • Rich metadata")
        print("  • Custom schemas\n")
        
        print("📚 Complete guide: docs/all-scenarios.md - Connector Scenarios section")
        print("📚 Microsoft Docs: https://learn.microsoft.com/graph/connecting-external-content-connectors-overview")
