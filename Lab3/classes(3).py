class Shape:
    s=0
    def area(self):
        print("Area is",self.s)

class Rectangle(Shape):
    def __init__(self, a,b):
        self.length=a
        self.width=b
    def calcArea(self):
        self.s=self.length*self.width

MyRectangle = Rectangle(3,14)
MyRectangle.calcArea()
MyRectangle.area()