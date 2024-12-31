import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '329dc898210433a168fe558429213a39'
Header = {
    "Content-Type" : "application/json",
    "trainer_token":token
    }
pokemon = {
    "name":"Bob",
    "photo_id": 1
}
body_confirmation = {
    "trainer_token": token
}

def test_trainers():
    trainers = requests.get(url=f"{URL}/trainers",headers=Header)
    assert trainers.status_code == 200

def test_me_trainer():
    trainers = requests.get(url=f"{URL}/trainers?trainer_id=11644",headers=Header)
    assert trainers.status_code == 200
