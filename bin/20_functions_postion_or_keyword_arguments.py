"""
In this section,
Case-2: How pass values to variables present inside the function

In Case-2, we have 3 ways to pass values
1-way: position or keyword arguments
2-way: position only arguments
3-way: keyword only arguments

Here we will discuss
1-way: position or keyword arguments

"""

print("position or keyword arguments")
print("-"*20)
# -------------


def employee(name, company):
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    return [name, company]

received_value = employee("emp-1", "comp-1") # positional arguments, We can pass only values
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-2", company="comp-2")  # keyword arguments, We can pass only values
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################


print("position or keyword arguments with default values")
print("-"*20)
# -------------


def employee(name, company="comp-1"):
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    return [name, company]

received_value = employee("emp-1") # company will make use of default value
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-2", company="comp-2")  # keyword arguments, We can pass only values
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################