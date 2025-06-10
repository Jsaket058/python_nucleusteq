# 6. Build a regex to validate complex passwords (at least 1 digit, 1 symbol, 8+ chars).

import re

pattern = r"^(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
string = "S@ket789!"
ans = bool(re.match(pattern , string))

print(ans)