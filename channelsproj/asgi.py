import os
from .wsgi import *
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
import django
from notifier.consumer import NoseyConsumer
from channels.auth import AuthMiddlewareStack


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channelsproj.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter([
        path("ws/some_url/",NoseyConsumer.as_asgi()),
    ]))
    # Just HTTP for now. (We can add other protocols later.)
})


# application = get_asgi_application()