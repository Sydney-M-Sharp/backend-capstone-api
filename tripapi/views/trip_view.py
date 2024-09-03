from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from tripapi.models import Trip, Invite
from tripapi.serializers import TripSerializer

class TripView(ViewSet):
    """View for handling requests about trips"""

    def list(self, request):
        """Handle GET requests to list trips"""
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new Trip with invitations"""

        # Create a Trip object and assign it property values
        trip = Trip()
        trip.user = request.auth.user
        trip.location = request.data['location']
        trip.start_date = request.data['start_date']
        trip.end_date = request.data['end_date']
        trip.save()

        # Handle invites
        invited_users = request.data.get('invited_users', [])
        for user_id in invited_users:
            Invite.objects.create(trip=trip, user_id=user_id)

        try:
            serializer = TripSerializer(trip, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete a Trip"""
        try:
            product = Trip.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
