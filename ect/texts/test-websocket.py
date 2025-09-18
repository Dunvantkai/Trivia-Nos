# trivia_server.py
import asyncio
import websockets
import random
import json

# Trivia questions
questions = [
    {"question": "Capital of Italy?", "answer": "Rome"},
    {"question": "Largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"}
]

# Keep track of connected clients
clients = set()

async def send_question(websocket):
    question = random.choice(questions)
    await websocket.send(json.dumps({"type": "question", "question": question["question"]}))
    return question["answer"]

async def handler(websocket):
    clients.add(websocket)
    print("New player joined!")
    try:
        correct_answer = await send_question(websocket)

        async for message in websocket:
            data = json.loads(message)
            if data["type"] == "answer":
                if data["answer"].strip().lower() == correct_answer.lower():
                    await websocket.send(json.dumps({"type": "result", "result": "Correct!"}))
                    correct_answer = await send_question(websocket)  # Send a new question
                else:
                    await websocket.send(json.dumps({"type": "result", "result": "Wrong, try again!"}))
    finally:
        clients.remove(websocket)
        print("Player disconnected.")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Trivia server running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

asyncio.run(main())
