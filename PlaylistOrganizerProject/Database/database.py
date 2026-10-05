import sqlite3
from pathlib import Path


class Database:
    def __init__(self, database_path: str | Path | None = None):
        self.database_path = (
            Path(database_path)
            if database_path is not None
            else Path(__file__).resolve().parent / "spotify_data.db"
        )

    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def create_tables(self) -> None:
        with self.connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                );
                """
            )