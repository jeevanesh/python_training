"""
Generators: We can create objects whenever it is required
OR
we can create objects on the fly
"""

print("WITHOUT generators")
print("-"*20)
# -------------

def squares(my_list):
    squared_list = []
    for i in my_list:
        squared_list.append(i*i)
    return squared_list

# Call Function

my_values_list = [10, 20, 30, 40]
print("my_values_list :", my_values_list)

my_values_squared_list = squares(my_values_list)

for each_squared_value in my_values_squared_list:
    print("each_squared_value:", each_squared_value)

import sys
print("Memory Used By 'my_values_squared_list' is: ", sys.getsizeof(my_values_squared_list), " Bytes")

print("#"*40, end="\n\n")
#########################

# FINAL REQUIREMENT IN ABOVE BLOCK OF CODE
# -------------
# FINAL REQUIREMENT is print each squared value
#########################

# Square function
# -------------
# - Square function will square each value and
#  put all squared values in list and returning.
# - Returned list is captured in 'my_values_squared_list'
#########################

# IMPORTANT with respect to MEMORY USAGE
# -------------
# - Since 'my_values_squared_list' is having all the values
#   it occupies some memory which is required to keep all the values
#########################

# REQUIREMENT: to save memory
# -------------
# - Since our FINAL REQUIREMENT is to print each squared value
#   that means at a time only one value we need
# - Currently we are keeping all the sqaured values ready in the list
#   and one by one we are taking it using for-loop
#
# IMPORTANT
# - Eventhough we are processing one squared value at time,
#   we are keeping all squared values in the memory
# - ARE THERE ANY WAY WHERE WE CAN GET VALUES/OBJECTS WHENEVER IT
#   IS REQUIRED/ON_THE_FLY/WHENEVER WE ARE ASKING???
#
# SOLUTION: GENERATOR
#########################

print("USING generators")
print("-"*20)
# -------------

def generator_squares(my_list):
    for i in my_list:
        yield i*i


# Call Function

my_values_list = [10, 20, 30, 40]
# my_values_list = range(1000)
print("my_values_list :", my_values_list)

my_values_squared_list = generator_squares(my_values_list)

for each_squared_value in my_values_squared_list:
    print("each_squared_value:", each_squared_value)

import sys
print("Memory Used By 'my_values_squared_list' is: ", sys.getsizeof(my_values_squared_list), " Bytes")

print("#"*40, end="\n\n")
#########################

print("""Since we are not storing generated Values,
It is one time generation,
If we want again then we need to call generator function again
""")
print("-"*20)
# -------------

def generator_squares(my_list):
    for i in my_list:
        yield i*i


# Call Function

my_values_list = [10, 20, 30, 40]
# my_values_list = range(1000)
print("my_values_list :", my_values_list)


# 1st Time
my_values_squared_list = generator_squares(my_values_list)
for each_squared_value in my_values_squared_list:
    print("1st TIME: each_squared_value:", each_squared_value)

# 2nd Time: It will not generate
for each_squared_value in my_values_squared_list:
    print("2nd TIME: each_squared_value:", each_squared_value)

# 3rd Time: If we want again then call function again
my_values_squared_list = generator_squares(my_values_list)
for each_squared_value in my_values_squared_list:
    print("3rd TIME: each_squared_value:", each_squared_value)

print("#"*40, end="\n\n")
#########################


print("""If we want to reuse items generated from generator
then we can convert to list/tuple/set etc
""")
print("-"*20)
# -------------

def generator_squares(my_list):
    for i in my_list:
        yield i*i


# Call Function

my_values_list = [10, 20, 30, 40]
# my_values_list = range(1000)
print("my_values_list :", my_values_list)



my_values_squared_list = generator_squares(my_values_list)
# Get all values in list
my_values_squared_list = list(my_values_squared_list)
print("Generated Values In List:", my_values_squared_list)

print("#"*40, end="\n\n")
#########################

print("""Comprehension using () is Not-TUPLE,
It is GENERATOR
""")
print("-"*20)
# -------------

my_values_list = [10, 20, 30, 40]
print("my_values_list :", my_values_list)

my_values_squared_gen = (i*i for i in my_values_list)
print("my_values_squared_gen:", my_values_squared_gen)
print("my_values_squared_gen in list:", list(my_values_squared_gen))

print("#"*40, end="\n\n")
#########################

print("""Without using for-loop, MANUALLY also we can generate
using builtin function
iter()
next()
""")
print("-"*20)
# -------------

def generator_squares(my_list):
    for i in my_list:
        yield i*i


# Call Function

my_values_list = [10, 20, 30, 40]
print("my_values_list :", my_values_list)



my_values_squared_gen = generator_squares(my_values_list)

# Steps to iterate
# Step-1: Create object of iter()
# Step-2: Get values using next()

# Step-1: Create object of iter()
my_iterator = iter(my_values_squared_gen)

# Step-2: Get values using next()
print("Each Value:", next(my_iterator))
print("Each Value:", next(my_iterator))
print("Each Value:", next(my_iterator))
print("Each Value:", next(my_iterator))
# print("Each Value:", next(my_iterator)) # StopIteration Error, for-loop handles this

print("#"*40, end="\n\n")
#########################

print("""
We can also iterate any collection like list/tuple/set etc
using
iter()
next()
""")
print("-"*20)
# -------------


my_values_list = [10, 20, 30, 40]
print("my_values_list :", my_values_list)

# Steps to iterate
# Step-1: Create object of iter()
# Step-2: Get values using next()

# Step-1: Create object of iter()
my_iterator = iter(my_values_list)

# Step-2: Get values using next()
print("Each Value:", next(my_iterator))
print("Each Value:", next(my_iterator))
print("Each Value:", next(my_iterator))
print("Each Value:", next(my_iterator))
# print("Each Value:", next(my_iterator)) # StopIteration Error, for-loop handles this

print("#"*40, end="\n\n")
#########################