# 8. Create a regex pattern that identifies valid IPv4 addresses.

import re

pattern =r"^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"

string= "198.168.1.1"

ans = bool(re.match(pattern,string))

print(ans)