def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative indices.")
    if n in (0, 1):
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(8))