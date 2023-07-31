from lib.track import Track
from unittest.mock import Mock

"""Given a title and artist
title and artist properties should be set correctly"""

def test_add_track_artist():
    track1 = Track('Smooth Operator', 'Sade')
    assert track1.title == 'Smooth Operator'
    assert track1.artist == 'Sade'

"""Given a keyword
should return true for matching keyword"""

def test_matching_keyword():
    track1 = Track('Smooth Operator', 'Sade')
    assert track1.matches('Sade') == True

def test_non_matching_keyword():
    track1 = Track('Smooth Operator', 'Sade')
    assert track1.matches('Kate') == False