def returned(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
a = returned(n)

for i in range(n+1):
    print(next(a))