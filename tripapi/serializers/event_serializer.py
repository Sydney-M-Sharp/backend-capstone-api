from rest_framework import serializers
from tripapi.models import Event, Invite, Like
from tripapi.serializers import TripSerializer
from django.contrib.auth.models import User



# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields =  "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name' )


class InviteSerializer(serializers.ModelSerializer):
    trip = TripSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Invite
        fields = ('id', 'trip', 'user',)

class EventSerializer(serializers.ModelSerializer):
    trip = TripSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Event
        fields =  ('id', 'title', 'location', 'date', 'time','description','link','trip',"user")

# class LikeSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False)
#     event = EventSerializer(many=False)
    
#     class Meta:
#         model = Like
#         fields = ('event', 'user')