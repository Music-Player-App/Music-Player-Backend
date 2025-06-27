# Music-Player-Backend
A backend service for a music player web application connected to a React frontend. It handles user authentication, song management, and secure media storage using Cloudinary.
---
## Features
- User registration and login with password hashing and JWT authentication
- Upload and manage songs, including title, artist, album cover, and audio URL
- Integration with Cloudinary for media file storage (images + audio)
- Song ownership via foreign key relationship to the user
- Routes for both users and songs
- Connected to a React frontend for UI and playback

## How it works
### User Authentication (auth routes)
- Backend (Flask):
  register_user handles user creation, hashes the password, and stores it in the DB.








