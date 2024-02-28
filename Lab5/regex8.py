import re

txt = "Write a Python program to split a string at uppercase letters."
words = re.split("[A-Z]", txt)
print(words)