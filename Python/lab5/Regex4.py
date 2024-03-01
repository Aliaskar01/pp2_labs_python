import re
str = input()
pattern = '[A-Z]+[a-z]+'
result = re.findall(pattern,  str)
if result:
    print(result)
else:
    print('NO')