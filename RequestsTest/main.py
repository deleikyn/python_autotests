import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5ead39d664fd4c232b42281dca98f34a'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}


#Создание покемона
body_pok_create = {
    "name": "generate",
    "photo_id": -1
}

#Смена имени покемона (pokemon_id надо вводить вручную)
body_put = {
    "pokemon_id": "185521",
    "name": "New Name",
    "photo_id": 302
}

#Поймать покемона в покебол (pokemon_id надо вводить вручную)
body_pokeball = {
    "pokemon_id": "185521"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = body_pok_create)
print(response.text)'''

'''response_pokeball= requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_pokeball)
print(response_pokeball.text)'''

response_put= requests.put(url = f'{URL}/pokemons', headers = HEADER , json = body_put)
print(response_put.text)