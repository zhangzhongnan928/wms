# Warpcast MCP Server

A Model Context Protocol (MCP) server for Warpcast integration that allows you to use Claude to interact with your Warpcast account.  
The implementation uses the official  [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) and[ Warpcast API](https://docs.farcaster.xyz/reference/warpcast/api).

## Features

- Post casts to your Warpcast account
- Read casts from Warpcast
- Search casts by keyword or hashtag
- Browse and interact with channels
- Follow/unfollow channels
- Get trending casts


## Usage

`mcp-warpcast-server` is usually launched automatically by Claude Desktop's MCP client when the Warpcast tools are configured.
After the server starts you can ask Claude to:

- "Post a cast about [topic]"
- "Read the latest casts from [username]"
- "Search for casts about [topic]"
- "Show me trending casts on Warpcast"
- "Show me popular channels on Warpcast"
- "Get casts from the [channel] channel"
- "Follow the [channel] channel for me"

## Available Tools

This MCP server provides several tools that Claude can use:

1. **post-cast**: Create a new post on Warpcast (max 320 characters)
2. **get-user-casts**: Retrieve recent casts from a specific user
3. **search-casts**: Search for casts by keyword or phrase
4. **get-trending-casts**: Get the currently trending casts on Warpcast
5. **get-all-channels**: List available channels on Warpcast
6. **get-channel**: Get information about a specific channel
7. **get-channel-casts**: Get casts from a specific channel
8. **follow-channel**: Follow a channel
9. **unfollow-channel**: Unfollow a channel


## Setup



## Using with Claude Desktop

Follow these steps to access the Warpcast tools from Claude's desktop application:

1. Start the server (or let Claude launch it) using the setup instructions above.
2. Open your Claude configuration file:
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the Warpcast server under the `mcpServers` key. Replace the path with the location of this repository:

```json
{
  "mcpServers": {
    "warpcast": {
      "command": "",
      "args": [
        "",
        "/ABSOLUTE/PATH/TO/mcp-warpcast-server",
        "",
      ],
      "url": "http://localhost:8000/mcp",
      "env": {
        "WARPCAST_API_TOKEN": "YOUR_API_TOKEN"
      }
    }
  }
}
```

4. Save the file and restart Claude Desktop. You should now see a hammer icon in the chat input that lets you use the Warpcast tools.

## Running Tests



## MCP Compatibility

This server uses the official MCP Python SDK and is fully compatible with the [Model Context Protocol](https://modelcontextprotocol.org/). Clients can connect to the `/mcp` endpoint provided by FastMCP and interact with the tools defined here.

## License

This project is licensed under the [MIT License](LICENSE).
