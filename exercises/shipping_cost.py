def shipping__cost(weight: float, has_label: bool, international: bool) -> float:
    """The cost of the package will be returned based on weight, label and international"""
    cost: float
    if has_label == False:
        return 0.0 
    elif weight <= 1.0:
        return 5.0
    elif weight <= 5.0:
        return 10.0
    else:
        return 20.0
    
    if international == True:
        cost = cost + 10.0

    return cost
    

    