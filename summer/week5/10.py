import re
# Write a Python program to convert a given camel case string to snake case.

camel = input()
snake = re.sub(r"([A-Z])", r" \1", camel)
snake = snake.lower()
snake = snake.strip()
snake = re.sub(r'\s', '_', snake)
print(snake)