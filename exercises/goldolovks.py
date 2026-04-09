def goldilocks(porridge__temp: int, low: int, high: int) -> str:
    if porridge__temp < low:
        return "too cold"
    elif porridge__temp > high:
        return "too hot"
    else:
        return "just right"
    