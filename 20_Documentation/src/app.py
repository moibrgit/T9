def add(x:int, y:int) -> int:
    """Add two numbers together x + y

    Args:
        x (int): first term
        y (int): second term

    Returns:
        int: total of the sum
    """
    total = x + y
    return total


def subtract(x:int, y:int) -> int:
    """subtract two numbers x - y

    Args:
        x (int): first term
        y (int): second term

    Returns:
        int: total of the subtraction
    """
    total = x - y
    return total


if __name__ == "__main__":
    print(add(4,5))