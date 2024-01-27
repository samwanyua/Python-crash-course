# Strings are surrounded either by "" or ''

name = 'Brad'
age = 34

# Concantinate
print('Hello my name is ' + name + ' and I am' + str(age))

# to write the above in a better way (arguments by position)
print('Hello, my name is {name} and I an turning {age} years old'.format(name=name, age=age) )

# Using f-strings --> same as template literals
print(f'Hello, they call me {name} and I am {age} years old. I live in San Fransisco')

# String formatting

s = 'helloworld'
print(s.capitalize()) # to capitalize

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# count
sub = 'l' # to count the number of 'l' in the 's' string
print(s.count(sub))

print(s.startswith('Hello')) #starts with
print(s.endswith('d')) #ends with


#split in in a list (basically an array)
print(s.split())

#find position
print(s.find('r'))

#is all alphanumeric --> alphanumeric characters include both letters (alphabetic characters) and numbers (numeric characters).
print(s.isalnum())

#is alphabetic --> Alphabetic characters refer to letters in the alphabet (both uppercase and lowercase) in Python.
print(s.isalpha())

#is numeric --> Numeric characters refer to digits (0-9) in Python.
print(s.isnumeric())















































