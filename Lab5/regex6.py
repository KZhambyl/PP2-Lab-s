import re

txt="Because, in.quarrel of, the. house of York"
x=re.sub(r",| |\.",":",txt)
print(x)