import asyncio
import websockets
import dotenv
import os
import sys
import logging

dotenv.load_dotenv()
SERVER_PORT = os.getenv('SERVER_PORT', 3950)  
SERVER_URL = os.getenv('SERVER_URL', "ws://ws-server")
WAIT_TIME = int(os.getenv('WAIT_TIME', 1))  

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
)

global msg

async def test():
    uri = f"{SERVER_URL}:{SERVER_PORT}"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                logging.info(f"Connected to server at {uri}")
                try:
                    await websocket.send(msg)
                    logging.info(f"Sent initial '{msg}'")
                    while True:
                        response = await websocket.recv()
                        logging.info(f"Received from server: {response} -- sending '{msg}' again")
                        await asyncio.sleep(WAIT_TIME)
                        await websocket.send(msg)
                except websockets.ConnectionClosed:
                    logging.warning("The connection was closed")
        except Exception as e:
            logging.warning(f"Server not ready or connection failed: {e}. Retrying in 3 seconds...")
            await asyncio.sleep(3)
                        

if __name__ == "__main__":
    if (len(sys.argv) == 2) and (sys.argv[1] == "tick" or sys.argv[1] == "ping") :
        msg = sys.argv[1]
        asyncio.run(test())
    else:
        logging.error("Invalid argument(s) provided. Please provide a message to send to the server --> 'tick' or 'ping'")
