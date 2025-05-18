"""Warpcast MCP Server."""

from .server import mcp
from . import tools  # register tools on import

__all__ = ["mcp"]
__version__ = "1.0.0"
