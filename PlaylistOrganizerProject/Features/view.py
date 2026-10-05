import sys
import datetime
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit
)
from PyQt6.QtGui import QPalette, QColor
from Features.repository import TrackRepository

class MusicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spotify Music Data")
        self.setGeometry(200, 200, 600, 400)
        self.repo = TrackRepository()

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("black"))
        palette.setColor(QPalette.ColorRole.Base, QColor("black"))
        palette.setColor(QPalette.ColorRole.Text, QColor("white"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.text_area = QTextEdit()
        self.text_area.setStyleSheet("background-color: black; color: white;")
        layout.addWidget(self.text_area)

        self.load_button = QPushButton("Load Tracks")
        self.save_button = QPushButton("Save to File")

        self.load_button.setStyleSheet("background-color: #333; color: white;")
        self.save_button.setStyleSheet("background-color: #333; color: white;")

        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        self.load_button.clicked.connect(self.load_tracks)
        self.save_button.clicked.connect(self.save_tracks)

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


def run_gui():
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())
