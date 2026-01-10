"""
Template Manager - Agent Store browser and template importer
"""

import json
import os
import shutil
from typing import Dict, Any, List, Optional
from pathlib import Path


class TemplateManager:
    """Manage templates from community and Agent Store."""
    
    # Simulated Agent Store catalog (in production, this would fetch from actual store)
    AGENT_STORE_TEMPLATES = {
        "customer-support": {
            "name": "Customer Support Agent",
            "category": "Support",
            "description": "AI agent for customer support with ticket management",
            "author": "Microsoft",
            "rating": 4.8,
            "downloads": 15000,
            "capabilities": ["WebSearch", "MicrosoftGraph"],
            "file": "customer-support-agent"
        },
        "sales-assistant": {
            "name": "Sales Assistant",
            "category": "Sales",
            "description": "CRM integration and lead qualification agent",
            "author": "Microsoft",
            "rating": 4.6,
            "downloads": 12000,
            "capabilities": ["MicrosoftGraph", "OneDriveAndSharePoint"],
            "file": "sales-assistant-agent"
        },
        "hr-onboarding": {
            "name": "HR Onboarding Agent",
            "category": "HR",
            "description": "Automate employee onboarding process",
            "author": "Community",
            "rating": 4.5,
            "downloads": 8000,
            "capabilities": ["MicrosoftGraph", "WebSearch"],
            "file": "hr-onboarding-agent"
        },
        "data-analyst": {
            "name": "Data Analyst Agent",
            "category": "Analytics",
            "description": "Analyze data and generate insights",
            "author": "Microsoft",
            "rating": 4.7,
            "downloads": 10000,
            "capabilities": ["MicrosoftGraph", "GraphConnectors"],
            "file": "data-analyst-agent"
        },
        "meeting-assistant": {
            "name": "Meeting Assistant",
            "category": "Productivity",
            "description": "Schedule meetings and manage calendars",
            "author": "Community",
            "rating": 4.4,
            "downloads": 7500,
            "capabilities": ["MicrosoftGraph"],
            "file": "meeting-assistant-agent"
        }
    }
    
    def __init__(self, verbose: bool = False):
        """Initialize template manager.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.local_templates_path = Path("templates")
        self.examples_path = Path("examples")
        
    def browse_store(self, category: Optional[str] = None, sort_by: str = "downloads"):
        """Browse Agent Store templates.
        
        Args:
            category: Filter by category (Support, Sales, HR, Analytics, Productivity)
            sort_by: Sort by 'downloads', 'rating', or 'name'
        """
        print("\n" + "="*80)
        print("🏪 AGENT STORE - Browse Templates")
        print("="*80 + "\n")
        
        templates = self.AGENT_STORE_TEMPLATES.copy()
        
        # Filter by category
        if category:
            templates = {k: v for k, v in templates.items() if v["category"] == category}
            print(f"📂 Category: {category}\n")
        
        # Sort templates
        sorted_templates = sorted(
            templates.items(),
            key=lambda x: x[1].get(sort_by, 0),
            reverse=(sort_by in ["downloads", "rating"])
        )
        
        # Display templates
        for i, (key, template) in enumerate(sorted_templates, 1):
            print(f"{i}. {template['name']}")
            print(f"   Category: {template['category']} | Author: {template['author']}")
            print(f"   ⭐ {template['rating']}/5.0 | 📥 {template['downloads']:,} downloads")
            print(f"   {template['description']}")
            print(f"   Capabilities: {', '.join(template['capabilities'])}")
            print(f"   Template ID: {key}")
            print()
        
        print(f"Total templates: {len(sorted_templates)}")
        print("\n💡 To import: use 'template import <template-id>'\n")
        
    def import_template(self, template_id: str, output_dir: Optional[str] = None) -> bool:
        """Import a template from Agent Store.
        
        Args:
            template_id: Template identifier
            output_dir: Output directory (default: current directory)
            
        Returns:
            True if successful
        """
        if template_id not in self.AGENT_STORE_TEMPLATES:
            print(f"❌ Template '{template_id}' not found in Agent Store")
            print("\nAvailable templates:")
            for tid in self.AGENT_STORE_TEMPLATES.keys():
                print(f"  • {tid}")
            return False
        
        template = self.AGENT_STORE_TEMPLATES[template_id]
        
        print(f"\n📥 Importing template: {template['name']}")
        print(f"   Category: {template['category']}")
        print(f"   Author: {template['author']}\n")
        
        # Determine output directory
        if output_dir is None:
            output_dir = template_id
        
        output_path = Path(output_dir)
        
        # Check if directory exists
        if output_path.exists():
            response = input(f"Directory '{output_dir}' exists. Overwrite? (y/n): ")
            if response.lower() != 'y':
                print("Import cancelled.")
                return False
            shutil.rmtree(output_path)
        
        # Create directory
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate template files based on type
        self._generate_template_files(template_id, template, output_path)
        
        print(f"\n✅ Template imported successfully to: {output_dir}/")
        print(f"\n📁 Created files:")
        for file in output_path.rglob("*"):
            if file.is_file():
                print(f"   • {file.relative_to(output_path)}")
        
        print(f"\n📚 Next steps:")
        print(f"   1. cd {output_dir}")
        print(f"   2. Review and customize the agent configuration")
        print(f"   3. Test with Teams Toolkit or assistant.py")
        print(f"   4. Deploy to Microsoft Teams\n")
        
        return True
    
    def _generate_template_files(self, template_id: str, template: Dict[str, Any], output_path: Path):
        """Generate template files.
        
        Args:
            template_id: Template identifier
            template: Template metadata
            output_path: Output directory path
        """
        # Create declarativeAgent.json
        agent_config = {
            "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
            "version": "v1.0",
            "name": template["name"],
            "description": template["description"],
            "instructions": "$[file('instructions.txt')]",
            "conversation_starters": self._get_conversation_starters(template_id),
            "capabilities": [{"name": cap} for cap in template["capabilities"]]
        }
        
        with open(output_path / "declarativeAgent.json", 'w') as f:
            json.dump(agent_config, f, indent=2)
        
        # Create instructions.txt
        instructions = self._get_instructions(template_id, template)
        with open(output_path / "instructions.txt", 'w') as f:
            f.write(instructions)
        
        # Create README.md
        readme = self._get_readme(template_id, template)
        with open(output_path / "README.md", 'w') as f:
            f.write(readme)
    
    def _get_conversation_starters(self, template_id: str) -> List[Dict[str, str]]:
        """Get conversation starters for template."""
        starters_map = {
            "customer-support": [
                {"title": "Check ticket status", "text": "What's the status of ticket #12345?"},
                {"title": "Report issue", "text": "I need to report a technical problem"},
                {"title": "Get help", "text": "How do I reset my password?"}
            ],
            "sales-assistant": [
                {"title": "Qualify lead", "text": "Tell me about the new lead from Contoso"},
                {"title": "Check pipeline", "text": "Show me my sales pipeline"},
                {"title": "Schedule demo", "text": "Schedule a product demo with the prospect"}
            ],
            "hr-onboarding": [
                {"title": "Start onboarding", "text": "I need to onboard a new employee"},
                {"title": "Check progress", "text": "What's the onboarding status for John Doe?"},
                {"title": "Get checklist", "text": "Show me the onboarding checklist"}
            ],
            "data-analyst": [
                {"title": "Analyze data", "text": "Analyze sales data for last quarter"},
                {"title": "Generate report", "text": "Create a revenue report"},
                {"title": "Show trends", "text": "What are the trends in customer acquisition?"}
            ],
            "meeting-assistant": [
                {"title": "Schedule meeting", "text": "Schedule a team meeting for next week"},
                {"title": "Check availability", "text": "When is everyone available on Friday?"},
                {"title": "Meeting summary", "text": "Summarize yesterday's meeting"}
            ]
        }
        return starters_map.get(template_id, [])
    
    def _get_instructions(self, template_id: str, template: Dict[str, Any]) -> str:
        """Get instructions for template."""
        return f"""You are {template['name']}, an AI agent specialized in your domain.

{template['description']}

## Your Role
- Assist users with tasks in the {template['category']} domain
- Provide accurate and helpful information
- Use configured capabilities effectively

## Response Guidelines
- Be professional, helpful, and accurate
- Ask clarifying questions when needed
- Provide step-by-step guidance
- Use data from your capabilities to ground responses

## Capabilities
You have access to the following capabilities:
{chr(10).join(f'- {cap}: Use this for relevant tasks' for cap in template['capabilities'])}

## Examples

User: "Can you help me?"
You: "Of course! I'm {template['name']}. I can help you with {template['category'].lower()}-related tasks. What do you need assistance with?"

## Limitations
- Provide information within your domain expertise
- Escalate complex issues when appropriate
- Follow enterprise policies and guidelines
"""
    
    def _get_readme(self, template_id: str, template: Dict[str, Any]) -> str:
        """Get README for template."""
        return f"""# {template['name']}

{template['description']}

## Template Information

- **Category**: {template['category']}
- **Author**: {template['author']}
- **Rating**: ⭐ {template['rating']}/5.0
- **Downloads**: {template['downloads']:,}

## Capabilities

{chr(10).join(f'- **{cap}**: Microsoft 365 integration' for cap in template['capabilities'])}

## Setup

1. Review `declarativeAgent.json` configuration
2. Customize `instructions.txt` for your use case
3. Add conversation starters as needed
4. Test locally with Teams Toolkit
5. Deploy to Microsoft Teams

## Customization

### Instructions
Edit `instructions.txt` to:
- Define specific behavior for your organization
- Add domain knowledge
- Customize response style

### Capabilities
Modify `declarativeAgent.json` to:
- Add or remove capabilities
- Configure capability-specific settings
- Add API plugins or connectors

## Testing

```bash
# Validate configuration
python assistant.py
# Then run: agent validate

# Test in Teams
# 1. Package with Teams Toolkit
# 2. Upload to Teams
# 3. Test conversation starters
```

## Deployment

1. Create Teams app package
2. Upload to Teams Admin Center
3. Publish to your organization
4. Monitor usage and feedback

## Support

- Documentation: See main project docs/
- Templates: Browse more at Agent Store
- Issues: Report via GitHub

---

*Imported from Agent Store*
"""
    
    def list_local_templates(self):
        """List locally available templates."""
        print("\n" + "="*80)
        print("📁 LOCAL TEMPLATES")
        print("="*80 + "\n")
        
        if not self.local_templates_path.exists():
            print("No local templates found.")
            return
        
        templates = []
        for template_dir in self.local_templates_path.iterdir():
            if template_dir.is_dir() and (template_dir / "declarativeAgent.json").exists():
                templates.append(template_dir.name)
        
        if not templates:
            print("No templates found in templates/ directory")
        else:
            print(f"Found {len(templates)} template(s):\n")
            for i, template in enumerate(templates, 1):
                print(f"{i}. {template}")
        
        print()
    
    def interactive_mode(self):
        """Run template manager in interactive mode."""
        while True:
            print("\n" + "="*80)
            print("🏪 TEMPLATE MANAGER")
            print("="*80)
            print("\n1. Browse Agent Store")
            print("2. Import template from Store")
            print("3. List local templates")
            print("4. Browse by category")
            print("5. Back to main menu")
            
            choice = input("\nSelect option (1-5): ").strip()
            
            if choice == "1":
                sort_choice = input("\nSort by (downloads/rating/name) [downloads]: ").strip() or "downloads"
                self.browse_store(sort_by=sort_choice)
            elif choice == "2":
                template_id = input("\nEnter template ID: ").strip()
                output_dir = input("Output directory (press Enter for default): ").strip() or None
                self.import_template(template_id, output_dir)
            elif choice == "3":
                self.list_local_templates()
            elif choice == "4":
                print("\nCategories: Support, Sales, HR, Analytics, Productivity")
                category = input("Enter category: ").strip()
                self.browse_store(category=category)
            elif choice == "5":
                break
            else:
                print("Invalid option")
            
            input("\nPress Enter to continue...")
