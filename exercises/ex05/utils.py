"""Creating new utility functions and using unit tests on them."""


__author__ = "730569838"


def only_evens(number_list: list[int]) -> list[int]:
    """Goes through the given list and returns a list with only the even numbers from said list."""
    count: int = 0
    even_list: list[int] = []
    while count < len(number_list):
        if number_list[count] % 2 == 0:
            even_list.append(number_list[count])
        count = count + 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Returns a list with all elements of the first list followed by all elements of the second list."""
    final_list = list1 + list2
    return final_list


def sub(number_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a List which is a subset of the given list, between the specified start index and the end index - 1."""
    new_list = number_list[start_index:end_index]
    return new_list