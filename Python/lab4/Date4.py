import datetime
import random

day_1 = random.randint(1, 28)
day_2 = random.randint(1, 31)

hour_1 = random.randint(1, 23)
hour_2 = random.randint(1, 23)

date_1 = datetime.datetime(2024, 2, day_1, hour_1, 0, 0)
date_2 = datetime.datetime(2024, 2, day_2, hour_2, 0, 0)

difference = date_2 - date_1
s = difference.total_seconds()

print(date_2)
print(date_1)
print(abs(s))