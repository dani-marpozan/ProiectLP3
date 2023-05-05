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
SPOTIFY_PLAYLIST_ID='2mzwbxKdw7aK2yHqMeiy01'


        
choice=input('Press 1 for YT -> Spotify conversion or 2 for Spotify -> YT conversion \n')

if choice=='1':
    #YT -> Spotify
    ytmusic = YTMusic()
    token=util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope=SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI,)
    if token:
        spotify=spotipy.Spotify(auth=token)
    else:
        print('Invalid token')
    YTplaylistID='PLGqugLjBO8lI1Ui4OJQQjmEf16_Gb2u3L'
    YT_playlist=ytmusic.get_playlist(YTplaylistID)
    #create Spotify new playlist
    new_playlist_name=YT_playlist['title']
    new_playlist_description='transffered from YT via API'
    spotify_playlist=spotify.user_playlist_create(user=SPOTIFY_PLAYLIST_OWNER, name=new_playlist_name, public=True, description=new_playlist_description)
    print('Melodiile din playlist sunt:')
    trackIDs=[]
    for track in YT_playlist['tracks']:
        print ('YT Song name: {}; Artist: {}'.format (track['title'], track['artists'][0]['name']))
        spotify_search_track=spotify.search(q=track['title'] + track['artists'][0]['name'], type='track')
        spotify_search_track_str=str(spotify_search_track)
        res=re.search(r"\b/track/\w+", spotify_search_track_str)
        trackIDs.append(res.group().split('/')[-1])
    spotify.user_playlist_add_tracks(user=spotify_playlist['owner']['id'], playlist_id=spotify_playlist['id'], tracks=trackIDs)

if choice=='2':
    ytmusic = YTMusic('oauth.json')
    token=util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope=SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI,)
    if token:
        spotify=spotipy.Spotify(auth=token)
    else:
        print('Invalid token')
    spotifyPlaylist=spotify.user_playlist(user=SPOTIFY_USERNAME, playlist_id=SPOTIFY_PLAYLIST_ID)
    #Create new YT Playlist 
    YTsongIDs=[]
    new_playlist_name_YT=spotifyPlaylist['name']
    new_playlist_description_YT='transffered from Spotify via API'
    print ('PLaylist name: {}'.format(spotifyPlaylist['name']))
    spotify_tracks=spotifyPlaylist['tracks']
    for i, item in enumerate(spotify_tracks['items']):
        track = item['track']
        print('{}. Song name: {},  Artist: {}'.format(i, track['name'], track['artists'][0]['name']))
        searchYT=ytmusic.search(query=track['name']+track['artists'][0]['name'], filter='songs')
        YTsongIDs.append(searchYT[0]['videoId'])
    ytmusic.create_playlist(title=new_playlist_name_YT, description=new_playlist_description_YT, privacy_status='PRIVATE', video_ids=YTsongIDs)




    

