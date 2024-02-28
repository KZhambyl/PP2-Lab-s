import re

txt ="my_name_is_Ivan_Drago"
count = len(re.findall(r"_",txt))
for i in range(count):
    rep = re.search(r"_[A-Za-z]",txt)
    n = rep.span()[0]
    let = txt[n:n+2]
    letter = let[1]
    letter = letter.upper()
    txt=re.sub(let,letter,txt)
print(txt)