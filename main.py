"""
main.py

Main entry point for PokeStats Studio.
Allows the user to enter Pokémon names,
optionally save their data to a JSON file,
and visualize stats using the radar chart visualizer.
"""

from api import fetch_pokemon_data
from visualizer import plot_poke_data
from file_io import save_to_file


def main():
    """
    Main function to run PokeStats Studio.

    Workflow:
    1. Prompt the user to enter Pokémon names (max 3).
    2. Ask if the user wants to save the fetched data.
    3. Fetch Pokémon data using the PokeAPI.
    4. Save data to a local JSON file if requested.
    5. Generate and save a radar chart visualization of the Pokémon stats.

    Notes:
    - If a Pokémon name is invalid, fetch_pokemon_data will return None.
    - The maximum number of Pokémon compared is currently set to 3
      to avoid overcrowding the radar chart.
    """
    print("welcome to pokestats studio!")
    pokemon_names = []
    save = False

    # step 1: collect pokemon names from the user
    user_input = input("enter a pokemon name (or 'done'): ")
    pokemon_names.append(user_input)

    # keep prompting for names unless input is 'done' or they reach max of 3
    while user_input != "done" and len(pokemon_names) < 3:
        user_input = input("enter a pokemon name (or 'done'): ")
        if user_input != 'done':
            pokemon_names.append(user_input)

    # step 2: ask if user wants to save fetched data
    save_choice = input("would you also like to save this pokemon data"
                        "to a file on your computer? ('y'/'n'): ")
    if save_choice == 'y':
        save = True

    # step 3: fetch pokemon data
    pokemon_data = []
    graph_file_name = 'pokemon-graph'
    for pokemon in pokemon_names:
        graph_file_name += f'-{pokemon}'
        data = fetch_pokemon_data(pokemon)
        pokemon_data.append(data)

    # step 4: save data if requested
    if save:
        filename = 'pokemon_data.json'
        save_to_file(pokemon_data, filename)
        print(f"saved Pokémon data to '{filename}'")

    # step 5: visualize data
    graph_file_name += '.html'
    plot_poke_data(pokemon_data, graph_file_name)


if __name__ == "__main__":
    main()
