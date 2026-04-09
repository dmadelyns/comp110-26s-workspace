"""Mutating functions."""

__author__ = "730674804"


def manual_append(dates: list[int], new: int) -> None:
    dates.append(new)


# a: list[int] = [2, 4, 12, 14, 22]
# manual_append(a, 26)
# print(a)


def double(items_number: list[int]) -> None:
    index: int = 0
    while index < len(items_number):
        items_number[index] = items_number[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
