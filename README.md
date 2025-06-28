# Music-Player-Backend
A backend service for a music player web application connected to a React frontend. It handles user authentication, song management, and secure media storage using Cloudinary.
---
## Features
- User registration and login with password hashing and JWT authentication
- Upload and manage songs, including title, artist, album cover, and audio URL
- Integration with Cloudinary for media file storage (images + audio)
- Song ownership via foreign key relationship to the user
- Routes for both users and songs
- Connected to a React frontend 

### Resources
---
- Navigate to 
```Bash
requirements.txt
```
- All requirements/tools are listed!
---
  ## How it works
### User Authentication (auth routes)
- (Flask):
- register_user: handles user creation, hashes the password, and stores it in the DB.
- login_user: validates credentials, returns a JWT token.
- get_profile uses token to identify the user and return their info.
---
### Music Handling (song routes)
- add_song uploads files to Cloudinary, saves song metadata + URLs + user ID in the DB.
- get_all_songs returns a list of songs with:
  title, artist, album_cover_url, audio_url
- search_songs filters songs based on the title or artist.
---
---

## API Endpoints

### Authentication Routes (`/api`)
| Method | Endpoint            | Description                        |
|--------|---------------------|------------------------------------|
| POST   | `/register`         | Register a new user                |
| POST   | `/login`            | Log in a user and return JWT cookie|
| GET    | `/profile`          | Get current user profile           |
| PUT    | `/profile`          | Update username/email              |
| PUT    | `/profile/password` | Change user password               |
| DELETE | `/profile`          | Delete user account                |

### Song Routes (`/api/songs`)
| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| GET    | `/songs`             | Get all songs (with optional `?q=`)|
| POST   | `/songs`             | Upload a new song + media          |
| GET    | `/songs/:id`         | Get single song details            |
| PUT    | `/songs/:id`         | Update song info                   |
| DELETE | `/songs/:id`         | Delete a song                      |

---

## Folder Structure

```
Music-Player-Backend/
.
├── app.py
├── config.py
├── controllers
│   ├── auth_controller.py
│   ├── __init__.py
│   └── song_controller.py
├── models
│   ├── db.py
│   ├── __init__.py
│   ├── song.py
│   └── user.py
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── requirements.txt
├── routes
│   ├── auth_routes.py
│   ├── __init__.py
│   └── song_routes.py
├── tests
│   └── test_routes.py
└── utils
    ├── auth.py
    └── cloudinary.py


```

---

## Dependencies

All packages needed are listed in:

```bash
requirements.txt
```

Install with:

```bash
pip install -r requirements.txt
```

Make sure your `.env` contains:

```env
JWT_SECRET_KEY=your_secret_key
DATABASE_URL=your_db_uri
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## Video Documentation

Watch a detailed walkthrough here:  
**[Reja Beats Backend Demo (Google Drive)](https://drive.google.com/file/d/1FOGogzFNxFLNR4a8U16DmaEhSi7nKMBT/view?usp=drivesdk)**

---

## Setup & Run

```bash
# Create virtual environment (if needed)
python -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run app
python app.py
```

App should be running on:  
`http://localhost:5000`

---

## Deployment

This project is deployable on **Render** or similar platforms.  
Make sure to:
- Enable **CORS** with `supports_credentials=True`
- Serve on `host='0.0.0.0'` and dynamic `PORT`
- Include `.env` variables in Render's environment tab

---

## Author

**Alex Njugi Karanja**  
[alexnjugi.com](https://alexnjugi.com)  
[LinkedIn](https://linkedin.com/in/alex-njugi-04521b367)  
[GitHub](https://github.com/alex-njugi)

---

_This backend is fully integrated with the React-based frontend: [Reja Beats Music Player](https://github.com/Music-Player-App/reja-beats-music-player)_







