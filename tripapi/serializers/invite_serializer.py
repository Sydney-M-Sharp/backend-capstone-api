from rest_framework import serializers
from tripapi.models import Invite
from tripapi.serializers import TripSerializer, UserSerializer
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ( 'first_name', 'last_name' )

class InviteSerializer(serializers.ModelSerializer):
    trip = TripSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Invite
        fields = ('id', 'trip', 'user',)
        