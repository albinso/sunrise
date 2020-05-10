from django.conf.urls import url

from . import views

app_name = 'jukebox'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'panel', views.panel, name='panel'),
    url(r'play', views.play, name='play'),
    url(r'pause', views.pause, name='pause'),
    url(r'next', views.next, name='next'),
    url(r'prev', views.prev, name='prev'),
    url(r'setvol', views.set_volume, name='setvolume'),
    url(r'search', views.search, name='search'),
    url(r'clear', views.clear, name='clear'),
    url(r'load', views.load_playlist, name='load'),
]
