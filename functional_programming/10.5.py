# 5. Create a higher-order function that returns a power function.

def make_power_function(power):
    """
    Returns a function that raises a number to the specified power.

    Args:
        power: The exponent to raise to.

    Returns:
        A function that takes a number and raises it to the given power.
    """
    def power_func(x):
        return x ** power
    return power_func

square = make_power_function(2)
cube = make_power_function(3)

print(square(4))  # Output: 16
print(cube(2))    # Output: 8
