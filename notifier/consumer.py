from channels.consumer import AsyncConsumer
from time import sleep
import asyncio

class EchoConsumer(AsyncConsumer):
    async def websocket_connect(self, message):
        await self.send({
            "type": "websocket.accept",
            "text": "connected"
        })
        print(message)

    async def websocket_receive(self, message):
        # await asyncio.sleep(1)
        for i in ["kaif","Mohammad","Lucky"]:
            await self.send({
                "type": "websocket.send",
                "text": i,
            })
            await asyncio.sleep(1)
            