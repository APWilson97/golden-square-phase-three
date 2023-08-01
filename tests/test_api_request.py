from lib.api_request import *
from unittest.mock import Mock
import time
import requests

def test_get_server_time():
    request = Mock()
    response = Mock()
    json = Mock()
    request.get.return_value = response
    response.json.return_value = {"abbreviation":"BST","client_ip":"82.163.117.26","datetime":"2023-08-01T14:21:24.774875+01:00","day_of_week":2,"day_of_year":213,"dst":True,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":0,"timezone":"Europe/London","unixtime":1690896084,"utc_datetime":"2023-08-01T13:21:24.774875+00:00","utc_offset":"+01:00","week_number":31}
    json = response.json.return_value['unixtime']
    assert json == 1690896084

def test_error():
    timer = Mock()
    timer.time.return_value = 1690898557
    request = Mock()
    response = Mock()
    request.get.return_value = response
    response.json.return_value = {"unixtime":1690896084}
    time_error = TimeError(request, timer)
    result = time_error.error()
    assert result == 1690896084 - 1690898557