import json

def save_to_file(data: list, file_name: str) -> None:
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


def load_from_file(file_name: str) -> dict:
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data