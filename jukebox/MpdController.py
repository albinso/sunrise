from subprocess import call, Popen, STDOUT, PIPE, check_output
import os
import time
import random
import math


class MpdController:
    def __init__(self, default_volume=15):
        self.vol = default_volume
        #self.process = self.init_mopidy()
        #print(self.process.pid)
        self.wait_for_mopidy_startup()
        self.playing = False
        playlist = random.choice(self.get_playlists())
        #self.load_playlist(playlist)

    def init_mopidy(self):
        FNULL = open(os.devnull, 'w')
        return Popen(["mopidy"], stdout=FNULL, stderr=STDOUT)

    def wait_for_mopidy_startup(self):
        code = 1
        while code != 0:
            code = self.set_volume(self.vol)
            time.sleep(1)

    def set_volume(self, vol):
        self.vol = vol
        return call(self.make_mpc_command(['volume', str(vol)]))

    def raise_volume(self, change):
        self.vol = min(self.vol + change, 100)
        return call(self.make_mpc_command(['volume', '+' + str(change)]))

    def lower_volume(self, change):
        self.vol = max(self.vol - change, 0)
        return call(self.make_mpc_command(['volume', '-' + str(change)]))

    def get_volume(self):
        return self.vol

    def load_playlist(self, name):
        clear_command = self.make_mpc_command(['clear'])
        call(clear_command)
        command = self.make_mpc_command(['load', name])
        return call(command)

    def play(self):
        self.playing = True
        command = self.make_mpc_command(['play'])
        return call(command)

    def pause(self):
        self.playing = False
        command = self.make_mpc_command(['pause'])
        return call(command)

    def next(self):
        command = self.make_mpc_command(['next'])
        return call(command)

    def prev(self):
        command = self.make_mpc_command(['prev'])
        return call(command)

    def get_playlists(self):
        command = self.make_mpc_command(['lsplaylists'])
        output = str(check_output(command))
        return output.split('\n')

    def is_empty(self):
        playlist = self.get_playlist()
        print(playlist)
        return len(playlist) == 0

    def search_song(self, songname):
        command = self.make_mpc_command(['search', 'Artist', songname])
        search = str(check_output(command)).split('\n')
        max_songs = 5
        i = max_songs
        for song in search:
            if i <= 0:
                break
            if 'track' in song:
                i -= 1
                command = self.make_mpc_command(['insert', song])
                call(command)
        return self.play()
       
    def clear(self):
        command = self.make_mpc_command(['clear'])
        return call(command)

    def make_mpc_command(self, *args):
        out = ['mpc', '-h', '192.168.0.100'] + args[0]
	#out = ' '.join(map(str, out))
	print(out)
	return out

