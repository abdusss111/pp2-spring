import re
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

txt = input()
x = re.sub('[ .,]', ':', txt, 4)
print(x)