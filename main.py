import requests

host = "https://pokemonbattle.me:9104"
token = "66fb662e644ce0302e2576f01278f69b" 

## Создание покемона

answer = requests.post(f'{host}/pokemons', json = { 
    "name": "Лошара",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"}, 
headers= {"Content-Type" : "application/json", "trainer_token": token})
print(answer.text)


## Смена имени покемона

answer = requests.put(f'{host}/pokemons', json = { 
    "pokemon_id": "12847",
    "name": "Не лошара",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"}, 
headers= {"Content-Type" : "application/json", "trainer_token": token})
print(answer.text)


## Поймать покемона в покебол

answer = requests.post(f'{host}/trainers/add_pokeball', json = { 
    "pokemon_id": "12847"
    }, 
headers= {"Content-Type" : "application/json", "trainer_token": token})
print(answer.text)
