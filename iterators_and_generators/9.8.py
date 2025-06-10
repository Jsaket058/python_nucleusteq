# 8. Implement an infinite generator for Fibonacci numbers.

def infinite_fibonacci():
    """
    Infinite generator for Fibonacci numbers.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = infinite_fibonacci()

for _ in range(10):
    print(next(fib))
