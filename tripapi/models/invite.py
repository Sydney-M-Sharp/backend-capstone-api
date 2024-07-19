from django.db import models
from django.contrib.auth.models import User
from .trip import Trip

class Invite(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='Invite')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Invite')

    def __str__(self):
        return f"{self.user} was invited to {self.trip}"
    
    # https://www.digitalocean.com/community/tutorials/python-str-repr-functions