def is_prime_number(value):
    """
    Determines if the given number is a prime number.
    
    Args:
        value: The number to check (can be any type).
        
    Returns:
        str: Message indicating whether the number is prime or not.
    """
    try:
        num = float(value)

        # Only positive integers greater than 1 can be prime
        if not num.is_integer() or num <= 1:
            return f"{value} is not a prime number (prime numbers are positive integers greater than 1)."

        num = int(num)

        if num == 2:
            return f"{num} is a prime number."

        if num % 2 == 0:
            return f"{num} is not a prime number."

        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return f"{num} is not a prime number."

        return f"{num} is a prime number."

    except ValueError:
        return f"{value}' is not a valid number."

# Input from user
user_input = input("Enter any number to check if it's a prime: ")
result = is_prime_number(user_input)
print(result)
