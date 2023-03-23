class Track: 

  #Represents a piece of music on Spotify

  def __init__(self, name, id, artist):
    """
    :param name: (str) Track name
    :param id: (int) Track ID 
    :param artist: (str) Artist name
    """

    self.name = name
    self.id = id
    self.artist = artist

  def __str__(self):
    return f"Track: {self.name} by {self.artist}"

  def create_spotify_uri(self):
    return f"spotify:track:{self.id}" 