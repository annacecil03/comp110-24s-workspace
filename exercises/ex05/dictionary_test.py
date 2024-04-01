"""Using EX05's variables to make test cases for each of the variables."""
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


__author__: str = "730464679"


def test_invert_use_case() -> None:
    """Test if function will switch keys and values."""
    input = {"a": "b", "c": "d", "e": "f"}
    output = {"b": "a", "d": "c", "f": "e"}
    test = invert(input)
    assert test == output


def test_invert_duplicates() -> None:
    """Test the function for identical values."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_invert_empty_list() -> None:
    """Test an empty list."""
    input = {}
    test = invert(input)
    assert test == {}


def test_favorite_color_correct_count() -> None:
    """Test to see if the most popular color is returned."""
    input = {"Anna": "pink", "Tori": "blue", "Jayden": "green", "Ashley": "pink"}
    test = favorite_color(input)
    assert test == "pink"


def test_favorite_color_empty_dict() -> None:
    """Test an empty dictionary."""
    input = {}
    test = favorite_color(input)
    assert test == ""


def test_favorite_color_one_value() -> None:
    """Test the function if only one value is present."""
    input = {"Anna": "pink"}
    test = favorite_color(input)
    assert test == "pink"


def test_count_number_of_values() -> None:
    """Test to use a given list with values that are all different and assign a number."""
    input = ["coffee", "syrup", "sugar", "cream"]
    test = count(input)
    assert test == {"coffee": 1, "syrup": 1, "sugar": 1, "cream": 1}


def test_count_multiple_same() -> None:
    """Test to use a given list with values that are repeating."""
    input = ["coffee", "coffee", "syrup", "syrup"]
    test = count(input)
    assert test == {"coffee": 2, "syrup": 2}


def test_count_empty_list() -> None:
    """Test an empty list."""
    input = []
    test = count(input)
    assert test == {}


def test_alphabetizer_one_value() -> None:
    """Test a list with one value to correct match."""
    input = ["abby"]
    test = alphabetizer(input)
    assert test == {"a": ["abby"]}


def test_alphabetizer_alphabetize_different_letters() -> None:
    """Test to see if alphabetize words beginning with different letters."""
    input = ["anna", "ezra", "katrina"]
    test = alphabetizer(input)
    assert test == {"a": ["anna"], "e": ["ezra"], "k": ["katrina"]}


def test_alphabetizer_empty_list() -> None:
    """Test an empty list."""
    input = []
    test = alphabetizer(input)
    assert test == {}


def test_update_attendance_existing_day() -> None:
    """Test the function to update attendance with a day already in the dictionary."""
    attendance = {"Friday": ["Anna", "Ezra"], "Thursday": ["Anna"]}
    day = "Friday"
    in_class = "Katrina"
    update_attendance(attendance, day, in_class)
    test = {"Friday": ["Anna", "Ezra", "Katrina"], "Thursday": ["Anna"]}
    assert attendance == test


def test_update_attendance_new() -> None:
    """Test to update attendance with two names of a day already known."""
    attendance = {"Thursday": ["Anna", "Ashley", "Jayden"], "Wednesday": ["Anna", "Ashley"]}
    day = "Friday"
    in_class = "Breanna"
    update_attendance(attendance, day, in_class)
    test = {"Thursday": ["Anna", "Ashley", "Jayden"], "Wednesday": ["Anna", "Ashley"], "Friday": "Breanna"}
    assert attendance == test


def test_update_attendance_empty() -> None:
    """Test to update attendance with a new day."""
    attendance = {}
    update_attendance(attendance, "Friday", "Ashley")
    assert attendance == {"Monday": ["Ashley"]}