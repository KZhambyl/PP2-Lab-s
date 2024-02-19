def function(n):
    [print(el,end=' ') for el in range(n+1) if el%3==0 and el%4==0]

n=int(input())
function(n)