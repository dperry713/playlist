from datetime import datetime
from typing import List, Dict
from .song import Song

class Playlist:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.songs: List[Song] = []
        self.created_at = datetime.now()
        
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "songs": [song.to_dict() for song in self.songs],
            "created_at": self.created_at.isoformat()
        }
