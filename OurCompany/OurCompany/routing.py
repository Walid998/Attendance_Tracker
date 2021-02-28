from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path 
from channels.auth import AuthMiddlewareStack
from Accounts.consumers import EchoConsumer,EmployeeConsumer
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
            URLRouter([
            path('ws/<str:username>/',EmployeeConsumer),
            path('ws/',EchoConsumer)
        ])
    )
})