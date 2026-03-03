import urllib.request
import json

API_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon_data(pokemon: str) -> dict:
    url_name = API_URL + str(pokemon)
    req = urllib.request.Request(
        url_name,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = resp.read().decode()
        api_data_obj = json.loads(resp_data)
        return api_data_obj
    except urllib.error.HTTPError as e:
        raise ValueError(f"Pokémon '{pokemon}' not found.") from e


def save_to_file(data: list, file_name: str) -> None:
    with open(file_name, 'a') as f:
        json.dump(data, f, indent=4)


def load_from_file(file_name: str) -> list:
    pass