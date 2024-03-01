import re
str = input()
splitted = re.split(' ', str)
for i in range(len(splitted)):
    splitted[i] = splitted[i].lower()
print('_'.join(splitted))