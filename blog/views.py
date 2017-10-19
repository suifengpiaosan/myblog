from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Student
def hello(request):
    template = get_template('hello.html')
    students = Student.objects.all()
    html = template.render({'Students':students})
    return HttpResponse(html)
# Create your views here.
def home(request):
    return None