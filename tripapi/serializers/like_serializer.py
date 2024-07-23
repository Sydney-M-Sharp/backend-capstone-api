from rest_framework import serializers
from tripapi.models import Like
from tripapi.serializers import EventSerializer, UserSerializer

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    event = EventSerializer(many=False)
    
    class Meta:
        model = Like
        fields = ('id', 'event', 'user',)