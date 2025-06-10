# 3. Develop a generator that yields the prime numbers under 100.

def prime_numbers_under_100():
    """
    Generator that yields prime numbers less than 100.
    """
    for num in range(2, 100):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

for prime in prime_numbers_under_100():
    print(prime, end=' ')
