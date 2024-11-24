from typing import Dict, List, Optional
from app.models.song import Song
from app.models.playlist import Playlist

class Database:
    def __init__(self):
        self.songs: Dict[str, Song] = {}
        self.playlists: Dict[str, Playlist] = {}
        
    def binary_search_songs(self, songs: List[Song], key: str, value: str) -> Optional[Song]:
        """Binary search implementation for sorted song lists"""
        songs_sorted = sorted(songs, key=lambda x: getattr(x, key).lower())
        left, right = 0, len(songs_sorted) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_val = getattr(songs_sorted[mid], key).lower()
            
            if mid_val == value.lower():
                return songs_sorted[mid]
            elif mid_val < value.lower():
                left = mid + 1
            else:
                right = mid - 1
        return None

    def quick_sort_songs(self, songs: List[Song], key: str) -> List[Song]:
        """QuickSort implementation for sorting songs"""
        if len(songs) <= 1:
            return songs
            
        pivot = songs[len(songs)//2]
        pivot_val = getattr(pivot, key).lower()
        
        left = [song for song in songs if getattr(song, key).lower() < pivot_val]
        middle = [song for song in songs if getattr(song, key).lower() == pivot_val]
        right = [song for song in songs if getattr(song, key).lower() > pivot_val]
        
        return self.quick_sort_songs(left, key) + middle + self.quick_sort_songs(right, key)
from typing import Dict, List, Optional
        

        
class Database:
            def __init__(self):
                self.songs: Dict[str, Song] = {}
                self.playlists: Dict[str, Playlist] = {}
                
            # Binary search implementation for sorted song lists
            def binary_search_songs(self, songs: List[Song], key: str, value: str):
                # implement binary search
                pass
                
            # QuickSort implementation for sorting songs
            def quick_sort_songs(self, songs: List[Song], key: str):
                # implement quick sort
                pass