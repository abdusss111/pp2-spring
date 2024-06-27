def divisible(n):
    for i in range(1, n+1):
        if i%12 == 0:
            yield i
        
n = int(input())
generator = divisible(n)

print(*generator)