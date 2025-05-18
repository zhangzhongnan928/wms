"""Cast management tools."""

from ..utils import format_error, validate_cast_text
from ..api import get_api_client
from ..server import mcp


@mcp.tool()
async def post_cast(text: str, parent_cast_id: str | None = None) -> str:
    """Post a new cast to Warpcast."""
    if not validate_cast_text(text):
        return format_error("InputValidation", "Cast text exceeds 320 character limit")
    try:
        data = await get_api_client().post_cast(text, parent_cast_id)
        url = data.get("url", "")
        return f"Cast posted successfully! View at: {url}"
    except Exception as exc:  # pragma: no cover - network errors mocked in tests
        return format_error("APIError", "Error posting cast", str(exc))


@mcp.tool()
async def get_user_casts(username: str):
    """Retrieve recent casts from a user."""
    try:
        return await get_api_client().get_user_casts(username)
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to get user casts", str(exc))


@mcp.tool()
async def search_casts(query: str):
    """Search casts on Warpcast."""
    try:
        return await get_api_client().search_casts(query)
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to search casts", str(exc))


@mcp.tool()
async def get_trending_casts():
    """Get trending casts."""
    try:
        return await get_api_client().get_trending_casts()
    except Exception as exc:  # pragma: no cover
        return format_error("APIError", "Failed to get trending casts", str(exc))
