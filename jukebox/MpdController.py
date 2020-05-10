from subprocess import call, Popen, STDOUT, PIPE, check_output, CalledProcessError
import os
import time
import random
import math


class MpdController:
    def __init__(self):
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
            code = 0
            try:
                self.get_volume()
            except CalledProcessError:
                code = 1
            time.sleep(1)

    def set_volume(self, vol):
        return call(self.make_mpc_command(['volume', str(vol)]))

    def raise_volume(self, change):
        return call(self.make_mpc_command(['volume', '+' + str(change)]))

    def lower_volume(self, change):
        return call(self.make_mpc_command(['volume', '-' + str(change)]))

    def get_volume(self):
        proc = check_output(self.make_mpc_command(['volume']))
        return proc

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

    def __next__(self):
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
        playlist = self.get_playlists()
        return len(playlist) <= 4

    def search_song(self, songname):
        command = self.make_mpc_command(['search', 'Artist', songname])
        search_unprocessed = check_output(command).decode("UTF-8")
        print("Search results: {}".format(search_unprocessed))
        search = search_unprocessed.split('\n')
        print("List of songs found in search: {}".format(search))
        max_songs = 5
        i = max_songs
        for song in search:
            print(song)
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
        out = ['mpc', '-h', 'mopidy'] + args[0]
        #out = ' '.join(map(str, out))
        print("MPC command to run: {}".format(out))
        return out

