import asyncio
import websockets
import dotenv
import os
import logging

dotenv.load_dotenv()
PORT = int(os.getenv('PORT', 3950))  # Default to 8765 if PORT is not set
WAIT_TIME = int(os.getenv('WAIT_TIME', 2))  # Default to 1 second if WAIT_TIME is not set

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
)

async def echo(websocket):
    client_ip, client_port = websocket.remote_address
    logging.info(f"Client ({client_ip}:{client_port}) connected")
    try:
        async for message in websocket:
            if message == "tick":
                logging.info(f"Received '{message}' from {client_ip}:{client_port} -- sending 'tock'")
                await asyncio.sleep(WAIT_TIME)
                await websocket.send("tock")
            elif message == "ping":
                logging.info(f"Received '{message}' from {client_ip}:{client_port} -- sending 'pong'")
                await asyncio.sleep(WAIT_TIME)
                await websocket.send("pong")

    except websockets.ConnectionClosedOK:
        logging.info(f"Client ({client_ip}:{client_port}) closed the connection")

    except websockets.ConnectionClosedError:
        logging.warning(f"Client ({client_ip}:{client_port}) disconnected unexpectedly")

async def main():
    print(f"~~~~~~ CS395 WebSocket Server - Ping-Pong, Tick-Tock ~~~~~~\n")
    async with websockets.serve(echo, "0.0.0.0", PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
