# 5. Write a regex to replace all whitespace with hyphens.

import re

pattern = r"\s+"

string="Hello from Indore to Sagar  "

ans = re.sub(pattern,"-",string.strip())

print(ans)