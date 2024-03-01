import re
str = input()
pattern = '^a(b*)$'
if re.search(pattern, str):
    print('YES') 
else:
    print('NO')