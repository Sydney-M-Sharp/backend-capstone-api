from django.db import models
from django.contrib.auth.models import User
from .event import Event

class Like(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user} likes {self.event} event"