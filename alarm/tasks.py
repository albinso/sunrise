from albinso import celery_app
import time
from jukebox import mpd_instance
import requests
import random
from .lightconfig import url


@celery_app.task(bind=True)
def alarm(self):
    lightemup()
    mpd_instance.set_volume(0)
    mpd_instance.pause()
    #queue_random_artist()
    #time.sleep(10)
    mpd_instance.play()
    for i in range(100):
        mpd_instance.raise_volume(1)
        time.sleep(1)

def queue_random_artist():
    from . import models
    items = models.Artist.objects.all()
    random_artist = random.choice(items)
    mpd_instance.clear()
    mpd_instance.search("artist", str(random_artist), 30)
    
def lightemup():
    for brightness in range(1, 256):
        for i in range(1, 7):
            requests.get(url + "/light/bright?id={}&brightness={}".format(i, brightness))
            if brightness == 1:
                requests.get(url + "/light/on?id={}".format(i))
                
        time.sleep(1)
