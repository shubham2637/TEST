from django.db import models

# Create your models here.
from django.db import models
import os

# Create your models here.

class Doner(models.Model):
    #to store a Image file

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField()
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    image = models.FileField(upload_to='photos/doner')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")



class Collector(models.Model):
    #to store a Image file

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField()
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=16)
    Driving_License = models.CharField(max_length=32)
    Driving_License_image = models.FileField(upload_to='photos/collector/DL')
    image = models.FileField(upload_to='photos/collector')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")


class Acceptor(models.Model):
    #to store a Image file


    name = models.CharField(max_length=64)
    proprietor = models.CharField(max_length=64)
    license_no = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pincode = models.PositiveIntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=16)
    Phone_no = models.IntegerField()
    image = models.FileField(upload_to='photos/acceptor')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")


class vehicle(models.Model):
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    RC_no =models.CharField(max_length=32)
    registration_no = models.CharField(max_length=16)
    last_servicing = models.DateField()
    fuel = ('Petrol','Deisel','CNG','Electric')
    fuel_type = models.CharField(max_length=32)
    insurence_no = models.CharField(max_length=32)
    owner_name = models.CharField(max_length=32)
    Date_purchase = models.DateField()
    owner_number = models.IntegerField()


    def __str__(self):
        return (f"{self.type} {self.name}")


class assigned_vehicle(models.Model):
    vehicle_id = models.ManyToManyField(vehicle,blank=True)
    collector_id = models.ManyToManyField(Collector,blank=True)
    vehicle_assigned_time = models.DateTimeField(auto_now=True)
    vehicle_return_time = models.DateTimeField(auto_now=True)
    duration = models.DurationField()
    destination = models.ManyToManyField(Doner,blank=True)
    distance = models.FloatField()

    def __str__(self):
        return(f"{self.vehicle_id} {self.collector_id}")
