from django.db import models
from django.contrib.auth.models import User
from .trip import Trip

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    # remember the time is 24 hours
    description = models.TextField()
    link = models.URLField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='events')
    
#     def formatted_time(self):
#         return self.time.strftime("%I:%M %p")  # Format time as am/pm

# # Usage in view or template:
# event = Event.objects.get(pk=1)
# print(event.formatted_time())  # Output: 11:00 AM

    def __str__(self):
        return f"Event at {self.location} on {self.date} at {self.time}"