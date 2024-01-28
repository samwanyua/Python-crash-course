# A dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members
# Similar to object in JS

person = {
    'first_name': 'John',
    'last_name': 'Wesley',
    'age': 30
}
 
print(person, type(person))

# Using a constructor
person2 = dict(first_name='Donovans', last_name='Gishu',age=22)
print(person2)

# Get a value
print(person2['last_name'])
print(person2.get('first_name'))

# Add a key/value
person2['phone']='324-234-234-453-435'
print(person2)

# get dict keys
print(person2.keys())

# get items
print(person2.items())

# copy dict
person2 = person.copy()
person2['city']='boston'
print(person2)

# remove an item
del person2['age']
print(person2)

# using pop to remove an item
person2.pop('city')
print(person2)

# clear
person2.clear()
print(person2) #empty dict

# Getting length
print(len(person))

# list of dicts
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kobe', 'age': 32}
]

print(people)

# getting specifics
print(people[1])
print(people[1]['name'])