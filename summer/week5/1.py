import re
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

txt = input()
match = re.search('a.*b', txt)
print(match)
