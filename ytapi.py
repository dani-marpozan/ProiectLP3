from ytmusicapi import YTMusic

ytmusic = YTMusic()
print ("Good")

from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")

#playlistId = ytmusic.create_playlist("bababa", "test description")
res=search_results = ytmusic.search("Dani")
print(res)
# YTMusic.get_user_playlists
