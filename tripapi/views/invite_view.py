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
        invites = Invite.objects.all()
        serializer = InviteSerializer(invites, many=True, context={'request': request})
        return Response(serializer.data)
