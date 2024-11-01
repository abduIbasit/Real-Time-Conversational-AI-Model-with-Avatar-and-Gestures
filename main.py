from fastapi import FastAPI, WebSocket

from websocket_routes import conversation_endpoint

app = FastAPI()


# WebSocket route
@app.websocket("/ws/conversation")
async def websocket_route(websocket: WebSocket):
    await conversation_endpoint(websocket)
