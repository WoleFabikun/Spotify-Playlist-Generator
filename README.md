#Spotify Playlist Generator
This script uses the Spotify API to generate a new playlist based on the user's recent Spotify listening history. The program allows the user to choose up to 10 tracks they recently listened to and then select up to five of these tracks as the "seed" for the new playlist. The program then generates a new playlist with recommended tracks based on the seed tracks.

##Prerequisites
Python 3
A Spotify Developer account (for access to the Spotify API)

##Setup
Clone the repository.
Create a virtual environment and activate it.
Install the required packages using the following command: pip install -r requirements.txt.
Create an application on the Spotify Developer Dashboard to obtain a client ID and a client secret.
Once you have created the application, add http://localhost:8000/callback to the list of Redirect URIs.
In the application settings, locate the client ID and client secret and add them to your environment variables as SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.
Run the script using the command python3 CreatePlaylist.py

##How to Use
When prompted, enter the number of tracks you would like to choose from your recent listening history (up to 10).
The program will display the last played tracks and their indexes. Choose up to five tracks by entering their indexes separated by spaces.
When prompted, enter the number of tracks you want in your new playlist (up to 100).
The program will display the recommended tracks based on the selected tracks and create a new playlist with the name you provided.


##Acknowledgments
This project was created as part of Valerio Velardo's Host of The Sound of AI course. 
