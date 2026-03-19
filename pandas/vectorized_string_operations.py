import os
import pandas as pd
os.system('clear')

# vectorized string operations
data = ['peter', 'Paul', 'MARY', 'gUIDO']
print([s.capitalize() for s in data])

# This is perhaps sufficient to work with some data,
# but it will break if there are any missing values.
# For example:

# data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
# print([s.capitalize() for s in data])

# We will get the error saying -
# attributeError: 'NoneType' object has no attribute 'capitalize'

# for correctly handling missing data,
# we will use str attribute of Pandas Series and Index objects containing strings.
data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
names = pd.Series(data)
print(names)
print()

# We can now call a single method that will capitalize all the entries,
# while skipping over any missing values:
print(names.str.capitalize())
print()

### Vectorized item access and slicing: ###

# we can get a slice of the first three characters of each array using str.slice(0, 3)
# df.str.slice(0, 3) is equivalent to df.str[0:3]
print(names.str[0:3])
print()

names = ['Ethan Walker', 'Maya Rodriguez', 'Liam Bennett',
         'Aria Thompson', 'Noah Patel', 'Sofia Martinez']
df = pd.Series(names)
# If we want to print only the firstname then we can combine split with get
# For Example:
print(df.str.split().str.get(0))
# 0 because first name is at 0 index after split.
print()

print(df.str.split().str.get(1))
# 1 because last name is at 1 index after split.
print()

### Indicator variables ###
df = pd.DataFrame({'names': names,
                   'info': ['B|C|D', 'A|C', 'D|C', 'C|D', 'B|D', 'A|B|C']})
print(df['info'].str.get_dummies('|'))
print()
