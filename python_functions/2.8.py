from typing import Union

def sum_varargs(*args: Union[int, float]) -> float:
    return sum(args)
