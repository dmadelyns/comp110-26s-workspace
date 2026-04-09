"""Create list utility functions from scratch"""

__author__ = "730674804"


def all(nums: list[int], value: int) -> bool:
    if len(nums) == 0:
        return False

    for num in nums:
        if num != value:
            return False
    # Don't use else because then it would connect it to the line above
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest = input[0]

    for num in input:
        if num > largest:
            largest = num

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False

    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index = index + 1
    # Python checks the next index until it reaches the length of list 1 (index = index + 1)
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    index = 0
    while index < len(list2):
        list1.append(list2[index])
        index = index + 1
