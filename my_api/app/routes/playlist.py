from flask import Blueprint

bp = Blueprint('playlist', __name__)

@bp.route('/playlist')
def playlist():
    # code for the playlist route
    pass