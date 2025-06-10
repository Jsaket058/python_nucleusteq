def is_leap_year(year: int) -> bool:
    """
    Determines whether a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if leap year, else False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year_input = int(input("Enter a year: "))
if is_leap_year(year_input):
    print("Leap year.")
else:
    print("Not a leap year.")
