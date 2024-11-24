from datetime import datetime
from typing import Dict

class Song:
    def __init__(self, id: str, name: str, artist: str, genre: str):
        self.id = id
        self.name = name
        self.artist = artist
        self.genre = genre
        
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "artist": self.artist,
            "genre": self.genre
        }
