from rest_framework import serializers
from tripapi.models import Trip

# todo change needed fields
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'location',)