#1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
import math


class StringClass:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())

if __name__ == "__main__":
    str = StringClass()
    str.getString()
    str.printString()



#2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2
    
shape = Shape()
print(f"Area of shape: {shape.area()}")  

square = Square(4)
print(f"Area of square: {square.area()}")  

#3. Define a class named Rectangle which inherits from Shape class from task 
#2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width
    
rect = Rectangle(4, 6)
print(rect.area())

#4. Write the definition of a Point class. Objects from this class should have a

# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
point1 = Point(2, 2)
point2 = Point(0, 0)

print(point1.dist(point2))

#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
#Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
    
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. Available balance: {self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

MyAccount = BankAccount("Abdussalam", 1000)

MyAccount.deposit(500)    
MyAccount.withdraw(30)   
MyAccount.withdraw(200)   
MyAccount.deposit(-20)    
MyAccount.withdraw(-10)   
MyAccount.withdraw(100)   
MyAccount.withdraw(25)    

#Write a program which can filter prime numbers in a list by using filter function. 
#Note: Use lambda to define anonymous functions.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 40, 42, 47]


primes_list = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", primes_list)






    
        

