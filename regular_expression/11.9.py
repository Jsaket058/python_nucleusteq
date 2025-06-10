# 9. Use regex to parse and extract key-value pairs from a query string.

import re

pattern = r'([^&=]+)=?([^&]*)'

query_string="name=SaketJain&age=22&city=Indore&hobbies=cricket&language=java/python"

pairs = re.findall(pattern, query_string)

# print(pairs)

for key , value in pairs:
    print(f"key:{key} , value:{value}")
