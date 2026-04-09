def initials(first: str, middle: str, last: str) -> str:
    """Return the initials of the first, middle, and last names."""
    if len(middle) == 0:
        return first[0] + last[0]
    else:
        return first[0] + middle[0] + last [0]

    