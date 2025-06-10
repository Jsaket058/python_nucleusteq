# 8. Develop a program that uses `os` and `sys` modules to list files and command-line args.

import os
import sys

def list_files(directory):
    """
    List and print all files in the specified directory.

    Args:
        directory (str): Path of the directory to list files from.
    """
    try:
        entries = os.listdir(directory)
        print(f"Files in directory '{directory}':")
        
        files = []

        for entry in entries:
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path):
               files.append(entry)

        if not files:
            print("  No files found.")
        else:
            for file in files:
                print(f"  {file}")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if len(sys.argv) > 1:
    dir_path = sys.argv[1]
else:
    dir_path = os.getcwd()

list_files(dir_path)

