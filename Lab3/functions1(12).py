def histogram(arr):
    for i in arr:
        for j in range(0,i):
            print('*',end="")
        print()

histogram([3,2,1,2,3])