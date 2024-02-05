def filter_prime(arr):
    for i in arr:
        divs=0
        for j in range(1,i):
            if i % j==0:
                divs+=j
        if divs == 1:
            print(i, end=" ")
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
filter_prime(arr)
