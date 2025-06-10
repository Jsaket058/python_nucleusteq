def swap_values(a, b):
    """
    Swaps two values without using a third variable.
    
    Args:
        a: First value.
        b: Second value.
        
    Returns:
        tuple: Swapped values.
    """
    a, b = b, a  # Works for any data type
    return a, b

x = input("Enter first value: ")
y = input("Enter second value: ")

x, y = swap_values(x, y)
print(f"After swapping: x = {x}, y = {y}")
