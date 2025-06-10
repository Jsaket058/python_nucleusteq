def fibonacci_memoized():
    cache = {0: 0, 1: 1}

    def fib(n: int) -> int:
        if n < 0:
            raise ValueError("Fibonacci number is not defined for negative indices.")
        if n not in cache:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib
