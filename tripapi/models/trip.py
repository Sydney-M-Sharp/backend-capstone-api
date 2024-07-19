from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    
    def __str__(self):
        return self.location