# 10. Implement a Python script that uses `glob` to search for all `.txt` files in a directory.

import glob
import os
import sys

def find_txt_files(directory):
    """
    Search and print all .txt files in the given directory.

    Args:
        directory (str): Path to the directory to search in.
    """
    # Create the search pattern for .txt files
    pattern = os.path.join(directory, "*.txt")
    
    # Use glob to get list of matching files
    txt_files = glob.glob(pattern)
    
    if txt_files:
        print(f".txt files found in '{directory}':")
        for file in txt_files:
            print(f"  {os.path.basename(file)}")
    else:
        print(f"No .txt files found in '{directory}'.")


if len(sys.argv) > 1:
    dir_path = sys.argv[1]
else:
        # Default to current directory
        dir_path = os.getcwd()
    
    # Check if directory exists
if not os.path.isdir(dir_path):
    print(f"Error: Directory '{dir_path}' does not exist.")
    
find_txt_files(dir_path)
