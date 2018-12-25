from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.db.models import Sum
from clickerRoot.models import User
from django.db import connection
import json


class GlobalCounterConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connection successful: ", event)
        await self.send({
            "type": "websocket.accept",
        })

        self.chat_room = "123"

        print("add to group")
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name,
        )

        print('channel name: ', self.channel_name)

    async def websocket_receive(self, event):
        print('from js: ', event)
        context = json.loads(event.get('text'))
        user = context.get('user')
        count = context.get('counter')
        await self.change_count(json.loads(user))
        global_c = context.get('global_count')

        await self.channel_layer.group_send(
            self.chat_room,
            {
                "type": "chat_message",
                "text": json.dumps(global_c),
            }
        )

    async def chat_message(self, event):
        print("message, ", event)
        await self.send({
            "type": "websocket.send",
            "text": event['text'],
        })

    @database_sync_to_async
    def change_count(self, user):
        user = User.parse_string_to_user(user)
        user.counter += 1
        connection.cursor().execute("select public.incrementor_func('{}',{})".format(user.pk, user.counter))


    @database_sync_to_async
    def get_global_count_from_database(self):
        return User.objects.all().aggregate(Sum('counter'))
