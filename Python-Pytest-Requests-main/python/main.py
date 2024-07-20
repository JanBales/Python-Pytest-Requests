import requests

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "26090513d2ed0fda15a3e67122aded17"
header = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_put = {
    "pokemon_id": "42357",
    "name": "Yaaar3",
    "photo_id": 3
}
body_add_pokeball = {
    "pokemon_id": "42357"
}



# Создание покемона
response = requests.post(url = f'{URL}pokemons', headers = header, json = body_create)

print(response.json)


#Изменение покемона
response = requests.put(url = f'{URL}pokemons', headers = header, json = body_put)

print(response.json)


#поймать покемона в покебол
response = requests.post(url = f'{URL}trainers/add_pokeball', headers = header, json =  body_add_pokeball)

print(response.json)









