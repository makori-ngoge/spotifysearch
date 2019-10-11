import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
from django.urls import reverse, resolve
from urllib.parse import quote

# from slugify import slugify
# import os
# import sys


SPOTIPY_CLIENT_ID='026c94177ab648e6af67c8653323dbe0'
SPOTIPY_CLIENT_SECRET="12f56f869d22422dbf4de353168e66b3"
SPOTIPY_REDIRECT_URI="http://localhost/"

# "https://github.com/makori-ngoge"

query = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
)

def commafy(num):
    num = str(num)
    split = []
    final = ""
    index = len(num) % 3

    if len(num) > 3:
        if index == 0:
            index += 3
        for x in num:
            split.append(x)
        while index < len(split):
            split.insert(index, ",")
            index += 4
        for x in split:
            final += x
        return final
    else:
        return num

class TrackObject:
    def __init__(self, trackid):
        self.trackid = trackid
        self.trackname = query.track(self.trackid)["name"]
        self.trackalbum = AlbumObject(query.track(self.trackid)["album"]["id"])
    
    def artist(self):
        return ArtistObject(query.track(self.trackid)["album"]["artists"][0]["id"])

    def image(self):
        return query.track(self.trackid)["album"]["images"][0]["url"]
    
    def featuredartist(self):
        featuredartist = []
        count = 1
        results = query.track(self.trackid)["artists"]
        while count < len(results):
            featuredartist.append(ArtistObject(results[count]["id"]))
            count += 1
        return featuredartist

class AlbumObject:
    def __init__(self, albumid):
        self.albumname = query.album(albumid)["name"]
        self.albumid = albumid

    def artist(self):
        return ArtistObject(query.album(self.albumid)["artists"][0]["id"])
    
    def image(self):
        return query.album(self.albumid)["images"][0]["url"]

    def tracklist(self):
        results = query.album_tracks(self.albumid)
        tracks = []
        for x in results["items"]:
            tracks.append(TrackObject(x["id"]))
        return tracks

class ArtistObject:
    def __init__(self, artistid):
        self.artistid = artistid
        self.artistname = query.artist(artistid)["name"]
        self.followers = commafy(query.artist(artistid)["followers"]["total"])

    def artistalbums(self):
        albums = []
        results = query.artist_albums(self.artistid, album_type="album")
        for x in results["items"]:
            albums.append(AlbumObject(x["id"]))
        return albums

    def toptracks(self):
        tracks = []
        results = query.artist_top_tracks(self.artistid)
        for x in results["tracks"]:
            tracks.append(TrackObject(x["id"]))
        return tracks

    def image(self):
        return query.artist(self.artistid)["images"][0]["url"]

    # (self.artistname)         
    #reverse("ArtistSearch:artist", kwargs={"slug": self.artistname})

def artistsearch(artistname):
    results = query.search(artistname, limit=20, type="artist")
    search_results = []
    for x in results["artists"]["items"]:
        search_results.append(ArtistObject(x["id"]))
    return search_results

def albumsearch(albumname):
    results = query.search(albumname, limit=20, type="album")
    albums_list = []
    for x in results["albums"]["items"]:
        albums_list.append(AlbumObject(x["id"]))
    # print(json.dumps(results, sort_keys=True, indent=2))
    return albums_list

def tracksearch(trackname):
    tracks = []
    results = query.search(trackname, limit=20, type="track")
    for x in results["tracks"]["items"]:
        tracks.append(TrackObject(x["id"]))
    return tracks

# print(json.dumps(VARIALBLE, sort_keys=True, indent=4))
