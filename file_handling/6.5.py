# 5. Develop a function to read a file and remove all empty lines.

def remove_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    non_empty_lines = []
    for line in lines:
        if line.strip():  # Check if line is not empty after stripping whitespace
            non_empty_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(non_empty_lines)

remove_empty_lines('file_handling/yo.txt')
