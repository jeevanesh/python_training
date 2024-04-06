"""
Here,
2-way: position only arguments
"""
print("position arguments only ")
print("-"*20)
# -------------


def employee(name, company, /):
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    return [name, company]


received_value = employee("emp-1", "comp-1") # positional arguments, We can pass only values
print("received_value:", received_value, end="\n\n")

# We can't pass with keyword because it is position only argument function
# received_value = employee(name="emp-2", company="comp-2")  # keyword arguments, We can pass only values
# print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################


print("position arguments only with default values")
print("-"*20)
# -------------


def employee(name, company="comp-1", /):
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    return [name, company]

received_value = employee("emp-1") # company will make use of default value
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "comp-2")
print("received_value:", received_value, end="\n\n")

# We can't pass with keyword because it is position only argument function
# received_value = employee(name="emp-2", company="comp-2")  # keyword arguments, We can pass only values
# print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################