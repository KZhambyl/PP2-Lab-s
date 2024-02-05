class Shape:
    s=0
    def area(self):
        print("Area is",self.s)
class Square(Shape):
    def __init__(self,l):
        self.length=l
        self.s=l*l
a=Shape()
a.area()
b=Square(3)
b.area()