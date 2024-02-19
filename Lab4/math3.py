import math
n=input("Input number of sides: ")
l=input("Input the length of a side: ")
x=math.pi/int(n)
s=int(n)*int(l)*int(l)/math.tan(x)/4
print(f"The area of the polygon is: {s}")

