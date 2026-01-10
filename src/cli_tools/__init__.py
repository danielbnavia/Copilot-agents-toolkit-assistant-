"""
CLI Tools module for M365 Agent Toolkit Assistant
Provides command-line utilities for enhanced productivity
"""

from .template_manager import TemplateManager
from .test_framework import TestFramework
from .cicd_helper import CICDHelper

__all__ = ['TemplateManager', 'TestFramework', 'CICDHelper']
