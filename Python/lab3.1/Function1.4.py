def filter_prime(num):
    prime = True
    if num == 1:
        prime = False 
    for i in range(2, int(num ** 0.5) + 1):
        if(num % i == 0):
            prime = False
    if prime:
        return num

numbers_input = input()
numbers_list = numbers_input.split()
numbers = [int(num) for num in numbers_list]
for num in numbers:
    if filter_prime(num) != None:
        print(filter_prime(num))