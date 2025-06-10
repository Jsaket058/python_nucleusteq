# 2. Use regex to validate a phone number format (e.g., 123-456-7890).

import re

pattern = r"^\d{3}-\d{3}-\d{4}$"
string="123-456-7890"

ans = bool(re.fullmatch(pattern,string))
print(ans)