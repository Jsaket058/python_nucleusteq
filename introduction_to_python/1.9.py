def fibonacci(n: int) -> list[int]:
    """
    Generates Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms.

    Returns:
        list[int]: List of Fibonacci numbers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

terms = int(input("Enter number of terms: "))
fib_sequence = fibonacci(terms)
print("Fibonacci sequence:", fib_sequence)
