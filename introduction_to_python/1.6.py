def calculate(a: float, b: float, operator: str) -> float | None:
    """
    Performs calculation using match-case (Python 3.10+).

    Args:
        a (float): First operand.
        b (float): Second operand.
        operator (str): One of '+', '-', '*', '/'.

    Returns:
        float | None: Result or None if invalid input.
    """
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            try:
                return a / b
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
                return None
        case _:
            print("Invalid operator.")
            return None

x = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
y = float(input("Enter second number: "))
result = calculate(x, y, op)
if result is not None:
    print(f"Result: {result}")
