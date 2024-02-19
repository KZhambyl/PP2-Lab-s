n = int(input())
arr = [el for el in range(n+1) if el%2==0]
print(*arr, sep=', ')