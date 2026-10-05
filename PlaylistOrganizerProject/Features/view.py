import sys
import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QTableWidget, QTableWidgetItem
from Features.repository import TrackRepository

class MusicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotify Music Data")
        self.setGeometry(200, 200, 600, 400)
        self.repo = TrackRepository()

        # Dark theme
        self.setStyleSheet("background-color: black; color: white;")

        layout = QGridLayout()

        # Table widget
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # adjust based on track fields
        self.table.setHorizontalHeaderLabels(["Title", "Artist", "Album"])  # example headers
        layout.addWidget(self.table, 0, 0, 1, 2)

        # Buttons
        self.load_button = QPushButton("Load Tracks")
        self.save_button = QPushButton("Save to File")
        layout.addWidget(self.load_button, 1, 0)
        layout.addWidget(self.save_button, 1, 1)

        self.setLayout(layout)

        # Connect signals
        self.load_button.clicked.connect(self.load_tracks)
        self.save_button.clicked.connect(self.save_tracks)

    def load_tracks(self):
        tracks = self.repo.get_all_tracks()
        self.table.setRowCount(len(tracks))  # set rows based on number of tracks

        for row, track in enumerate(tracks):
            # Assuming track is a dict or object with title, artist, album
            self.table.setItem(row, 0, QTableWidgetItem(str(track.title)))
            self.table.setItem(row, 1, QTableWidgetItem(str(track.artist)))
            self.table.setItem(row, 2, QTableWidgetItem(str(track.album)))

    def save_tracks(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        filename = f"music_compiled_{today}.csv"
        with open(filename, "w", encoding="utf-8") as f:
            # Write headers
            f.write("Title,Artist,Album\n")
            # Write table data
            for row in range(self.table.rowCount()):
                values = []
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    values.append(item.text() if item else "")
                f.write(",".join(values) + "\n")

def run_gui():
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())
