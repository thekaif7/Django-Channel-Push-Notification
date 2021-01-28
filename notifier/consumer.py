from channels.consumer import AsyncConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio



class NoseyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        event = {
            "text": "Hello Miya"
        }
        await self.send(json.dumps({
            'message': event
        }))
        await self.channel_layer.group_add("gossip",self.channel_name)
        print(f"Added {self.channel_name} channel to gossip ")
    
    async def disconnect(self,close_code):
    # await self.accept()
        print("disconnect")
        await self.channel_layer.group_discard("gossip",self.channel_name)
        print(f"Remove {self.channel_name} channel to gossip ")

    async def user_gossip(self,event):
        event = json.loads(event)['gossip']
        print("Hello Miya")

        await self.send(event)
        print(f"Got messsage {event} at {self.channel_name}")

            
            