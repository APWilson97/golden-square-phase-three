from lib.secret_diary import *
from unittest.mock import Mock
import pytest

def test_secret_diary_is_set_properly():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary._diary == fake_diary
    assert secret_diary.locked == True

def test_secret_diary_is_properly_locked_at_the_start():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    with pytest.raises(Exception) as error:
        secret_diary.read()
    error_message = str(error.value)
    assert error_message == 'Go away!'

def test_secret_diary_unlocks_properly():
    fake_diary = Mock()
    fake_diary.contents = 'Hello'
    fake_diary.read.return_value = 'Hello'
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Hello'

def test_secret_diary_locks_properly():
    fake_diary = Mock()
    fake_diary.contents = 'Hello'
    fake_diary.read.return_value = 'Hello'
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as error:
        secret_diary.read()
    error_message = str(error.value)
    assert error_message == 'Go away!'
    