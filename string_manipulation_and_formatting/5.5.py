# 5. Write a script to format a number as currency (e.g., 1000000 -> 1,000,000).

def format_currency(amount):
    """
    Format the given number with commas as currency format.

    Args:
        amount (int or float): The number to format.

    Returns:
        str: The number formatted with commas.
    """
    return f"{amount:,}"
num = 1000000
formatted = format_currency(num)
print(formatted) 

print(format_currency(1234567.89))  
