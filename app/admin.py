from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BusDetails)
admin.site.register(Ticket)
admin.site.register(BusStop)
admin.site.register(Location)