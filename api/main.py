from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import uvicorn
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="M365 Agent Toolkit Marketplace API",
    description="Community marketplace for Microsoft 365 agent templates",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Template(BaseModel):
    id: int
    name: str
    category: str
    description: str
    author: str
    downloads: int
    rating: float
    featured: bool
    created_at: datetime
    manifest: dict
    instructions: str

class TemplateCreate(BaseModel):
    name: str
    category: str
    description: str
    author: str
    manifest: dict
    instructions: str

class TemplateFilter(BaseModel):
    category: Optional[str] = None
    search: Optional[str] = None
    sort_by: Optional[str] = "downloads"
    featured_only: Optional[bool] = False

# Mock database (in production, use SQLAlchemy with PostgreSQL)
templates_db = [
    {
        "id": 1,
        "name": "Customer Support Agent",
        "category": "Support",
        "description": "Automated customer support with ticket management and FAQ capabilities",
        "author": "Microsoft",
        "downloads": 1523,
        "rating": 4.8,
        "featured": True,
        "created_at": datetime.now(),
        "manifest": {
            "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
            "version": "1.0",
            "name": "Customer Support Agent",
            "description": "Helps customers with common inquiries and ticket management"
        },
        "instructions": "You are a customer support agent. Help users with their questions and create tickets when needed."
    },
    {
        "id": 2,
        "name": "Sales Assistant",
        "category": "Sales",
        "description": "Lead qualification and CRM integration for sales teams",
        "author": "Community",
        "downloads": 892,
        "rating": 4.5,
        "featured": True,
        "created_at": datetime.now(),
        "manifest": {
            "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
            "version": "1.0",
            "name": "Sales Assistant",
            "description": "Qualifies leads and manages sales pipeline"
        },
        "instructions": "You are a sales assistant. Help qualify leads and manage the sales pipeline."
    }
]

@app.get("/")
def read_root():
    return {"message": "M365 Agent Toolkit Marketplace API", "version": "1.0.0"}

@app.get("/api/marketplace/templates", response_model=List[Template])
def get_templates(
    category: Optional[str] = None,
    search: Optional[str] = None,
    featured_only: Optional[bool] = False
):
    """Get all templates with optional filtering"""
    filtered = templates_db.copy()
    
    if category:
        filtered = [t for t in filtered if t["category"] == category]
    
    if search:
        filtered = [
            t for t in filtered
            if search.lower() in t["name"].lower() or search.lower() in t["description"].lower()
        ]
    
    if featured_only:
        filtered = [t for t in filtered if t["featured"]]
    
    return filtered

@app.get("/api/marketplace/templates/{template_id}", response_model=Template)
def get_template(template_id: int):
    """Get a specific template by ID"""
    template = next((t for t in templates_db if t["id"] == template_id), None)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

@app.post("/api/marketplace/templates", response_model=Template)
def create_template(template: TemplateCreate):
    """Create a new template (requires authentication in production)"""
    new_template = {
        "id": len(templates_db) + 1,
        "name": template.name,
        "category": template.category,
        "description": template.description,
        "author": template.author,
        "downloads": 0,
        "rating": 0.0,
        "featured": False,
        "created_at": datetime.now(),
        "manifest": template.manifest,
        "instructions": template.instructions
    }
    templates_db.append(new_template)
    return new_template

@app.post("/api/marketplace/import/{template_id}")
def import_template(template_id: int):
    """Import a template (downloads files)"""
    template = next((t for t in templates_db if t["id"] == template_id), None)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    
    # Increment download count
    template["downloads"] += 1
    
    return {
        "success": True,
        "message": f"Template '{template['name']}' imported successfully",
        "files": {
            "manifest": template["manifest"],
            "instructions": template["instructions"]
        }
    }

@app.get("/api/marketplace/categories")
def get_categories():
    """Get all available categories"""
    categories = list(set(t["category"] for t in templates_db))
    return {"categories": categories}

@app.get("/api/marketplace/stats")
def get_stats():
    """Get marketplace statistics"""
    return {
        "total_templates": len(templates_db),
        "total_downloads": sum(t["downloads"] for t in templates_db),
        "featured_count": len([t for t in templates_db if t["featured"]]),
        "categories": len(set(t["category"] for t in templates_db))
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
