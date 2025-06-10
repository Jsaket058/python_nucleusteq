def memoize(func):
    """
    Decorator to memoize a function's results.

    Args:
        func: The function to memoize.

    Returns:
        A wrapped function that caches results.
    """
    cache = {}

    def wrapper(x):
        if x in cache:
            print(f"Using cached value for {x}")
            return cache[x]
        result = func(x)
        cache[x] = result
        return result

    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
