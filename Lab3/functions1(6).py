def rev():
    s=input()
    l = len(s)
    for i in range(l-1,-1,-1):
        print(s[i] ,end="")

rev()