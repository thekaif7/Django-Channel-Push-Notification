from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumer import NoseyConsumer
from channels.auth import AuthMiddlewareStack

# application = ProtocolTypeRouter({
#     # "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(URLRouter([
#         path("ws/some_url/",NoseyConsumer.as_asgi()),
#     ]))
#     # Just HTTP for now. (We can add other protocols later.)
# })
