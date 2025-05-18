# Warpcast MCP Server

A Model Context Protocol (MCP) server for Warpcast integration that allows you to use Claude to interact with your Warpcast account. The implementation follows the requirements in `PRD.md` and uses a small stub of the MCP Python SDK and Warpcast API.

## Features

- Post casts to your Warpcast account
- Read casts from Warpcast
- Search casts by keyword or hashtag
- Browse and interact with channels
- Follow or unfollow channels
- Get trending casts

## Usage

`mcp-warpcast-server` is usually launched automatically by Claude Desktop's MCP client when the Warpcast tools are configured. After the server starts you can ask Claude to:

- "Post a cast about [topic]"
- "Read the latest casts from [username]"
- "Search for casts about [topic]"
- "Show me trending casts on Warpcast"
- "Show me popular channels on Warpcast"
- "Get casts from the [channel] channel"
- "Follow the [channel] channel for me"

## Available Tools

1. **post-cast** – Create a new post on Warpcast (max 320 characters)
2. **get-user-casts** – Retrieve recent casts from a specific user
3. **search-casts** – Search for casts by keyword or phrase
4. **get-trending-casts** – Get the currently trending casts on Warpcast
5. **get-all-channels** – List available channels on Warpcast
6. **get-channel** – Get information about a specific channel
7. **get-channel-casts** – Get casts from a specific channel
8. **follow-channel** – Follow a channel
9. **unfollow-channel** – Unfollow a channel

## Setup

1. Ensure Python 3.9+ is installed.
2. Clone this repository and install the dependencies listed in `requirements.txt` (for this environment the MCP and httpx modules are stubbed).
3. Create a `.env` file with your Warpcast API token:

```env
WARPCAST_API_TOKEN=YOUR_API_TOKEN
```

4. Start the server using:

```bash
python -m warpcast_server        # stdio transport
python -m warpcast_server --http # HTTP transport on port 8000
```

## Using with Claude Desktop

Add the server to your Claude configuration file. Example for HTTP transport:

```json
{
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

```

Restart Claude Desktop and the Warpcast tools will be available.

## Running Tests

Run the unit tests with:

```bash
python -m unittest discover tests
```

## MCP Compatibility

This server follows the Model Context Protocol. The real MCP SDK is not included here, so the provided implementation is a simplified stub suitable for demonstration and testing in an offline environment.

## License

This project is licensed under the MIT License.
