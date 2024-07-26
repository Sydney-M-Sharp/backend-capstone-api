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
        user_id = request.query_params.get('user_id', None)
        
        if user_id is not None:
            invites = Invite.objects.filter(user__id=user_id)
        else:
            invites = Invite.objects.all()
        
        serializer = InviteSerializer(invites, many=True, context={'request': request})
        return Response(serializer.data)
