def uniquelator(arr):
    l=len(arr)
    arr2=[]
    for i in range(0, l):
        for j in range(i+1,l):
            if arr[i]==arr[j]:
                arr[j]='*'
    for i in range(0,l):
        if type(arr[i])==int:
            arr2.append(arr[i])
    return arr2
arr=[1,2,2,4,4,4,5]
print(uniquelator(arr))