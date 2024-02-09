def histogram(numbers):
    for i in range(len(numbers)):
        for j in range(numbers[i]):
            print("*", end = '')
        print()

num_input = input()
num_list = num_input.split(", ")
numbers = [int(num) for num in  num_list]
histogram(numbers)