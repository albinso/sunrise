from django import forms
from . import mpd_instance

def list_to_tuples(lst):
    out = []
    for entry in lst:
        out.append((entry, entry))
    return out


class PlaylistForm(forms.Form):
    playlist = forms.CharField(label="Select playlist: ", widget=forms.Select(choices=list_to_tuples(mpd_instance.get_playlists())))
