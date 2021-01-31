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
        await self.channel_layer.group_add("newuser",self.channel_name)
        print(f"Added {self.channel_name} channel to newuser")
    
    async def disconnect(self,close_code):
    # await self.accept()
        print("disconnect")
        await self.channel_layer.group_discard("newuser",self.channel_name)
        print(f"Remove {self.channel_name} channel to newuser ")

    async def new_user_notify(self,event):
        # print("Hello Miya")
        print(event)

        await self.send(json.dumps(event))
        print(f"Got messsage {event} at {self.channel_name}")

            
            