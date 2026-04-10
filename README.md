# mcp-datetime-service
MCP service for date and time

This MCP service provides the current UTC time and date to an AI model. The MCP service is run as an isolated Docker container and is only active during the AI ​​model's runtime, automatically unloading after use. Communication takes place via stdio. The MCP service can be implemented via the AI ​​model's YAML configuration file. An example is shown below.

```json
mcp:
  stdio: |
     {
      "mcpServers": {
        "datetime": {
          "command": "docker",
          "args": [
            "run", "-i", "--rm",
            "openboatprojects/mcp-datetime-service:1.0.1"
          ]
        }
      }
     }
```

