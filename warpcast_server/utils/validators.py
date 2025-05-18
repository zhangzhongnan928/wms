"""Validation utilities."""


def validate_cast_text(text: str) -> bool:
    """Return True if text length is within Warpcast limits."""
    return len(text) <= 320
