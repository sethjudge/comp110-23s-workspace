"""Challenge Question 4."""


__author__ = "730569838"


def zip(string_list: list[str], int_list: list[int]) -> dict[str, int]:
    if len(string_list) != len(int_list) or len(string_list) == 0:
        return dict()
    result: dict[str, int] = {}
    index: int = 0
    for word in string_list:
        result[word] = int_list[index]
        index += 1
    return result