import re
# Write a Python program to find sequences of lowercase letters joined with a underscore.

txt = input()
match = re.findall("[a-z]+\_+[a-z]", txt)
if match:
    print("Match")
else:
    print("No match")