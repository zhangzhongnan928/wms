"""Channel management tools."""

from ..utils import format_error
from ..api import get_api_client
from ..server import mcp


@mcp.tool()
async def get_all_channels():
    """Retrieve all channels."""
    try:
        return await get_api_client().get_all_channels()
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to get channels", str(exc))


@mcp.tool()
async def get_channel(name: str):
    """Get details for a channel."""
    try:
        return await get_api_client().get_channel(name)
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to get channel", str(exc))


@mcp.tool()
async def get_channel_casts(name: str):
    """Get casts from a channel."""
    try:
        return await get_api_client().get_channel_casts(name)
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to get channel casts", str(exc))


@mcp.tool()
async def follow_channel(name: str) -> str:
    """Follow a channel."""
    try:
        await get_api_client().follow_channel(name, True)
        return f"Now following channel {name}"
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to follow channel", str(exc))


@mcp.tool()
async def unfollow_channel(name: str) -> str:
    """Unfollow a channel."""
    try:
        await get_api_client().follow_channel(name, False)
        return f"Unfollowed channel {name}"
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to unfollow channel", str(exc))
