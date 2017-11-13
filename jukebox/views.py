from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
# Create your views here.


def index(request):
    return HttpResponse("Hello from Partytown!")
