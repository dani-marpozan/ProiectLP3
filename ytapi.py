from ytmusicapi import YTMusic
import os
import sys
from dotenv import load_dotenv
import base64
from requests import post
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import re


SPOTIFY_USERNAME='31p3lj3vxwibxsc5ch7cpm5uxneq?si=9cf94d73d6544b11'
SPOTIFY_CLIENT_ID = '53fbce442277486fbbdc9b7aa9714eaf'   
SPOTIFY_CLIENT_SECRET = 'e72dd10b2de5481cbf31a472c890db50'  
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'  
SPOTIFY_SCOPE="playlist-modify-public"
SPOTIFY_PLAYLIST_OWNER='31p3lj3vxwibxsc5ch7cpm5uxneq'




def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print('{}. Song name: {},  Artist: {}'.format(i, track['name'], track['artists'][0]['name']))
        

#YT -> Spotify
ytmusic = YTMusic()
token=util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope=SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI,)
if token:
    spotify=spotipy.Spotify(auth=token)
else:
    print('Invalid token')
YTplaylistID='PLGqugLjBO8lI1Ui4OJQQjmEf16_Gb2u3L'
YT_playlist=ytmusic.get_playlist(YTplaylistID)
new_playlist_name=YT_playlist['title']
new_playlist_description='transffered from YT via API'
spotify_playlist=spotify.user_playlist_create(user=SPOTIFY_PLAYLIST_OWNER, name=new_playlist_name, public=True, description=new_playlist_description)
print('Melodiile din playlist sunt:')
trackIDs=[]
for track in YT_playlist['tracks']:
    #print ('Song name: {}; Artist: {}'.format (track['title'], track['artists'][0]['name']))
    spotify_search_track=spotify.search(q=track['title'] + track['artists'][0]['name'], type='track')
    spotify_search_track_str=str(spotify_search_track)
    res=re.search(r"\b/track/\w+", spotify_search_track_str)
    trackIDs.append(res.group().split('/')[-1])
spotify.user_playlist_add_tracks(user=spotify_playlist['owner']['id'], playlist_id=spotify_playlist['id'], tracks=trackIDs)


#authentication #Spotify


    # #showing tracks in playlists
    # playlists = spotify.user_playlists(SPOTIFY_PLAYLIST_OWNER)
    # for playlist in playlists['items']:
    #             print('Nume playlist: {}'. format(playlist['name']))
    #             results = spotify.user_playlist(SPOTIFY_USERNAME, playlist['id'], fields="tracks,next")
    #             tracks = results['tracks']
    #             show_tracks(tracks)
    #             while tracks['next']:
    #                 tracks = spotify.next(tracks)
    #                 show_tracks(tracks)
    #creating new spotify playlist
    # playlist_name=''
    # playlist_description=''
    # spotify.user_playlist_create(user=SPOTIFY_PLAYLIST_OWNER, name=playlist_name, public=True, description=playlist_description)





    

