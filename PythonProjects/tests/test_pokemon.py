import pytest
import requests
import json

URL = 'https://api.pokemonbattle.ru/v2'

def test_trainers():
    trainers = requests.get(url=f"{URL}/trainers")
    assert trainers.status_code == 200

def test_me_trainer():
    trainer = requests.get(url=f"{URL}/trainers?trainer_id=11644")
    trainer = json.loads(trainer.text)
    assert trainer["data"][0]["trainer_name"] == 'DIO'


def test_trainers():
    trainers = requests.get(url=f"{URL}/trainers",headers=Header)
    assert trainers.status_code == 200

def test_me_trainer():
    trainers = requests.get(url=f"{URL}/trainers?trainer_id=11644",headers=Header)
    assert trainers.status_code == 200
