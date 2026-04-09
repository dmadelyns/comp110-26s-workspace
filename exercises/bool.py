def can_eat(allergic: bool, temp:float) -> bool:
    """Is it safe to eat this food?"""
    return not allergic and temp >= 165.0

print(can_eat(allergic=False, temp=160.0))

def check_first_letter(word: str, letter: str) -> str: 

    if word(0) == letter:
        return "match"
    else:
        return: "no match"

print (check_first_letter(word="happy", letter="s"))




              
