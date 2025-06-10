# 6. Implement currying using closures in Python.

# Currying means transforming a function that takes multiple arguments into a sequence of functions, each taking one argument.

def curry_multiply(x):
    """
    Returns a function that takes y and returns x * y.
    This is a curried version of a two-argument multiply function.
    """
    def multiply_with_y(y):
        return x * y
    return multiply_with_y

multiply_by_3 = curry_multiply(3)
print(multiply_by_3(4))