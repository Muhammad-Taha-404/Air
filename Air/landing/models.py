# models.py
from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    
    airline = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight_class = models.CharField(max_length=20)
    seats_available = models.IntegerField()


class flight1(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    image = models.CharField(max_length=200)
    airline = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight_class = models.CharField(max_length=20)
    seats_available = models.IntegerField()


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    airline=models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100) 
    flight_class = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.IntegerField()
    
class booking1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    airline=models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100) 
    flight_class = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.IntegerField()
    image = models.CharField(max_length=200)
    
    
class booking2(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    airline=models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100) 
    flight_class = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.IntegerField()
    image = models.CharField(max_length=200)
    
    
    
