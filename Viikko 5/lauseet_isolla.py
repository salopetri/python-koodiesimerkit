import re

str = "hämeen ammattikorkeakoulu on suomen MIT? suomen presidentti on Sauli Niinistö. hpk on suomenmestari 2019!"

strList = list(str)
for iter in re.finditer("\w.+?[\.|\?|\!]", str):
    strList[iter.start()] = str[iter.start()].upper()

str = "".join(strList)
print(str)