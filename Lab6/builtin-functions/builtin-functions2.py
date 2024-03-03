s = input("text: ")
l =0
u = 0
for letter in s:
    if(letter.islower()==True): l+=1
    else: u+=1

print(f"Count of lowers: {l}\nCount of uppers: {u}")