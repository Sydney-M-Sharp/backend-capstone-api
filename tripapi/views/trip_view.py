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

    # def create(self, request):
    #     """Handle POST requests to create a new trip"""
    #     serializer = TripSerializer(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     """Handle GET requests for a single trip"""
    #     trip = get_object_or_404(Trip, pk=pk)
    #     serializer = TripSerializer(trip, context={'request': request})
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     """Handle PUT requests to update a trip"""
    #     trip = get_object_or_404(Trip, pk=pk)
    #     serializer = TripSerializer(trip, data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     """Handle DELETE requests to delete a trip"""
    #     trip = get_object_or_404(Trip, pk=pk)
    #     trip.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
