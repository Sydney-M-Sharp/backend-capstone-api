"""View module for handling requests about Invites"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from tripapi.models import Invite
from tripapi.serializers import InviteSerializer

class InviteView(ViewSet):
    """View for handling requests about Invites"""

    def list(self, request):
        """Handle GET requests to list Invites"""
        '''http://localhost:8000/invites?user_id=2'''
        ''' Invite list Response:
        [
            {
                "id": 2,
                "trip": {
                    "id": 1,
                    "location": "Chicago",
                    "start_date": "2024-08-01",
                    "end_date": "2024-08-10"
                },
                "user": {
                    "id": 2,
                    "first_name": "Joe",
                    "last_name": "Shepherd"
                }
            },
            {
                "id": 3,
                "trip": {
                    "id": 2,
                    "location": "New York",
                    "start_date": "2024-09-01",
                    "end_date": "2024-09-05"
                },
                "user": {
                    "id": 2,
                    "first_name": "Joe",
                    "last_name": "Shepherd"
                }
            }
        ]
        '''
        
        user_id = request.query_params.get('user_id', None)

        if user_id is not None:
            invites = Invite.objects.filter(user__id=user_id)
        else:
            invites = Invite.objects.all()
        
        serializer = InviteSerializer(invites, many=True, context={'request': request})
        return Response(serializer.data)
