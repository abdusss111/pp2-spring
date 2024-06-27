import math

def polygon_area(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area


n = int(input("number of sides: "))
s = float(input("length of a side: "))


area = polygon_area(n, s)


print(f"The area of the polygon is: {area}")
