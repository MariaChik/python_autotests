import requests
import pytest

host = "https://pokemonbattle.me:9104"
token = "66fb662e644ce0302e2576f01278f69b" 

def test_status_code_200():
    answer = requests.get(f'{host}/trainers', 
    headers= {"Content-Type" : "application/json", "trainer_token": token})
    assert answer.status_code == 200
    
def test_trainer_name():
    answer_body = requests.get(f'{host}/trainers', params = {"trainer_id" : 4640},
    headers = {"Content-Type" : "application/json", "trainer_token": token})
    assert answer_body.json()["trainer_name"] == "Машутка"