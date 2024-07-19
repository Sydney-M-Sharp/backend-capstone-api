from django.db import models
from django.contrib.auth.models import User
from .trip import Trip

class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    link = models.URLField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"Event at {self.location} on {self.date} at {self.time}"
