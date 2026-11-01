from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_name = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.flight_name