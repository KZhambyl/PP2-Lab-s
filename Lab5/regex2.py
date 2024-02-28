import re

txt="abba abbb abbba aba ab baaab babaabb bab aabbb"
x = re.match("ab{2,3}",txt)
print(x)