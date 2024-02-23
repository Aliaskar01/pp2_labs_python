def square(n, m):
    for i in range(n, m+1):
        yield i ** 2

num = input()
nums = num.split()
n, m = int(nums[0]), int(nums[1])

a = square(n, m)
for i in range(n, m+1):
    print(next(a))