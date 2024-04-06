"""
Numbers
"""

print("How to store numbers PART-1")
print("-"*20)
# -------------

# We don't have primitive data type so no need to declare variable
# in python, we are using 'object'

a = 10 # shortcut
# Internally it will create object of predefined/builtin-class 'int' and store the value

# OR we can use class name
b = int(10) # same as b=10

c = 12.5
# Internally it will create object of predefined/builtin-class 'float' and store the value

# OR we can use class name
d = float(12.5) # same as d = 12.5

print(a, b, c, d, sep="\n")

print("#"*40, end="\n\n")
#########################

print("How to store numbers PART-2")
print("Some operators")
print("-"*20)
# -------------

a = 10
b = 3

result = a/b
print("Division result:",result) # result is float value

result = a//b
print("Floor Division result:",result) # result is int value

result = a ** b
print("a to the power of b:", result)

print("#"*40, end="\n\n")
#########################