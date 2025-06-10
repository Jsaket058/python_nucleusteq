# 1. Write a script that reads a file and prints each line with line numbers.

with open('file_handling/yo.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        print(f"{i}: {line.strip()}")