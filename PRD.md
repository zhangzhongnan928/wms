
Warpcast MCP Server - Product Requirements Document
1. Overview
1.1 Purpose
The Warpcast MCP Server is designed to enable AI assistants, specifically Claude, to interact with the Warpcast social platform through the Model Context Protocol (MCP). This server will act as a bridge between Claude and the Warpcast API, allowing users to perform various Warpcast operations through natural language conversations.
1.2 Project Goals

Create a fully functional MCP server that integrates with the Warpcast API
Enable AI assistants to post, read, and search casts
Provide channel discovery and management capabilities
Ensure secure authentication and API token handling
Implement proper error handling and user feedback
Follow MCP best practices for server implementation

1.3 Target Users

Users of Claude Desktop who want to interact with Warpcast
Developers looking to extend Claude's capabilities with Warpcast integration
Warpcast community members seeking AI assistance with platform interactions

2. Technical Specifications
2.1 Technology Stack

Python 3.9+: Primary development language
MCP Python SDK (v1.5.0+): Core framework for implementing the MCP server
FastMCP: Streamlined server implementation from the MCP Python SDK
FastAPI: For any additional HTTP endpoints if needed
HTTP client library: For Warpcast API interactions (httpx recommended)
Environment variable management: For secure API token handling

2.2 Architecture Overview
The server will follow the standard MCP architecture with:

MCP Server Layer: Implements MCP protocol handling
Tools Layer: Defines and implements Warpcast functionality
API Integration Layer: Handles communication with Warpcast API
Authentication Layer: Manages API tokens and authentication
Error Handling Layer: Provides graceful error recovery and user feedback

2.3 Dependencies

mcp>=1.5.0: The official MCP Python SDK
httpx: For making HTTP requests to the Warpcast API
python-dotenv: For loading environment variables
pydantic: For data validation and settings management

3. Functional Requirements
3.1 MCP Server Setup

FastMCP Implementation: Use the FastMCP class from the MCP Python SDK
Transport Configuration: Support both stdio and HTTP/SSE transports
Initialization: Proper server initialization with name and version
Environment Variables: Load API tokens securely from environment variables
Transport Options: Command-line arguments to select transport type

3.2 Tool Implementations
3.2.1 Cast Management Tools

post-cast

Accept cast text (max 320 characters)
Optional parent cast ID for replies
Return success confirmation with cast URL


get-user-casts

Accept username parameter
Retrieve recent casts from specified user
Format and return cast information


search-casts

Accept search query parameter
Perform search via Warpcast API
Return formatted search results


get-trending-casts

Retrieve current trending casts
Format and return trending cast information



3.2.2 Channel Management Tools

get-all-channels

Retrieve list of available channels
Format and return channel information


get-channel

Accept channel name parameter
Retrieve detailed channel information
Return formatted channel data


get-channel-casts

Accept channel name parameter
Retrieve recent casts from specified channel
Format and return channel casts


follow-channel

Accept channel name parameter
Initiate channel follow operation
Return success confirmation


unfollow-channel

Accept channel name parameter
Initiate channel unfollow operation
Return success confirmation



3.3 Warpcast API Integration

API Authentication: Use API token for authentication
Endpoint Implementation: Map MCP tools to corresponding Warpcast API endpoints
Rate Limiting: Respect Warpcast API rate limits
Error Handling: Properly handle API errors and timeouts

3.4 Authentication & Security

API Token Management: Store and use Warpcast API token securely
Input Validation: Validate all user inputs before sending to API
Error Messages: Ensure error messages don't expose sensitive information

4. Implementation Details
4.1 Project Structure
mcp-warpcast-server/
├── README.md               # Project documentation
├── LICENSE                 # MIT License file
├── .gitignore              # Git ignore file
├── .env.example            # Example environment variables
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup file
├── warpcast_server/
│   ├── __init__.py         # Package initialization
│   ├── config.py           # Configuration management
│   ├── server.py           # MCP server implementation
│   ├── api.py              # Warpcast API client
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── cast_tools.py   # Cast-related tools
│   │   └── channel_tools.py # Channel-related tools
│   └── utils/
│       ├── __init__.py
│       ├── formatters.py   # Response formatting utilities
│       └── validators.py   # Input validation utilities
└── tests/                  # Test directory
    ├── __init__.py
    ├── test_server.py      # Server tests
    ├── test_api.py         # API integration tests
    ├── test_cast_tools.py  # Cast tools tests
    └── test_channel_tools.py # Channel tools tests
4.2 MCP Server Implementation
The server implementation should use the FastMCP approach from the MCP Python SDK:
pythonfrom mcp.server.fastmcp import FastMCP

mcp = FastMCP("warpcast-server", version="1.0.0")
4.3 Tool Implementation Pattern
Each tool should follow this implementation pattern:
python@mcp.tool()
async def post_cast(text: str, parent_cast_id: str = None) -> str:
    """Post a new cast to Warpcast.
    
    Args:
        text: The content of the cast (max 320 characters)
        parent_cast_id: Optional ID of a parent cast (for replies)
    
    Returns:
        Confirmation message with cast URL
    """
    # Input validation
    if len(text) > 320:
        return "Error: Cast text exceeds 320 character limit"
    
    # API call
    try:
        response = await api_client.post_cast(text, parent_cast_id)
        cast_url = response.get("url", "")
        return f"Cast posted successfully! View at: {cast_url}"
    except Exception as e:
        return f"Error posting cast: {str(e)}"
4.4 Warpcast API Integration
The Warpcast API client should be implemented as a class with methods corresponding to the required API actions:
pythonclass WarpcastAPI:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.warpcast.com/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}"
        }
        self.client = httpx.AsyncClient(headers=self.headers)
    
    async def post_cast(self, text, parent_cast_id=None):
        """Post a new cast to Warpcast."""
        endpoint = f"{self.base_url}/casts"
        data = {"text": text}
        if parent_cast_id:
            data["parent"] = parent_cast_id
        
        response = await self.client.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()
    
    # Additional API methods for other operations
4.5 Authentication & Configuration
Use environment variables for secure configuration:
pythonimport os
from dotenv import load_dotenv

load_dotenv()

WARPCAST_API_TOKEN = os.getenv("WARPCAST_API_TOKEN")
if not WARPCAST_API_TOKEN:
    raise ValueError("WARPCAST_API_TOKEN environment variable is required")

api_client = WarpcastAPI(WARPCAST_API_TOKEN)
4.6 Server Startup
Implement a main function that supports both stdio and HTTP transports:
pythonimport argparse

def main():
    parser = argparse.ArgumentParser(description="Warpcast MCP Server")
    parser.add_argument("--http", action="store_true", help="Run with HTTP transport")
    parser.add_argument("--port", type=int, default=8000, help="HTTP port (default: 8000)")
    args = parser.parse_args()
    
    if args.http:
        # For HTTP transport
        mcp.run_http(host="0.0.0.0", port=args.port)
    else:
        # For stdio transport
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
5. Testing Requirements
5.1 Unit Tests

Test individual tool functions with mocked API responses
Validate input validation and error handling
Ensure proper formatting of responses

5.2 Integration Tests

Test end-to-end functionality with test Warpcast account
Verify API integration working correctly
Test error cases and edge conditions

5.3 MCP Protocol Compliance

Test compatibility with Claude Desktop
Verify tool discovery and execution
Test both stdio and HTTP transport modes

6. Deployment & Usage
6.1 Package Distribution

Package as a Python module for pip installation
Provide Docker container option for easy deployment
Include clear installation instructions

6.2 Claude Desktop Integration
Configuration for Claude Desktop:
json{
  "mcpServers": {
    "warpcast": {
      "command": "python",
      "args": [
        "-m",
        "warpcast_server"
      ],
      "env": {
        "WARPCAST_API_TOKEN": "YOUR_API_TOKEN"
      }
    }
  }
}
6.3 Alternative HTTP Integration
For HTTP transport deployment:
json{
  "mcpServers": {
    "warpcast": {
      "url": "http://localhost:8000/mcp",
      "env": {
        "WARPCAST_API_TOKEN": "YOUR_API_TOKEN"
      }
    }
  }
}
7. API Reference
7.1 Warpcast API Endpoints Used
The implementation should use these Warpcast API endpoints:

POST /v2/casts: Create a new cast
GET /v2/user-casts: Get casts by user
GET /v2/search-casts: Search for casts
GET /v2/trending-casts: Get trending casts
GET /v2/all-channels: List all channels
GET /v2/channel: Get channel details
GET /v2/channel-casts: Get casts from a channel
POST /v2/channel-action: Follow/unfollow channel

7.2 MCP Tool Schemas
Each tool should have a proper JSON schema defining its parameters, for example:
pythonpost_cast_schema = {
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
            "description": "The content of the cast (max 320 characters)"
        },
        "parent_cast_id": {
            "type": "string",
            "description": "Optional ID of a parent cast (for replies)"
        }
    },
    "required": ["text"]
}
8. Error Handling
8.1 Error Categories
The server should handle these error categories:

Input Validation Errors: Invalid parameters or constraints
API Errors: Errors from Warpcast API
Authentication Errors: Missing or invalid API token
Network Errors: Connection issues with Warpcast API
Rate Limiting: Handling API rate limits

8.2 Error Response Format
All errors should be formatted consistently:
pythondef format_error(error_type, message, details=None):
    """Format error messages consistently."""
    response = f"Error ({error_type}): {message}"
    if details:
        response += f"\nDetails: {details}"
    return response
9. Documentation
9.1 README Requirements
The README should include:

Project overview and purpose
Features list
Installation instructions
Usage examples
Available tools description
Configuration guide for Claude Desktop
Troubleshooting tips
License information

9.2 Code Documentation

All functions should have proper docstrings
Include type hints for function parameters and return values
Document expected API responses and error handling
Add comments for complex logic
