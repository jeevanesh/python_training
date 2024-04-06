"""
Decorators: Assume we need to write more than one function where
in all function some-common-logic are implemented.

Instead of rewriting common-logic in all such functions,
we can write separate function for common-login and
we can make use this common-logic function in all other functions

How to write/design such common functions?
- ANSWER: Using DECORATOR DESIGN PATTERN
"""
print("Without Using Decorator")
print("-"*20)
# -------------

def add1(a, b):
    print("Result is")
    print(a+b)
    print("End of the result")

def add2(a, b):
    print("Result is")
    print(a+b+b)
    print("End of the result")

def sub1(a, b):
    print("Result is")
    print(a-b)
    print("End of the result")

def sub2(a, b):
    print("Result is")
    print(a-b-b)
    print("End of the result")


add1(10, 20)
add2(10, 20)
sub1(10, 20)
sub2(10, 20)

print("#"*40, end="\n\n")
#########################

print("Using Decorator Design Pattern: PARTIALLY IMPLEMENTED")
print("-"*20)
# -------------

# We need function to reuse below statements
# print("Result is")
# print("End of the result")

# As per the instructions/procedure given in DECORATOR DESIGN PATTERN
def my_decorator(my_func): # my_func=sub1
    def decorated_func(x, y): # We can use this decorator for 2 argument functions
        print("Result is")
        my_func(x, y) # sub1(10,20)
        print("End of the result")
    return decorated_func


def add1(a, b):
    print(a+b)

recevied_inner_function = my_decorator(add1)
# recevied_inner_function having reference to 'decorated_func'
recevied_inner_function(10, 20)
# -------------

def add2(a, b):
    print(a+b+b)

recevied_inner_function = my_decorator(add2)
# recevied_inner_function having reference to 'decorated_func'
recevied_inner_function(10, 20)
# --------------

def sub1(a, b):
    print(a-b)

recevied_inner_function = my_decorator(sub1)
# recevied_inner_function having reference to 'decorated_func'
recevied_inner_function(10, 20)

print("THIS IS PARTIALLY IMPLEMENTED")
print("#"*40, end="\n\n")
#########################

print("Using Decorator Design Pattern: FINAL")
print("-"*20)
# -------------


def my_decorator(my_func):
    def decorated_func(x, y):
        print("Result is")
        my_func(x, y)
        print("End of the result")
    return decorated_func


@my_decorator
def add1(a, b):
    print(a+b)


add1(10, 20)

# @my_decorator will take care of below 2 steps
# recevied_inner_function = my_decorator(add1)
# recevied_inner_function(10, 20)
# -------------

@my_decorator
def add2(a, b):
    print(a+b+b)

add2(10, 20)

# @my_decorator will take care of below 2 steps
# recevied_inner_function = my_decorator(add2)
# recevied_inner_function(10, 20)
# --------------

@my_decorator
def sub1(a, b):
    print(a-b)


sub1(10, 20)
# @my_decorator will take care of below 2 steps
# recevied_inner_function = my_decorator(sub1)
# recevied_inner_function(10, 20)
# --------------

print("THIS IS FINAL DECORATOR")

print("#"*40, end="\n\n")
#########################