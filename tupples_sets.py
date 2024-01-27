#A tuple is a collection which is ordered and unchangeable. Allows duplicate numbers
# Notice: 'unchangeable'

fruits = ('Apples', 'Oranges', 'Grapes')
sweet_fruits = tuple(('Banana', 'passion')) # Using a constructor

print(fruits, sweet_fruits)

citrus = ('Orange')
print(citrus,type(citrus)) # This is a string

citrus = ('Orange',) #remember to add a trailing comma ','
print(citrus,type(citrus)) #this is a tuple

# get value
print(citrus[0])

# You cannot change a tuple
# citrus[0] = 'Mangoes' # THis cannot work
print(citrus)

# getting the length
print(len(citrus))


#A set is a collection which is unordered and unindexed. No duplicate numbers
fruits_set = {'Watermelon','Apples', 'Oranges', 'Grapes'}

# check something in a set
print('Apples' in fruits_set) #Returns a boolean

# Add to set
fruits_set.add('Green apple')
print(fruits_set)

# To remove
fruits_set.remove('Apples')
print(fruits_set)

# To clear the set entirely
fruits_set.clear()
print(fruits_set) # You get an empty set


