My API
A Flask API project for managing playlists.

Table of Contents
Installation
Usage
Endpoints
Contributing
License
Installation
To install the project, run the following command:

bash
CopyInsert in Terminal
pip install -r requirements.txt
Usage
To run the API, execute the following command:

bash
CopyInsert in Terminal
python run.py
This will start the Flask development server, and you can access the API at http://localhost:5000.

Endpoints
The API has the following endpoints:

/playlist: Returns a list of all playlists.
/playlist/<id>: Returns a single playlist by ID.
/song: Returns a list of all songs.
/song/<id>: Returns a single song by ID.
