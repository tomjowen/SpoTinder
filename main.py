#imports
from tkinter import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

YOUR_CLIENT_ID = ""
YOUR_CLIENT_SECRET = ""
YOUR_BULK_PLAYLIST_ID =

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="7f196e0b98e94eaea978344cc2d40ce3",
                                                           client_secret="0cf08ae77b454902ae0925312d972d9e",
                                                           redirect_uri="https://localhost:8888/callback",
                                                           scope="user-modify-playback-state playlist-modify-public playlist-modify-private user-read-currently-playing"))
main = Tk()


def leftKey(event):
    #get song id
    song = sp.current_user_playing_track()['item']['id']
    print(song)
    #skip track
    sp.next_track()
    #remove song from main playlist
    sp.playlist_remove_all_occurrences_of_items('4wq1zhSpGgqj8b815VHQcd',[song])

def rightKey(event):
    print(sp.current_user_playlists())
    #get song id
    song = sp.current_user_playing_track()['item']['id']
    #skip track
    sp.next_track()
    #remove song from main playlist
    sp.playlist_remove_all_occurrences_of_items('4wq1zhSpGgqj8b815VHQcd',[song])
    #add song to good playlist
    sp.playlist_add_items('1aeTfXjlVRIMzXX54KKQIO',[song])

frame = Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
frame.pack()
main.mainloop()