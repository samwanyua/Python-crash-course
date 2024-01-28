#A loop is used for iterating over a sequence ie tuple, dictionary, set, string

# for loop
people = ['John','Paul','Sara','Susan']

for person in people:
    if person == 'Sara':
        break #Using break
    if person == 'Paul':
        continue # It skips
    print(f'Current person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0,11):
    print(f'Number: {i}')


# while loops - executes a set of statements as long as the condition is true
count = 0
while count <=12:
    print(f'List: {count}')
    count += 1
