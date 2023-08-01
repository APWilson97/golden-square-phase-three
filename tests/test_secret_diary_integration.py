from lib.secret_diary import *
from lib.diary import *
import pytest

"""Given a diary instance
It should be set properly to it diary property"""

def test_add_diary():
    diary = Diary('Today I studied coding')
    secret_diary = SecretDiary(diary)
    assert secret_diary._diary == diary

def test_secret_diary_is_initially_locked():
    diary = Diary('Today I studied coding')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as error:
        secret_diary.read()
    error_message = str(error.value)
    assert error_message == 'Go away!'

def test_secret_diary_is_unlocked():
    diary = Diary('Today I studied coding')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Today I studied coding'

def test_secret_diary_unlocked_then_locked():
    diary = Diary('Today I studied coding')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as error:
        secret_diary.read()
    error_message = str(error.value)
    assert error_message == 'Go away!'