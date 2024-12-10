from food.views import *
from django.urls import path

urlpatterns=[
    path('vegetarian/',vegetarian,name='vegetarian'),
    path('nonveg/',nonveg,name='nonveg'),
]