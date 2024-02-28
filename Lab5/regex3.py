import re

txt="abc_def aed efg_da_e ca_ade"
x = re.findall(r"[a-z]+_[a-z]+", txt)
print(x)
