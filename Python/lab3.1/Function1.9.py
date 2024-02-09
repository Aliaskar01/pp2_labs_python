import math
def volume(radius):
    Volume = 4 * math.pi * radius ** 2
    return Volume
radius = int(input())
print(volume(radius))