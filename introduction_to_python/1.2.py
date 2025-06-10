def find_largest(a: float, b: float, c: float) -> float:
    """
    Returns the largest among three numbers.

    Args:
        a (float): First number.
        b (float): Second number.
        c (float): Third number.

    Returns:
        float: The largest number.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
print(f"The largest number is: {find_largest(x, y, z)}")
