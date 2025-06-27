from flask import Blueprint
from controllers.song_controller import add_song, search_songs  

song_bp = Blueprint("songs", __name__, url_prefix="/api")

song_bp.route("/songs", methods=["POST"])(add_song)
song_bp.route("/songs", methods=["GET"])(search_songs) 
