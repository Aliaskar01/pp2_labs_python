import re
str = input()
result = re.sub('[  . ,]',  ':', str)
if result:
    print(result) 
else:
    print('NO')