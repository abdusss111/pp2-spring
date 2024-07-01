import re
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

txt = input()
x = re.search('a.*b$', txt)
print(x)