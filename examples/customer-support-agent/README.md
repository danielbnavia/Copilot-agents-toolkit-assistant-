# Customer Support Agent Example

This is a complete example of a declarative agent for customer support.

## Features

- **Knowledge Base Search** - Searches SharePoint for support documentation
- **Web Search** - Finds current solutions and information online
- **Ticket Management** - Can create and track support tickets (when integrated with API)
- **Troubleshooting Guidance** - Provides step-by-step help

## Files

- `declarativeAgent.json` - Main agent configuration following Microsoft schema v1.0
- `instructions.txt` - Detailed instructions for agent behavior
- `README.md` - This file

## Setup

1. **Update SharePoint URL** - Edit `declarativeAgent.json` and replace the SharePoint URL with your support site:
   ```json
   "items_by_url": [
     {
       "url": "https://YOUR-TENANT.sharepoint.com/sites/YOUR-SUPPORT-SITE"
     }
   ]
   ```

2. **Customize Instructions** - Edit `instructions.txt` to match your products, policies, and procedures

3. **Add Conversation Starters** - Modify the conversation starters in `declarativeAgent.json` to match common user queries

4. **Package for Teams** - Create a Teams app package:
   - Add a `manifest.json` (Teams app manifest)
   - Include color icon (192x192 PNG)
   - Include outline icon (32x32 PNG)
   - ZIP all files together

## Testing

1. Upload the package to Teams (Upload a custom app)
2. Start a chat with the agent
3. Try the conversation starters
4. Test with various support scenarios

## Extending

### Add API Plugin for Ticket System

Create `ticketing-plugin.json`:

```json
{
  "schema_version": "v2.1",
  "name_for_human": "Support Ticketing",
  "description_for_model": "Create and manage support tickets",
  "functions": [
    {
      "name": "createTicket",
      "description": "Create a new support ticket"
    },
    {
      "name": "getTicket",
      "description": "Get ticket details by ID"
    }
  ],
  "runtimes": [
    {
      "type": "OpenApi",
      "spec": {
        "url": "https://api.yourcompany.com/openapi.json"
      }
    }
  ]
}
```

Then add to `declarativeAgent.json`:

```json
"actions": [
  {
    "id": "ticketingSystem",
    "file": "ticketing-plugin.json"
  }
]
```

## Best Practices

1. **Keep Instructions Clear** - The instructions.txt should be comprehensive but focused
2. **Test Thoroughly** - Try edge cases and error scenarios
3. **Monitor Usage** - Track what users ask to improve the agent
4. **Update Knowledge Base** - Keep SharePoint documentation current
5. **Iterate Based on Feedback** - Continuously improve based on user feedback

## Resources

- [M365 Agents Knowledge Base](../../docs/m365-agents-knowledge-base.md)
- [Declarative Agents Guide](../../docs/declarative-agents.md)
- [Getting Started Guide](../../docs/getting-started.md)
