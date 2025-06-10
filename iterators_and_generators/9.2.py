# 2. Write an iterator class that returns Fibonacci numbers up to n terms.

class FibonacciIterator:
    """
    Iterator class to generate Fibonacci numbers up to n terms.
    """

    def __init__(self, n):
        self.n = n         # Total terms to generate
        self.count = 0     # Tracks how many terms have been returned
        self.a = 0         # First Fibonacci number
        self.b = 1         # Second Fibonacci number

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

fib = FibonacciIterator(7)

for num in fib:
    print(num)
