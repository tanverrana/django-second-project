from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def courses(request):
    return HttpResponse("This is course page that is created in second app.")


def feedback(request):
    return HttpResponse("This is feedback page that is created in second app.")
