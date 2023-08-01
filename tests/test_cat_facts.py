import requests
from lib.cat_facts import *
from unittest.mock import Mock

def test_provide():
    response = Mock()
    request = Mock()
    response = request.get.return_value
    response.json.return_value = {"fact":"The oldest cat to give birth was Kitty who, at the age of 30, gave birth to two kittens. During her life, she gave birth to 218 kittens.","length":136}
    cat_facts = CatFacts(request)
    assert cat_facts.provide() == "Cat fact: The oldest cat to give birth was Kitty who, at the age of 30, gave birth to two kittens. During her life, she gave birth to 218 kittens."