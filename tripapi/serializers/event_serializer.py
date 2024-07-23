from rest_framework import serializers
from tripapi.models import Event
from tripapi.serializers import TripSerializer, UserSerializer


class EventSerializer(serializers.ModelSerializer):
    trip = TripSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Event
        fields =  ('id', 'title', 'location', 'date', 'time','description','link','trip','user')
