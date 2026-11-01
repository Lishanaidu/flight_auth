from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ['id', 'flight_name', 'flight_number', 'source', 'destination', 'price']