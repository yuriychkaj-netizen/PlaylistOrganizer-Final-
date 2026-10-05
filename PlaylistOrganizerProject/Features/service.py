import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Features.track import Track
from Features.repository import TrackRepository

class SpotifyService:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            open_browser=False
        ))
        self.repo = TrackRepository()

    def fetch_and_store_tracks(self):
        recent = self.sp.current_user_recently_played(limit=5)
        for item in recent["items"]:
            track = item["track"]
            self.repo.save_track(Track(track["id"], track["name"], track["artists"][0]["name"]))

        top_tracks = self.sp.current_user_top_tracks(limit=5, time_range="short_term")
        for track in top_tracks["items"]:
            self.repo.save_track(Track(track["id"], track["name"], track["artists"][0]["name"]))
