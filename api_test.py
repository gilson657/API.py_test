import pytest
import requests

# URLs das APIs públicas que serão testadas
RICK_AND_MORTY_API_URL = "https://rickandmortyapi.com/api/character/1"  # API de Rick and Morty
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/ditto"             # API de Pokémon
JOKES_API_URL = "https://official-joke-api.appspot.com/jokes/random"    # API de Piadas
RANDOM_USER_API_URL = "https://randomuser.me/api/"                      # API de Usuários Aleatórios
CAT_FACTS_API_URL = "https://meowfacts.herokuapp.com/"                  # API de Fatos sobre Gatos

# Função auxiliar para testar o status code
def verifica_status(response, status_code=200):
    assert response.status_code == status_code

# Testes de Integração

# Teste para a API Rick and Morty (primeiro teste)
def test_rick_and_morty_character():
    response = requests.get(RICK_AND_MORTY_API_URL)
    verifica_status(response)
    data = response.json()
    assert data["name"] == "Rick Sanchez"  # Valida o nome do personagem
    assert "status" in data
    assert "species" in data

#  Teste para a API de Pokémon (segundo teste)
def test_pokemon_info():
    response = requests.get(POKEMON_API_URL)
    verifica_status(response)
    data = response.json()
    assert data["name"] == "ditto"
    assert "abilities" in data

# Teste para a API de Piadas (terceiro teste)
def test_joke_api():
    response = requests.get(JOKES_API_URL)
    verifica_status(response)
    data = response.json()
    assert "setup" in data
    assert "punchline" in data

# Teste para a API de Usuário Aleatório (quarto teste)
def test_random_user():
    response = requests.get(RANDOM_USER_API_URL)
    verifica_status(response)
    data = response.json()
    assert "results" in data
    assert "name" in data["results"][0]

# Teste para a API de Fatos sobre Gatos (quinto teste)
def test_cat_fact():
    response = requests.get(CAT_FACTS_API_URL)
    verifica_status(response)
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
