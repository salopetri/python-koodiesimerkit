str = "Hämeen ammattikorkeakoulu"
print(str.upper())
print(str.lower())

str = " sana   san2 "
print(str.strip())

str = "Hämeen ammattikorkeakoulu"
print(str[0:6])

str = "Hämeen ammattikorkeakoulu"
print(str[0:6:2])

str = "Hämeen ammattikorkeakoulu"
print(str[::-1])

import re
str = "On kivaa olla insinööri"
if (re.search("insinööri", str)):
    print("Insinööri löydetty!")

