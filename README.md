# Spotify-Cover-Art-Tiler
Creates uniquely tiled cover arts for Spotify playlists

## Description
This project uses the SpotiPy API to replace playlist cover arts with a tiled image based off the albums in the playlist.

## Requirements
* Spotify account and developer access
* Python 3.x
* spotipy
* numpy
* Pillow

## Setup
1. [Request developer access](https://developer.spotify.com/) for your Spotify account
2. Go to Dashboard and "Create an App". Add http://google.com/ or another website as the redirect URI.
3. In a terminal,
  export SPOTIPY_CLIENT_ID='client_id'
  export SPOTIPY_CLIENT_SECRET='client_secret'
  export SPOTIPY_REDIRECT_URI='http://google.com/'

https://spotipy.readthedocs.io/en/2.12.0/

