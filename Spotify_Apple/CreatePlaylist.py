from Spotify import Spotify
import os

def main():

    spot_post = os.environ.get("spotify_post")
    spot_get = os.environ.get("spotify_get")

    spotify = Spotify(spot_post, spot_get)
    
    spotify.run_program()

if __name__ == "__main__":
    main()