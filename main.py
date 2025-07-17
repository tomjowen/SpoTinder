#imports
from tkinter import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

YOUR_CLIENT_ID = ""
YOUR_CLIENT_SECRET = ""
YOUR_BULK_PLAYLIST_ID = ""
YOUR_NEW_PLAYLIST_ID = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_CLIENT_ID,
                                                           client_secret=YOUR_CLIENT_SECRET,
                                                           redirect_uri="https://localhost:8888/callback",
                                                           scope="user-modify-playback-state playlist-modify-public playlist-modify-private user-read-currently-playing"))
main = Tk()


def onLeftKey(event):
    #get song id
    song = sp.current_user_playing_track()['item']['id']
    #print(song)
    #skip track
    sp.next_track()
    #remove song from main playlist
    sp.playlist_remove_all_occurrences_of_items(YOUR_BULK_PLAYLIST_ID,[song])

def onRightKey(event):
    print(sp.current_user_playlists())
    #get song id
    song = sp.current_user_playing_track()['item']['id']
    #skip track
    sp.next_track()
    #remove song from main playlist
    sp.playlist_remove_all_occurrences_of_items(YOUR_BULK_PLAYLIST_ID,[song])
    #add song to good playlist
    sp.playlist_add_items(YOUR_NEW_PLAYLIST_ID,[song])

frame = Frame(main, width=100, height=100)
main.bind('<Left>', onLeftKey)
main.bind('<Right>', onRightKey)
frame.pack()
main.mainloop()
