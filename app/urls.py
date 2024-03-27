from django.urls import *
from .views import *
urlpatterns = [
    path('home',home,name = 'home'),
    path('signup',signup,name ='signup'),
    path('busdetails',bus_details,name = 'bus_details'),
    path('ticketform/<int:bus_id>',ticket_form,name = 'ticket_form'),
    path('aboutus',aboutus,name = 'aboutus'),

]