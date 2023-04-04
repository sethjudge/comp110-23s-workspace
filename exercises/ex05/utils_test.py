"""Creating unit tests."""


__author__ = "730569838"


from utils import only_evens, concat, sub


def only_evens_test_1() -> None:
    """Tests that only_evens returns an empty list if given an empty list."""
    assert only_evens([]) == []


def only_evens_test_2() -> None:
    """Second test of only_evens to test if it will return a 2 value list of even numbers."""
    assert only_evens([1, 3, 4, 5, 6]) == [4, 6]


def only_evens_test_3() -> None:
    """Final test of only_evens to see if it will return only one even value."""
    assert only_evens([1, 5, 7, 9, 12]) == [2, 12]


def concat_test_1() -> None:
    """Test to ensure that if 2 empty lists were given, then an empty list is returned."""
    assert concat([], []) == []


def concat_test_2() -> None:
    """Second concat test to ensure that 2 3 value lists will be concatenated together in the correct order."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def concat_test_3() -> None:
    """Final concat test to ensure that if 2 lists with random values are concatenated together, the return list will be in the correct order, from left to right."""
    assert concat([2, 9, 14], [3, 3, 1]) == [2, 9, 14, 3, 3, 1]


def sub_test_1() -> None:
    """Test to ensure that if the given list is empty, an empty list will be returned no matter what index values are given."""
    assert sub([], 1, 3) == []


def sub_test_2() -> None:
    """Second sub test to ensure that the sub function works as intended, giving a new list based on the start and end index given."""
    assert sub([1, 2, 3, 4, 5], 1, 3) == [2, 3]


def sub_test_3() -> None:
    """Final sub test to ensure that if the entire index of the list is given, then sub function will return the entire list."""
    assert sub([1, 2, 3, 4, 5], 0, 5) == [1, 2, 3, 4, 5]