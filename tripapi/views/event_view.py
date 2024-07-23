"""View module for handling requests about Event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tripapi.models import Event,Trip
from tripapi.serializers import EventSerializer

class EventView(ViewSet):
    """View for handling requests about Events"""

    def list(self, request):
        """Handle GET requests to list Events"""
        # Get the trip PK from the request query parameters
        trip_pk = request.query_params.get('trip', None)

        if trip_pk is not None:
            # Filter events based on the trip PK
            events = Event.objects.filter(trip__pk=trip_pk)
        else:
            # If no trip PK is provided, return all events
            events = Event.objects.all()

        serializer = EventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new Event"""

        # Create a Event object and assign it property values
        event = Event()
        event.user = request.auth.user
        event.title = request.data['title']
        event.location = request.data['location']
        event.date = request.data['date']
        event.time = request.data['time']
        event.description = request.data['description']
        event.link = request.data['link']
        event.trip = Trip.objects.get(pk=request.data["trip"])
        event.save()

        try:
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     """Handle GET requests for a single Event"""
    #     trip = get_object_or_404(Trip, pk=pk)
    #     serializer = TripSerializer(trip, context={'request': request})
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     """Handle PUT requests to update a Event"""
    #     trip = get_object_or_404(Trip, pk=pk)
    #     serializer = TripSerializer(trip, data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     """Handle DELETE requests to delete a Event"""
    #     trip = get_object_or_404(Trip, pk=pk)
    #     trip.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
