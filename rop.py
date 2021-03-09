class Rectangle:
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length


print("Rectangle 1")
a=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
obj=Rectangle(a,b)
print("Area 1 = ",obj.area())
print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob=Rectangle(a,b)
print("Area 2 = ",ob.area())
print(obj.area() < ob.area())

