# If/else used to decide to do something based on something being true or false
# Comparison operators(==, !=, >, <, >=, <=) used to compare values


x=18
y=14

if x > y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if statements
z = 3
if z > 2:
    if z <= 10:
        print(f'{z} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) combine conditional statements

if z > 2 and z <=30:
            print(f'{z} is greater than 2 and less than and equal to 30')


if z > 2 or z <=30:
            print(f'{z} is greater than 2 or less than or equal to 30')


if not(x == y):
            print(f'{x} is not equal to {y}')



# Membership operators(not, not in) - used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6]

# in
f = 3
if f in numbers:
    print(f in numbers) #gives either true or false

# not it
g = 23
if g not in numbers:
    print(g not in numbers) #gives either true or false

# Identity operators (is, is not) - compares the objects, not if they are equal
    # but if they are actually the same object, with the same memory location

# is
if x is y:
      print(x is y) #gives a boolean

# is not
if x is not y:
      print(x is not y) #gives a boolean

    





