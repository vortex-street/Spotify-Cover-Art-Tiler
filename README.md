# Spotify-Cover-Art-Tiler
Creates uniquely tiled cover arts for Spotify playlists
![alt text](https://i.ibb.co/gJ2FYjj/img2.png)

## Description
This project uses the SpotiPy API to replace playlist cover arts with a tiled image based off the albums in the playlist. Basic terminal prompts allow the user to apply the imaging to all, or select playlists on their account.

## Requirements
* Spotify account and developer access
* Python 3.x
* spotipy
* numpy
* Pillow

## Setup and Usage
1. [Request developer access](https://developer.spotify.com/) for your Spotify account.
2. Go to Dashboard and "Create an App". Add http://google.com/ or another website as the redirect URI.
3. In a terminal,
```
  export SPOTIPY_CLIENT_ID='client_id'
  export SPOTIPY_CLIENT_SECRET='client_secret'
  export SPOTIPY_REDIRECT_URI='http://google.com/'
```
client_id and client_secret can be found on the page of the app you created in step 2.
4. Run the program,
```
  python3 spotify_tiler.py
```
5. Enter user ID and URI when prompted.
6. Your browser will redirect to a page asking to connect to the app. Click Okay.
7. Enter http://google.com/ (or your redirect uri if other) when prompted.
8. Follow the prompts for awesome cover art tiling!
![alt text](https://i.ibb.co/DCK5cvD/img1.png)
![alt text](https://i.ibb.co/7vDRpM1/img3.png)
