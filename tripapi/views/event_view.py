"""View module for handling requests about Event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from tripapi.models import Event
from tripapi.serializers import EventSerializer

class EventView(ViewSet):
    """View for handling requests about Events"""

    def list(self, request):
        """Handle GET requests to list Events"""
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)