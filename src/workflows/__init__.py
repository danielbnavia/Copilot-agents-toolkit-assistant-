"""Workflows helper module"""

import json
import os
from typing import Dict, Any, List, Optional


class WorkflowHelper:
    """Helper class for creating and managing workflows."""
    
    def __init__(self, verbose: bool = False):
        """Initialize the workflow helper.
        
        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        
    def create_workflow(self, name: str, triggers: List[str], actions: List[str]) -> Dict[str, Any]:
        """Create a new workflow configuration.
        
        Args:
            name: Workflow name
            triggers: List of trigger types
            actions: List of action types
            
        Returns:
            Workflow configuration dictionary
        """
        workflow = {
            "name": name,
            "description": f"Automated workflow: {name}",
            "triggers": self._build_triggers(triggers),
            "actions": self._build_actions(actions),
            "enabled": True
        }
        
        return workflow
        
    def _build_triggers(self, trigger_types: List[str]) -> List[Dict[str, Any]]:
        """Build trigger configurations.
        
        Args:
            trigger_types: List of trigger type identifiers
            
        Returns:
            List of trigger configurations
        """
        triggers = []
        
        trigger_map = {
            "document_uploaded": {
                "type": "OnFileCreated",
                "site": "SharePoint",
                "library": "Documents"
            },
            "email_received": {
                "type": "OnEmailReceived",
                "folder": "Inbox"
            },
            "schedule": {
                "type": "Recurrence",
                "frequency": "Day",
                "interval": 1
            },
            "form_submitted": {
                "type": "OnFormSubmit",
                "formId": "FORM_ID"
            }
        }
        
        for trigger_type in trigger_types:
            if trigger_type in trigger_map:
                triggers.append(trigger_map[trigger_type])
                
        return triggers
        
    def _build_actions(self, action_types: List[str]) -> List[Dict[str, Any]]:
        """Build action configurations.
        
        Args:
            action_types: List of action type identifiers
            
        Returns:
            List of action configurations
        """
        actions = []
        
        action_map = {
            "send_notification": {
                "type": "SendEmail",
                "to": "user@example.com",
                "subject": "Notification",
                "body": "Action completed"
            },
            "request_approval": {
                "type": "StartApproval",
                "approvers": ["manager@example.com"],
                "title": "Approval Required"
            },
            "create_task": {
                "type": "CreateTask",
                "taskList": "Tasks",
                "title": "New Task"
            },
            "update_database": {
                "type": "UpdateRow",
                "table": "Data",
                "columns": {}
            },
            "send_teams_message": {
                "type": "PostToChannel",
                "channel": "General",
                "message": "Update from workflow"
            }
        }
        
        for action_type in action_types:
            if action_type in action_map:
                actions.append(action_map[action_type])
                
        return actions
        
    def create_new_workflow(self):
        """Interactive workflow creation."""
        print("\n🔄 Create New Workflow\n")
        
        name = input("Workflow name: ").strip()
        
        print("\nAvailable triggers:")
        print("  1. document_uploaded - When a file is uploaded")
        print("  2. email_received - When an email arrives")
        print("  3. schedule - On a recurring schedule")
        print("  4. form_submitted - When a form is submitted")
        
        trigger_input = input("\nSelect triggers (comma-separated, e.g., 1,3): ").strip()
        
        trigger_map = {
            "1": "document_uploaded",
            "2": "email_received",
            "3": "schedule",
            "4": "form_submitted"
        }
        
        triggers = [trigger_map[t.strip()] for t in trigger_input.split(",") if t.strip() in trigger_map]
        
        print("\nAvailable actions:")
        print("  1. send_notification - Send email notification")
        print("  2. request_approval - Request approval")
        print("  3. create_task - Create a task")
        print("  4. update_database - Update database record")
        print("  5. send_teams_message - Post to Teams channel")
        
        action_input = input("\nSelect actions (comma-separated, e.g., 1,2): ").strip()
        
        action_map = {
            "1": "send_notification",
            "2": "request_approval",
            "3": "create_task",
            "4": "update_database",
            "5": "send_teams_message"
        }
        
        actions = [action_map[a.strip()] for a in action_input.split(",") if a.strip() in action_map]
        
        workflow = self.create_workflow(name, triggers, actions)
        
        # Create workflow project
        workflow_dir = name.lower().replace(' ', '-') + "-workflow"
        os.makedirs(workflow_dir, exist_ok=True)
        
        # Save workflow configuration
        config_path = os.path.join(workflow_dir, "workflow.json")
        try:
            with open(config_path, 'w') as f:
                json.dump(workflow, f, indent=2)
        except OSError as e:
            print(f"❌ Failed to save workflow configuration: {e}")
            return
            
        # Create README
        self._create_workflow_readme(workflow_dir, name)
        
        print(f"\n✅ Workflow created successfully!")
        print(f"📁 Location: {workflow_dir}/")
        print(f"\nFiles created:")
        print(f"  • workflow.json - Workflow configuration")
        print(f"  • README.md - Setup instructions")
        print(f"\nNext steps:")
        print(f"  1. cd {workflow_dir}")
        print(f"  2. Review and customize workflow.json")
        print(f"  3. Import into Power Automate")
        print(f"  4. Test and deploy")
        
    def _create_workflow_readme(self, workflow_dir: str, name: str):
        """Create README for workflow project.
        
        Args:
            workflow_dir: Workflow directory
            name: Workflow name
        """
        readme_content = f"""# {name} Workflow

Automated workflow for {name}.

## Setup

1. Open Power Automate (https://flow.microsoft.com)
2. Create a new flow
3. Import the configuration from `workflow.json`
4. Configure connections and settings
5. Test the workflow
6. Enable and monitor

## Configuration

Edit `workflow.json` to customize:
- Triggers: When the workflow runs
- Actions: What the workflow does
- Conditions: Flow control logic

## Testing

1. Use Power Automate's test feature
2. Trigger the workflow manually
3. Check run history for results
4. Debug any errors

## Deployment

1. Test thoroughly in development
2. Export the workflow
3. Import to production environment
4. Monitor performance

## Support

For issues or questions, refer to the Power Automate documentation:
https://docs.microsoft.com/en-us/power-automate/
"""
        
        try:
            with open(os.path.join(workflow_dir, "README.md"), 'w') as f:
                f.write(readme_content)
        except OSError as e:
            # README is non-critical; log the error but do not abort the operation
            print(f"⚠️  Failed to write README.md: {e}")
            
    def add_action(self):
        """Add an action to existing workflow."""
        print("\n➕ Add Action to Workflow\n")
        print("This feature is coming soon!")
        
    def test_workflow(self):
        """Test workflow configuration."""
        print("\n🧪 Test Workflow\n")
        
        file_path = input("Enter workflow config file path: ").strip()
        
        try:
            with open(file_path, 'r') as f:
                workflow = json.load(f)
                
            print("\n✅ Workflow configuration loaded!")
            print(f"\nWorkflow: {workflow.get('name', 'Unnamed')}")
            print(f"Triggers: {len(workflow.get('triggers', []))}")
            print(f"Actions: {len(workflow.get('actions', []))}")
            print(f"Status: {'Enabled' if workflow.get('enabled', False) else 'Disabled'}")
            
            print("\nTo test in Power Automate:")
            print("  1. Import this configuration")
            print("  2. Use the 'Test' button")
            print("  3. Trigger manually or wait for trigger event")
            print("  4. Review run history")
            
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON in file: {file_path}")
            
    def interactive_mode(self):
        """Run in interactive mode for workflows."""
        print("Starting Workflows interactive mode...")
        print("Type 'back' to return to main menu\n")
        
        while True:
            print("\nWorkflow Commands:")
            print("  1. Create new workflow")
            print("  2. Add action to workflow")
            print("  3. Test workflow")
            print("  4. Back to main menu")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == "1":
                self.create_new_workflow()
            elif choice == "2":
                self.add_action()
            elif choice == "3":
                self.test_workflow()
            elif choice == "4" or choice.lower() == "back":
                break
            else:
                print("Invalid option. Please try again.")
