import re
# Write a Python program to insert spaces between words starting with capital letters.

str = input()
x = re.sub(r"([A-Z])", r" \1", str)
print(x)