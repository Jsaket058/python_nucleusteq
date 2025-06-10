# 1. Write a regex to extract all email addresses from a string.

import re

# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+\$' gives only single email from start
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

string = """jsaket068@gmail.com is my email address of form abc@gmail.com
            jsaket068@gmail.com is my email address of form abc@gmail.com"""

ans = re.findall(pattern,string)

print(ans)