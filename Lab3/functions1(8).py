def spy_game(arr):
    l = len(arr)
    res = False
    for i in range(0,l-2):
        if arr[i]==0 and arr[i+1]==0 and arr[i+2]==7:
            res=True
    return res

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))