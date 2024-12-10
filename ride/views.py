from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bike(request):
    return HttpResponse('<h1> I like to ride royal-enfield bike </h1>')