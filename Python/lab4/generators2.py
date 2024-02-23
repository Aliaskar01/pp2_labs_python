def even(n):
    for i in range(0, n+1, 2):
        yield i
    
n = int(input())
a = even(n)
for i in range(0, n+1, 2):
    print(next(a))