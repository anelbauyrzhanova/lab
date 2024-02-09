
#ex1
class String__:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print("uppercase str:", self.input_string.upper())


processor = String__()
processor.getString()
processor.printString()

#ex2
class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

number = int(input())
shape = Shape()
print("Area of shape:", shape.area()) 
square = Square(number)
print("Area of square:", square.area())

#ex3
class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self):
        self.length = float(input("length: "))
        self.width = float(input("width: "))

    def area(self):
        return self.length * self.width


rectangle = Rectangle()
print("Area of rectangle:", rectangle.area())

#ex4

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


x1 = float(input("x 1: "))
y1 = float(input("y 1: "))
point1 = Point(x1, y1)

x2 = float(input("x 2: "))
y2 = float(input("y 2: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

print("Distance between the points:", point1.dist(point2))

new_x = float(input("new x 1: "))
new_y = float(input("new y 1: "))
point1.move(new_x, new_y)
point1.show()

#ex5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. Current balance: {self.balance}")
        else:
            print("error")


owner = input("owner's name: ")
initial_balance = float(input("initial balance: "))
account = Account(owner, initial_balance)

print(f"Account owner: {account.owner}, Balance: {account.balance}")

deposit_ = float(input("to deposit: "))
account.deposit(deposit_)

withdraw_ = float(input("to withdraw: "))
account.withdraw(withdraw_)

#ex6

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = input().split()
numbers = list(map(int, numbers))  

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
