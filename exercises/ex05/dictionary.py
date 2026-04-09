"""Dictiornary ultility functions."""

_author_ = "730674804"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Return a dictionary swapping keys and values."""
    result = {}
    # go through each key in the dictionary
    for key in input:
        value = input[key]

        if value in result:
            raise KeyError("Duplicate key")
            # create an error if the value dosen't already exist

        result[value] = key

    return result


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Return the most common favorite color."""
    color_counts: dict[str, int] = {}

    for name in names_and_colors:
        color = names_and_colors[name]

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    # find the most common error
    most_color = ""
    most_count = 0

    for color in color_counts:
        if color_counts[color] > most_count:
            most_color = color
            most_count = color_counts[color]

    return most_color


def count(values: list[str]) -> dict[str, int]:
    """Count how many times each string appears in a list."""
    counts: dict[str, int] = {}

    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Sort words by their first letter."""
    result: dict[str, list[str]] = {}

    for word in words:
        first_letter = word[0].lower()
        # find the first letter in the word and convert to lower case

        if not first_letter.isalpha():
            continue

        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Add a student to the attendance dictiornary for a day."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
