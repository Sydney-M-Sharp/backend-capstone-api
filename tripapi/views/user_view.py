"""View module for handling requests about Users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from tripapi.serializers import UserSerializer

class UserView(ViewSet):
    """View for handling requests about Users"""

    def list(self, request):
        """Handle GET requests to list Users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)