"""EX04 List Utility Functions."""


__author__: str = "730464679"


def all(utility_list: list[int], utility: int) -> bool:
    """Defining a skeleton function."""
    if len(utility_list) == 0:
        return False
    idx: int = 0
    while idx < len(utility_list):
        if utility_list[idx] != utility:
            return False
        idx += 1
    return True
    

def max(utility_list: list[int]) -> int:
    """Defining another function."""
    if len(utility_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_number: int = utility_list[0]
    idx: int = 0
    while idx < len(utility_list):
        if utility_list[idx] > max_number:
            max_number = utility_list[idx]
        idx += 1
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Part 3 defining a function."""
    if len(list_1) and len(list_2) == 0:
        return True
    if len(list_1) != len(list_2):
        return False
    idx_1: int = 0
    idx_2: int = 0
    while idx_1 < len(list_1) and idx_2 < len(list_2):
        if list_1[idx_1] != list_2[idx_2]:
            return False
        idx_1 += 1
        idx_2 += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Defining function part 4."""
    idx: int = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])
        idx += 1