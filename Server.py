# broadcast_server.py
import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            for client in clients:
                await client.send(f"Broadcast: {message}")
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Broadcast server running on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
