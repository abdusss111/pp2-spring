#syntax
print("Hello World!")

if 5 > 2:
    print("YES")

#comments
#This is a comment
'''
multi
line
comment
'''

#variables
carname = "Volvo"

x = 50

x = 5
y = 10
print(x+y)

x = 5
y = 10
z = x + y
print(z)

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "Orange"

def myfunc():
  global x
  x = "fantastic"


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





