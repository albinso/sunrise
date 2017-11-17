from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from . import models
import subprocess

# Create your views here.


def index(request):
    return HttpResponse("Hello from Partytown!")


def panel(request):
    return render(request, 'jukebox/panel.html')


def load(request):
    playlist = get_object_or_404(models.PlayList, pk=request.POST['listID'])
    playlist.load()
    return HttpResponseRedirect(reverse('jukebox:panel'))


def play(request):
    command = models.make_mpc_command(['play'])
    subprocess.call(command)
    return HttpResponseRedirect(reverse('jukebox:panel'))


def pause(request):
    command = models.make_mpc_command(['pause'])
    subprocess.call(command)
    return HttpResponseRedirect(reverse('jukebox:panel'))

