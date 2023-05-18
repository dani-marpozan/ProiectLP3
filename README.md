# ProiectLP3
Proiect Limbaje de Programare 3 - Tema proiect: D1-T2 | Consum API 

Utilizarea API-urilor YT Music și Spotify pentru conversie de playlist.


Cerinte minimale:
1. Creați un script ce preia ca parametru numele unui playlist și un serviciu (ytmusic, spotify).
2. Identificați toate melodiile din playlist.
3. Creați un playlist nou, asemănător cu cel dat ca parametru, dar în celălalt serviciu de muzica.


Resurse:
https://ytmusicapi.readthedocs.io/en/latest/
https://developer.spotify.com/documentation/web-api/
https://medium.com/@mklaben15/using-python-to-download-a-youtube-playlist-and-convert-to-mp3-for-acustom-spotify-library-87ab950958a7


**Detalii pentru testare:** <br />
1.Pachete necesare: ytmusicapi, spotipy (din requirements.txt)<br />
2.Trebuie creat fisierul config.py ce contine datele de logare la API Spotify. In interiorul acestui fisier trebuie sa apara: <br />
          **SPOTIFY_CLIENT_ID = 'Your Spotify CLIENT ID'  # se gaseste in url-ul pt copy link profile din Spotify <br />
          **SPOTIFY_CLIENT_SECRET = 'Your Spotify CLIENT SECRET' # se gaseste in proiectul creat in https://developer.spotify.com/dashboard **<br />
          **SPOTIFY_REDIRECT_URI = 'Your Spotify REDIRECT URI' # se gaseste in proiectul creat in https://developer.spotify.com/dashboard** <br />
          **SPOTIFY_USER_ID='Your Spotify USER ID' # se gaseste in proiectul creat in https://developer.spotify.com/dashboard** <br />
3.In folderul in care e aplicatia, se ruleaza in linia de comanda: **ytmusicapi oauth**, care va creea fisierul 'ouath.json' (credentiale pentru YT) <br/>
4. Se ruleaza aplicatia, denumita **ytapi.py** <br/>


<br/>

Toate pachetele necesare se afla in fisierul **requirements.txt**

