s = input("Text: ")
n=0
for i in range(int(len(s)/2)):
    if(s[i]==s[len(s)-1-i]): n+=1

if(n==int(len(s)/2)):
    print("Is palindrome")
else:
    print("Is not palindrome")