from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def contact(request):
    return HttpResponse('''
                        <h3>This is contact page that is created in first app.</h3>
                        <a href ='/first_app/about/'>About</a>
                        
                        ''')


def about(request):
    return HttpResponse('''
                        <h3>This is about page that is created in first app.</h3>
                        <a href ='/first_app/contact/'>Contact</a>
                        
                        ''')
