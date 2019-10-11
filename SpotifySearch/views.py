from django.shortcuts import render
from . import forms
from . import backend
from urllib.parse import unquote

def home(request):
    return render(request, "home.html")


def artistsearch(request):
    template_name = "search-by-artist.html"
    artist_search = forms.ArtistSearch
    assets = {"artist_search": artist_search}

    if request.method == "POST":
        answeredform = artist_search(request.POST)
        if answeredform.is_valid():
            artist_request = answeredform.cleaned_data["artistname"]
            artist_results = backend.artistsearch(artist_request)
            assets.update({"artist_results": artist_results})
            return render(request, template_name, assets)

    return render(request, template_name, assets)


def artistinfo(request, slug):
    template_name = "artist-info.html"

    assets = {"artist": backend.ArtistObject(slug)}
    
    return render(request, template_name, assets)


def albumsearch(request):
    template_name = "search-by-album.html"
    album_search = forms.AlbumSearch
    assets = {"album_search": album_search}

    if request.method == "POST":
        answeredform = album_search(request.POST)
        if answeredform.is_valid():
            album_request = answeredform.cleaned_data["albumname"]
            album_results = backend.albumsearch(album_request)
            assets.update({"album_results": album_results})
            return render(request, template_name, assets)

    return render(request, template_name, assets)


def albuminfo(request, slug):
    template_name = "album-info.html"
    
    assets = {"album": backend.AlbumObject(slug)}

    return render(request, template_name, assets)

def tracksearch(request):
    template_name = "search-by-track.html"
    track_search = forms.TrackSearch
    assets = {"track_search": track_search}

    if request.method == "POST":
        answeredform = track_search(request.POST)
        if answeredform.is_valid():
            track_request = answeredform.cleaned_data["trackname"]
            track_results = backend.tracksearch(track_request)
            assets.update({"track_results": track_results})
            return render(request, template_name, assets)

    return render(request, template_name, assets)

def trackinfo(request, slug):
    template_name = "track-info.html"

    assets = {"track": backend.TrackObject(slug)}

    return render(request, template_name, assets)