from typing import List, Tuple, Union

def sum_and_average(numbers: List[Union[int, float]]) -> Tuple[float, float]:
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0.0
    return total, average

x = [1,5,20.5,21,36]
print(sum_and_average(x))