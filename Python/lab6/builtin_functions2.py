string = 'AAAadsadhf'
upper = 0
lower = 0

for i in string:
    if(i.isupper()):
        upper+=1
    else:
        lower+=1
print('Upper: ', upper)
print('LOwer: ',lower)