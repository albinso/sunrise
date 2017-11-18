from albinso import celery_app
import time
from jukebox import mpd_instance


@celery_app.task(bind=True)
def alarm(self):
    mpd_instance.set_volume(0)
    mpd_instance.play()
    for i in range(100):
        mpd_instance.raise_volume(1)
        time.sleep(2)