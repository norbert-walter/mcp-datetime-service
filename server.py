#!/usr/bin/env python3
import asyncio
from datetime import datetime
from mcp.server import Server
from mcp.types import Tool, ToolResponse

server = Server("multi-time-service")

@server.tool(
    Tool(
        name="current_datetime",
        description="Gibt das aktuelle Datum und die Uhrzeit zurück.",
        input_schema={"type": "object", "properties": {}}
    )
)
async def current_datetime(_input):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return ToolResponse(content=f"Aktuelle Zeit: {now}")

@server.tool(
    Tool(
        name="current_date",
        description="Gibt das aktuelle Datum zurück.",
        input_schema={"type": "object", "properties": {}}
    )
)
async def current_date(_input):
    today = datetime.now().strftime("%Y-%m-%d")
    return ToolResponse(content=f"Heutiges Datum: {today}")

@server.tool(
    Tool(
        name="current_time",
        description="Gibt die aktuelle Uhrzeit zurück.",
        input_schema={"type": "object", "properties": {}}
    )
)
async def current_time(_input):
    time = datetime.now().strftime("%H:%M:%S")
    return ToolResponse(content=f"Aktuelle Uhrzeit: {time}")

async def main():
    await server.run_stdio()

if __name__ == "__main__":
    asyncio.run(main())

