"""
Strings
"""

print("Strings PART-1")
print("How to store the values")
print("-"*20)
# -------------

a = 'PERSON' # shortcut
# Internally it will create object of predefined/builtin-class 'str' and store the values

# Or we can use class name
b = str('PERSON')

print(a, b)

print("#"*40, end="\n\n")
#########################

print("Strings PART-2")
print("How to store the values")
print("-"*20)
# -------------

a = 'PERSON'
b = 'PERSON\'S' # \ is escape character, \ will not come in output
c = "PERSON'S"
d = '''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCH)'''
e = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCH)"""

print(a, b, c, d, e, sep='\n')

# Difference between multiline comment and a string?
# -- multiline comments are strings only
# -- it is not assigned to any variable
# -- but comments usually getting skipped when we run the program
#   but since multiline comments are strings, multiline comments are not skipped
#   instead it will get executed
# -- When  multiline comments are executed, it will create object of 'str' class
#   in the memory and store the values, since no reference to it, it will
#   get garbage collected
#   so
#   -- multiline comments are taking time to create object
#   -- multiline comments are using memory
# -- Finally we need to avoid using multiline comments

print("Strings PART-3")
print("How to store the values")
print("-"*20)
# -------------

a = "C:\newfolder\test.py"
# We are using few characters with \ for some other purpose
# Example: \n for to put new line, \t for to put tab space etc
# In above string \n will be replace with newline, \t will get replaced with tab space
print("Value of a:", a)

b = r"C:\newfolder\test.py"
# r-> raw string, \n\t etc will store as it is
print("Value of b:", b)

print("converting non-raw string 'a' to raw-string:", repr(a))

print("#"*40, end="\n\n")
#########################

print("Strings PART-4")
print("How to store the values")
print("-"*20)
# -------------

x = 10
y = 20
z = x + y

add_result = f'add of {x} and {y} is {z}'
# f-> format
# f -> will replace {variable_name} with value
print("add_result:", add_result)

print("#"*40, end=r"\n\n")
#########################

print("Strings PART-5")
print("Indexes: We can access each character using index")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-1
print("2nd character using +ve index no:", my_string[1])
print("2nd character using -ve index no:", my_string[-7])

# print("100th character using +ve index no:", my_string[100]) # ERROR

print("#"*40, end=r"\n\n")
#########################

print("Strings PART-6")
print("Slicing: We can get substring")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-2
print("Substring from index 1 to index-6 using +ve index:", my_string[1:6]) # char at 6 will be excluded
print("Substring from index 1 to index-6 using -ve index:", my_string[-7:-2])
print("Substring from index 1 to index-6 using +ve/-ve index:", my_string[-7:6])
print("Substring from index 1 to index-6 using +ve/-ve index:", my_string[1:-2], end="\n\n")

print("Substring from index 1 to END using +ve index:", my_string[1:])
print("Substring from index 1 to END using -ve index:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to index-6 using +ve index:", my_string[:6])
print("Substring from BEGINNING to index-6 using -ve index:", my_string[:-2], end="\n\n")

print("same string my_strin[:]=", my_string[:])

print("#"*40, end=r"\n\n")
#########################

print("Strings PART-7")
print("Step value: We can skip characters")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-3

print("substring from index-1 to 6 using +ve index no, default step by=1:", my_string[1:6])
print("substring from index-1 to 6 using -ve index no, default step by=1:", my_string[-7:-2], end="\n\n")
# by default step value=1,
# which means, from 1 to 6, give me every character

print("substring from index-1 to 6 using +ve index no, step by=1:", my_string[1:6:1])
print("substring from index-1 to 6 using -ve index no, step by=1:", my_string[-7:-2:1], end="\n\n")
# step value=1,
# which means, from 1 to 6, give me every character

print("substring from index-1 to 6 using +ve index no, step by=2:", my_string[1:6:2])
print("substring from index-1 to 6 using -ve index no, step by=2:", my_string[-7:-2:2], end="\n\n")
# step value=2,
# which means, from 1 to 6, give me every 2nd character

print("substring from index-1 to 6 using +ve index no, step by=3:", my_string[1:6:3])
print("substring from index-1 to 6 using -ve index no, step by=3:", my_string[-7:-2:3], end="\n\n")
# step value=3,
# which means, from 1 to 6, give me every 3rd character

print("#"*40, end=r"\n\n")
#########################

print("Strings PART-8")
print("-ve Step value: Reverse direction")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx Section-4

# Example: suppose if we want index-6 to 1 in reverse then
# mandatory 3 steps
# step-1: start index should be 6
# step-2: end index should be 1
# step-3: step value should be -ve step value
# If we miss any of the above step then we will get EMPTY string instead of ERROR

print("substring from index-6 to 1 in reverse direction using +ve index no & step='-1':", my_string[6:1:-1])
print("substring from index-6 to 1 in reverse direction using -ve index no & step='-1':", my_string[-2:-7:-1], end="\n\n")
# Value at end-index-1 will be excluded

print("substring from index-6 to 1 in reverse direction using +ve index no & step='-2':", my_string[6:1:-2])
print("substring from index-6 to 1 in reverse direction using -ve index no & step='-2':", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end=r"\n\n")
#########################

print("Strings PART-9")
print("Methods inside 'str' class")
print("-"*20)
# -------------

print(dir(my_string))

# OR we can also pass class name
# print(dir(str))

print("#"*40, end=r"\n\n")
#########################

# __ (DOUBLE UNDERSCORE) names
# -------------
# __ (DOUBLE UNDERSCORE) names are system defined names
# __ (DOUBLE UNDERSCORE) names are internally mapped to some-function/some-operators
#
# Example:
# '__add__' mapped to operator '+'
# to concatinate 2 strings we can use +
# + internally calls __add__
# inside __add__ method, there is a logic to concatinate 2 strings
#########################

print("Strings PART-10")
print("'startswith' method")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.startswith("WEL") # True/False
print("result:", result)

print("#"*40, end=r"\n\n")
#########################

print("Strings PART-11")
print("'strip' method")
print("-"*20)
# -------------

my_string = "     WEL       COME       "
print("my_string:", my_string, end="\n\n")

result = my_string.strip() # Removes extra spaces,\n\t at the ENDS (BOTH ENDS)
print("result:", result)

print("#"*40, end="\n\n")
#########################

print("Strings PART-11")
print("'split' method")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.split() # ["WEL", "COME"]
print("result:", result)

result = my_string.split('E') # ["W", "L COM", '']
print("result:", result)

print("#"*40, end="\n\n")
#########################

print("Strings PART-12")
print("'index' method")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

index_of_1st_E = my_string.index('E') # It will return index of 1st E
index_of_next_E = my_string.index('E', 3) # start looking from index-3

index_of_1st_E_find = my_string.find('E') # It will return index of 1st E
index_of_next_E_find = my_string.find('E', 3) # start looking from index-3

# Difference b/n find&index is
# - find will return -1 if given string not found
# - index will throw error if given string not found

print("index_of_1st_E:", index_of_1st_E)
print("index_of_next_E:", index_of_next_E)
print("index_of_1st_E_find:", index_of_1st_E_find)
print("index_of_next_E_find:", index_of_next_E_find)

print("#"*40, end=r"\n\n")
#########################

