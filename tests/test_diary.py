from lib.diary import *

def test_writing_diary_contents():
    diary = Diary('Today I studied coding')
    assert diary.contents == 'Today I studied coding'

def test_read_diary_contents():
    diary = Diary('Today I studied coding')
    assert diary.read() == 'Today I studied coding'