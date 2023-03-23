import json
import requests

from Track import Track
from Playlist import Playlist


class Spotify:

    def __init__(self, spotify_api, user_id):
        """
        :param spotify_api (str): Spotify API token
        :param user_id (str): Spotify user id
        """
        self.spotify_api = spotify_api
        self.user_id = user_id

    def get_username(self):
        """
        :return username (str): Spotify username
        """
        url = "https://api.spotify.com/v1/me"
        response = self.get_api_request(url)
        response_json = response.json()
        return response_json["id"]
    

    def get_last_played(self, limit=10):
        """
        :param limit (int): Number of tracks to get. 
        :return tracks: list of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self.get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                track in response_json['items']]
        return tracks

    def get_track_recommendations(self, seed_tracks, limit):
        """
        :param seed_tracks (list of Track): Reference tracks to get recommendations. Should be 5 or less.
        :param limit (int): Number of recommended tracks to be returned
        :return tracks: list of recommended tracks
        """
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self.get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for
                track in response_json["tracks"]]
        return tracks

    def create_playlist(self, name):
        """
        :param name (str): New playlist name
        :return playlist: (Playlist): Newly created playlist
        """
        data = json.dumps({
            "name": name,
            "description": "Recommended songs",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.get_username()}/playlists"
        response = self.post_api_request(url, data)
        response_json = response.json()

        # create playlist
        playlist_id = (response_json["id"])
        playlist = Playlist(name, playlist_id)
        return playlist

    def populate_playlist(self, playlist, tracks):
        """
        :param playlist (Playlist): Playlist to which to add tracks
        :param tracks (list of Track): Tracks to be added to playlist
        :return response: API response
        """
        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self.post_api_request(url, data)
        response_json = response.json()
        return response_json

    def get_api_request(self, url):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.spotify_api}"
        }
        params = {
            "limit": 10,
            "offset": 0
        }
        response = requests.get(url, headers=headers, params=params)
        return response

    def post_api_request(self, url, input):
        response = requests.post(
            url,
            data=input,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_api}"
            }
        )
        return response

    def run_program(self):
        # get last played tracks
        choose_tracks = int(input("How many tracks would you like to choose from your recently played tracks? Max number of tracks is 10: "))
        while int(choose_tracks) > 10:
            choose_tracks = int(input("\nError: Max number of tracks exceeded. Try Again: "))
        last_played_tracks = self.get_last_played(choose_tracks)

        print(f"\n Here are the last {choose_tracks} tracks you listened to on Spotify:")
        for index, track in enumerate(last_played_tracks):
            print(f"{index+1} - {track}")

        # choose which tracks to use as a seed to generate a playlist
        indexes = input("\nChoose up to 5 tracks you'd like to use as input. Separate each number with a space: ")
        indexes = indexes.split()
        seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

        # get recommended tracks based off seed tracks
        num_tracks = input("\nHow many tracks do you want in your new playlist? Max number of tracks is 100: ")
        while int(num_tracks) > 100:
            num_tracks = input("\nError: Max number of tracks exceeded. Try Again: ")
        recommended_tracks = self.get_track_recommendations(seed_tracks, num_tracks)
        print("\nHere are the recommended tracks which will be included in your new playlist:")
        for index, track in enumerate(recommended_tracks):
            print(f"{index+1} - {track}")

        # get playlist name from user and create playlist
        playlist_name = input("\nWhat would you like to name your new playlist? ")
        playlist = self.create_playlist(playlist_name)

        print(f"\n'{playlist.name}' was successfully created and added to your library. Enjoy!")

        self.populate_playlist(playlist, recommended_tracks)

