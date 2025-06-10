# 7. Write a script using regex to extract dates in dd-mm-yyyy format.

import re

# pattern = r"\d{2}-\d{2}-\d{4}"
pattern = r"(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-(\d{4})"

string="22-04-2002 blah blah 20-042220 ko ek or 23-08-4525"

ans = re.findall(pattern,string)

formatted_dates = [f"{day}-{month}-{year}" for day, month, year in ans]

print(formatted_dates)