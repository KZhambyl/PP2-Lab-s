import re

txt="Write Python proProgram to insert spaces between words starting with capital letters."


count = len(re.findall(r"[A-Z]",txt))
capWords = re.findall(r"[A-Z]",txt)
it = iter(capWords)
it2 = iter(capWords)
for i in range(count):
    let = next(it2)
    letter = " " + let
    txt=re.sub(next(it),letter,txt)
txt = re.sub(r" +"," ",txt)
print(txt)