def multipyNumbers(arr):
    res = 1
    for i in arr:
        res*=i
    return res

arr = [1,2,3,4,5]
print(multipyNumbers(arr))
