"""
How to store the values and get the values

1-way to store the values and get the values

In this section, we should get clarity on
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("CLASS VARIABLES and INSTANCE VARIABLES")
print("-"*20)
# -------------

class Employee:
    pass

# Create 2 object
e1 = Employee()
e2 = Employee()

# Store Values
Employee.company_name = "XYZ Company"
# Internally it will create ''company_name' variable inside 'Employee' object and store the values
e1.name = "emp-1"
# Internally it will create 'name' variable inside 'e1' object and store the values
e2.name = "emp-2"
# Internally it will create 'name' variable inside 'e2' object and store the values

# print
print("Company Name:", Employee.company_name)
print("Employee-1 name:", e1.name)
print("Employee-2 name:", e2.name)

print("#"*40, end="\n\n")
#########################

print("Inside each object")
print("-"*20)
# -------------

print("Inside BRANDNEW CLASS object 'Employee':", dir(Employee))
print("Inside BRANDNEW INSTANCE object 'e1':", dir(e1))
print("Inside BRANDNEW INSTANCE object 'e2':", dir(e2))

print("#"*40, end="\n\n")
#########################

# CLASS OBJECT 'Employee' is common space for all instance objects
# If some data is common for all instance objects then we can make use
# class object to store and access using class or instance object

print("WE CAN Access class object data using instance objects")
print("-"*20)
# -------------

print("Company Name using class object 'Employee':", Employee.company_name)
print("Company Name using instance object 'e1':", e1.company_name)
print("Company Name using instance object 'e2':", e2.company_name)

print("#"*40, end="\n\n")
#########################