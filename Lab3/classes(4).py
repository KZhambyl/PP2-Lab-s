import math
class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"The coordinates of point is ({self.x},{self.y})")
    def move(self, x,y):
        self.x+=x
        self.y+=y
    def dist(self, x,y):
        res=math.sqrt((self.x-x)*(self.x-x) + (self.y-y)*(self.y-y))
        print(f"Distance between point ({self.x},{self.y}) and ({x},{y}) is {res}")
pointA=Point(5,24)
pointA.move(12,-13)
pointA.show()
pointA.dist(19,19)