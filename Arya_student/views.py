from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    name = 'Ashish'
    return HttpResponse('<h1>This is home</h1><br><h2>This is home</h2>')