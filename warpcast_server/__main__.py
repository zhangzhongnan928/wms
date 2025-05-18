"""Entry point for the Warpcast MCP server."""

from __future__ import annotations

import argparse
import os

from dotenv import load_dotenv

from .api import init_api_client
from .server import mcp
from . import tools  # noqa: F401 - ensure tools registered


def main() -> None:
    parser = argparse.ArgumentParser(description="Warpcast MCP Server")
    parser.add_argument("--http", action="store_true", help="Run with HTTP transport")
    parser.add_argument("--port", type=int, default=8000, help="HTTP port")
    args = parser.parse_args()

    load_dotenv()
    token = os.getenv("WARPCAST_API_TOKEN")
    if not token:
        raise ValueError("WARPCAST_API_TOKEN environment variable is required")
    init_api_client(token)

    if args.http:
        mcp.run_http(host="0.0.0.0", port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":  # pragma: no cover - manual start
    main()
