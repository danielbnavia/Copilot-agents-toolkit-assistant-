# Visual Workflow Designer - Web UI

React-based visual workflow designer for building Microsoft 365 agent workflows.

## Features

- **Drag-and-drop interface** for building workflows
- **Node library** (triggers, actions, conditions, API calls)
- **Real-time validation**
- **Export to JSON**
- **Template library**

## Tech Stack

- React 18
- React Flow Renderer (workflow canvas)
- Vite (build tool)
- TailwindCSS (styling)
- Zustand (state management)

## Getting Started

```bash
cd web-ui
npm install
npm run dev
```

Open http://localhost:3000

## Pages

### 1. Workflow Designer
- Visual canvas for building agent workflows
- Node palette with drag-and-drop
- Properties panel for node configuration
- Export workflow as JSON

### 2. Agent Builder
- Form-based agent creation
- Capability selection
- Conversation starters
- Real-time validation
- Generate declarativeAgent.json

### 3. Template Gallery
- Browse community templates
- Filter by category
- Import templates
- Rate and review

## API Integration

The web UI connects to the marketplace API:

```javascript
// Fetch templates
GET /api/marketplace/templates

// Import template
POST /api/marketplace/import/{templateId}
```

## Development

```bash
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Run tests
npm run test
```

## Deployment

### Azure Static Web Apps

```bash
# Build
npm run build

# Deploy
az staticwebapp create \
  --name m365-agent-designer \
  --resource-group myResourceGroup \
  --source .
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "3000"]
```

## Architecture

```
web-ui/
├── src/
│   ├── components/
│   │   ├── WorkflowDesigner.jsx  # Main workflow canvas
│   │   ├── AgentBuilder.jsx      # Agent creation form
│   │   └── TemplateGallery.jsx   # Template marketplace
│   ├── styles/                   # Component CSS
│   ├── App.jsx                   # Main app component
│   └── main.jsx                  # Entry point
├── public/                       # Static assets
├── index.html                    # HTML template
├── vite.config.js               # Vite configuration
└── package.json                 # Dependencies
```

## Features in Detail

### Workflow Designer
- Add nodes (triggers, actions, conditions, APIs)
- Connect nodes with edges
- Configure node properties
- Validate workflow logic
- Export as JSON for deployment

### Agent Builder
- Guided form for agent creation
- Character count validation (100/1000/8000)
- Capability toggles with icons
- Dynamic conversation starters
- JSON preview and download

### Template Gallery
- Filter by category (Support, Sales, HR, Analytics)
- Search by name/description
- Sort by downloads, rating, date
- Featured templates highlighted
- One-click import

## Browser Support

- Chrome/Edge (recommended)
- Firefox
- Safari

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit pull request

## License

MIT
