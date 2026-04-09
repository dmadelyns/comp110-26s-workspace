"""Dictionary tests."""

import pytest

from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)

_author_ = "730674804"


def test_invert_switches_keys_and_values():
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_one_pair():
    assert invert({"a": "1"}) == {"1": "a"}


def test_invert_duplicate_keys():
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "1"})


def test_favorite_color_most_common_color():
    assert (
        favorite_color(
            {"Maddy": "Blue", "Mike": "Blue", "Emma": "Red", "Lisa": "Green"}
        )
    ) == "Blue"


def test_favorite_color_just_one_color():
    assert favorite_color({"Abby": "Red"}) == "Red"


def test_favorite_color_two_competitors():
    assert (
        favorite_color(
            {
                "Grace": "Blue",
                "Mike": "Red",
                "Helen": "Blue",
                "Bob": "Red",
                "Kylie": "Red",
            }
        )
        == "Red"
    )


def test_count_how_many_times_string_appears_in_list():
    assert count(["a", "b", "a", "b", "a"]) == {"a": 3, "b": 2}


def test_count_singular_characters():
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_empty_list():
    assert count([]) == {}


def test_alphabetizer_group_word_by_first_letter():
    assert alphabetizer(["chicken", "drink", "drum"]) == {
        "c": ["chicken"],
        "d": ["drink", "drum"],
    }


def test_alphabetizer_upper_and_lower_case():
    assert alphabetizer(["Car", "people", "Cat"]) == {
        "c": ["Car", "Cat"],
        "p": ["people"],
    }


def test_alphabetizer_empty_list():
    """Test the alphabetizer with an empty list."""
    assert alphabetizer([]) == {}


def test_update_attendance_add_student_to_attendance():
    attendance = {"Monday": ["Maddy"]}
    update_attendance(attendance, "Monday", "Emma")
    assert attendance == {"Monday": ["Maddy", "Emma"]}


def test_update_attendance_new_day():
    attendance = {}
    update_attendance(attendance, "Thursday", "Maddy")
    assert attendance == {"Thursday": ["Maddy"]}


def test_update_attendance_empty_list():
    attendance = {}
    update_attendance(attendance, "Friday", "")
    assert attendance == {"Friday": [""]}


def test_update_add_student_to_attendance():
    attendance = {"Monday": ["Maddy"]}
    update_attendance(attendance, "Monday", "Emma")
    assert attendance == {"Monday": ["Maddy", "Emma"]}
