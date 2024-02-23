def dividble(n):
    for i in range(n+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

n = int(input())
g = (n // 3) + (n // 4) - (n // 12)
a = dividble(n)
for i in range(g+1):
    print(next(a))