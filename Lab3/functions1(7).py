def has_33(arr):
    l = len(arr)
    res = False
    for i in range(0,l-1):
        if arr[i]==3 and arr[i+1]==3:
            res=True
    return res

print(has_33([1,3,3,4]))
print(has_33([3,0,3,2]))
print(has_33([3,3,0,3]))