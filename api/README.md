# Community Templates Marketplace API

Backend API for the M365 Agent Toolkit community marketplace.

## Features

- Browse and search agent templates
- Filter by category, featured status
- Import templates with automatic setup
- Track downloads and ratings
- Submit new templates to the community

## Setup

```bash
cd api
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

API will be available at `http://localhost:8000`

## API Documentation

Interactive API docs available at: `http://localhost:8000/docs`

## Endpoints

- `GET /api/marketplace/templates` - List all templates
- `GET /api/marketplace/templates/{id}` - Get specific template
- `POST /api/marketplace/templates` - Create new template
- `POST /api/marketplace/import/{id}` - Import template
- `GET /api/marketplace/categories` - List categories
- `GET /api/marketplace/stats` - Marketplace statistics

## Production Deployment

For production, configure:
- PostgreSQL database
- Authentication (OAuth 2.0)
- File storage (Azure Blob Storage)
- Rate limiting
- CDN for static assets
