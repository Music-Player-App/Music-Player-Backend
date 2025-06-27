from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import db
from models.song import Song
from utils.cloudinary import upload_mp3

@jwt_required()
def add_song():
    title = request.form.get("title")
    artist = request.form.get("artist")
    album_cover = request.form.get("album_cover") or ""  # Optional
    file = request.files.get("file")

    # Validate input
    if not title or not artist or not file:
        return jsonify({"error": "Title, artist, and MP3 file are required."}), 400

    if not file.filename.lower().endswith(".mp3"):
        return jsonify({"error": "Only MP3 files are allowed."}), 400

    try:
        url = upload_mp3(file)
    except Exception as e:
        return jsonify({"error": f"Cloudinary upload failed: {str(e)}"}), 500

    user_id = get_jwt_identity()

    song = Song(
        title=title,
        artist=artist,
        album_cover=album_cover,
        url=url,
        user_id=user_id
    )
    db.session.add(song)
    db.session.commit()

    return jsonify(song.serialize()), 201


def get_all_songs():
    songs = Song.query.all()
    return jsonify([song.serialize() for song in songs]), 200


def search_songs():
    query = request.args.get("q", "")
    if not query:
        return get_all_songs()

    query = query.lower()
    songs = Song.query.filter(
        (Song.title.ilike(f"%{query}%")) |
        (Song.artist.ilike(f"%{query}%"))
    ).all()

    return jsonify([song.serialize() for song in songs]), 200
