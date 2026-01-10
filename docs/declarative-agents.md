# Declarative Agents Complete Guide

## Introduction

Declarative agents are the foundation of Microsoft 365 Copilot extensibility. This guide provides complete information on building production-ready declarative agents.

## What are Declarative Agents?

Declarative agents extend Microsoft Copilot through JSON-based configuration files. Unlike traditional bots that require extensive code, declarative agents are configured through:

- **JSON manifest** - Defines capabilities and behavior
- **Instructions** - Natural language description of agent's role
- **API Plugins** - OpenAPI-based service integrations
- **Capabilities** - Built-in features like search and Graph access

## Official Schema

Always use the official Microsoft schema:

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  "version": "v1.0"
}
```

## Complete Manifest Structure

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  "version": "v1.0",
  "name": "Agent Name",
  "description": "Description up to 1000 characters",
  "instructions": "Detailed instructions or $[file('path.txt')]",
  "conversation_starters": [
    {
      "title": "Starter title",
      "text": "Example query"
    }
  ],
  "capabilities": [
    {
      "name": "CapabilityName",
      "...": "capability-specific config"
    }
  ],
  "actions": [
    {
      "id": "actionId",
      "file": "plugin.json"
    }
  ]
}
```

## Field Reference

### Required Fields

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| $schema | string | - | Must be official schema URL |
| version | string | - | Must be "v1.0" |
| name | string | 100 | Agent display name |
| description | string | 1000 | Brief description |

### Optional Fields

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| instructions | string | 8000 | Agent behavior instructions |
| conversation_starters | array | - | Suggested prompts |
| capabilities | array | - | Built-in capabilities |
| actions | array | - | API plugins |

## Capabilities Reference

### WebSearch

**Purpose:** Enable web search for current information

**Configuration:**
```json
{
  "name": "WebSearch"
}
```

**Use When:**
- Need current events/news
- Real-time information required
- General knowledge queries
- Research and fact-checking

**Limitations:**
- May not have access to paid/subscription content
- Results depend on search engine availability

### MicrosoftGraph

**Purpose:** Access Microsoft 365 data

**Configuration:**
```json
{
  "name": "MicrosoftGraph",
  "allowed_scopes": [
    "User.Read",
    "Mail.Read",
    "Calendars.Read"
  ]
}
```

**Supported Scopes:**
- `User.Read` - Basic user profile
- `User.ReadBasic.All` - Basic info for all users
- `Mail.Read` - Read user's email
- `Mail.ReadBasic` - Basic email properties
- `Calendars.Read` - Read calendar events
- `Calendars.ReadBasic` - Basic calendar info
- `Files.Read.All` - Read all files user can access
- `Sites.Read.All` - Read SharePoint sites
- `Chat.Read` - Read Teams chats
- `Team.ReadBasic.All` - Basic Teams info

**Best Practices:**
- Request minimum required scopes
- Document why each scope is needed
- Test with different permission levels

### OneDriveAndSharePoint

**Purpose:** Search documents and content

**Configuration:**
```json
{
  "name": "OneDriveAndSharePoint",
  "items_by_url": [
    {
      "url": "https://contoso.sharepoint.com/sites/SiteName"
    }
  ],
  "items_by_id": [
    {
      "site_id": "site-id",
      "web_id": "web-id",
      "list_id": "list-id",
      "unique_id": "item-id"
    }
  ]
}
```

**Use When:**
- Need to search documents
- Access knowledge base content
- Find project documentation
- Reference collaborative content

**Tips:**
- Limit to relevant sites for better results
- Ensure users have appropriate permissions
- Keep indexed content current

### GraphConnectors

**Purpose:** Access custom data sources

**Configuration:**
```json
{
  "name": "GraphConnectors",
  "connections": [
    {
      "connection_id": "your_connector_id"
    }
  ]
}
```

**Prerequisites:**
- Graph connector must be created
- Data must be indexed
- Connection ID must be valid

**Use When:**
- Integrating third-party data
- Custom enterprise data sources
- Legacy system integration
- Specialized content repositories

## Writing Effective Instructions

Instructions are critical for agent behavior. Follow this structure:

### 1. Role Definition
```
You are [Agent Name], an AI agent specialized in [domain].
```

### 2. Core Responsibilities
```
## Your Role
- [Primary task 1]
- [Primary task 2]
- [Primary task 3]
```

### 3. Capabilities Explanation
```
## Your Capabilities
You have access to:
- [Capability 1]: Use this to [purpose]
- [Capability 2]: Use this to [purpose]
```

### 4. Response Guidelines
```
## How to Respond
- Be [tone/style]
- Always [specific behavior]
- Never [prohibited action]
- When [condition], do [action]
```

### 5. Action Triggers
```
## When to Use Actions
- Use [action] when user asks about [scenario]
- Use [action] when you need to [purpose]
- Call [action] with [parameters] for [result]
```

### 6. Examples
```
## Examples

User: "[Example query]"
You: "[Expected response with reasoning]"

User: "[Complex query]"
You: [Call appropriate action]
[Present results clearly]
```

### 7. Constraints
```
## Limitations
- Cannot [limitation 1]
- Should not [limitation 2]
- Must escalate when [scenario]
```

## Conversation Starters

### Purpose
Guide users on what the agent can do.

### Best Practices
1. **Be Specific** - Show exact capabilities
2. **Use Natural Language** - Write as users would ask
3. **Demonstrate Value** - Highlight key features
4. **Vary Complexity** - Mix simple and advanced
5. **Limit Count** - 3-5 optimal

### Good Examples

```json
{
  "title": "Search knowledge base",
  "text": "Find documentation about API authentication"
}
```

```json
{
  "title": "Create support ticket",
  "text": "I need to report a critical production issue"
}
```

```json
{
  "title": "Get system status",
  "text": "What's the current status of all our services?"
}
```

### Bad Examples

❌ Too vague:
```json
{
  "title": "Help",
  "text": "Help me"
}
```

❌ Too generic:
```json
{
  "title": "Start",
  "text": "Get started"
}
```

## API Plugins

See the M365 Agents Knowledge Base for complete API plugin documentation.

## Testing Checklist

- [ ] Schema validates (use assistant validation)
- [ ] All required fields present
- [ ] Field length limits respected
- [ ] Instructions are clear and complete
- [ ] Conversation starters demonstrate features
- [ ] Capabilities are correctly configured
- [ ] API plugins work (if any)
- [ ] Test in Teams environment
- [ ] Mobile and desktop testing
- [ ] Error scenarios handled
- [ ] Edge cases covered

## Deployment Process

1. **Validate Configuration**
   ```bash
   python assistant.py
   # Run: agent validate
   ```

2. **Create Icons**
   - Color: 192x192 PNG
   - Outline: 32x32 PNG

3. **Package for Teams**
   - Create Teams manifest.json
   - Include all agent files
   - Add icons
   - ZIP package

4. **Test in Teams**
   - Upload custom app
   - Test all features
   - Verify on all platforms

5. **Publish**
   - Teams Admin Center (organizational)
   - AppSource (public)

## Common Patterns

### Pattern: Knowledge Base Agent

**Use Case:** Search and retrieve enterprise information

**Components:**
- OneDriveAndSharePoint for documents
- GraphConnectors for custom data
- WebSearch for external info

**Example:**
```json
{
  "capabilities": [
    {
      "name": "WebSearch"
    },
    {
      "name": "OneDriveAndSharePoint",
      "items_by_url": [
        {"url": "https://contoso.sharepoint.com/sites/KB"}
      ]
    }
  ]
}
```

### Pattern: Task Automation Agent

**Use Case:** Create and manage tasks/tickets

**Components:**
- API plugin for CRUD operations
- MicrosoftGraph for user context
- Authentication via OAuth

**Example:**
```json
{
  "capabilities": [
    {
      "name": "MicrosoftGraph",
      "allowed_scopes": ["User.Read"]
    }
  ],
  "actions": [
    {
      "id": "taskAPI",
      "file": "tasks-plugin.json"
    }
  ]
}
```

## Troubleshooting

### Agent doesn't respond as expected
- **Check:** Instructions clarity
- **Fix:** Add more specific examples
- **Fix:** Clarify when to use capabilities

### Capabilities not working
- **Check:** Configuration syntax
- **Check:** Required permissions
- **Check:** Resource accessibility

### Validation errors
- **Check:** Schema URL correct
- **Check:** Version is "v1.0"
- **Check:** Field length limits
- **Use:** Assistant validation tool

## Resources

- [M365 Agents Knowledge Base](m365-agents-knowledge-base.md)
- [Getting Started Guide](getting-started.md)
- [Teams Agents Guide](teams-agents.md)
- [Installation Guide](installation.md)

## Using the Assistant

This toolkit provides an expert assistant:

```bash
# Interactive mode
python assistant.py --mode declarative-agent

# Quick validation
python assistant.py
# Then: agent validate

# List capabilities with details
python assistant.py
# Then: agent list
```

The assistant has complete knowledge of the Microsoft 365 Agents Toolkit and will guide you through creating production-quality agents.
