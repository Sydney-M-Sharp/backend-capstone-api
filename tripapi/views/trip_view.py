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

    