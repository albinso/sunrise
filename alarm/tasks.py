from albinso import celery_app
import time
from jukebox import mpd_instance
import requests
from lightconfig import url


@celery_app.task(bind=True)
def alarm(self):
    lightemup()
    mpd_instance.set_volume(0)
    mpd_instance.pause()
    mpd_instance.play()
    for i in range(100):
        mpd_instance.raise_volume(1)
        time.sleep(2)

def lightemup():
    for i in range(1, 7):
        requests.get(url + "/light/on?id=" + str(i))
