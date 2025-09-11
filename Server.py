# broadcast_server.py
import asyncio
import websockets

clients = set()
host = "0.0.0.0"
port = 8765

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            for client in clients:
                await client.send(f"Broadcast: {client} {message}")
                print(client)
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, host, port):
        print(f"Broadcast server running on ws://{host}:{port}")
        await asyncio.Future()

asyncio.run(main())
