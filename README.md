# Spotify Playlist Generator
This script uses the Spotify API to generate a new playlist based on the user's recent Spotify listening history. The program allows the user to choose up to 10 tracks they recently listened to and then select up to five of these tracks as the "seed" for the new playlist. The program then generates a new playlist with recommended tracks based on the seed tracks.

## Prerequisites
- Python 3
- A Spotify Developer account (for access to the Spotify API)

## Setup
-Clone the repository.

-Create a virtual environment and activate it.

-Use these links to obtain the Spotify Access tokens for your account:

  spotify_get: https://developer.spotify.com/console/get-current-user/
  
  spotify_post: https://developer.spotify.com/console/post-playlists/?user_id=&body=%7B%0A%20%20%22name%22%3A%20%22New%20Playlist%22%2C%0A%20%20%22description%22%3A%20%22Recommended%20Songs%22%2C%0A%20%20%22public%22%3A%20True%0A%7D
  
-Fill in these scopes:

<img width="577" alt="Screen Shot 2023-03-23 at 2 03 41 AM" src="https://user-images.githubusercontent.com/115600563/227128122-f0b47453-978e-4bd9-92e1-47ce6adb84e8.png">

-Copy each token and assign it to the respective environmental variable using this command in the terminal:

  export spotify_get={your get access token]
  
  export spotify_post={your post access token}

-Run the script using this command:

python3 CreatePlaylist.py

## How to Use
When prompted, enter the number of tracks you would like to choose from your recent listening history (up to 10).
The program will display the last played tracks and their indexes. Choose up to five tracks by entering their indexes separated by spaces.
When prompted, enter the number of tracks you want in your new playlist (up to 100).
The program will display the recommended tracks based on the selected tracks and create a new playlist with the name you provided.


## Acknowledgments
This project was created as part of Valerio Velardo's Host of The Sound of AI course. 
