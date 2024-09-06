from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from tripapi.models import Trip, Invite
from tripapi.serializers import TripSerializer,InviteSerializer

class TripView(ViewSet):
    """View for handling requests about trips"""

    def list(self, request):
        """Handle GET requests to list trips"""
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True, context={'request': request})
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a Trip and manage its invitations"""
        '''Postman test: 
                {
                "location": "New York",
                "start_date": "2024-09-15",
                "end_date": "2024-09-20",
                "invited_users": [1, 2, 3]
                }
        '''
        try:
            trip = Trip.objects.get(pk=pk)
            trip.user = request.auth.user
            trip.location = request.data['location']
            trip.start_date = request.data['start_date']
            trip.end_date = request.data['end_date']
            trip.save()

            # Handle invites
            invited_users = set(request.data.get('invited_users', []))

            # Get current invites for the trip
            current_invites = Invite.objects.filter(trip=trip)
            current_invited_user_ids = set(invite.user_id for invite in current_invites)

            # Determine which users to add and which to remove
            users_to_add = invited_users - current_invited_user_ids
            users_to_remove = current_invited_user_ids - invited_users

            # Add new invites
            for user_id in users_to_add:
                Invite.objects.create(trip=trip, user_id=user_id)

            # Remove uninvited users
            Invite.objects.filter(trip=trip, user_id__in=users_to_remove).delete()

            # Serialize and return the updated trip and invites
            trip_serializer = TripSerializer(trip, context={'request': request})
            updated_invites = Invite.objects.filter(trip=trip)
            invite_serializer = InviteSerializer(updated_invites, many=True, context={'request': request})

            response_data = {
                'trip': trip_serializer.data,
                'invited_users': invite_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Trip.DoesNotExist:
            return Response({'message': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


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

    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a single Trip"""
        try:
            trip = Trip.objects.get(pk=pk)
            trip_serializer = TripSerializer(trip, context={'request': request})
            
            # Get the invites related to this trip
            invites = Invite.objects.filter(trip=trip)
        
            # Serialize the invites
            invite_serializer = InviteSerializer(invites, many=True, context={'request': request})
        
            # Combine the trip and invite data
            response_data = {
                'trip': trip_serializer.data,
                'invited_users': invite_serializer.data
            }

            return Response(response_data)

        except Exception as ex:
            return HttpResponseServerError(ex)