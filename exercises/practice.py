"""Practice using while loops to iterate over a string."""

def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1

def find_low_card(cards: str) -> int:
    index: int = 0 
    low_card: int = int(cards[0])
    while index < len(cards):
        current_cards: int = int(cards[index])
        if current_cards < low_card:
            low_card = current_cards
        index = index + 1 
    return low_card

    print(find_low_card(cards = "32423019"))
    