import re
str = input()
splitted = re.split('_', str)
for i in range(len(splitted)):
    splitted[i] = splitted[i].capitalize()
print(''.join(splitted))