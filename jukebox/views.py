from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import mpd_instance
from .forms import PlaylistForm, VolumeForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello from Partytown!")


def panel(request):
    return render(request, 'jukebox/panel.html', {'form': PlaylistForm(), 'volume_form': VolumeForm()})

def lolpanel(request):
    return render(request, 'jukebox/panel.html', {'form': PlaylistForm(), 'volume_form': VolumeForm(), 'lolscript': '/scripts/js/unauth.js'})
    

def play(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    if mpd_instance.is_empty():
        mpd_instance.search("artist", "journey", 5)
    mpd_instance.play()
    return HttpResponseRedirect(reverse('jukebox:panel'))


def pause(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    mpd_instance.pause()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def next(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    mpd_instance.__next__()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def prev(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    mpd_instance.prev()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def set_volume(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    form = VolumeForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(reverse('jukebox:panel'))
    mpd_instance.set_volume(int(form.cleaned_data['volume']))
    return HttpResponseRedirect(reverse('jukebox:panel'))

def clear(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    mpd_instance.clear()
    return HttpResponseRedirect(reverse('jukebox:panel'))

def load_playlist(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    form = PlaylistForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(reverse('jukebox:panel'))
    print(form.cleaned_data)
    mpd_instance.load_playlist(form.cleaned_data["playlist"])
    return HttpResponseRedirect(reverse('jukebox:panel'))

@csrf_exempt
def search(request):
    if not request.user.is_authenticated:
        return lolpanel(request)
    print(request.POST.keys())
    mpd_instance.search(request.POST['Type'], request.POST['Artist'], int(request.POST['NumSongs']))
    return HttpResponseRedirect(reverse('jukebox:panel'))
