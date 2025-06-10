# 6. Implement a function that validates a strong password based on given criteria.

import string

def is_strong_password(password):
    """
    Validate if the given password is strong based on defined criteria.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if password is strong, False otherwise.
    """
    # Check for minimum length
    if len(password) < 8:
        return False

    # Flags for required character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = string.punctuation  # Includes: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_lower and has_digit and has_special

print(is_strong_password("Hello@123"))     
print(is_strong_password("hello123"))      
print(is_strong_password("HELLO@123"))     
print(is_strong_password("Hi@1"))          