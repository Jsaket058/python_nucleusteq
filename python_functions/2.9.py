from typing import List, Any

def flatten_list(nested_list: List[Any]) -> List[Any]:
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            # If item is a list, recursively flatten it and extend the result
            flattened.extend(flatten_list(item))
        else:
            # If item is not a list, just append it
            flattened.append(item)
    return flattened
