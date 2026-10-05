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
- Features/
- │── track.py           
- │── repository.py      
- │── service.py         
- │── view.py            
- Database.py            
- main.py                


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

Sample Screenshots:
-Empty Gui
<img width="614" height="439" alt="image_2026-10-05_180559453" src="https://github.com/user-attachments/assets/9eaa6a06-04f6-473a-8cce-67fb164c62fb" />
-Loaded Data
<img width="617" height="444" alt="image_2026-10-05_180625577" src="https://github.com/user-attachments/assets/e92b7aeb-c030-49ef-bd77-8b0209c96f6f" />
-Saved Data
<img width="619" height="449" alt="image_2026-10-05_180638127" src="https://github.com/user-attachments/assets/7eb1c150-ada7-4790-88f9-5981da78ef9a" />
-Data in Database
<img width="821" height="426" alt="image_2026-10-05_180702021" src="https://github.com/user-attachments/assets/04dcd058-2323-41a0-ae0e-9826de985ae9" />
-Data in txt File
<img width="646" height="264" alt="image_2026-10-05_180713384" src="https://github.com/user-attachments/assets/5bdb168e-1f35-4bde-8396-c5343486dd5f" />


