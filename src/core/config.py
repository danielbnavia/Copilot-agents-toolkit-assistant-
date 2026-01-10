"""
Configuration management for M365 Assistant
"""

import os
import json
from typing import Dict, Any, Optional


class AssistantConfig:
    """Configuration manager for the assistant."""
    
    DEFAULT_CONFIG = {
        "version": "1.0.0",
        "default_template": "basic-project",
        "output_directory": "./projects",
        "verbose": False,
        "azure": {
            "subscription_id": "",
            "resource_group": "",
            "region": "eastus"
        },
        "m365": {
            "tenant_id": "",
            "app_id": "",
        },
        "templates_path": "./templates",
        "examples_path": "./examples"
    }
    
    def __init__(self, config_file: Optional[str] = None):
        """Initialize configuration.
        
        Args:
            config_file: Path to configuration file (optional)
        """
        self.config_file = config_file or os.path.expanduser("~/.m365-assistant-config.json")
        self.config = self.load_config()
        
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults.
        
        Returns:
            Configuration dictionary
        """
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    # Merge with defaults
                    config = self.DEFAULT_CONFIG.copy()
                    config.update(loaded_config)
                    return config
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
                return self.DEFAULT_CONFIG.copy()
        else:
            return self.DEFAULT_CONFIG.copy()
            
    def save_config(self):
        """Save current configuration to file."""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config file: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value.
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'azure.region')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
                
        return value
        
    def set(self, key: str, value: Any):
        """Set a configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
            
        config[keys[-1]] = value
        self.save_config()
        
    def get_azure_config(self) -> Dict[str, str]:
        """Get Azure configuration.
        
        Returns:
            Azure configuration dictionary
        """
        return self.config.get("azure", {})
        
    def get_m365_config(self) -> Dict[str, str]:
        """Get M365 configuration.
        
        Returns:
            M365 configuration dictionary
        """
        return self.config.get("m365", {})
