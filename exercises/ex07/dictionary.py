"""Creating functions with dictionaries."""


__author__ = "730569838"


def invert(first_dict: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and inverts it - the values become the keys and the keys become the values."""
    new_list: dict[str, str] = {}
    for values in first_dict:
        key: str = first_dict[values]
        if key in new_list:
            raise KeyError("KeyError. Key is not unique.")
        new_list[key] = values
    return new_list


def favorite_color(names_colors: dict[str, str]) -> str:
    """Takes a dictionary of names and favorite colors and returns the most common favorite color. If two tie, it gives the first one that comes up on the dictionary."""
    index: dict[str, str] = {}
    for values in names_colors:
        color: str = names_colors[values]
        if color in index:
            index[color] += 1
        else:
            index[color] = 1
    top: int = 0
    fav_color: str = ""
    for color in index:
        common = index[color]
        if common > top:
            top = common
            fav_color = color
    return fav_color


def count(given_list: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    new_dict: dict[str, int] = {}
    for values in given_list:
        if values in new_dict:
            new_dict[values] += 1
        else:
            new_dict[values] = 1
    return new_dict