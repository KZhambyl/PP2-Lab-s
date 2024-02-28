import re

txt ="myNameIsIvanDrago"
count = len(re.findall(r"[A-Z]",txt))
words = re.findall(r"[A-Z]",txt)
it = iter(words)
it2 = iter(words)
for i in range(count):
    let = next(it)
    rep = "_"+let
    txt = re.sub(let,rep,txt)
txt=re.sub(r"_+","_",txt)
print(txt)