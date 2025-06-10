# 6. Create a script to merge multiple text files into one.

import glob

with open('file_handling/merged.txt', 'w') as outfile:
    for file in glob.glob('file_handling/texts/*.txt'):
        with open(file, 'r') as infile:
            outfile.write(infile.read() + '\n')
