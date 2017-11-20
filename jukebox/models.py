from django.db import models
import subprocess
from . import mpd_instance


class PlayList(models.Model):
    name = models.CharField(max_length=255, default="")

    def load(self):
        command = mpd_instance.load_playlist(self.get_name())
        return subprocess.call(command)

    def get_name(self):
        return self.name

    def __unicode__(self):
        return self.name



