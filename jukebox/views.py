from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import mpd_instance
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello from Partytown!")


def panel(request):
    return render(request, 'jukebox/panel.html')


def play(request):
    if mpd_instance.is_empty():
        self.search_song("journey")
    mpd_instance.play()
    return HttpResponseRedirect(reverse('jukebox:panel'))


def pause(request):
    mpd_instance.pause()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def next(request):
    mpd_instance.next()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def prev(request):
    mpd_instance.prev()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def set_volume(request):
    mpd_instance.set_volume(request.GET['volume'])
    return HttpResponseRedirect(reverse('jukebox:panel'))

def clear(request):
    mpd_instance.clear()
    return HttpResponseRedirect(reverse('jukebox:panel'))

@csrf_exempt
def search(request):
    mpd_instance.search_song(request.POST['Artist'])
    return HttpResponseRedirect(reverse('jukebox:panel'))
