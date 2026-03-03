"""
fileio.py

This module provides utility functions to save
and load data to and from JSON files.

Functions:
- save_to_file(data: list, file_name: str) -> None
    Save a list of JSON-serializable data to a file.

- load_from_file(file_name: str) -> dict
    Load JSON data from a file.

Author: Jennifer Yan
Email: jenniy16@uci.edu
"""

import json


def save_to_file(data: list, file_name: str) -> None:
    """
    Save a list of data to a JSON file.

    Parameters:
    - data : list
        The data to be saved. Each element should be JSON-serializable.
    - file_name : str
        The path or filename of the JSON file to write to.

    Returns:
    None

    Raises:
    - TypeError
        If `data` contains non-serializable objects.
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except TypeError as e:
        print(f"Error: data contains non-serializable objects. {e}")
        raise


def load_from_file(file_name: str) -> dict:
    """
    Abstracts data from a JSON file.

    Parameters:
    - file_name : str
        The path or filename of the JSON file to abstract from.

    Returns:
    - dict
        The data loaded from the JSON file

    Raises:
    - FileNotFoundError
        If the specified file does not exist.
    - TypeError
        If `data` contains non-serializable objects.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        print(f"Error: file '{file_name}' not found. {e}")
        raise
    except TypeError as e:
        print(f"Error: data contains non-serializable objects. {e}")
        raise
