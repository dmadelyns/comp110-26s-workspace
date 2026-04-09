"""EX02 - Chardle - A cute step toward Wordle."""

_author_ = "730674804"


def input_word() -> str:
    word = input("Enter a 5-character word: ")

    if len(word) != 5:
        print("Error: Word must contain 5 charcters.")
        exit()

    return word


def input_letter() -> str:
    letter = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return letter


def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")
    count = 0

    if word[0] == letter:
        print(f"{letter} found at index 0")
        count += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1

    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    if __name__ == "__main__":
        main()
