from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
# from django.contrib.auth.models import User

class EchoConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.room_name = 'broadcast'
        self.send({
            'type' : 'websocket.accept'
        })
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
        print(f'[{self.channel_name}] - You are connected')
    
    def websocket_receive(self,event):
        print(f'[{self.channel_name}] - receive message - [{event["text"]}]')
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type' : 'websocket.message',
                'text' : event['text']
            }
        )

    def websocket_message(self,event):
        print(f'[{self.channel_name}] - Message sent - [{event["text"]}]')
        self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })
    def websocket_disconnect(self,event):
        print(f'[{self.channel_name}] - Disconnected ')
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)

class EmployeeConsumer(SyncConsumer):
    def websocket_connect(self,event):
        employee_username = self.scope['url_route']['kwargs']['username']

        self.room_name = f'personal_{employee_username}'
        self.send({
            'type' : 'websocket.accept'
        })
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
        print(f'[{self.channel_name}] - {employee_username } You arex connected')
    
    def websocket_receive(self,event):
        print(f'[{self.channel_name}] - receive message - [{event["text"]}]')
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type' : 'websocket.message',
                'text' : event['text']
            }
        )

    def websocket_message(self,event):
        print(f'[{self.channel_name}] - Message sent - [{event["text"]}]')
        self.send({
            'type' : 'websocket.send',
            'text' : event['text']
        })
    def websocket_disconnect(self,event):
        print(f'[{self.channel_name}] - Disconnected ')
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)

