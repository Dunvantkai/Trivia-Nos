# client.py
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        await websocket.send("Hello server!")


        # Wait for a response
        response = await websocket.recv()
        print(f"Received: {response}")

# Run the client
asyncio.run(hello())
