from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dhoni(request):
    return HttpResponse('<h1>Ms dhoni is the one of best wicketer and captain</h1>')