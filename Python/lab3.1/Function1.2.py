def convert(fahrenheit):
    centigrade = (5/9) * (fahrenheit - 32)
    return centigrade

temperature = int(input())
print(convert(temperature))