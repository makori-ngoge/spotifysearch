from django.db import models
from django.urls import reverse

class ArtistSearch(models.Model):
    artistname = models.CharField(verbose_name="Search For An Artist:", max_length=100)

class AlbumSearch(models.Model):
    albumname = models.CharField(verbose_name="Search For An Album:", max_length=100)

class TrackSearch(models.Model):
    trackname = models.CharField(verbose_name="Search For A Track:", max_length=100)