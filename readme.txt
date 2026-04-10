#Info für Docker Container
This MCP Service present the date and time 

# In Docker.Desktop im Treminal (Symbol unten rechts)das Verzeichnis mit dem Docker-Files auswählen
# Man muss sich in dem Verzeichnis befinden im dem sich das Dockerfile befindet
cd C:\Norbert_Privat\OpenPlotter\mcp-datetime-service\

# Docker Image mcp-datetime-service erstellen !!!!Achtung!!! Den Punkt am Ende nicht vergessen!!!!
docker build -t mcp-datetime-service:1.0.2 .

# Docker Container mcp-datetime-service container stoppen
docker rm -f mcp-datetime-service

# Docker Container testen, ob Antwort korrekt kommt
# Für Docker.Desktop (PowerShell)
@'
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"manual-test","version":"1.0.2"}}}
{"jsonrpc":"2.0","method":"notifications/initialized"}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"current_date","arguments":{}}}
'@ | docker run -i --rm mcp-datetime-service:1.0.2
# Für Linux Konsole
(
  echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"manual-test","version":"1.0.2"}}}'
  echo '{"jsonrpc":"2.0","method":"notifications/initialized"}'
  echo '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
) | docker run -i --rm mcp-datetime-service:1.0.2

# Lokales Docker Image in Remote Docker Image für Github umladen und Tag setzen
docker tag mcp-datetime-service:1.0.2 openboatprojects/mcp-datetime-service:1.0.2

# Docker Image nach DockerHub hochladen
# In Docker.Desktop die Push-Funktion (Push to Docker Hub) benutzen und Image hochladen
docker push openboatprojects/mcp-datetime-service:1.0.2

