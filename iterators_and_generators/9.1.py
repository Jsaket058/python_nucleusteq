# 1. Create a generator that yields even numbers up to a given number.

def even_numbers_upto(n):
    """
    Generator that yields even numbers from 0 to n (inclusive).

    Args:
        n (int): The upper limit.

    Yields:
        int: The next even number in the range.
    """
    for i in range(0, n + 1, 2):
        yield i

# Print all even numbers up to 10
for num in even_numbers_upto(10):
    print(num)
