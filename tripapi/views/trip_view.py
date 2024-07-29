"""View module for handling requests about Trips"""
import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from tripapi.models import Trip
from tripapi.serializers import TripSerializer



class TripView(ViewSet):
    """View for handling requests about trips"""

    def list(self, request):
        """Handle GET requests to list trips"""
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new Event"""

        # Create a Trip object and assign it property values
        event = Trip()
        event.user = request.auth.user
        event.location = request.data['location']
        event.start_date = request.data['start_date']
        event.end_date = request.data['end_date']
        event.save()

        try:
            serializer = TripSerializer(event, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)