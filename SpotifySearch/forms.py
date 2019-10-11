from django import forms
from . import models

class ArtistSearch(forms.ModelForm):
    class Meta:
        model = models.ArtistSearch
        fields = ["artistname"]

class AlbumSearch(forms.ModelForm):
    class Meta:
        model = models.AlbumSearch
        fields = ["albumname"]

class TrackSearch(forms.ModelForm):
    class Meta:
        model = models.TrackSearch
        fields = ["trackname"]