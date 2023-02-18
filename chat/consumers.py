from channels.generic.websocket import AsyncJsonWebsocketConsumer 
from authentication.utils.user_authorization import authorization_with_jwt
from urllib.parse import parse_qs
from asgiref.sync import async_to_sync
import json


class GlobalChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):

        token_qs = parse_qs(self.scope["query_string"]).get(b"token", None)

        if token_qs is None:
            await self.close(400)

        jwt_auth_reult = await async_to_sync(authorization_with_jwt)(token_qs[0].decode())
        
        print(jwt_auth_reult)



        
  


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
