#syntax
print("Hello World!")

import sys

print(sys.version)

if 5 > 2:
    print("YES")

# if 5 > 2:
# print("Five is greater than two!") syntax error

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

if 5 > 2:
 print("Five is greater than two!")
        # print("Five is greater than two!") error

#comments
#This is a comment
#This is a comment.
print("Hello, World!")
print("Hello, World!") #This is a comment
#print("Hello, World!")
print("Cheers, Mate!")
#This is a comment
#written in
#more than just one line
print("Hello, World!")
'''
multi
line
comment
'''
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#variables

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

x = 5
y = "Hello, World!"

carname = "Volvo"

#valid var names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#invalid var names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

myVariableName = "John"

MyVariableName = "John"

my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x + y) #error

x = 5
y = "John"
print(x, y)

x = 5
y = 10
print(x + y)

x = 50

x = 5
y = 10
print(x+y)

x = 5
y = 10
z = x + y
print(z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "Orange"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#data types

x = 5
print(type(x)) #int

x = "Hello World"
print(type(x)) #str

x = 20.5
print(type(x)) #float

x = ["apple", "banana", "cherry"]
print(type(x)) #list

x = ("apple", "banana", "cherry")
print(type(x)) #tuple

x = {"name" : "John", "age" : 36}
print(type(x)) #dict

x = True
print(type(x)) #bool

#numbers

x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

x = 5
print(type(x))

# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType	

# x = str("Hello World")	str	
# x = int(20)	int	
# x = float(20.5)	float	
# x = complex(1j)	complex	
# x = list(("apple", "banana", "cherry"))	list	
# x = tuple(("apple", "banana", "cherry"))	tuple	
# x = range(6)	range	
# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	bool	
# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	







