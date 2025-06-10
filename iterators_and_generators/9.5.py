# 5. Write a generator to yield lines from a file one by one.

def read_lines(filepath):
    """
    Generator that yields lines from a file one by one.

    Args:
        filepath (str): Path to the file.

    Yields:
        str: Next line from the file (with newline stripped).
    """
    with open(filepath, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

for line in read_lines(r"C:\Users\hp\Desktop\python_nucleusteq\iterators_and_generators\textfile.txt"):
    print(line)
