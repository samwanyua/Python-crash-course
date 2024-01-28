# A function is a block of code that runs when called
# In python no curry braces but indentations with tabs and spaces


def sayHello(name, age = 23): #age is a default argument
    print(f'Hello,  {name}  {age}')

sayHello('Sam Wanyua')

# Return values

def getSum(num1,num2):
    total = num1 + num2
    return total

print(getSum(34,23))
# Alternatively
num = getSum(3234,34242)
print(num)


# A lamda function - small anonymous function
# A lamda function can take any number of arguments but can only have one expression. Similar to arrow functions in JS

get_sum = lambda num3,num4:  num3 + num4

print(get_sum(34,23))