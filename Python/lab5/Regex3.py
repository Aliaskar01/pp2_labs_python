import re
str = input()
pattern = '[a-z]+_[a-z]+'
result = re.findall(pattern,  str)
if result:
    print(result)
else:
    print('NO')