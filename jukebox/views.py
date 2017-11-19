from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import mpd_instance

def index(request):
    return HttpResponse("Hello from Partytown!")


def panel(request):
    return render(request, 'jukebox/panel.html')


def load(request):
    mpd_instance.load_playlist(request.POST['listID'])
    return HttpResponseRedirect(reverse('jukebox:panel'))


def play(request):
    mpd_instance.play()
    return HttpResponseRedirect(reverse('jukebox:panel'))


def pause(request):
    mpd_instance.pause()
    return HttpResponseRedirect(reverse('jukebox:panel'))

