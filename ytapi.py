from ytmusicapi import YTMusic
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import re
import config


SPOTIFY_SCOPE="playlist-modify-public"


SPOTIFY_CLIENT_ID = config.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
SPOTIFY_REDIRECT_URI = config.SPOTIFY_REDIRECT_URI
SPOTIFY_USER_ID= config.SPOTIFY_USER_ID


def Conversion():       
    choice=input('Press 1 for YT -> Spotify conversion or 2 for Spotify -> YT conversion \n')

    if choice=='1':
        #YT Music -> Spotify
        ytmusic = YTMusic('oauth.json')
        token=util.prompt_for_user_token(username=SPOTIFY_USER_ID, scope=SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI)
        if token:
            spotify=spotipy.Spotify(auth=token)
        else:
            print('Invalid token')
        YTplaylistID=input('Enter YT Music playlist ID:')
        try:
            YT_playlist=ytmusic.get_playlist(YTplaylistID)
        except Exception as e:
            print('Unable to get YT Playlist')
            print(e)
            exit()

        #create Spotify new playlist
        new_playlist_name=YT_playlist['title']
        new_playlist_description='transferred from YT via API'
        try:
            spotify_playlist=spotify.user_playlist_create(user=SPOTIFY_USER_ID, name=new_playlist_name, public=True, description=new_playlist_description)
        except Exception as e:
            print('Unable to create a new Spotify playlist')
            print(e)
            exit()

        print('Tracks from YT playlist {}'.format(YT_playlist['title']))
        trackIDs=[]
        for i, track in enumerate(YT_playlist['tracks']):
            print ('{}. YT Song name: {}; Artist: {}'.format (i, track['title'], track['artists'][0]['name']))
            spotify_search_track=spotify.search(q=track['title'] + track['artists'][0]['name'], type='track')
            spotify_search_track_str=str(spotify_search_track)
            res=re.search(r"\b/track/\w+", spotify_search_track_str)
            if ('match' in str(res)):
                trackIDs.append(res.group().split('/')[-1])
                #print ('--- Similar song found on Spotify')
            else:
                print('--- Unable to find a match on Spotify')
        try:
            spotify.user_playlist_add_tracks(user=spotify_playlist['owner']['id'], playlist_id=spotify_playlist['id'], tracks=trackIDs)
        except:
            print ('Something went wrong. Unable to create new spotify playlist')
            exit()
        else:
            print ('Succesfulluy created new Spotify playlist: "{}" from your YT Music Playlist. Link to the new Spotify playlist: {}'.format(new_playlist_name, spotify_playlist['external_urls']['spotify']))
        


    if choice=='2':
        #Spotify->YT Music
        ytmusic = YTMusic('oauth.json')
        token=util.prompt_for_user_token(username=SPOTIFY_USER_ID, scope=SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI,)
        if token:
            spotify=spotipy.Spotify(auth=token)
        else:
            print('Invalid token')
        SPOTIFY_PLAYLIST_ID=input('Enter Spotify playlist ID:')
        try: 
            spotifyPlaylist=spotify.user_playlist(user=SPOTIFY_USER_ID, playlist_id=SPOTIFY_PLAYLIST_ID)
        except Exception as e:
            print('Unable to get Spotify Playlist')
            print(e)
            exit()
        #Create new YT Playlist 
        YTsongIDs=[]
        new_playlist_name_YT=spotifyPlaylist['name']
        new_playlist_description_YT='transferred from Spotify via API'
        print('Tracks from Spotify playlist {}'.format(spotifyPlaylist['name']))
        spotify_tracks=spotifyPlaylist['tracks']
        for i, item in enumerate(spotify_tracks['items']):
            track = item['track']
            print('{}. Spotify Song name: {},  Artist: {}'.format(i, track['name'], track['artists'][0]['name']))
            searchYT=ytmusic.search(query=track['name']+track['artists'][0]['name'], filter='songs')
            if(searchYT):
                YTsongIDs.append(searchYT[0]['videoId'])
        try: 
            newYTPlaylist=ytmusic.create_playlist(title=new_playlist_name_YT, description=new_playlist_description_YT, privacy_status='PRIVATE', video_ids=YTsongIDs)
        except Exception as e:
            print ('Unable to crate new YT Playlist')
            print (e)
            exit()
        else: 
            print ('Succesfulluy created new YT Music playlist: "{}" from your Spotify Playlist. Link to the new Spotify playlist: {}'.format(new_playlist_name_YT, str('https://music.youtube.com/playlist?list='+newYTPlaylist)))




if __name__=='__main__':
    Conversion()

