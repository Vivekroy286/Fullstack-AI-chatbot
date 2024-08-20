
class StreamConsumer:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    async def consume_stream(self, count: int, block: int,  stream_channel):

        response = await self.redis_client.xread(
            streams={stream_channel:  '0-0'}, count=count, block=block)

        return response

    async def delete_message(self, stream_channel, message_id):
        await self.redis_client.xdel(stream_channel, message_id)
        
    from .config import Redis
    class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    

