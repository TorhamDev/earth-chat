from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class GlobalChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            "global_chat",
            self.channel_name,
        )

        # Send message to all
        await self.channel_layer.group_send(
            "global_chat",
            {
                "type": "chat.message",
                "message": "New User Connected!"
            },

        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        message = content["message"]

        # Send message to all
        await self.channel_layer.group_send(
            "global_chat",
            {
                "type": "chat_message",
                "message": message
            },

        )

    async def disconnect(self, code=None):
        return await super().disconnect(code)

    async def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
