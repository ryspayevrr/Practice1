myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John" #camelcase

MyVariableName = "John" #pascalcase

my_variable_name = "John" #snakecase


#one value to many variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#many values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#unpacking a collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#printing methods

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # first

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # second

x = 5
y = 10
print(x + y) # for integers

x = 5
y = "John"
print(x, y) # output variables without errors