Spotify Playlist Organizer

Project Title
Spotify Playlist Organizer

Project Description
A desktop application that integrates with the Spotify API to fetch a user’s recently played and top tracks, store them in a local SQLite database, and organize them into playlists.  
It provides an offline‑friendly way to automatically generate and manage playlists based on listening habits, outside of Spotify’s native app.

Project Objectives
- Fetch Spotify listening data (recently played and top tracks).
- Store track information in a local SQLite database.
- Organize tracks into playlists automatically.
- Provide a GUI for viewing, managing, and exporting playlists.
- Allow exporting playlists into CSV files for offline use.

Features
- **Spotify API Integration**: Fetches recent and top tracks using OAuth authentication.
- **Database Storage**: Saves track data into SQLite for persistence.
- **Playlist Organization**: Automatically compiles playlists based on listening history.
- **GUI Display**: Dark‑themed PyQt6 interface with a table view of playlists.
- **Export Functionality**: Save playlists into CSV files named `music_compiled_<date>.csv`.

Technologies Used
- Programming Language: Python  
- GUI Framework: PyQt6  
- Database: SQLite  
- Other Libraries:  
  - `spotipy` (Spotify API client)  
  - `sqlite3` (database operations)  
  - `pathlib` (file path handling)  

Project Structure:
Features/
- │── track.py           - Track class definition
- │── repository.py      - TrackRepository class for database operations
- │── service.py         - SpotifyService class for API integration
- │── view.py            - MusicApp GUI implementation
- Database.py            - Database class for user authentication table
- main.py                - Entry point, runs SpotifyService and GUI


- track.py → Defines the `Track` object.  
- repository.py → Handles CRUD operations for tracks in SQLite.  
- service.py → Connects to Spotify API and organizes playlists.  
- view.py → PyQt6 GUI for displaying and exporting playlists.  
- Database.py → Manages user authentication table.  
- main.py → Runs the service and launches the GUI.  

Installation and Setup:
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   
2. Install dependencies:
 - pip install spotipy PyQt6

3. Set up Spotify API credentials:
 - Create a Spotify Developer account.
 - Register an app and get CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI.
 - Replace values in main.py

4. Run it

How to Use:
1. Launch the application with python main.py.
2. Authenticate with Spotify (first run).
3. Click Load Tracks to display stored tracks.
4. Playlists are automatically organized based on listening history.
5. Click Save to File to export playlists into a CSV file.

OOP Implementation:
- Track → Represents a music track (encapsulation of id, name, artist).
- TrackRepository → Encapsulates database operations (CRUD).
- SpotifyService → Handles Spotify API integration and playlist organization.
- MusicApp → GUI class for displaying and exporting playlists.
- Database → Manages user authentication table.
- Encapsulation: Each class hides its internal logic (database connection inside TrackRepository).
- Inheritance: MusicApp inherits from QWidget (PyQt6).
- Polymorphism: GUI buttons trigger different methods (load_tracks, save_tracks) depending on user action.

Database:
Tables:
- users → Stores authentication info (id, username, password).
- tracks → Stores Spotify track data (id, name, artist).

Operations:
- Create: Tables created if not exist.
- Read: Fetch all tracks from database.
- Update: Insert or replace tracks.
- Delete: Not yet implemented.
