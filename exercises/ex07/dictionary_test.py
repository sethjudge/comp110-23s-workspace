"""Tests for our dictionary functions."""


__author__ = "730569838"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert1():
    """Tests the invert function for if the given dictionary is empty that it will return an empty dictionary."""
    given_dict: dict[str, str] = {}
    return_dict: dict[str, str] = {}
    assert invert(given_dict) == return_dict


def test_invert2():
    """Tests the invert function for if all the string values are words and inverts them correctly."""
    given_dict: dict[str, str] = {"Brother": "Sister", "Dog": "Cat", "Panthers": "Patriots", "Blue": "Red"}
    return_dict: dict[str, str] = {"Sister": "Brother", "Cat": "Dog", "Patriots": "Panthers", "Red": "Blue"}
    assert invert(given_dict) == return_dict


def test_invert3():
    """Ensures that the invert test still inverts the dictionaries correctly even if all the strings are numbers."""
    given_dict: dict[str, str] = {"1": "2", "3": "4", "5": "6", "7": "8"}
    return_dict: dict[str, str] = {"2": "1", "4": "3", "6": "5", "8": "7"}
    assert invert(given_dict) == return_dict


def test_favorite_color1():
    """Ensures that if the favorite color function is given an empty dictionary then it will return an empty string."""
    given_dict: dict[str, str] = {}
    return_value: str = ""
    assert favorite_color(given_dict) == return_value


def test_favorite_color2():
    """Ensures that if there is a majority of one color then the favorite color function will return that color."""
    given_dict: dict[str, str] = {"Seth": "Blue", "Justin": "Red", "Chinmay": "Blue", "James": "Green"}
    return_value: str = "Blue"
    assert favorite_color(given_dict) == return_value


def test_favorite_color3():
    """Ensures that if there is a tie for majority of colors then the favorite color function will return the first color that came up of said colors that tied."""
    given_dict: dict[str, str] = {"Seth": "Blue", "Justin": "Red", "Chinmay": "Blue", "James": "Red"}
    return_value: str = "Blue"
    assert favorite_color(given_dict) == return_value


def test_count1():
    """Tests the count function to show that if an empty list is given, than an empty dictionary is returned."""
    given_list: list[str] = []
    return_value: dict[str, int] = {}
    assert count(given_list) == return_value


def test_count2():
    """Tests the count function to show that if all the values in the list are the same, only that item will be returned in the new dictionary with the number of times it appeared."""
    given_list: list[str] = ["dog", "dog", "dog", "dog"]
    return_value: dict[str, int] = {"dog": 4}
    assert count(given_list) == return_value


def test_count3():
    """Tests the count function to ensure that if a multitude of items are given in the list, it will sort them out correctly and count how many times they appear."""
    given_list: list[str] = ["dog", "cat", "zebra", "giraffe", "cat", "zebra", "cat"]
    return_value: dict[str, int] = {"cat": 3, "zebra": 2, "dog": 1, "giraffe": 1}
    assert count(given_list) == return_value