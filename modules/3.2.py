# 2. Use the `math` module to calculate square root, factorial, and power of a number.

import math

def perform_math_operations(number, power_base, power_exp):
    """
    Perform square root, factorial, and power operations.

    Args:
        number (int): Number to apply sqrt and factorial on.
        power_base (float): Base number for power operation.
        power_exp (float): Exponent for power operation.

    Returns:
        dict: Dictionary containing results of operations.
    """
    results = {}

    # Calculate square root
    if number >= 0:
        results['square_root'] = math.sqrt(number)
    else:
        results['square_root'] = "NaN (negative number)"

    # Calculate factorial
    if isinstance(number, int) and number >= 0:
        results['factorial'] = math.factorial(number)
    else:
        results['factorial'] = "Undefined (only for non-negative integers)"

    # Calculate power
    results['power'] = math.pow(power_base, power_exp)

    return results

num = 5
base = 2
exponent = 3

output = perform_math_operations(num, base, exponent)

print("Square Root:", output['square_root'])    
print("Factorial:", output['factorial'])        
print("Power:", output['power'])                
