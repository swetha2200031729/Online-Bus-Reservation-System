from django.db import models

from django.contrib.auth.models import User
#password :admin admin: admin
# Create your models here.
class BusDetails(models.Model):
    bus_name = models.CharField(max_length = 40)
    bus_number = models.CharField(max_length =  30)
    avaliable_date = models.DateField()
    ticket_pricing = models.FloatField()

    def __str__(self):
        return f'{self.bus_name} {self.avaliable_date}'
    class Meta:
        unique_together = ('bus_number','avaliable_date')
class Ticket(models.Model):
    user = models.ForeignKey(to = User,on_delete = models.CASCADE)
    bus_stop = models.ForeignKey(to = 'BusStop',on_delete = models.CASCADE)
    no_of_seats = models.IntegerField()
    @property
    def pricing(self):
        return self.bus_stop.bus_details.ticket_pricing  * self.no_of_seats


class BusStop(models.Model):
    stop_name = models.CharField(max_length = 50)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    bus_details = models.ForeignKey(to = 'BusDetails',on_delete = models.CASCADE)
    class Meta:
        unique_together = ('stop_name','bus_details')
    def __str__(self):
        return f'{self.stop_name} {self.bus_details}'
class Location(models.Model):
    name = models.CharField(max_length =100)
    img = models.ImageField()
    @property
    def imageurl(self):
        return self.img.url