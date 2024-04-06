"""
Variable Scopes
1. Local
2. Enclosed
3. Global
4. Builtins
"""

print("1. Local Scope Example")
print("-"*20)
# -------------

def f():
    a = 10 # Local Scope, we can't access outside the function
    print("Value of a:", a)

f()

print("#"*40, end="\n\n")
#########################


print("2. Enclosed Scope Example-1")
print("-"*20)
# -------------

def outer_function():
    b = 10 # Enclosed Scope Variable where current-function & inner-function can access
    def inner_function():
        print("Value of b in inner_function:", b) # Inner function accessing outer function variable
    inner_function()
    print("Value of b in outer_function:", b)

outer_function()

print("#"*40, end="\n\n")
#########################


print("2. Enclosed Scope Example-2")
print("-"*20)
# -------------

def outer_function():
    b = 10 # Enclosed Scope Variable where current-function & inner-function can access
    def inner_function():
        # b = 1000 # It will create local variable
        nonlocal b # It refers enclosed scope variable
        b = 1000 # It changes value enclosed scope variable b
        print("Value of b in inner_function:", b) # Inner function accessing outer function variable
    inner_function()
    print("Value of b in outer_function:", b)

outer_function()

print("#"*40, end="\n\n")
#########################

print("3. Global Scope Example-1")
print("-"*20)
# -------------

c = 2000 # Global Scope, We can access anywhere
def outer_function():
    def inner_function():
        print("Value of c in InnerFunction:", c)
    inner_function()
    print("Value of c in OuterFunction:", c)

outer_function()
print("Value of c in Global:", c)

print("#"*40, end="\n\n")
#########################


print("3. Global Scope Example-2")
print("-"*20)
# -------------

c = 2000 # Global Scope, We can access anywhere
def outer_function():
    def inner_function():
        # c = 3000 # Creates Local Variable
        global c
        c = 3000
        print("Value of c in InnerFunction:", c)
    inner_function()
    print("Value of c in OuterFunction:", c)

outer_function()
print("Value of c in Global:", c)

print("#"*40, end="\n\n")
#########################

# 1. Local # Check in local
# 2. Enclosed # if not present in local then check in enclosed
# 3. Global # If not present in enclosed then check in global
# 4. Builtins : If not present in global then
#               Check in builtins if variable not present in all 3
#
# If not present in all 4 places then only it will throw error