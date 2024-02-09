def convert(gram):
    ounce = gram / 28.3495231
    return ounce

weight = int(input())
weight = convert(weight)
print(weight)

grams = int(input("Write grams : "))
def converting(grams):
    print("Result is : ", 28.3495231 * grams)

converting(grams)