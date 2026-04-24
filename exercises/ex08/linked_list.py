"""Linked list utility functions."""

from __future__ import annotations


class Node:
    """A node in a linked list."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None = None) -> None:
        """Create a node with a value."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Return a string of the linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value that is at the given index in the list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Return current node value if index is 0
    if index == 0:
        return head.value
    # Decrease index as you move to next node
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the list."""
    # Raise an error if list is empty
    if head is None:
        raise ValueError("Cannot call max with None.")

    if head.next is None:
        return head.value

    rest_max = max(head.next)
    # compare current node value to max of rest of the list to see if it is higher
    if head.value > rest_max:
        return head.value
    else:
        return rest_max


def linkify(items: list[int]) -> Node | None:
    """Return a linked list with the same values at the intput list."""
    if len(items) == 0:
        return None
    # Create node with first value and link to rest of list
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Rteurn a new link list scaling each factor."""
    if head is None:
        return None
    # Scale current node value then link to the rets of list
    return Node(head.value * factor, scale(head.next, factor))
