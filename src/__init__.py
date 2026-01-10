# M365 Assistant Package

"""
Microsoft 365 Agent Toolkit Assistant
A comprehensive toolkit for building M365 agents, apps, and workflows
"""

__version__ = "1.0.0"
__author__ = "M365 Assistant Team"

from .core import M365Assistant, AssistantConfig
from .declarative_agents import DeclarativeAgentHelper
from .teams_agents import TeamsAgentHelper
from .adaptive_cards import AdaptiveCardHelper
from .workflows import WorkflowHelper

__all__ = [
    'M365Assistant',
    'AssistantConfig',
    'DeclarativeAgentHelper',
    'TeamsAgentHelper',
    'AdaptiveCardHelper',
    'WorkflowHelper'
]
