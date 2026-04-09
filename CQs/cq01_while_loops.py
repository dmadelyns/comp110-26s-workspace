"""Practice using a while loop to iterate over a string."""

__author__ = "730674804"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1

    return count


def get_evens(numbers: str) -> str:
    result = ""
    index = 0

    while index < len(numbers):
        digit = numbers[index]

        if int(digit) % 2 == 0:
            result += digit

        index += 1

    return result
