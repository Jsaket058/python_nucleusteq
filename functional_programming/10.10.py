# 10. Implement a generic compose() function that chains multiple functions.

# compose() function in Python that can chain multiple functions together — in a way where the output of one function becomes the input of the next.
# compose(f, g, h)(x) → f(g(h(x)))

def compose(*functions):
    """
    Composes multiple functions into a single function.

    Args:
        *functions: A sequence of functions to apply, from last to first.

    Returns:
        A function that applies them in order.
    """
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

def double(x):
    return x * 2

def increment(x):
    return x + 1

def square(x):
    return x ** 2

# Compose them: square → increment → double
my_function = compose(double, increment, square)

print(my_function(3))  # Output: double(increment(square(3))) → 20