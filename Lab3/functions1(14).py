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

def histogram(arr):
    for i in arr:
        for j in range(0,i):
            print('*',end="")
        print()

arr=[6,1,1,2,2,4,8,8,4]

histogram(uniquelator(arr))
