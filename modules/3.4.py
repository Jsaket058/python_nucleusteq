# 4. Create a program using the `datetime` module to display the current date and time.

from datetime import datetime

def show_current_datetime():
    """
    Display the current date and time using datetime module.

    Returns:
        str: Formatted current date and time.
    """
    now = datetime.now()

    formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    return f"Current Date and Time: {formatted}"

print(show_current_datetime())