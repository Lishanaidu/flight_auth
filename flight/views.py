from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Flight
from .serializers import FlightSerializer

@api_view(['GET', 'POST'])
def flight_list(request):
    """
    GET: Return a list of all flights.
    POST: Create a new flight.
    """
    if request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlightSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST
    )

