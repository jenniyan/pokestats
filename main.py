"""
main.py

Main entry point for PokeStats Studio.
Allows the user to enter Pokémon names, optionally save their data to a JSON file,
and visualize stats using the radar chart visualizer.
"""

from api import fetch_pokemon_data
from visualizer import plot_poke_data
from file_io import save_to_file, load_from_file


def main():
    print("welcome to pokestats studio!")
    pokemon_names = []
    save = False
    user_input = input("enter a pokemon name (or 'done'): ")
    pokemon_names.append(user_input)
    while user_input != "done" and len(pokemon_names) < 3:
        user_input = input("enter a pokemon name (or 'done'): ")
        if user_input != 'done':
            pokemon_names.append(user_input)
    save_choice = input("would you also like to save this pokemon data to a file on your computer? ('y'/'n'): ")
    if save_choice == 'y':
        save = True

    pokemon_data = []
    for pokemon in pokemon_names:
        data = fetch_pokemon_data(pokemon)
        pokemon_data.append(data)

    if save: 
        filename = 'pokemon_data.json'
        save_to_file(pokemon_data, filename)
        print(f"saved Pokémon data to '{filename}'")
    plot_poke_data(pokemon_data)


if __name__ == "__main__":
    main()