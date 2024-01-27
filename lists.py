# A list is a collection which is ordered and changeable
# List allows duplicate members

numbers = [1,2,3,4,5,6]

# Using a constructor
evennums = list((2,4,6,8,20))

print(numbers)
print(evennums)

fruits = ['Apples','oranges','pears']

# Get a single value
print(fruits[1])
print(len(fruits))

# Append
fruits.append('Mangoes')
print(fruits)

# remove
fruits.remove('Apples')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove by position
fruits.pop(2)
print(fruits)

# Reverse
fruits.reverse()
print(fruits)

# sort list
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)

# change a value
fruits[0] = 'Blueberries'
print(fruits)