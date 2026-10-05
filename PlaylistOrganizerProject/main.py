from Features.service import SpotifyService
import Features.view

CLIENT_ID = "dcdf6f4334714642a0aea221c354c749"
CLIENT_SECRET = "2eb908b2aa7c48c19d4258306ae46830"
REDIRECT_URI = "http://127.0.0.1:8888"
SCOPE = "user-read-recently-played user-top-read"

if __name__ == "__main__":
    service = SpotifyService(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE)
    service.fetch_and_store_tracks()
    Features.view.run_gui()
