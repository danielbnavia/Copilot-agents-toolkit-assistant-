# Microsoft 365 Agents Toolkit - All Scenarios Coverage

## Complete Scenario Reference

This document covers ALL scenarios supported by Microsoft 365 Agents Toolkit.

## Table of Contents

1. [Declarative Agent Scenarios](#declarative-agent-scenarios)
2. [API Plugin Scenarios](#api-plugin-scenarios)
3. [Message Extension Scenarios](#message-extension-scenarios)
4. [Teams Bot Scenarios](#teams-bot-scenarios)
5. [Adaptive Card Scenarios](#adaptive-card-scenarios)
6. [Workflow & Automation Scenarios](#workflow--automation-scenarios)
7. [Microsoft Graph Integration Scenarios](#microsoft-graph-integration-scenarios)
8. [Office Add-in Scenarios](#office-add-in-scenarios)
9. [Connector Scenarios](#connector-scenarios)
10. [Advanced Integration Scenarios](#advanced-integration-scenarios)

---

## Declarative Agent Scenarios

### 1. Knowledge Base & Search Agents

**Scenario:** Search enterprise content and provide answers

**Capabilities Used:**
- OneDriveAndSharePoint
- GraphConnectors
- WebSearch

**Use Cases:**
- Corporate knowledge base search
- Policy and procedure lookups
- Document findability
- FAQ automation
- Technical documentation search

**Example Configuration:**
```json
{
  "capabilities": [
    {
      "name": "OneDriveAndSharePoint",
      "items_by_url": [
        {"url": "https://contoso.sharepoint.com/sites/KB"}
      ]
    },
    {
      "name": "WebSearch"
    },
    {
      "name": "GraphConnectors",
      "connections": [
        {"connection_id": "knowledgebase_connector"}
      ]
    }
  ]
}
```

### 2. Task & Ticket Management Agents

**Scenario:** Create, track, and manage tasks or support tickets

**Capabilities Used:**
- MicrosoftGraph (for user context)
- API Plugins (for ticket system integration)

**Use Cases:**
- IT helpdesk automation
- Project task creation
- Bug tracking
- Service requests
- Incident management

**Example Configuration:**
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
      "id": "ticketingSystem",
      "file": "ticketing-api-plugin.json"
    }
  ]
}
```

### 3. Data Analysis & Reporting Agents

**Scenario:** Analyze data and generate reports

**Capabilities Used:**
- API Plugins (for analytics services)
- MicrosoftGraph (for M365 data)
- GraphConnectors (for custom data)

**Use Cases:**
- Sales performance analysis
- Financial reporting
- Customer analytics
- Operational metrics
- Trend analysis

### 4. Employee Onboarding & HR Agents

**Scenario:** Assist with employee lifecycle management

**Capabilities Used:**
- MicrosoftGraph (User, Groups, Calendar)
- OneDriveAndSharePoint (HR documents)
- API Plugins (HR systems)

**Use Cases:**
- New employee onboarding
- Benefits enrollment
- Time-off requests
- Performance reviews
- Training coordination

### 5. Sales & CRM Agents

**Scenario:** Sales assistance and CRM integration

**Capabilities Used:**
- API Plugins (CRM integration)
- MicrosoftGraph (Contacts, Calendar)
- WebSearch (company research)

**Use Cases:**
- Lead qualification
- Opportunity management
- Customer information lookup
- Meeting scheduling
- Pipeline reporting

### 6. Customer Support Agents

**Scenario:** Customer service and support automation

**Capabilities Used:**
- OneDriveAndSharePoint (support KB)
- API Plugins (support systems)
- WebSearch (product info)

**Use Cases:**
- Troubleshooting assistance
- Account management
- Product information
- Issue escalation
- Status updates

### 7. Legal & Compliance Agents

**Scenario:** Legal document search and compliance checking

**Capabilities Used:**
- OneDriveAndSharePoint (legal documents)
- GraphConnectors (contract repositories)
- API Plugins (compliance systems)

**Use Cases:**
- Contract search
- Compliance verification
- Policy guidance
- Document review
- Legal research

### 8. Finance & Expense Agents

**Scenario:** Financial data and expense management

**Capabilities Used:**
- API Plugins (expense systems)
- MicrosoftGraph (user data)
- OneDriveAndSharePoint (receipts)

**Use Cases:**
- Expense submission
- Budget tracking
- Invoice processing
- Financial approvals
- Spending analysis

---

## API Plugin Scenarios

### 1. CRUD Operations Plugin

**Scenario:** Create, Read, Update, Delete records

**OpenAPI Operations:**
- GET /items/{id}
- GET /items
- POST /items
- PUT /items/{id}
- DELETE /items/{id}

**Use Cases:**
- Database record management
- Content management
- User management
- Inventory tracking

### 2. Search & Filter Plugin

**Scenario:** Advanced search and filtering

**OpenAPI Operations:**
- GET /search?q={query}&filter={filter}
- POST /search/advanced
- GET /filter/options

**Use Cases:**
- Product search
- Document search
- User lookup
- Advanced filtering

### 3. Notification & Alerts Plugin

**Scenario:** Send notifications and manage alerts

**OpenAPI Operations:**
- POST /notifications
- GET /notifications/{id}
- PUT /notifications/{id}/read
- DELETE /notifications/{id}

**Use Cases:**
- System alerts
- User notifications
- Event triggers
- Status updates

### 4. Authentication & Authorization Plugin

**Scenario:** User authentication and permissions

**OpenAPI Operations:**
- POST /auth/login
- POST /auth/logout
- GET /auth/permissions
- POST /auth/token/refresh

**Use Cases:**
- SSO integration
- Permission checks
- Access control
- Token management

### 5. File Upload & Management Plugin

**Scenario:** Handle file operations

**OpenAPI Operations:**
- POST /files/upload
- GET /files/{id}
- DELETE /files/{id}
- GET /files/{id}/download

**Use Cases:**
- Document uploads
- Image management
- File sharing
- Attachment handling

### 6. Scheduling & Calendar Plugin

**Scenario:** Manage schedules and appointments

**OpenAPI Operations:**
- GET /availability
- POST /appointments
- PUT /appointments/{id}
- DELETE /appointments/{id}

**Use Cases:**
- Meeting scheduling
- Resource booking
- Availability checking
- Calendar management

### 7. Payment & Transaction Plugin

**Scenario:** Handle payments and transactions

**OpenAPI Operations:**
- POST /payments
- GET /payments/{id}
- POST /refunds
- GET /transactions

**Use Cases:**
- Payment processing
- Order management
- Refund handling
- Transaction history

### 8. Analytics & Metrics Plugin

**Scenario:** Gather and analyze metrics

**OpenAPI Operations:**
- GET /metrics
- GET /analytics/summary
- POST /analytics/query
- GET /reports/{reportId}

**Use Cases:**
- Performance metrics
- Usage analytics
- Custom reporting
- Data visualization

---

## Message Extension Scenarios

### 1. Search-based Message Extensions

**Scenario:** Search external content and insert into conversations

**Configuration:**
```json
{
  "composeExtensions": [{
    "botId": "bot-id",
    "commands": [{
      "id": "searchCmd",
      "type": "query",
      "title": "Search",
      "description": "Search for items"
    }]
  }]
}
```

**Use Cases:**
- Product lookup
- Ticket search
- Document finding
- Contact lookup

### 2. Action-based Message Extensions

**Scenario:** Create content from conversations

**Configuration:**
```json
{
  "composeExtensions": [{
    "botId": "bot-id",
    "commands": [{
      "id": "createCmd",
      "type": "action",
      "title": "Create",
      "description": "Create new item"
    }]
  }]
}
```

**Use Cases:**
- Create tasks from messages
- Log bugs from conversations
- Create calendar events
- Generate documents

### 3. Link Unfurling

**Scenario:** Automatically unfurl links in conversations

**Configuration:**
```json
{
  "composeExtensions": [{
    "botId": "bot-id",
    "messageHandlers": [{
      "type": "link",
      "value": {
        "domains": ["example.com"]
      }
    }]
  }]
}
```

**Use Cases:**
- Ticket preview cards
- Product information
- Document previews
- Link enrichment

---

## Teams Bot Scenarios

### 1. Conversational Bots

**Scenario:** Interactive Q&A and chat

**Features:**
- Message handling
- Proactive messaging
- Adaptive Cards
- Rich responses

**Use Cases:**
- FAQ bots
- Virtual assistants
- Training bots
- Survey bots

### 2. Meeting Bots

**Scenario:** Participate in Teams meetings

**Features:**
- Meeting events
- Recording
- Transcription
- Note-taking

**Use Cases:**
- Meeting assistants
- Transcription services
- Meeting summaries
- Action item tracking

### 3. Notification Bots

**Scenario:** Send proactive notifications

**Features:**
- Proactive messaging
- Channel posting
- User notifications
- Alert management

**Use Cases:**
- System alerts
- Build notifications
- Status updates
- Reminders

### 4. Command Bots

**Scenario:** Execute specific commands

**Features:**
- Command lists
- Parameter handling
- Help system
- Command routing

**Use Cases:**
- DevOps bots
- Admin tools
- System control
- Automation triggers

---

## Adaptive Card Scenarios

### 1. Information Display Cards

**Scenario:** Present formatted information

**Card Types:**
- Status cards
- Profile cards
- Summary cards
- List cards

**Use Cases:**
- User profiles
- System status
- Reports
- Dashboards

### 2. Input Collection Cards

**Scenario:** Gather user input

**Card Elements:**
- Input.Text
- Input.Number
- Input.Date
- Input.ChoiceSet
- Input.Toggle

**Use Cases:**
- Forms
- Surveys
- Feedback collection
- Data entry

### 3. Approval Cards

**Scenario:** Request approvals

**Card Features:**
- Action buttons
- Input fields
- Status indicators
- Comment sections

**Use Cases:**
- Expense approvals
- Leave requests
- Purchase orders
- Document reviews

### 4. Interactive Dashboard Cards

**Scenario:** Dynamic data visualization

**Card Features:**
- Data binding
- Refresh actions
- Chart integration
- Multiple sections

**Use Cases:**
- KPI dashboards
- Metrics display
- Live data views
- Analytics cards

---

## Workflow & Automation Scenarios

### 1. Approval Workflows

**Scenario:** Multi-step approval processes

**Components:**
- Trigger: Document uploaded
- Actions: Request approval, notify stakeholders
- Conditions: Approval status checks

**Use Cases:**
- Document approvals
- Expense approvals
- Purchase requests
- Access requests

### 2. Data Synchronization Workflows

**Scenario:** Sync data between systems

**Components:**
- Trigger: Data changed
- Actions: Update target system
- Error handling

**Use Cases:**
- CRM sync
- Database replication
- File synchronization
- Contact updates

### 3. Notification Workflows

**Scenario:** Automated notifications

**Components:**
- Trigger: Event occurs
- Actions: Send notifications
- Conditions: User preferences

**Use Cases:**
- Alert systems
- Deadline reminders
- Status updates
- Event notifications

### 4. Scheduled Workflows

**Scenario:** Recurring automated tasks

**Components:**
- Trigger: Schedule/time
- Actions: Execute tasks
- Reporting

**Use Cases:**
- Daily reports
- Backup processes
- Data cleanup
- Scheduled emails

---

## Microsoft Graph Integration Scenarios

### 1. User & Identity Management

**Graph APIs:**
- /users
- /groups
- /me
- /organization

**Use Cases:**
- User lookup
- Group membership
- Profile updates
- Directory search

### 2. Mail & Calendar

**Graph APIs:**
- /me/messages
- /me/events
- /me/mailFolders
- /users/{id}/calendar

**Use Cases:**
- Email reading
- Event creation
- Calendar management
- Meeting scheduling

### 3. Files & Content

**Graph APIs:**
- /me/drive
- /sites/{id}/drives
- /me/drive/root/children
- /shares/{id}

**Use Cases:**
- File access
- Document search
- Content management
- Sharing management

### 4. Teams & Collaboration

**Graph APIs:**
- /teams
- /teams/{id}/channels
- /chats
- /me/joinedTeams

**Use Cases:**
- Team management
- Channel operations
- Chat access
- Membership control

### 5. Planner & Tasks

**Graph APIs:**
- /planner/tasks
- /planner/plans
- /me/todo/lists
- /me/todo/lists/{id}/tasks

**Use Cases:**
- Task management
- Plan creation
- To-do lists
- Assignment tracking

### 6. Security & Compliance

**Graph APIs:**
- /security/alerts
- /security/secureScores
- /compliance/ediscovery
- /identityProtection

**Use Cases:**
- Security monitoring
- Threat detection
- Compliance checks
- Risk assessment

---

## Office Add-in Scenarios

### 1. Word Add-ins

**Scenario:** Extend Word functionality

**Features:**
- Content insertion
- Document automation
- Template management
- Custom task panes

**Use Cases:**
- Document generation
- Template insertion
- Content validation
- Style enforcement

### 2. Excel Add-ins

**Scenario:** Enhance Excel capabilities

**Features:**
- Custom functions
- Data import/export
- Chart creation
- Automation

**Use Cases:**
- Data analysis
- Report generation
- Custom calculations
- External data integration

### 3. PowerPoint Add-ins

**Scenario:** Extend presentations

**Features:**
- Slide insertion
- Content generation
- Design automation
- Media integration

**Use Cases:**
- Template slides
- Brand compliance
- Content import
- Automated presentations

### 4. Outlook Add-ins

**Scenario:** Extend email functionality

**Features:**
- Email analysis
- Action buttons
- Context cards
- Automation

**Use Cases:**
- Email tracking
- CRM integration
- Meeting scheduling
- Contact management

---

## Connector Scenarios

### 1. Custom Data Source Connectors

**Scenario:** Index external data for search

**Components:**
- Schema definition
- Data ingestion
- Search integration
- ACLs

**Use Cases:**
- Database indexing
- Legacy system integration
- Third-party data
- Custom repositories

### 2. File Share Connectors

**Scenario:** Index network file shares

**Components:**
- File crawler
- Metadata extraction
- Content indexing
- Permission mapping

**Use Cases:**
- Network drives
- Legacy file systems
- Archived content
- Shared directories

### 3. Web Content Connectors

**Scenario:** Index web content

**Components:**
- Web crawler
- HTML parsing
- Link following
- Content extraction

**Use Cases:**
- Intranet sites
- Public websites
- Knowledge bases
- Documentation sites

### 4. API-based Connectors

**Scenario:** Index data from APIs

**Components:**
- API integration
- Data transformation
- Incremental updates
- Error handling

**Use Cases:**
- SaaS applications
- Cloud services
- REST APIs
- Data platforms

---

## Advanced Integration Scenarios

### 1. Multi-Agent Orchestration

**Scenario:** Multiple agents working together

**Pattern:**
- Specialized agents for domains
- Agent-to-agent communication
- Shared context
- Workflow coordination

**Use Cases:**
- Complex business processes
- Multi-department workflows
- Escalation chains
- Collaborative problem-solving

### 2. Hybrid AI/Human Workflows

**Scenario:** AI assistance with human oversight

**Pattern:**
- AI handles routine tasks
- Human approval for critical decisions
- Feedback loops
- Learning from interventions

**Use Cases:**
- Content moderation
- Financial approvals
- Legal reviews
- Medical diagnostics

### 3. Real-time Data Integration

**Scenario:** Live data from multiple sources

**Pattern:**
- WebSockets/SignalR
- Event-driven updates
- Data streaming
- Real-time sync

**Use Cases:**
- Stock trading info
- IoT sensor data
- Live dashboards
- Monitoring systems

### 4. AI-Enhanced Automation

**Scenario:** AI models integrated with workflows

**Pattern:**
- Custom AI models
- Azure Cognitive Services
- Form recognizer
- Language understanding

**Use Cases:**
- Document classification
- Sentiment analysis
- Image recognition
- Predictive analytics

---

## Implementation Matrix

| Scenario Type | Declarative Agent | API Plugin | Teams Bot | Message Extension | Workflow | Graph API | Connector |
|--------------|-------------------|------------|-----------|-------------------|----------|-----------|-----------|
| Search & Retrieval | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Task Automation | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Notifications | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Approvals | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Data Analysis | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Content Creation | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| User Interaction | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Scheduled Tasks | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |

---

## Choosing the Right Approach

### Use Declarative Agent When:
- Primary interface is conversational
- Need AI-powered responses
- Require context understanding
- Multiple data sources needed
- Natural language interaction essential

### Use API Plugin When:
- Specific actions needed
- External system integration
- CRUD operations required
- Well-defined APIs exist
- Structured data exchange

### Use Teams Bot When:
- Rich conversational UI needed
- Proactive messaging required
- Meeting participation needed
- Complex interaction flows
- Custom logic essential

### Use Message Extension When:
- In-context actions needed
- Quick data insertion
- Search while composing
- Link unfurling required
- Lightweight interactions

### Use Workflow When:
- Multi-step processes
- Scheduled automation
- Cross-system orchestration
- Business process automation
- No user interaction needed

### Use Graph Connector When:
- Custom data indexing
- Enterprise search needed
- Legacy system integration
- Unified search required
- ACL preservation important

---

This document provides complete coverage of all Microsoft 365 Agents Toolkit scenarios. Refer to specific implementation guides in the `docs/` directory for detailed instructions.
