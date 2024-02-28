import re

txt = "Brother of Gloucester, at Saint Alban's field\nThis lady's husband, Sir Richard Grey, was slain..."

x = re.findall(r"[A-Z][a-z]+", txt)
print(x)