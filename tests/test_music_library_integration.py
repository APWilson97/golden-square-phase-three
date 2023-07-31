from lib.music_library import MusicLibrary
from lib.track import Track

"""Given two tracks to be added
track list of music library is properly set"""

def test_add_two_tracks():
    library = MusicLibrary()
    track1 = Track('Sade', 'Smooth Operator')
    track2 = Track('Kate Bush', 'Cloudbusting')
    library.add(track1)
    library.add(track2)
    assert library.track_list == [track1, track2]

"""Given three tracks added to the list
return a list of track instances matching keyword"""

def test_add_three_tracks_search_one_keyword():
    library = MusicLibrary()
    track1 = Track('Sade', 'Smooth Operator')
    track2 = Track('Kate Bush', 'Cloudbusting')
    track3 = Track('Kate Bush', 'Running Up The Hill')
    library.add(track1)
    library.add(track2) 
    library.add(track3)
    assert library.search('Kate Bush') == [track2, track3]

"""Given three tracks
return list of track instance matching partial keyword"""

def test_add_three_tracks_search_partial_keyword():
    library = MusicLibrary()
    track1 = Track('Sade', 'Smooth Operator')
    track2 = Track('Kate Bush', 'Cloudbusting')
    track3 = Track('Kate Bush', 'Running Up The Hill')
    library.add(track1)
    library.add(track2) 
    library.add(track3)
    assert library.search('Kate') == [track2, track3]

