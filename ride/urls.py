from ride.views import *
from django.urls import path

urlpatterns=[
    path('bike/',bike,name='bike'),
]