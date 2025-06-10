# 3. Write a program to copy the contents of one file into another.

def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
            with open(destination_path, 'w') as dest_file:
                dest_file.write(content)
        print(f"Successfully copied {source_path} to {destination_path}")
        return True
    except FileNotFoundError:
        print(f"Error: Source file {source_path} not found")
    except IOError:
        print(f"Error: Could not write to {destination_path}")
    return False


copy_file('file_handling/yo.txt', 'file_handling/paste.txt')