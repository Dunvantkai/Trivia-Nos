# trivia_client.py
import asyncio
import websockets
import json

async def play_trivia():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            # Receive a question or result
            message = await websocket.recv()
            data = json.loads(message)

            if data["type"] == "question":
                print(f"Question: {data['question']}")
                answer = input("Your answer: ")
                await websocket.send(json.dumps({"type": "answer", "answer": answer}))
            elif data["type"] == "result":
                print(data["result"])

asyncio.run(play_trivia())
