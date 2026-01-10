"""Utility functions for M365 Assistant"""

import os
import json
from typing import Any, Dict, Optional


def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Read and parse a JSON file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Parsed JSON data or None if error
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


def write_json_file(file_path: str, data: Dict[str, Any], indent: int = 2) -> bool:
    """Write data to a JSON file.
    
    Args:
        file_path: Path to JSON file
        data: Data to write
        indent: Indentation level
        
    Returns:
        True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        return False


def validate_json_schema(data: Dict[str, Any], required_fields: list) -> tuple[bool, list]:
    """Validate JSON data against required fields.
    
    Args:
        data: JSON data to validate
        required_fields: List of required field names
        
    Returns:
        Tuple of (is_valid, missing_fields)
    """
    missing = [field for field in required_fields if field not in data]
    return len(missing) == 0, missing


def format_error(error_msg: str) -> str:
    """Format an error message for display.
    
    Args:
        error_msg: Error message
        
    Returns:
        Formatted error message
    """
    return f"❌ Error: {error_msg}"


def format_success(success_msg: str) -> str:
    """Format a success message for display.
    
    Args:
        success_msg: Success message
        
    Returns:
        Formatted success message
    """
    return f"✅ {success_msg}"


def format_info(info_msg: str) -> str:
    """Format an info message for display.
    
    Args:
        info_msg: Info message
        
    Returns:
        Formatted info message
    """
    return f"ℹ️  {info_msg}"
