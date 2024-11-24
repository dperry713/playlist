from flask import Blueprint

bp = Blueprint('song', __name__)

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
@bp.route('/song')
def song():
    # code for the song route
    pass