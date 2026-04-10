#!/usr/bin/env python3
from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("multi-time-service")

@mcp.tool()
def current_datetime() -> str:
    """Returns the current UTC system date and time as a formatted string."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {now}"

@mcp.tool()
def current_date() -> str:
    """Returns the current UTC system date as a formatted string."""
    today = datetime.now().strftime("%Y-%m-%d")
    return f"Current date: {today}"

@mcp.tool()
def current_time() -> str:
    """Returns the current UTC system time as a formatted string."""
    current = datetime.now().strftime("%H:%M:%S")
    return f"Current time: {current}"

if __name__ == "__main__":
    mcp.run()