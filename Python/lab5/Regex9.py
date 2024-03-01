import re
str = input()
splitted = re.findall('[A-Z][^A-Z]*', str)
print(' '.join(splitted))