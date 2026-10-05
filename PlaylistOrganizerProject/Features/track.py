class Track:
    def __init__(self, id, name, artist):
        self.id = id
        self.name = name
        self.artist = artist

    def __str__(self):
        return f"{self.name} - {self.artist}"
