from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'panel', views.panel, name='panel'),
    url(r'play', views.play, name='play')
]