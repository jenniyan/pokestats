from api import fetch_pokemon_data, save_to_file

if __name__ == "__main__":
    pokemon_names = []
    user_input = input("enter a pokemon name (or 'done'): ")
    pokemon_names.append(user_input)
    while user_input != "done":
        user_input = input("enter a pokemon name (or 'done'): ")
        if user_input != 'done':
            pokemon_names.append(user_input)
    for pokemon in pokemon_names:
        data = fetch_pokemon_data(pokemon)
        save_to_file(data, 'pokemon_data.json')