# Declarative Agent Template

Use this template to create a new Microsoft 365 declarative agent.

## Files

- `declarativeAgent.json` - Main agent manifest (required)
- `instructions.txt` - Agent behavior instructions (recommended)
- `README.md` - This file

## Quick Start

1. **Copy this template:**
   ```bash
   cp -r templates/declarative-agent my-agent
   cd my-agent
   ```

2. **Edit declarativeAgent.json:**
   - Change the `name` field (max 100 characters)
   - Update the `description` (max 1000 characters)
   - Modify conversation starters to match your use case
   - Add capabilities as needed

3. **Edit instructions.txt:**
   - Define the agent's role and responsibilities
   - Specify response guidelines
   - Provide examples of expected behavior
   - List limitations

4. **Test locally:**
   - Use the M365 Assistant to validate: `python assistant.py`
   - Run: `agent validate` and provide the path to declarativeAgent.json

5. **Package for Teams:**
   - Create a Teams app manifest.json
   - Add icons (color: 192x192, outline: 32x32)
   - ZIP all files
   - Upload to Teams

## Capabilities

Choose from these official Microsoft 365 capabilities:

### WebSearch
```json
{
  "name": "WebSearch"
}
```
Enables web search for current information.

### MicrosoftGraph
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
Access Microsoft 365 data through Graph API.

### OneDriveAndSharePoint
```json
{
  "name": "OneDriveAndSharePoint",
  "items_by_url": [
    {
      "url": "https://contoso.sharepoint.com/sites/YourSite"
    }
  ]
}
```
Search documents and content.

### GraphConnectors
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
Access custom data sources through Graph connectors.

## Adding API Plugins

Create an API plugin file (e.g., `my-plugin.json`) and add to the manifest:

```json
"actions": [
  {
    "id": "myPlugin",
    "file": "my-plugin.json"
  }
]
```

See `docs/m365-agents-knowledge-base.md` for complete plugin specifications.

## Best Practices

1. **Be Specific** - Clear, focused agents work better than generalists
2. **Good Instructions** - Detailed instructions improve agent behavior
3. **Test Thoroughly** - Try edge cases and error scenarios
4. **Iterate** - Refine based on user feedback
5. **Monitor** - Track usage to identify improvements

## Resources

- [M365 Agents Knowledge Base](../../docs/m365-agents-knowledge-base.md)
- [Getting Started Guide](../../docs/getting-started.md)
- [Example Agents](../../examples/)

## Validation

Validate your agent configuration:

```bash
python assistant.py
# Then run: agent validate
```

Or use the assistant tool directly:

```python
from src.declarative_agents import DeclarativeAgentHelper

helper = DeclarativeAgentHelper()
helper.validate_agent()
```
