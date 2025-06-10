# 6. Create a nested generator to yield Cartesian product of two lists.

def cartesian_product(list1, list2):
    """
    Generator that yields the Cartesian product of two lists.

    Args:
        list1 (list): First list.
        list2 (list): Second list.

    Yields:
        tuple: Pairs (a, b) where a ∈ list1 and b ∈ list2.
    """
    for a in list1:
        for b in list2:
            yield (a, b)

A = [1, 2]
B = ['x', 'y', 'z']

for pair in cartesian_product(A, B):
    print(pair)

