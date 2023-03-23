class Playlist :
  #Playlist represents Spotify playlist

  def __init__(self, name, id): 
    """
    :param name: (str) Playlist name
    :param id: (int) Playlist ID
    """
    self.name = name
    self.id = id
  
  def __str__(self):
    return f"Playlist: {self.name}"