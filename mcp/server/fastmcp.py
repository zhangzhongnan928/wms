class FastMCP:
    """Minimal stub for FastMCP used for testing."""

    def __init__(self, name: str, version: str = "0.0.0"):
        self.name = name
        self.version = version
        self.tools = {}

    def tool(self, schema=None):
        """Decorator to register a tool function."""
        def decorator(func):
            self.tools[func.__name__] = func
            func.__mcp_schema__ = schema
            return func
        return decorator

    def run(self, transport: str = "stdio") -> None:
        print(f"FastMCP running {self.name} ({self.version}) via {transport}")

    def run_http(self, host: str = "0.0.0.0", port: int = 8000) -> None:
        print(f"FastMCP HTTP running on {host}:{port}")
