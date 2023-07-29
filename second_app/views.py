from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def courses(request):
    return HttpResponse('''
                        <h3>This is Course page that is created in Second app.</h3>
                        <a href ='/second_app/feedback/'>Feedback</a>
                        
                        ''')


def feedback(request):
    return HttpResponse('''
                        <h3>This is Feedback page that is created in second app.</h3>
                        <a href ='/second_app/courses/'>Courses</a>
                        
                        ''')
