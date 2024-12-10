from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vegetarian(request):
    return HttpResponse('<h1> I like vegetarian food like mutton briyani.....')

def nonveg(request):
    return render(request,'nonveg.html')
