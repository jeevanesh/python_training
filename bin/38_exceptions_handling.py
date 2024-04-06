"""
Exception Handling
"""

# print("Without Handling Exception, Program will terminate abruptly")
# print("-"*20)
# # -------------
#
# a = 10
# b = 0
# result = a / b # Program will terminate abruptly here, Remaining part of the program will never execute
# print("result:", result)
#
# print("#"*40, end="\n\n")
# #########################

print("Handling Exception")
print("-"*20)
# -------------

try:
    pass # If error goto except block else skip except block
except:
    pass

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate instead it will goto except block
    print("result:", result) # This will never execute
except:
    print("Some Error in Try")
    print("Here we will write logic to solve the error")

print("#"*40, end="\n\n")
#########################


print("Handling Exception with class")
print("-"*20)
# -------------

# - We need to have classes for all type of exceptions
# - few exception classes are in builtins like ZeroDivisionErro
# - we can also write exception classes
# - all classes should be sub-class of 'Exception'
# - We can specify class name in except block

try:
    a = 10
    b = 0
    result = a / xyz # Program will NOT terminate instead it will goto except block
    print("result:", result) # This will never execute
except ZeroDivisionError:
    print("In ZDE except block")
except NameError as ne: # store thrown error class object in varaible 'ne'
    print("In NE except block, value of 'ne':", ne)
except (KeyError, IndexError):
    print("It can be KE or IE")

print("#"*40, end="\n\n")
#########################

print("try-except-else")
print("-"*20)
# -------------


try:
    a = 10
    b = 0
    result = a / xyz # Program will NOT terminate instead it will goto except block
    print("result:", result) # This will never execute
except NameError as ne: # store thrown error class object in varaible 'ne'
    print("In NE except block, value of 'ne':", ne)
else:
    print("In Else block")

# if 'try' success execute 'else' block and skip 'except' block
# if 'try' failed execute 'except' block and skip 'else' block

# Use of 'else' block
# - Assume we are writing to file where open, write and close will come in 'try'
# - Suppose, except block we wrote only error happining till open() function
#   then till open() function code we will keep it in try, remaining code
#   we will put it in 'else'
# - PROBLEM If we keep all code in try is, assume till open() no issus,
#   after open() function we got the error then it will execute 'except' block
#   written for error happening till open() function

print("#"*40, end="\n\n")
#########################

print("try-except-else-finally")
print("-"*20)
# -------------


try:
    a = 10
    b = 0
    result = a / xyz # Program will NOT terminate instead it will goto except block
    print("result:", result) # This will never execute
except NameError as ne: # store thrown error class object in varaible 'ne'
    print("In NE except block, value of 'ne':", ne)
else:
    print("In Else block")
finally:
    print("In final block")

# if 'try' success/failed, 'finally' will execute
# if 'except' success/failed, 'finally' will execute
# if 'else' success/failed, 'finally' will execute
# at any condition, finally will execute

# When to use?
# Irrespective of success/failure we need to logout/close-file/close-db/cleanup etc

print("#"*40, end="\n\n")
#########################

print("'assert' statement:")
print("-"*20)
# -------------

# assert:
#  - if given condition fails then throw error
#  - it will throw 'AssertionError' for any provided condition in assert
#  - if given condition is true then it will not do anything

try:
    a = 10
    b = 0
    assert b != 0
    result = a / b
    print("result:", result)
except AssertionError:
    print("This is AssertionError")


print("#"*40, end="\n\n")
#########################

print("'raise' statement:")
print("-"*20)
# -------------

# 'raise'
# - We can specify which type of error we want to throw

try:
    a = 10
    b = 0
    if b == 0:
        raise LookupError
    if b > 0:
        raise MemoryError
    if b < 0:
        raise NotImplementedError
    result = a / b
    print("result:", result)
except Exception as e:
    print("In Except block")
    print("error is:", e)
    print("Type of error is:", type(e))

print("#"*40, end="\n\n")
#########################

print("User Defined Exception Class Example - 1")
print("-"*20)
# -------------

# Mandatory Step:
# User Defined Exception Class should be sub-class of 'Exception' class
#   OR if some classes are already subclass of 'Exception' then
#   we can also create subclass of that class

class MyError(Exception):
    pass
# It valid Exception class where try/except/raise will understand

try:
    a = 10
    b = 0
    if b == 0:
        raise MyError
    if b > 0:
        raise MyError
    if b < 0:
        raise MyError
    result = a / b
    print("result:", result)
except MyError:
    print("In Except and it is MyError")

print("#"*40, end="\n\n")
#########################

print("User Defined Exception Class Example - 2")
print("-"*20)
# -------------

# Requirement: send some message while raising MyError

class MyError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg
    def __str__(self):
        return self.error_msg

try:
    a = 10
    b = 0

    if b == 0:
        raise MyError("Here value of b is 0")
    if b > 0:
        raise MyError("Here value of b gt 0")
    if b < 0:
        raise MyError("Here value of b lt 0")

    result = a / b
    print("result:", result)
except MyError as me:
    print("In Except and it is MyError and me:", me) # It calls __str__

print("#"*40, end="\n\n")
#########################