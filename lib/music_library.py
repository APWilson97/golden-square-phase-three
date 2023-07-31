from lib.track import Track

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.track_list = []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        self.track_list.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        valid_tracks = [track for track in self.track_list if track.matches(keyword) == True]
        return valid_tracks
