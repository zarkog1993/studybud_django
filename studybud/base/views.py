from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Hello World')


def room(request):
    return HttpResponse('Hello World')
