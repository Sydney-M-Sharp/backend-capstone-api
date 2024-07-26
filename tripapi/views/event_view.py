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
        '''http://localhost:8000/events?trip_id=2'''
        ''' Event list Response:
        [
            {
                "id": 9,
                "title": "dinner again",
                "location": "that food place",
                "date": "2024-08-04",
                "time": "10:00:00",
                "description": "it proly gonna be fun",
                "link": "https://deeslounge.com/",
                "trip": {
                    "id": 2,
                    "location": "New York",
                    "start_date": "2024-09-01",
                    "end_date": "2024-09-05"
                },
                "user": {
                    "id": 1,
                    "first_name": "Sydney",
                    "last_name": "Sharp"
                }
            }
        ]
        '''
        
        # Get the trip PK from the request query parameters
        trip_pk = request.query_params.get('trip_id', None)  # 'trip_id' to match the query parameter
        
        if trip_pk is not None:
            # Filter events based on the trip PK
            events = Event.objects.filter(trip__pk=trip_pk)
        else:
            # If no trip PK is provided, return all events
            events = Event.objects.all()

        serializer = EventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)

        """" Event retrieve Response:
        {
            "id": 3,
            "title": "dinner",
            "location": "that food place",
            "date": "2024-08-04",
            "time": "10:00:00",
            "description": "it proly gonna be fun",
            "link": "https://deeslounge.com/",
            "trip": {
                "id": 1,
                "location": "Chicago"
            },
            "user": {
                "id": 1,
                "first_name": "Sydney",
                "last_name": "Sharp"
            }
        }
        """
        try:
            events = Event.objects.get(pk=pk)
            serializer = EventSerializer(events, context={'request': request})

            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)
    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a single Event"""
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

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
        
    def update(self, request, pk=None):
        """Handle PUT requests to update an Event"""
        
        event = Event.objects.get(pk=pk)
        event.user = request.auth.user
        event.title = request.data['title']
        event.location = request.data['location']
        event.date = request.data['date']
        event.time = request.data['time']
        event.description = request.data['description']
        event.link = request.data['link']
        # event.trip = Trip.objects.get(pk=request.data["trip"])
        event.save()
        
        serializer = EventSerializer(event, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete a Event"""
        try:
            product = Event.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

