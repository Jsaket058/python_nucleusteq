# 4. Use regex to find all words starting with a capital letter.

import re

pattern = r"[A-Z]\w+"

string = "Always have Faith and Believe"

ans = re.findall(pattern,string)

print(ans)