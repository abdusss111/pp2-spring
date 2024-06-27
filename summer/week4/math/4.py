def parallelogram_area(base, height):
    return base * height

base, height = map(int, input().split())

print(parallelogram_area(base, height))
