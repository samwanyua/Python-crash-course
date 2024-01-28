# A module is a file containing a set of functions to include in your application
# There are core modules, you can install through pip manager


# Core modules
import datetime
from datetime import date

tarehe = datetime.date.today()
current_date = date.today()

print(current_date)
print(tarehe)

import time
from time import time
timestamp = time()
print(timestamp)

# pip module
from camelcase import CamelCase

c= CamelCase()
print(c.hump('hello there')) #Convert each word to camel case