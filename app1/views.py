from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse ("<h1>Hello everyone</h1>")

def day(request):
    return HttpResponse ("<h3>Today is a great day</h3>")