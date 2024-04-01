"""Practice with dictionary functions."""


__author__: str = "730464679"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Return inverted list."""
    dict_2: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in dict_2:
            raise KeyError("Incorrect key found, cannot invert")
        dict_2[dict_1[key]] = key
    return dict_2


def favorite_color(dict_1: dict[str, str]) -> str:
    """Return most frequent color in dict."""
    dict_2: dict[str, int] = {}    
    popular_color: str = ""
    max_counter: int = 0
    for key in dict_1:
        color: str = dict_1[key]
        if color in dict_2:
            dict_2[color] += 1
        else:
            dict_2[color] = 1
    for key in dict_2:
        if dict_2[color] > max_counter:
            max_counter = dict_2[key]
            popular_color = key
    return popular_color


def count(list_1: list[str]) -> dict[str, int]:
    """Return a dictionary of counts of each item."""
    new_dict: dict[str, int] = {}
    for key in list_1:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1
    return new_dict


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Return a dictionary of letters and list of words."""
    dict_1: dict[str, list[str]] = {}
    for key in list_1:
        first: str = key[0].lower()
        if first in dict_1:
            dict_1[first].append(key)   
        else:
            dict_1[first] = [key]
    return dict_1


def update_attendance(dict_1: dict[str, list[str]], day: str, student: str) -> None:
    """Mutate current dictionary to update present students."""
    if day in dict_1:
        dict_1[day].append(student)
    else:
        dict_1[day] = [student]