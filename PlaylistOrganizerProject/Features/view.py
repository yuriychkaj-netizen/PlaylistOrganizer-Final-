import sys
import datetime
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QInputDialog
)
from PyQt6.QtGui import QPalette, QColor
from Features.repository import TrackRepository


class MusicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotify Music Data")
        self.setGeometry(200, 200, 600, 400)
        self.repo = TrackRepository()

        # Dark theme palette
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("black"))
        palette.setColor(QPalette.ColorRole.Base, QColor("black"))
        palette.setColor(QPalette.ColorRole.Text, QColor("white"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Text area
        self.text_area = QTextEdit()
        self.text_area.setStyleSheet("background-color: black; color: white;")
        layout.addWidget(self.text_area)

        # Buttons
        self.load_button = QPushButton("Load Tracks")
        self.save_button = QPushButton("Save to File")
        self.delete_button = QPushButton("Delete Track")

        # Style buttons
        for btn in (self.load_button, self.save_button, self.delete_button):
            btn.setStyleSheet("background-color: #333; color: white;")

        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

        # Connect signals
        self.load_button.clicked.connect(self.load_tracks)
        self.save_button.clicked.connect(self.save_tracks)
        self.delete_button.clicked.connect(self.delete_track)

    def load_tracks(self):
        tracks = self.repo.get_all_tracks()
        self.text_area.clear()
        for track in tracks:
            self.text_area.append(str(track))

    def save_tracks(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        filename = f"music_compiled_{today}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.text_area.toPlainText())
        self.text_area.append(f"\nSaved to {filename}")

    def delete_track(self):
        # Ask user for track ID or name
        track_id, ok = QInputDialog.getText(self, "Delete Track", "Enter Track ID to delete:")
        if ok and track_id:
            success = self.repo.delete_track(track_id)  # assumes repo has delete_track method
            if success:
                self.text_area.append(f"\nDeleted track with ID {track_id}")
                self.load_tracks()
            else:
                self.text_area.append(f"\nTrack with ID {track_id} not found.")


def run_gui():
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())
