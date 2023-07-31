from lib.music_library import MusicLibrary
from unittest.mock import Mock

"""When initialising an instance of MusicLibrary
track_list property should be empty list"""

def test_inital_empty_list():
    library = MusicLibrary()
    assert library.track_list == []

"""Given an empty track list
searches keyword should return empty list"""

def test_empty_list_search_one_keyword():
    library = MusicLibrary()
    assert library.search('Kate Bush') == []

"""Given three tracks
searches for keyword should return list with matches"""

def test_three_tracks_two_matches_with_keyword():
    library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.matches.return_value = True

    fake_track2 = Mock()
    fake_track2.matches.return_value = False

    fake_track3 = Mock()
    fake_track3.matches.return_value = True

    library.add(fake_track1)
    library.add(fake_track2)
    library.add(fake_track3)

    assert library.search('Kate') == [fake_track1, fake_track3]

"""Given two tracks
Successfully add them to list and list property should be correctly set"""

def test_two_tracks_added():
    library = MusicLibrary()
    fake_track1 = Mock()
    fake_track2 = Mock()

    library.add(fake_track1)
    library.add(fake_track2)
    assert library.track_list == [fake_track1, fake_track2]