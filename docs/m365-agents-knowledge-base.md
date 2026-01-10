# Microsoft 365 Agents Toolkit - Complete Knowledge Base

## Expert Guide to Microsoft 365 Declarative Agents and Copilot Extensions

## Table of Contents

1. [Overview](#overview)
2. [Declarative Agents Architecture](#declarative-agents-architecture)
3. [Agent Manifest Schema](#agent-manifest-schema)
4. [Capabilities and Plugins](#capabilities-and-plugins)
5. [API Plugins](#api-plugins)
6. [Connectors](#connectors)
7. [Actions and Skills](#actions-and-skills)
8. [Conversation Starters](#conversation-starters)
9. [Instructions and Grounding](#instructions-and-grounding)
10. [Authentication and Security](#authentication-and-security)
11. [Deployment and Publishing](#deployment-and-publishing)
12. [Best Practices](#best-practices)

---

## Overview

### What are Microsoft 365 Declarative Agents?

Declarative agents are AI-powered assistants that extend Microsoft Copilot capabilities through JSON-based configuration files. They enable:

- **Custom AI behavior** through instructions and grounding
- **Data integration** via API plugins and connectors
- **Action execution** through skills and capabilities
- **Enterprise integration** with Microsoft 365 and third-party services

### Key Components

1. **Agent Manifest** - JSON file defining the agent's configuration
2. **Instructions** - Custom prompts and behavior guidelines
3. **Capabilities** - Built-in features (Graph, search, code interpreter)
4. **API Plugins** - OpenAPI-based integrations
5. **Connectors** - Graph connector data sources
6. **Actions** - Executable skills and workflows

---

## Declarative Agents Architecture

### Agent Manifest Structure

The agent manifest follows this schema:

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  "version": "v1.0",
  "name": "Agent Name",
  "description": "Brief description of the agent",
  "instructions": "Detailed instructions for agent behavior",
  "conversation_starters": [],
  "capabilities": [],
  "actions": []
}
```

### Required Fields

- **$schema** - JSON schema URL (always use v1.0)
- **version** - Agent manifest version (v1.0)
- **name** - Display name (max 100 characters)
- **description** - Short description (max 1000 characters)

### Optional Fields

- **instructions** - Custom behavior instructions (max 8000 characters)
- **conversation_starters** - Suggested prompts for users
- **capabilities** - Built-in capabilities to enable
- **actions** - API plugins and connectors to integrate

---

## Agent Manifest Schema

### Complete Schema Example

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  "version": "v1.0",
  "name": "Customer Support Agent",
  "description": "AI agent specialized in customer support and ticket management",
  "instructions": "$[file('instructions.txt')]",
  "conversation_starters": [
    {
      "title": "Check ticket status",
      "text": "What's the status of ticket #12345?"
    },
    {
      "title": "Create new ticket",
      "text": "I need to report a technical issue"
    },
    {
      "title": "Get support metrics",
      "text": "Show me this month's support metrics"
    }
  ],
  "capabilities": [
    {
      "name": "WebSearch"
    },
    {
      "name": "GraphConnectors",
      "connections": [
        {
          "connection_id": "supportTicketsConnector"
        }
      ]
    }
  ],
  "actions": [
    {
      "id": "ticketingAPI",
      "file": "ticketing-api-plugin.json"
    }
  ]
}
```

### Name and Description Guidelines

**Name:**
- Max 100 characters
- Should be unique and descriptive
- Use title case
- Avoid special characters

**Description:**
- Max 1000 characters
- Clearly explain the agent's purpose
- Mention key capabilities
- Target user audience

---

## Capabilities and Plugins

### Built-in Capabilities

#### 1. WebSearch

Enables the agent to search the web for information.

```json
{
  "capabilities": [
    {
      "name": "WebSearch"
    }
  ]
}
```

**Use Cases:**
- Current events and news
- General knowledge queries
- Real-time information
- Research and fact-checking

#### 2. GraphConnectors

Access data from Microsoft Graph connectors.

```json
{
  "capabilities": [
    {
      "name": "GraphConnectors",
      "connections": [
        {
          "connection_id": "yourConnectorId"
        }
      ]
    }
  ]
}
```

**Use Cases:**
- Enterprise search across custom data
- Integration with third-party data sources
- Document and content search
- Unified data access

#### 3. OneDriveAndSharePoint

Search and access OneDrive and SharePoint content.

```json
{
  "capabilities": [
    {
      "name": "OneDriveAndSharePoint",
      "items_by_url": [
        {
          "url": "https://contoso.sharepoint.com/sites/ProjectX"
        }
      ],
      "items_by_id": [
        {
          "site_id": "site-id-here",
          "web_id": "web-id-here",
          "list_id": "list-id-here",
          "unique_id": "unique-id-here"
        }
      ]
    }
  ]
}
```

**Use Cases:**
- Document search and retrieval
- Collaborative content access
- File-based knowledge base
- Project document management

#### 4. MicrosoftGraph

Direct Microsoft Graph API access.

```json
{
  "capabilities": [
    {
      "name": "MicrosoftGraph",
      "allowed_scopes": [
        "User.Read",
        "Mail.Read",
        "Calendars.Read"
      ]
    }
  ]
}
```

**Supported Scopes:**
- `User.Read` - User profile information
- `Mail.Read` - Read user emails
- `Calendars.Read` - Read calendar events
- `Files.Read.All` - Read all files
- `Sites.Read.All` - Read SharePoint sites
- `Chat.Read` - Read Teams chats
- `Team.ReadBasic.All` - Read Teams information

---

## API Plugins

### OpenAPI Plugin Structure

API plugins use OpenAPI 3.0 specification to define REST APIs.

#### Plugin Manifest (JSON)

```json
{
  "schema_version": "v2.1",
  "name_for_human": "Ticketing System",
  "description_for_human": "Access and manage support tickets",
  "description_for_model": "This plugin allows the agent to search, create, update, and close support tickets. Use it when users ask about ticket status, want to create new tickets, or need to manage existing ones.",
  "contact_email": "support@company.com",
  "namespace": "ticketing",
  "capabilities": {
    "localization": {},
    "conversation_starters": [
      {
        "text": "Check my open tickets"
      }
    ]
  },
  "functions": [
    {
      "name": "getTicket",
      "description": "Retrieve details of a specific support ticket",
      "capabilities": {
        "response_semantics": {
          "data_path": "$.ticket",
          "properties": {
            "title": "$.title",
            "subtitle": "$.status",
            "url": "$.url"
          },
          "static_template": {
            "type": "AdaptiveCard",
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.5",
            "body": []
          }
        }
      },
      "states": {
        "reasoning": {
          "description": "Use this to get ticket information when user asks about ticket status"
        },
        "responding": {
          "description": "Present ticket details in a user-friendly format"
        }
      }
    }
  ],
  "runtimes": [
    {
      "type": "OpenApi",
      "auth": {
        "type": "OAuthPluginVault",
        "reference_id": "oauth_ticketing"
      },
      "spec": {
        "url": "https://api.company.com/openapi.json"
      },
      "run_for_functions": ["getTicket", "createTicket"]
    }
  ]
}
```

### OpenAPI Specification

```yaml
openapi: 3.0.0
info:
  title: Ticketing API
  version: 1.0.0
  description: API for managing support tickets

servers:
  - url: https://api.company.com/v1

paths:
  /tickets/{ticketId}:
    get:
      operationId: getTicket
      summary: Get ticket details
      description: Retrieve information about a specific support ticket
      parameters:
        - name: ticketId
          in: path
          required: true
          schema:
            type: string
          description: The unique ticket identifier
      responses:
        '200':
          description: Ticket details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Ticket'
        '404':
          description: Ticket not found

  /tickets:
    post:
      operationId: createTicket
      summary: Create new ticket
      description: Create a new support ticket
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - title
                - description
              properties:
                title:
                  type: string
                  description: Brief ticket title
                description:
                  type: string
                  description: Detailed description of the issue
                priority:
                  type: string
                  enum: [low, medium, high, critical]
                  description: Ticket priority level
      responses:
        '201':
          description: Ticket created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Ticket'

components:
  schemas:
    Ticket:
      type: object
      properties:
        id:
          type: string
          description: Unique ticket ID
        title:
          type: string
          description: Ticket title
        description:
          type: string
          description: Ticket description
        status:
          type: string
          enum: [open, in_progress, resolved, closed]
          description: Current ticket status
        priority:
          type: string
          enum: [low, medium, high, critical]
          description: Ticket priority
        created_at:
          type: string
          format: date-time
          description: Creation timestamp
        url:
          type: string
          format: uri
          description: URL to view ticket

  securitySchemes:
    oauth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.company.com/oauth/authorize
          tokenUrl: https://auth.company.com/oauth/token
          scopes:
            tickets:read: Read ticket information
            tickets:write: Create and update tickets

security:
  - oauth2: [tickets:read, tickets:write]
```

### Plugin Best Practices

1. **Description for Model** - Critical for agent understanding
   - Be specific about when to use the plugin
   - Mention key scenarios and use cases
   - Include parameter usage guidelines

2. **Operation IDs** - Must be unique and descriptive
   - Use camelCase or snake_case consistently
   - Make them self-explanatory

3. **Response Semantics** - Guide how agent presents data
   - Use data_path to extract relevant data
   - Map properties to user-friendly fields
   - Provide Adaptive Card templates for rich responses

4. **Authentication** - Secure your APIs properly
   - Use OAuth 2.0 for production
   - Store credentials in Plugin Vault
   - Request minimum required scopes

---

## Connectors

### Graph Connector Integration

Graph connectors enable agents to search enterprise data sources.

#### Creating a Graph Connector

1. **Define the connection:**
```json
{
  "id": "customDataConnector",
  "name": "Company Knowledge Base",
  "description": "Internal documentation and knowledge articles"
}
```

2. **Configure in agent manifest:**
```json
{
  "capabilities": [
    {
      "name": "GraphConnectors",
      "connections": [
        {
          "connection_id": "customDataConnector"
        }
      ]
    }
  ]
}
```

#### Connector Schema Example

```csharp
var schema = new Schema
{
    BaseType = "microsoft.graph.externalItem",
    Properties = new List<Property>
    {
        new Property
        {
            Name = "title",
            Type = PropertyType.String,
            IsQueryable = true,
            IsSearchable = true,
            IsRetrievable = true,
            Labels = new List<Label> { Label.Title }
        },
        new Property
        {
            Name = "content",
            Type = PropertyType.String,
            IsSearchable = true,
            IsRetrievable = true
        },
        new Property
        {
            Name = "category",
            Type = PropertyType.String,
            IsQueryable = true,
            IsRefinable = true,
            IsRetrievable = true
        },
        new Property
        {
            Name = "lastModified",
            Type = PropertyType.DateTime,
            IsQueryable = true,
            IsRetrievable = true,
            Labels = new List<Label> { Label.LastModifiedDateTime }
        }
    }
};
```

---

## Actions and Skills

### Defining Actions

Actions in the manifest reference plugin files:

```json
{
  "actions": [
    {
      "id": "ticketingAPI",
      "file": "plugins/ticketing-plugin.json"
    },
    {
      "id": "weatherAPI",
      "file": "plugins/weather-plugin.json"
    }
  ]
}
```

### Action States

Plugins support reasoning and responding states:

```json
{
  "states": {
    "reasoning": {
      "description": "Determine if this action is needed based on user intent"
    },
    "responding": {
      "description": "Format and present the action results to user"
    }
  }
}
```

---

## Conversation Starters

### Best Practices

Conversation starters guide users on what the agent can do:

```json
{
  "conversation_starters": [
    {
      "title": "Short descriptive title",
      "text": "The actual prompt text that will be sent"
    }
  ]
}
```

### Guidelines

1. **Be Specific** - Show concrete examples of what agent can do
2. **Cover Key Features** - Include starters for main capabilities
3. **Use Natural Language** - Write as users would ask
4. **Limit Count** - 3-5 starters is optimal
5. **Vary Complexity** - Mix simple and advanced queries

### Examples

**Good:**
```json
[
  {
    "title": "Search tickets",
    "text": "Show me all open high-priority tickets"
  },
  {
    "title": "Create ticket",
    "text": "I need to report a login issue"
  },
  {
    "title": "Get metrics",
    "text": "What's our average ticket resolution time this month?"
  }
]
```

**Avoid:**
```json
[
  {
    "title": "Help",
    "text": "Help me"
  },
  {
    "title": "Start",
    "text": "Get started"
  }
]
```

---

## Instructions and Grounding

### Writing Effective Instructions

Instructions define the agent's persona, behavior, and response style:

```text
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
- Never make promises about resolution times

## When to Use Actions
- Use getTicket when users ask about specific ticket numbers
- Use createTicket when users report new issues
- Use searchTickets when users want to see their ticket history
- Use escalateTicket for issues beyond your capability

## Examples
User: "My login isn't working"
You: "I'm sorry you're experiencing login issues. Let me help you troubleshoot. First, can you tell me:
1. What error message do you see?
2. When did this start happening?
3. Have you recently changed your password?"

User: "What's the status of ticket #12345?"
You: [Call getTicket with ticket_id: "12345"]
```

### Instruction Components

1. **Persona Definition** - Who is the agent
2. **Capabilities** - What it can do
3. **Behavior Guidelines** - How it should act
4. **Response Format** - How to structure answers
5. **Action Triggers** - When to use plugins/actions
6. **Examples** - Sample interactions
7. **Constraints** - What not to do

### External Instructions File

For better maintainability, use external file:

**declarativeAgent.json:**
```json
{
  "instructions": "$[file('instructions.txt')]"
}
```

**instructions.txt:**
```
[Your detailed instructions here]
```

---

## Authentication and Security

### OAuth 2.0 Authentication

For API plugins requiring authentication:

```json
{
  "runtimes": [
    {
      "type": "OpenApi",
      "auth": {
        "type": "OAuthPluginVault",
        "reference_id": "oauth_myapi"
      },
      "spec": {
        "url": "https://api.example.com/openapi.json"
      }
    }
  ]
}
```

### API Key Authentication

```json
{
  "runtimes": [
    {
      "type": "OpenApi",
      "auth": {
        "type": "ApiKeyPluginVault",
        "reference_id": "apikey_myapi"
      },
      "spec": {
        "url": "https://api.example.com/openapi.json"
      }
    }
  ]
}
```

### Security Best Practices

1. **Principle of Least Privilege** - Request minimum scopes
2. **Secure Credential Storage** - Use Plugin Vault
3. **HTTPS Only** - All API endpoints must use HTTPS
4. **Token Expiration** - Implement proper token refresh
5. **Input Validation** - Validate all user inputs
6. **Error Handling** - Don't expose sensitive information in errors

---

## Deployment and Publishing

### Package Structure

```
MyDeclarativeAgent/
├── declarativeAgent.json          # Main manifest
├── instructions.txt               # Agent instructions
├── plugins/
│   ├── ticketing-plugin.json     # API plugin manifest
│   └── weather-plugin.json
├── openapi/
│   ├── ticketing-api.yaml        # OpenAPI spec
│   └── weather-api.yaml
├── icons/
│   ├── color.png                 # 192x192 color icon
│   └── outline.png               # 32x32 outline icon
└── README.md
```

### Teams App Package

Create a Teams app package (ZIP file):

```
myagent.zip
├── manifest.json                  # Teams app manifest
├── declarativeAgent.json
├── instructions.txt
├── plugins/
├── color.png
└── outline.png
```

### Teams Manifest Integration

**manifest.json:**
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.17/MicrosoftTeams.schema.json",
  "manifestVersion": "1.17",
  "version": "1.0.0",
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "packageName": "com.company.customeragent",
  "developer": {
    "name": "Company Name",
    "websiteUrl": "https://company.com",
    "privacyUrl": "https://company.com/privacy",
    "termsOfUseUrl": "https://company.com/terms"
  },
  "name": {
    "short": "Customer Agent",
    "full": "Customer Support Declarative Agent"
  },
  "description": {
    "short": "AI agent for customer support",
    "full": "Declarative agent specialized in customer support, ticket management, and technical assistance"
  },
  "icons": {
    "color": "color.png",
    "outline": "outline.png"
  },
  "accentColor": "#FFFFFF",
  "copilotAgents": {
    "declarativeAgents": [
      {
        "id": "customerAgent",
        "file": "declarativeAgent.json"
      }
    ]
  }
}
```

### Publishing Steps

1. **Package Creation**
   - Create ZIP with all required files
   - Validate manifest with Teams Toolkit
   - Test locally

2. **Testing**
   - Upload to Teams (Upload a custom app)
   - Test all capabilities and plugins
   - Verify authentication flows

3. **Submission**
   - Submit to Teams Admin Center (for organization)
   - Or submit to AppSource (for public distribution)

---

## Best Practices

### 1. Agent Design

- **Single Purpose** - Keep agents focused on specific domains
- **Clear Instructions** - Be explicit about capabilities and limitations
- **Good Examples** - Provide conversation starters that showcase features
- **Graceful Degradation** - Handle missing data or failed API calls well

### 2. API Plugin Design

- **Descriptive Names** - Use clear operation IDs and parameter names
- **Rich Descriptions** - Help the model understand when to use each operation
- **Error Handling** - Return meaningful error messages
- **Response Semantics** - Guide how to present data to users

### 3. Performance

- **API Response Time** - Keep under 3 seconds when possible
- **Pagination** - Implement for large result sets
- **Caching** - Cache frequently accessed data
- **Timeouts** - Set appropriate timeouts

### 4. User Experience

- **Context Awareness** - Remember conversation context
- **Confirmation** - Confirm before executing destructive actions
- **Progress Indicators** - Inform users during long operations
- **Helpful Errors** - Provide actionable error messages

### 5. Testing

- **Unit Tests** - Test individual plugin operations
- **Integration Tests** - Test end-to-end workflows
- **User Testing** - Get real user feedback
- **Edge Cases** - Test error conditions and unusual inputs

---

## Common Patterns and Examples

### Pattern: Data Retrieval Agent

**Use Case:** Search and retrieve information from enterprise systems

**Key Components:**
- Graph connector for enterprise data
- API plugin for external systems
- OneDriveAndSharePoint for documents

### Pattern: Task Automation Agent

**Use Case:** Create, update, and manage tasks/tickets

**Key Components:**
- API plugins with CRUD operations
- Adaptive Cards for rich responses
- OAuth authentication

### Pattern: Notification Agent

**Use Case:** Monitor and alert on important events

**Key Components:**
- API plugins for event sources
- Proactive messaging capability
- Graph connector for user preferences

### Pattern: Analysis Agent

**Use Case:** Analyze data and provide insights

**Key Components:**
- Multiple data source connectors
- API plugins for analytics services
- Rich formatting for results presentation

---

This knowledge base provides the complete, expert-level information needed to build production-quality Microsoft 365 declarative agents and Copilot extensions.
