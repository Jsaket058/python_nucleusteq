def reverse_integer(number: int) -> int:
    """
    Reverses the digits of an integer.

    Args:
        number (int): The integer to reverse.

    Returns:
        int: Reversed integer.
    """
    sign = -1 if number < 0 else 1
    reversed_num = int(str(abs(number))[::-1])
    return sign * reversed_num

num = int(input("Enter an integer to reverse: "))
print(f"Reversed: {reverse_integer(num)}")
