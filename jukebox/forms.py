from django import forms
from . import mpd_instance

def list_to_tuples(lst):
    out = []
    for entry in lst:
        out.append((entry, entry))
    return out


class PlaylistForm(forms.Form):
    playlist = forms.CharField(widget=forms.Select(choices=list_to_tuples(mpd_instance.get_playlists())))

class FakePlaylistForm(forms.Form):
    playlist = forms.CharField(widget=forms.Select(choices=list_to_tuples(["Spice Girls top hits", "Best of Britney", "Aqua: The complete collection", "Justin Bieber 2010 hits", "German Boy Bands"])))

class VolumeForm(forms.Form):
    volume = forms.IntegerField(min_value=0, max_value=25)
