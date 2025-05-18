"""Formatting helpers."""


def format_error(error_type: str, message: str, details: str | None = None) -> str:
    """Format error messages consistently."""
    response = f"Error ({error_type}): {message}"
    if details:
        response += f"\nDetails: {details}"
    return response
