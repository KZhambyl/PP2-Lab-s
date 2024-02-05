from itertools import permutations

def perm(s):
    perm = permutations(s)
    for i in list(perm): 
        print (i) 

perm(input("Enter your string "))