from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from . import models
# Create your views here.


def index(request):
    return HttpResponse("Hello from Partytown!")


def panel(request):
    return render(request, 'jukebox/panel.html')


def play(request):
    print(request.POST)
    playlist = get_object_or_404(models.PlayList, pk=request.POST['listID'])
    playlist.load()
    return HttpResponseRedirect(reverse('jukebox:panel'))

