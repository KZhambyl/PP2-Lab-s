class FirstClass ():
    def getString(self):
        self.a=input("Print your string: ")
    def printString(self):
        print(self.a.upper())
b = FirstClass()
b.getString()
b.printString()