# 3. Create a script to extract all hashtags from a given text.

import re

pattern=r"#\w+"

string="""
    hello #guyz this is a #Python scripts! #coding is fun. 
    written by Saket #jain , trainee #Nucleusteq
    """
ans =  re.findall(pattern,string)

print(ans)