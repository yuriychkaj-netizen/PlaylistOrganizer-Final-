import sqlite3
from Features.track import Track

class TrackRepository:
    def __init__(self, db_path="spotify_data.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
            id TEXT PRIMARY KEY,
            name TEXT,
            artist TEXT
        )
        """)
        conn.commit()
        conn.close()

    def save_track(self, track: Track):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO tracks (id, name, artist) VALUES (?, ?, ?)",
            (track.id, track.name, track.artist),
        )
        conn.commit()
        conn.close()

    def get_all_tracks(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, artist FROM tracks")
        rows = cursor.fetchall()
        conn.close()
        return [Track(id=row[0], name=row[1], artist=row[2]) for row in rows]
