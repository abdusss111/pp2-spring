def trapezoid_area(base1, base2, height):
    return 0.5 *height * (base1 + base2)

base1, base2, height = map(int, input().split())

print(trapezoid_area(base1, base2, height))