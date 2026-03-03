import plotly.graph_objects as go

TYPE_COLORS = {
    "normal": (211, 211, 211), # light gray
    "fire": (242, 51, 51), # red
    "water": (51, 51, 242), # blue
    "electric": (255, 250, 94), # yellow
    "grass": (126, 245, 103), # green
    "ice": (143, 226, 242), # light blue/turquoise
    "fighting": (232, 166, 74), # orange
    "poison": (165, 111, 227), # purple
    "ground": (196, 165, 122), # taupe
    "flying": (161, 208, 255), # light blue
    "psychic": (207, 141, 242), # magenta
    "bug": (91, 122, 102), # olive
    "rock": (108, 118, 128), # dark gray
    "ghost": (103, 69, 138), # darker purple
    "dragon": (75, 66, 133), # indigo
    "dark": (41, 39, 51), # black
    "steel": (94, 98, 125), # silver/grey
    "fairy": (235, 190, 218), # pink
}


def _filter_valid_pokemons(p_list: list) -> list:
    """Return a list of valid Pokémon dictionaries."""
    if not p_list:
        print("No Pokémon in list.")
        return []

    valid_pokemons = [p for p in p_list if p and "stats" in p and isinstance(p["stats"], dict)]
    if not valid_pokemons:
        print("No Pokémon with valid stats found.")
        return []

    return valid_pokemons


def _type_to_rgba(poke_type: str, alpha: float = 0.5) -> str:
    """Convert a named color to an RGBA string for Plotly."""
    rgb = TYPE_COLORS.get(poke_type.lower(), (128, 128, 128))  # default gray
    return f"rgba({rgb[0]},{rgb[1]},{rgb[2]},{alpha})"


def plot_poke_data(pokemon_list: list) -> None:
    fig = go.Figure()

    valid_pokemons = _filter_valid_pokemons(pokemon_list)
    if not valid_pokemons:
        return

    categories = list(valid_pokemons[0]["stats"].keys())

    for pokemon in valid_pokemons:
        values = list(pokemon['stats'].values())
        values += values[:1]
        categories_loop = categories + categories [:1]

        poke_type = pokemon["types"][0] if pokemon.get("types") else "normal"
        fill_rgba = _type_to_rgba(poke_type, alpha=0.4)  # semi-transparent fill
        line_rgba = _type_to_rgba(poke_type, alpha=1.0)

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories_loop,
            fill='toself',
            name=pokemon['name'],
            fillcolor=fill_rgba,
            line=dict(color=line_rgba, width=3),
            hovertemplate=(
                f"<b>{pokemon['name']} ({poke_type.capitalize()})</b><br>"
                "%{theta}: %{r}<br>"
                "<extra></extra>"
            )
        ))

        fig.update_layout(
            font=dict(
                family="Source Code Pro, Arial, sans-serif",
                size=14,
                color="black"
            )
        )

        fig.update_layout(
            title="pokemon stats comparison and visualizer",
            showlegend=True,
            template='plotly_white',
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0,150]
                )
            )
        )

    fig.show()