"""
api.py

This module provides functions to fetch Pokémon data from the PokeAPI.

Functions:
- fetch_pokemon_data(pokemon: str) -> dict
    Retrieve stats and type information for a given Pokémon.
"""

import urllib.request
import json

API_URL = "https://pokeapi.co/api/v2/pokemon/"


def fetch_pokemon_data(pokemon: str) -> dict:
    """
    Fetch Pokémon data from the PokeAPI.

    Parameters:
    - pokemon : str
        The name or Pokemon whose data to fetch

    Returns:
    - dict
        A dictionary containing:
        - "name": Pokémon name (str)
        - "types": List of Pokémon types (List[str])
        - "stats": Dictionary of stat name -> base_stat (Dict[str, int])
        Returns None if the Pokémon is not found or there is an HTTP error.

    Raises:
    - urllib.error.URLError
        If there is a network problem (e.g., no internet connection).
    - urllib.error.HTTPError
        If the requested pokemon is not found
    """
    url_name = API_URL + str(pokemon)
    req = urllib.request.Request(
        url_name,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = resp.read().decode()
            api_data_obj = json.loads(resp_data)
            types = []
            stats = {}

            for t in api_data_obj['types']:
                types.append(t["type"]["name"])
            for s in api_data_obj['stats']:
                stats[s['stat']['name']] = s['base_stat']

            return {
                "name": pokemon,
                'types': types,
                'stats': stats
            }
    except urllib.error.HTTPError:
        print(f"Pokémon '{pokemon}' not found.")
        return None
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        return None
