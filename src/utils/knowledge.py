"""
Expert knowledge module for Microsoft 365 Agents Toolkit
Contains authoritative information about M365 agents, schemas, and best practices
"""

from typing import Dict, Any, List, Optional


class M365AgentsKnowledge:
    """Expert knowledge base for Microsoft 365 Agents Toolkit."""
    
    # Official schema URL for declarative agents
    DECLARATIVE_AGENT_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json"
    
    # Current supported version
    CURRENT_VERSION = "v1.0"
    
    # Official Teams manifest schema
    TEAMS_MANIFEST_SCHEMA = "https://developer.microsoft.com/json-schemas/teams/v1.17/MicrosoftTeams.schema.json"
    
    @staticmethod
    def get_declarative_agent_template() -> Dict[str, Any]:
        """Get the official declarative agent template.
        
        Returns:
            Complete template following Microsoft's schema
        """
        return {
            "$schema": M365AgentsKnowledge.DECLARATIVE_AGENT_SCHEMA_URL,
            "version": M365AgentsKnowledge.CURRENT_VERSION,
            "name": "",  # Max 100 characters
            "description": "",  # Max 1000 characters
            "instructions": "",  # Max 8000 characters, can use $[file('path.txt')]
            "conversation_starters": [],
            "capabilities": [],
            "actions": []
        }
    
    @staticmethod
    def get_capabilities_info() -> Dict[str, Dict[str, Any]]:
        """Get detailed information about available capabilities.
        
        Returns:
            Dictionary of capabilities with usage information
        """
        return {
            "WebSearch": {
                "description": "Enable web search capability for current information",
                "use_cases": [
                    "Current events and news",
                    "Real-time information",
                    "General knowledge queries",
                    "Research and fact-checking"
                ],
                "schema": {
                    "name": "WebSearch"
                },
                "requirements": []
            },
            "GraphConnectors": {
                "description": "Access data from Microsoft Graph connectors",
                "use_cases": [
                    "Enterprise search across custom data sources",
                    "Third-party data integration",
                    "Custom content indexing",
                    "Unified data access"
                ],
                "schema": {
                    "name": "GraphConnectors",
                    "connections": [
                        {
                            "connection_id": "your_connector_id"
                        }
                    ]
                },
                "requirements": ["Graph connector must be created and configured"]
            },
            "OneDriveAndSharePoint": {
                "description": "Search and access OneDrive and SharePoint content",
                "use_cases": [
                    "Document search and retrieval",
                    "Collaborative content access",
                    "File-based knowledge base",
                    "Project documentation"
                ],
                "schema": {
                    "name": "OneDriveAndSharePoint",
                    "items_by_url": [
                        {
                            "url": "https://contoso.sharepoint.com/sites/SiteName"
                        }
                    ]
                },
                "requirements": ["SharePoint site URL or OneDrive location"]
            },
            "MicrosoftGraph": {
                "description": "Direct Microsoft Graph API access",
                "use_cases": [
                    "User profile information",
                    "Email and calendar access",
                    "Teams data",
                    "Files and sites access"
                ],
                "schema": {
                    "name": "MicrosoftGraph",
                    "allowed_scopes": [
                        "User.Read",
                        "Mail.Read",
                        "Calendars.Read"
                    ]
                },
                "supported_scopes": [
                    "User.Read",
                    "User.ReadBasic.All",
                    "Mail.Read",
                    "Mail.ReadBasic",
                    "Calendars.Read",
                    "Calendars.ReadBasic",
                    "Files.Read.All",
                    "Sites.Read.All",
                    "Chat.Read",
                    "Team.ReadBasic.All"
                ],
                "requirements": ["Appropriate permissions must be granted"]
            }
        }
    
    @staticmethod
    def get_api_plugin_template() -> Dict[str, Any]:
        """Get the official API plugin template.
        
        Returns:
            Complete API plugin manifest template
        """
        return {
            "schema_version": "v2.1",
            "name_for_human": "",
            "description_for_human": "",
            "description_for_model": "",  # Critical for AI understanding
            "contact_email": "",
            "namespace": "",
            "capabilities": {
                "localization": {},
                "conversation_starters": []
            },
            "functions": [],
            "runtimes": [
                {
                    "type": "OpenApi",
                    "auth": {
                        "type": "None"  # or "OAuthPluginVault" or "ApiKeyPluginVault"
                    },
                    "spec": {
                        "url": ""  # URL to OpenAPI specification
                    },
                    "run_for_functions": []
                }
            ]
        }
    
    @staticmethod
    def get_conversation_starters_guidelines() -> Dict[str, Any]:
        """Get guidelines for creating effective conversation starters.
        
        Returns:
            Guidelines and best practices
        """
        return {
            "best_practices": [
                "Be specific and actionable",
                "Show concrete examples of agent capabilities",
                "Use natural language as users would ask",
                "Limit to 3-5 starters for clarity",
                "Mix simple and advanced queries",
                "Cover key features of the agent"
            ],
            "schema": {
                "title": "Short descriptive title (max 50 chars)",
                "text": "The actual prompt that will be sent to the agent"
            },
            "good_examples": [
                {
                    "title": "Search tickets",
                    "text": "Show me all open high-priority tickets assigned to me"
                },
                {
                    "title": "Create ticket",
                    "text": "I need to report a login issue with my account"
                }
            ],
            "bad_examples": [
                {
                    "title": "Help",
                    "text": "Help me",
                    "why_bad": "Too vague, doesn't demonstrate specific capability"
                },
                {
                    "title": "Start",
                    "text": "Get started",
                    "why_bad": "Generic, doesn't show what agent can do"
                }
            ]
        }
    
    @staticmethod
    def get_instructions_guidelines() -> Dict[str, str]:
        """Get guidelines for writing agent instructions.
        
        Returns:
            Guidelines for effective instructions
        """
        return {
            "purpose": "Instructions define the agent's persona, behavior, and response style",
            "max_length": "8000 characters",
            "external_file": "Can use $[file('instructions.txt')] to reference external file",
            "structure": """
## Recommended Structure:

1. **Role Definition**
   - Who is the agent
   - What domain/area it specializes in
   
2. **Core Capabilities**
   - List what the agent can do
   - Be specific about features
   
3. **Behavior Guidelines**
   - How to interact with users
   - Tone and style (professional, friendly, etc.)
   - When to ask clarifying questions
   
4. **Response Format**
   - How to structure answers
   - When to use lists, tables, etc.
   
5. **Action Triggers**
   - When to use specific API plugins
   - Parameter requirements
   - Error handling
   
6. **Examples**
   - Sample user queries and responses
   - Show expected behavior patterns
   
7. **Constraints**
   - What the agent should NOT do
   - Limitations to communicate
   - When to escalate to humans
            """,
            "example": """
You are a Customer Support Agent specialized in helping users with technical issues.

## Your Role
- Assist users with product inquiries and technical problems
- Create and manage support tickets
- Provide status updates on existing issues
- Escalate complex problems to human agents when needed

## Response Guidelines
- Be professional, empathetic, and solution-focused
- Ask clarifying questions when information is incomplete
- Provide step-by-step troubleshooting when appropriate
- Always confirm ticket creation and provide ticket numbers

## When to Use Actions
- Use getTicket when users ask about specific ticket numbers
- Use createTicket when users report new issues
- Use searchTickets when users want to see their ticket history
            """
        }
    
    @staticmethod
    def get_openapi_best_practices() -> List[str]:
        """Get best practices for OpenAPI specifications.
        
        Returns:
            List of best practices
        """
        return [
            "Use OpenAPI 3.0 or higher",
            "Provide detailed operation descriptions for the AI model",
            "Use clear, descriptive operationId values",
            "Include examples in schema definitions",
            "Define proper error responses (400, 401, 404, 500)",
            "Use security schemes (OAuth 2.0 recommended)",
            "Keep operations focused and single-purpose",
            "Use appropriate HTTP methods (GET for reads, POST for creates)",
            "Include parameter descriptions and constraints",
            "Version your API properly",
            "Use HTTPS endpoints only",
            "Implement proper pagination for list operations",
            "Return meaningful error messages",
            "Use standard HTTP status codes correctly"
        ]
    
    @staticmethod
    def get_authentication_types() -> Dict[str, Dict[str, Any]]:
        """Get information about supported authentication types.
        
        Returns:
            Dictionary of authentication methods
        """
        return {
            "None": {
                "description": "No authentication required (public APIs)",
                "schema": {
                    "type": "None"
                },
                "use_cases": ["Public APIs", "Testing", "Internal non-sensitive data"]
            },
            "OAuthPluginVault": {
                "description": "OAuth 2.0 authentication with credentials stored in Plugin Vault",
                "schema": {
                    "type": "OAuthPluginVault",
                    "reference_id": "unique_oauth_reference"
                },
                "use_cases": ["Production APIs", "User-delegated permissions", "Secure access"],
                "best_practice": "Recommended for production deployments"
            },
            "ApiKeyPluginVault": {
                "description": "API Key authentication with key stored in Plugin Vault",
                "schema": {
                    "type": "ApiKeyPluginVault",
                    "reference_id": "unique_apikey_reference"
                },
                "use_cases": ["Service-to-service", "Simple authentication", "Legacy APIs"]
            }
        }
    
    @staticmethod
    def validate_agent_manifest(manifest: Dict[str, Any]) -> tuple[bool, List[str]]:
        """Validate a declarative agent manifest.
        
        Args:
            manifest: The agent manifest to validate
            
        Returns:
            Tuple of (is_valid, list of errors/warnings)
        """
        errors = []
        warnings = []
        
        # Required fields
        required_fields = ["$schema", "version", "name", "description"]
        for field in required_fields:
            if field not in manifest:
                errors.append(f"Missing required field: {field}")
        
        # Validate schema URL
        if manifest.get("$schema") != M365AgentsKnowledge.DECLARATIVE_AGENT_SCHEMA_URL:
            errors.append(f"Invalid schema URL. Use: {M365AgentsKnowledge.DECLARATIVE_AGENT_SCHEMA_URL}")
        
        # Validate version
        if manifest.get("version") != M365AgentsKnowledge.CURRENT_VERSION:
            errors.append(f"Invalid version. Use: {M365AgentsKnowledge.CURRENT_VERSION}")
        
        # Validate field lengths
        if "name" in manifest and len(manifest["name"]) > 100:
            errors.append("Name exceeds 100 characters")
        
        if "description" in manifest and len(manifest["description"]) > 1000:
            errors.append("Description exceeds 1000 characters")
        
        if "instructions" in manifest:
            instructions = manifest["instructions"]
            if not instructions.startswith("$[file(") and len(instructions) > 8000:
                errors.append("Instructions exceed 8000 characters. Consider using external file.")
        
        # Warnings for best practices
        if "instructions" not in manifest and "capabilities" not in manifest:
            warnings.append("Agent has no instructions or capabilities defined")
        
        if "conversation_starters" not in manifest or len(manifest.get("conversation_starters", [])) == 0:
            warnings.append("No conversation starters defined. Consider adding 3-5 starters.")
        
        return len(errors) == 0, errors + warnings
    
    @staticmethod
    def get_deployment_checklist() -> List[Dict[str, Any]]:
        """Get deployment checklist for agents.
        
        Returns:
            List of deployment steps
        """
        return [
            {
                "step": "Validate Manifest",
                "items": [
                    "Schema URL is correct",
                    "All required fields present",
                    "Field length limits respected",
                    "Instructions are clear and complete"
                ]
            },
            {
                "step": "Test API Plugins",
                "items": [
                    "All endpoints are accessible",
                    "Authentication works correctly",
                    "OpenAPI spec is valid",
                    "Response formats are correct",
                    "Error handling is implemented"
                ]
            },
            {
                "step": "Prepare Icons",
                "items": [
                    "Color icon: 192x192 PNG",
                    "Outline icon: 32x32 PNG",
                    "Icons follow design guidelines"
                ]
            },
            {
                "step": "Create Package",
                "items": [
                    "All files in correct structure",
                    "ZIP file created",
                    "Package validated with Teams Toolkit"
                ]
            },
            {
                "step": "Test in Teams",
                "items": [
                    "Upload custom app",
                    "Test all conversation starters",
                    "Verify all capabilities work",
                    "Test error scenarios",
                    "Verify on mobile and desktop"
                ]
            },
            {
                "step": "Publish",
                "items": [
                    "Submit to Teams Admin Center or AppSource",
                    "Provide admin documentation",
                    "Include support information"
                ]
            }
        ]
    
    @staticmethod
    def get_common_patterns() -> Dict[str, Dict[str, Any]]:
        """Get common agent patterns and use cases.
        
        Returns:
            Dictionary of patterns with implementations
        """
        return {
            "data_retrieval": {
                "name": "Data Retrieval Agent",
                "description": "Search and retrieve information from enterprise systems",
                "components": [
                    "GraphConnectors for enterprise data",
                    "OneDriveAndSharePoint for documents",
                    "API plugins for external systems"
                ],
                "example_use_cases": [
                    "Knowledge base search",
                    "Document lookup",
                    "Policy information retrieval"
                ]
            },
            "task_automation": {
                "name": "Task Automation Agent",
                "description": "Create, update, and manage tasks or tickets",
                "components": [
                    "API plugins with CRUD operations",
                    "OAuth authentication",
                    "Adaptive Cards for rich responses"
                ],
                "example_use_cases": [
                    "IT helpdesk ticketing",
                    "Project task management",
                    "Workflow automation"
                ]
            },
            "notification": {
                "name": "Notification Agent",
                "description": "Monitor and alert on important events",
                "components": [
                    "API plugins for event sources",
                    "Proactive messaging",
                    "Graph connectors for preferences"
                ],
                "example_use_cases": [
                    "System monitoring alerts",
                    "Business metric notifications",
                    "Deadline reminders"
                ]
            },
            "analysis": {
                "name": "Analysis Agent",
                "description": "Analyze data and provide insights",
                "components": [
                    "Multiple data source connectors",
                    "API plugins for analytics services",
                    "Rich formatting for results"
                ],
                "example_use_cases": [
                    "Sales analytics",
                    "Performance reporting",
                    "Trend analysis"
                ]
            }
        }
