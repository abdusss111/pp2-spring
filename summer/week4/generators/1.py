n = int(input())

def generate_squares(n):
    for i in range (1, n+1):
        yield i*i

squares = generate_squares(n)
print(*squares)
