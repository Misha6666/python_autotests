import requests
import json
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

create = requests.post(url=f'{URL}/pokemons', headers=Header, json=pokemon).text
print(create)
create = json.loads(create)
change_json = {
"pokemon_id": create["id"],
"name": "Bob2",
"photo_id": 2
}
change = requests.put(url=f"{URL}/pokemons",headers=Header, json=change_json)
print(change.text)
add_json = {
    "pokemon_id": create["id"]
}
add = requests.post(url=f"{URL}/trainers/add_pokeball",headers=Header,json=add_json)
print(add.text)