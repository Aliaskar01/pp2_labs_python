import re
str = input()
pattern = '^a(b{2,3})$'
if re.search(pattern,  str):
    print('YES') 
else:
    print('NO')