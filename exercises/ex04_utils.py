"""Creating Utility Functions."""


__author__ = "730569838"


def all(number_list: list[int], return_value: int) -> bool:
    """Returns true if all numbers match the indicated number, false if it is an empty list or numbers don't match."""
    index: int = 0
    if not number_list:
        return False
    while index < len(number_list):
        if number_list[index] != return_value:
            return False
        index = index + 1
    return True


def max(number: list[int]) -> int:
    """Finds the max number inside of a given list."""
    if len(number) == 0:
        raise ValueError("max() arg is an empty List")
    largest_number: int = number[0]
    count: int = 1
    while count < len(number):
        if largest_number < number[count]:
            largest_number = number[count]
        count = count + 1
    return largest_number


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Returns: True if lists are equal, False otherwise. Testing if the lists are exactly equal."""
    count: int = 0
    if len(first_list) == 0 and len(second_list) == 0:
        return True
    if len(first_list) != len(second_list):
        return False
    while len(first_list) == len(second_list):
        if first_list[count] != second_list[count]:
            return False
        if first_list[count] == second_list[count]:
            return True
        count = count + 1
    return True