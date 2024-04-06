"""
2 Cases
Case-1: How access values outside the function
Case-2: How pass values to variables present inside the function

In this section,
Case-1: How access values outside the function
"""

print("Function with 1 return value")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    # step-1: use 'return' statement inside function to send value
    return name

# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################

print("Function with more than 1 return value: TUPLE")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    # step-1: use 'return' statement inside function to send value
    return name, company # It will return in tuple

# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################


print("Function with more than 1 return value: LIST")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    # step-1: use 'return' statement inside function to send value
    return [name, company]

# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################


print("Function with more than 1 return value: Dictionary")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    # step-1: use 'return' statement inside function to send value
    return {"name": name, "company": company}

# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################

print("Function without return value: None")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    # step-1: use 'return' statement inside function to send value
    return

# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################


print("Function without return statement: None")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)


# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################


print("Function with expression in 'return'")
print("-"*20)
# -------------

# 2 steps to access values outside the function
# step-1: use 'return' statement inside function to send value
# step-2: assign function call to variable so that returned value will be stored


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    # step-1: use 'return' statement inside function to send value
    return (10+20)/(10-29) # returns the result

# step-2: assign function call to variable so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################