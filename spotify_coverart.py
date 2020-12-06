import os
import base64
import spotipy
import requests
import numpy as np
from PIL import Image
import spotipy.util as util

SEARCH_LIMIT = 50
WIDTH = 640
HEIGHT = 640


def get_all_playlists():
    i = 0
    finished = False
    playlistUris = []
    playlistNames = []
    while True:
        offset = i * SEARCH_LIMIT
        searchResults5 = spotifyObject.current_user_playlists(limit=SEARCH_LIMIT, offset=offset)
        for item in range(SEARCH_LIMIT):
            try:
                playlistResults = searchResults5['items'][item]
                playlistUri1 = playlistResults['uri']
                playlistName1 = playlistResults['name']
                playlistUris.append(playlistUri1)
                playlistNames.append(playlistName1)
            except:
                finished = True
            i += 1
        if finished:
            break
    return playlistUris, playlistNames


def replace_image(uri):
    playlistResults = spotifyObject.playlist(playlist_id=uri)
    numTracks = int(playlistResults['tracks']['total'])
    playlistName = playlistResults['name']
    numIter = int(np.ceil(numTracks / SEARCH_LIMIT))

    albumNames = []
    albumUris = []
    albumArts = []
    for i in range(numIter):
        offset = SEARCH_LIMIT * i
        searchResults2 = spotifyObject.playlist_tracks(uri, limit=SEARCH_LIMIT, offset=offset)
        if i < numIter - 1:
            iters = SEARCH_LIMIT
        else:
            iters = numTracks % SEARCH_LIMIT
        for item in range(iters):
            trackResults = searchResults2['items'][item]
            albumName = trackResults['track']['album']['name']
            albumUri = trackResults['track']['album']['uri']
            try:
                albumArt = trackResults['track']['album']['images'][0]['url']
                if albumName not in albumNames:
                    albumNames.append(albumName)
                    albumUris.append(albumUri)
                    albumArts.append(albumArt)
            except:
                continue

    sideLength = int(np.floor(np.sqrt(len(albumUris))))

    for i, album in enumerate(albumArts[:sideLength ** 2]):
        name = f'{str(i)}.jpg'
        url = album
        with open(name, 'wb') as f:
            f.write(requests.get(url).content)

    k = 0
    blank = Image.new('RGB', (WIDTH, HEIGHT), 'white')
    for i in range(sideLength):
        for j in range(sideLength):
            imageName = f'{str(k)}.jpg'
            try:
                im = Image.open(imageName)
                horizontal = round(WIDTH / sideLength)
                vertical = round(HEIGHT / sideLength)
                left = horizontal * j
                right = left + horizontal
                top = vertical * i
                bottom = top + vertical
                im1 = im.crop((left, top, right, bottom))
                blank.paste(im1, (left, top, right, bottom))
                os.remove(imageName)
            except:
                continue
            k += 1
    blank.save('Tile.jpg')

    with open('Tile.jpg', 'rb') as imageFile:
        tileStr = base64.b64encode(imageFile.read())

    spotifyObject.playlist_upload_cover_image(playlist_id=uri, image_b64=tileStr)
    return playlistName


username = input('What is your user ID?\n')
userUri = input('\nWhat is your user Uri?\n')
scope = 'playlist-modify-public ugc-image-upload'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username, scope)

# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)


all_playlists = input('\nDo you want to apply tiling to ALL of your playlists? (y/n)\n').lower()
if all_playlists == 'y' or all_playlists == 'yes':
    playlistUris, playlistNames = get_all_playlists()
    for uri, name in zip(playlistUris, playlistNames):
        replace_image(uri)
        print(f'\nCover art complete: {name}')
elif all_playlists == 'n' or all_playlists == 'no':
    while True:
        uri = input('\nEnter a playlist uri '
                            '(ex. spotify:playlist:6p4vH5K9skL9KEoDnyfGi3 or 6p4vH5K9skL9KEoDnyfGi3):\n')
        uri = uri.replace('spotify:playlist:', '')
        name = replace_image(uri)
        print(f'\nCover art complete: {name}')
        another_playlist = input('Another one? (y/n)').lower()
        if another_playlist == 'y' or another_playlist == 'yes':
            continue
        else:
            break
else:
    print('Invalid response. Enter \'y\' or \'n\'.')
