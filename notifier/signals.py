from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

@receiver(post_save, sender = User)
def announce_new_user(sender,instance,created, **kwargs):
    if created:
        print(f"{instance.username} just created!")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "newuser" ,{
                "type" : "new.user.notify", #make function in consumer.py same as name (new_user_notify)
                "event" : "New user",
                "username" : instance.username
            }
        )
    else:
        print(f"{instance.username} was saved!")
    
