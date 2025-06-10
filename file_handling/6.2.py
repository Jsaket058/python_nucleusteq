# 2. Create a function to count the number of words in a text file.

import re
from pathlib import Path

def count_words(filename):
    if not Path(filename).exists():
        return 0
        
    try:
        with open(filename) as f:
            return len(re.findall(r'\w+', f.read()))
    except (UnicodeError, PermissionError):
        return 0
    
print(count_words('file_handling/yo.txt'))