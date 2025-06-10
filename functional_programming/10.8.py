# 8. Develop a function that uses both map() and filter() in a pipeline.

def process_numbers(numbers):
    """
    Filters even numbers and returns their squares.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of squared even numbers.
    """
    # Step 1: Filter even numbers
    evens = filter(lambda x: x % 2 == 0, numbers)

    # Step 2: Square each even number
    squared = map(lambda x: x ** 2, evens)

    # Convert to list before returning
    return list(squared)

nums = [1, 2, 3, 4, 5, 6]
result = process_numbers(nums)
print(result)  