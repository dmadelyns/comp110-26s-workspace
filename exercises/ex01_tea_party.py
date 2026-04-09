"""Tea Party COMP 110!"""

__author__ = "730674804"


def main_planner(guests: int) -> None:
    """Plans and prints the details for a cozy tea party."""
    # main function that ties things together and prints details
    # Returns none because its not answering a question is just displaying the results

    teas: int = tea_bags(people=guests)
    snacks: int = treats(people=guests)
    total_cost: float = cost(tea_count=teas, treat_count=snacks)

    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea bags: " + str(teas))
    print("Treats: " + str(snacks))
    print("cost: $" + str(total_cost))
    # str converts the number into text
    return None


def tea_bags(people: int) -> int:
    # defining a function and tea_bags decsribes the functions job
    # people is returned as an int because its a numerical value
    # returns people * 2 because each person gets two teabags

    """Calculates the number of tea bags needed for a tea party."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed for the party."""
    teas: int = tea_bags(people=people)
    # keyword argument passes down the value given to people to the new parameter people
    total_treats: float = teas * 1.5
    # Total treats = (the number of people * 2 = teas) * 1.5
    # Float because the number of treats is a decimal
    return int(total_treats)


def cost(tea_count: int, treat_count: int) -> float:
    # Defining the function and cost means the functions job it to calculate cost
    # tea_count and treat_count are ints, returns float for cost decimal
    """Calculates the total cost of tea bags and treats."""
    tea_cost: float = tea_count * 0.5
    # cost of tea is tea_count * 0.5 and float becaise decimal
    treat_cost: float = treat_count * 0.75
    return tea_cost + treat_cost


# final restult is the total cost of tea plus the cost of treats


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
