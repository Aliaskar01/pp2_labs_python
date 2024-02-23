import datetime

a = datetime.datetime.now()
b = a.replace(microsecond=0)
print(b)