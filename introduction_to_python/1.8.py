def convert_temperature(value: float, to_unit: str) -> float:
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        value (float): Input temperature.
        to_unit (str): 'C' or 'F'.

    Returns:
        float: Converted temperature.
    """
    if to_unit.upper() == 'F':
        return (value * 9/5) + 32
    if to_unit.upper() == 'C':
        return (value - 32) * 5/9
    raise ValueError("Invalid target unit. Use 'C' or 'F'.")

temp = float(input("Enter temperature: "))
unit = input("Convert to (C/F): ")
try:
    converted = convert_temperature(temp, unit)
    print(f"Converted Temperature: {converted:.2f}°{unit.upper()}")
except ValueError as e:
    print(e)
