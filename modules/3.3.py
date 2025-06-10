# 3. Write a program that uses `random` to generate a password of given length.

import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length.

    Args:
        length (int): The desired password length.

    Returns:
        str: The generated password.
    """
    if length < 4:
        return "Password length should be at least 4 for strong password."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

length = 12
print("Generated Password:", generate_password(length))