def pal(s):
    l=len(s)
    hl=int(l/2)
    e=0
    for i in range(0,hl):
        if s[i]==s[l-1-i]:
            e+=1
    if e==hl:
        print("Is Palindrome")
    else:
        print("Is Not Palindrome")

pal("12321")
pal("Biceps")