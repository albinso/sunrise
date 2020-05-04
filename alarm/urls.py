from django.conf.urls import url

from . import views

app_name = 'alarm'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.set_alarm, name='set_alarm'),
    url(r'save/$', views.save_alarm, name='save_alarm'),
]
