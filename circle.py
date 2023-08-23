1/
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def get_coordinates(self):
        return self.x, self.y, self.z

my_point = Point3D(1, 2, 3)

print(my_point.get_coordinates())  
2/
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


my_rectangle = Rectangle(4, 3)


print("Area:", my_rectangle.area())  
print("Perimeter:", my_rectangle.perimeter())  
3/
import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def is_inside(self, x, y):
        distance = math.sqrt((x - self.center_x) ** 2 + (y - self.center_y) ** 2)
        return distance <= self.radius
my_circle = Circle(0, 0, 5)

print("Area:", my_circle.area()) 
print("Perimeter:", my_circle.perimeter())  
print(my_circle.is_inside(3, 4)) 
print(my_circle.is_inside(6, 7))  
4/
class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

my_account = Bank(1000)

my_account.deposit(500)
print("Balance after deposit:", my_account.balance) 

my_account.withdraw(200)
print("Balance after withdrawal:", my_account.balance)  
