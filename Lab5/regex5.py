import re

txt="aefevb advb aevb"
x = re.match(r"a.+b",txt)
print(x)