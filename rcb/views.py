from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kohli(request):
    return HttpResponse('<h1>Virat is the one man King in cricket</h1>')
