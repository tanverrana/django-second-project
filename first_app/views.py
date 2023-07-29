from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def contact(request):
    return HttpResponse("This is contact page that is created in first app.")


def about(request):
    return HttpResponse("This is about page that is created in first app.")
