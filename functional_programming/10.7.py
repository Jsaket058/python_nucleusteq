# 7. Use `reduce()` to calculate the factorial of a number.

from functools import reduce

def factorial(n):
    """
    Calculates the factorial of a number using reduce().

    Args:
        n (int): The number to calculate factorial for.

    Returns:
        int: Factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(2, n + 1))

print(factorial(7))

print(factorial(0))
