# 4. Write a function that takes a function and a list, and applies it to all items.

def apply_function(func, data) -> list:
    """
    Applies a function to each item in the list.

    Args:
        func: A function to apply.
        data: A list of items.

    Returns:
        A new list with the function applied to each item.
    """
    return [func(item) for item in data]

# Define a simple function to double a number
def double(x):
    return x * 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Apply the function to the list
result = apply_function(double, numbers)

# Output result
print(result)
