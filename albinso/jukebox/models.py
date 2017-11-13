from django.db import models
import subprocess


def make_mpc_command(*args):
    return ['mpc', '-p', '6680'] + args[0]


class MopidyInstance(subprocess.Popen):

    def __init__(self):
        subprocess.Popen.__init__(self, ["mopidy"])
        self.playing = False

    def play(self):
        if self.playing:
            print('Already playing so doing nothing')
            return 0
        self.playing = True
        command = self.make_mpc_command(['play'])
        return subprocess.call(command)

    def pause(self):
        self.playing = False
        command = self.make_mpc_command(['pause'])
        return subprocess.call(command)

    def get_playlists(self):
        command = self.make_mpc_command(['lsplaylists'])
        output = subprocess.check_output(command)
        return output.split('\n')


class PlayList(models.Model):

    def __init__(self, name):
        models.Model.__init__(self)
        self.name = models.CharField(max_length=255)

    def load(self):
        command = make_mpc_command(['load', self.get_name()])
        return subprocess.call(command)

    def get_name(self):
        return self.name



