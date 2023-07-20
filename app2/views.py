from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def life (request):
    return HttpResponse ("<h1>Don't afraid to be alone goals are personal...</h1>")

def bye (request):
    return HttpResponse ("<h3>Bye everyone god bless you all...</h3>")