# variable is a container for a value, which can be various types
"""
This is
a  multiline 
comment
 """
# Variable names are case sensitive, should start with a letter or underscore
# Variables can have numbers but cannot start with one

# Data types
x = 1 #int
y = 2.3 # float
name = 'John' #string
is_cool = True #bool

# Multiple assignment
x,y,name, is_cool =(1,2.3,'John',True)

a = x +y

# Checking type
print(type(x))

# Casting --> converting data types
x = str(x)
print(type(x))
y=int(y)
print(type(y),y)
z = float(y)
print(type(z),z)

print('Hello')
print(x,y,is_cool,a)