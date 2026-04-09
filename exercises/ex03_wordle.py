"""EX03 - Wordle"""

__author__ = "730674804"

WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(length: int) -> str:
    guess = input(f"Enter a {length} character word: ")

    while len(guess) != length:
        # keep asking the user to input a word untill it matches the requires length
        print(f"That wasn't {length} chars! Try again:")
        guess = input()

    return guess


def contains_char(word: str, char: str) -> bool:
    """Return True if char is found in word, otherwise return False."""

    assert len(char) == 1

    index = 0
    # Go through each letter of the guessed word to check for a match
    while index < len(word):
        if word[index] == char:
            return True
        index += 1

    return False


def emojified(guess: str, secret_word: str) -> str:
    """return emoji feedback comparing guess to secret_word."""

    assert len(guess) == len(secret_word)
    # Make sure the length of the word is the same as the secret word

    result = ""
    index = 0

    while index < len(secret_word):
        if guess[index] == secret_word[index]:
            result += GREEN_BOX
            # If the letter in the guessed word is in the exact position as the secret word return a green box
        elif contains_char(secret_word, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
            # The letter in the guessed word is not in the secret word

        index += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turn = 1
    max_turns = 6

    while turn <= max_turns:
        # continue playing untill turns run out
        print(f"=== Turn {turn}/{max_turns} ===")

        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {turn}/{max_turns} turns!")
            # if the guess matches the secret word than the player won
            return

        turn += 1

    print("X/6 - Sorry, try again tommorw!")


if __name__ == "__main__":
    main(secret="codes")
