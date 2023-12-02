import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

# fetih34986@nasmis.com
# fetih34986
# https://developer.spotify.com/dashboard


# def check_if_playlist(f_playlist_name: str, f_sp: spotipy):
#     get_user_paylist = sp.user_playlists(user=user_id)
#     return get_user_paylist

SPOTIPY_CLIENT_ID = "3251a207a7a14b9d9304e1442f2b3fb2"
SPOTIPY_CLIENT_SECRET = "4ca246079979411c807b2c5bc95ea954"
SPOTIPY_REDIRECT_URI = "http://example.com"


#time_user_input = str(input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "))
time_user_input = "1998-05-26"
user_year = time_user_input.split('-', 1)[0]

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{time_user_input}/")
response.raise_for_status()

billboard_plain_html = response.text

soup = BeautifulSoup(billboard_plain_html, features="html.parser")
titles = [title.getText().strip() for title in soup.select("li>h3[id='title-of-a-story']")]

artists = [title.getText().strip() for title in soup.select("ul>li>span[class*='c-label a-no-trucate']")]

##################################################################################################


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope
                                               ))
current_user = sp.current_user()
user_id = current_user['id']

# user_id = 31mmsk775o2u4mjvefiy2v3qknqa
# user_uri = 'uri': 'spotify:user:31mmsk775o2u4mjvefiy2v3qknqa'

uri_list = []
for track in titles[0:10]:
    track_index = titles.index(track)
    search_response = sp.search(q=f"remaster%20track:{titles[track_index]}%20"
                                 f"year:{user_year}%20"
                                 f"artist:{artists[track_index]}",
                                type="track",
                                market="US",
                                limit=20
                                )
    # pprint(search_response)
    counter = 0
    for item in search_response['tracks']['items']:
        counter += 1
        item_track_name = item['name']
        item_track_artist = item['artists'][0]['name']
        item_track_uri = item['uri']

        if item_track_name == titles[track_index]: # and item_track_artist == artists[track_index]:
            uri_list.append(item_track_uri)
            break
        elif len(search_response['tracks']['items']) == counter:
            uri_list.append('NULL')

playlist_name = "{time_user_input} Billboard 100"

new_user_playlist = sp.user_playlist_create(name=f"{time_user_input} Billboard 100",
                        public="false",
                        user=user_id
                        )

user_playlist_id = new_user_playlist['id']

tracks_to_add = [track for track in uri_list if track != "NULL"]

sp.playlist_add_items(playlist_id=user_playlist_id, items=tracks_to_add, position=None)