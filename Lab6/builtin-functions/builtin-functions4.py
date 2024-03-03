from time import sleep
import math

num=int(input())
ms=int(input())

sleep(ms/1000)
res=math.sqrt(num)

print(f"Square root of {num} after {ms} miliseconds is {res}")
