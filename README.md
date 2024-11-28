# Kitchen's Ping-Tock
## About
Ping-Tock is a basic system with a WebSocket server and 2(or more if added to docker-compose.yml) clients that plays Ping-pong(or Tick-tock) with the server.

When the Tick-tock client sends 'tick' message to the server, server responds with 'tock'. Additionally, ping-pong client sends 'ping' message to the server, server responds with 'pong'. This messaging between the clients and the server keeps going until a client disconnects.

## Prerequisites
- Docker
- Also, Docker containers use some Python packages but they are automatically installed to the containers while building the images. (Listed in ws-server/requirements.txt and client/requirements.txt)

## Run
- With docker compose:
```$ docker compose up #"docker compose down" to stop the containers```

> **Important Note:**
> I did not put docker build and run scripts since there are 3 containers (6 commands for build and run) + there are some network configurations that may need more commands. So, using docker-compose.yml is much more easier.
