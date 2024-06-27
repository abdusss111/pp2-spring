def from_n_to_0(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())

generator = from_n_to_0(n)

print(*generator)
