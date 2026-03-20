"""Adaptive Cards helper module"""

import json
import os
from typing import Dict, Any, List, Optional


class AdaptiveCardHelper:
    """Helper class for creating and managing Adaptive Cards."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the adaptive card helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def create_card(self, card_type: str, title: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create an adaptive card.
        
        Args:
            card_type: Type of card (e.g., 'approval', 'notification', 'form')
            title: Card title
            data: Card data
            
        Returns:
            Adaptive card JSON
        """
        if card_type == "approval":
            return self._create_approval_card(title, data)
        elif card_type == "notification":
            return self._create_notification_card(title, data)
        elif card_type == "form":
            return self._create_form_card(title, data)
        else:
            return self._create_basic_card(title, data)
            
    def _create_basic_card(self, title: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a basic adaptive card.
        
        Args:
            title: Card title
            data: Card data
            
        Returns:
            Adaptive card JSON
        """
        return {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.5",
            "body": [
                {
                    "type": "TextBlock",
                    "text": title,
                    "weight": "Bolder",
                    "size": "Large"
                },
                {
                    "type": "TextBlock",
                    "text": data.get("description", ""),
                    "wrap": True
                }
            ]
        }
        
    def _create_approval_card(self, title: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create an approval card.
        
        Args:
            title: Card title
            data: Card data with requestor, amount, etc.
            
        Returns:
            Approval card JSON
        """
        return {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.5",
            "body": [
                {
                    "type": "TextBlock",
                    "text": title,
                    "weight": "Bolder",
                    "size": "Large",
                    "color": "Accent"
                },
                {
                    "type": "FactSet",
                    "facts": [
                        {
                            "title": "Requestor:",
                            "value": data.get("requestor", "N/A")
                        },
                        {
                            "title": "Amount:",
                            "value": data.get("amount", "N/A")
                        },
                        {
                            "title": "Date:",
                            "value": data.get("date", "Today")
                        }
                    ]
                },
                {
                    "type": "TextBlock",
                    "text": data.get("description", ""),
                    "wrap": True,
                    "spacing": "Medium"
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "Approve",
                    "style": "positive",
                    "data": {
                        "action": "approve",
                        "id": data.get("id", "")
                    }
                },
                {
                    "type": "Action.Submit",
                    "title": "Reject",
                    "style": "destructive",
                    "data": {
                        "action": "reject",
                        "id": data.get("id", "")
                    }
                }
            ]
        }
        
    def _create_notification_card(self, title: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a notification card.
        
        Args:
            title: Card title
            data: Card data
            
        Returns:
            Notification card JSON
        """
        return {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.5",
            "body": [
                {
                    "type": "Container",
                    "style": data.get("style", "emphasis"),
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": title,
                            "weight": "Bolder",
                            "size": "Large"
                        },
                        {
                            "type": "TextBlock",
                            "text": data.get("message", ""),
                            "wrap": True
                        }
                    ]
                }
            ],
            "actions": [
                {
                    "type": "Action.OpenUrl",
                    "title": "View Details",
                    "url": data.get("url", "https://example.com")
                }
            ] if data.get("url") else []
        }
        
    def _create_form_card(self, title: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a form card.
        
        Args:
            title: Card title
            data: Form fields data
            
        Returns:
            Form card JSON
        """
        body = [
            {
                "type": "TextBlock",
                "text": title,
                "weight": "Bolder",
                "size": "Large"
            }
        ]
        
        # Add form fields
        for field in data.get("fields", []):
            if field.get("type") == "text":
                body.append({
                    "type": "Input.Text",
                    "id": field.get("id", ""),
                    "placeholder": field.get("placeholder", ""),
                    "label": field.get("label", "")
                })
            elif field.get("type") == "choice":
                body.append({
                    "type": "Input.ChoiceSet",
                    "id": field.get("id", ""),
                    "label": field.get("label", ""),
                    "choices": field.get("choices", [])
                })
                
        return {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.5",
            "body": body,
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "Submit",
                    "data": {
                        "action": "submit"
                    }
                }
            ]
        }
        
    def create_new_card(self):
        """Interactive card creation."""
        print("\n🎨 Create New Adaptive Card\n")
        
        print("Card types:")
        print("  1. Basic - Simple text card")
        print("  2. Approval - Request approval")
        print("  3. Notification - Send notification")
        print("  4. Form - Collect user input")
        
        card_type_choice = input("\nSelect card type (1-4): ").strip()
        
        card_type_map = {
            "1": "basic",
            "2": "approval",
            "3": "notification",
            "4": "form"
        }
        
        card_type = card_type_map.get(card_type_choice, "basic")
        title = input("Card title: ").strip()
        
        # Collect data based on card type
        data = {}
        
        if card_type == "approval":
            data["requestor"] = input("Requestor name: ").strip()
            data["amount"] = input("Amount: ").strip()
            data["description"] = input("Description: ").strip()
            data["id"] = "approval-" + title.lower().replace(" ", "-")
        elif card_type == "notification":
            data["message"] = input("Notification message: ").strip()
            data["url"] = input("Details URL (optional): ").strip()
        elif card_type == "form":
            print("\nForm fields (press Enter with empty field name to finish):")
            fields = []
            while True:
                field_name = input("  Field name: ").strip()
                if not field_name:
                    break
                field_type = input("  Field type (text/choice): ").strip()
                fields.append({
                    "id": field_name.lower().replace(" ", "_"),
                    "label": field_name,
                    "type": field_type,
                    "placeholder": f"Enter {field_name}"
                })
            data["fields"] = fields
        else:
            data["description"] = input("Description: ").strip()
            
        card = self.create_card(card_type, title, data)
        
        output_file = f"{title.lower().replace(' ', '-')}-card.json"
        try:
            with open(output_file, 'w') as f:
                json.dump(card, f, indent=2)
        except OSError as e:
            print(f"❌ Failed to save adaptive card: {e}")
            return
            
        print(f"\n✅ Adaptive card saved to: {output_file}")
        print(f"\nNext steps:")
        print(f"  1. Test at https://adaptivecards.io/designer")
        print(f"  2. Integrate into your Teams bot or app")
        print(f"  3. Customize styling and actions")
        
    def list_templates(self):
        """List available card templates."""
        print("\n📋 Available Card Templates:\n")
        
        templates = [
            {
                "name": "Approval Request",
                "type": "approval",
                "description": "Request approval with details and action buttons"
            },
            {
                "name": "Notification",
                "type": "notification",
                "description": "Send important notifications with optional link"
            },
            {
                "name": "Form Input",
                "type": "form",
                "description": "Collect structured data from users"
            },
            {
                "name": "Status Update",
                "type": "basic",
                "description": "Simple status update card"
            },
            {
                "name": "Task Card",
                "type": "task",
                "description": "Display task information with actions"
            }
        ]
        
        for template in templates:
            print(f"  • {template['name']} ({template['type']})")
            print(f"    {template['description']}\n")
            
    def preview_card(self):
        """Preview a card in the designer."""
        print("\n👁️  Preview Adaptive Card\n")
        
        file_path = input("Enter card file path: ").strip()
        
        try:
            with open(file_path, 'r') as f:
                card = json.load(f)
                
            print("\n✅ Card loaded successfully!")
            print(f"\nTo preview your card:")
            print(f"  1. Go to https://adaptivecards.io/designer")
            print(f"  2. Click 'New Card'")
            print(f"  3. Paste the card JSON from {file_path}")
            print(f"\nCard preview:")
            print(json.dumps(card, indent=2))
            
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON in file: {file_path}")
            
    def interactive_mode(self):
        """Run in interactive mode for adaptive cards."""
        print("Starting Adaptive Cards interactive mode...")
        print("Type 'back' to return to main menu\n")
        
        while True:
            print("\nAdaptive Cards Commands:")
            print("  1. Create new card")
            print("  2. List templates")
            print("  3. Preview card")
            print("  4. Back to main menu")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == "1":
                self.create_new_card()
            elif choice == "2":
                self.list_templates()
            elif choice == "3":
                self.preview_card()
            elif choice == "4" or choice.lower() == "back":
                break
            else:
                print("Invalid option. Please try again.")
