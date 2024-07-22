"""View module for handling requests about Likes"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from tripapi.models import Like
from tripapi.serializers import LikeSerializer

class LikeView(ViewSet):
    """View for handling requests about Likes"""

    def list(self, request):
        """Handle GET requests to list Likes"""
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True, context={'request': request})
        return Response(serializer.data)