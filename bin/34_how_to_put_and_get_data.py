"""
How to store the values and get the values

3-way to store the values and get the values

In this section, we should get clarity on
1. __new__ : constructor
2. __init__ : Initializer
"""

print("CLASS Methods and INSTANCE Methods")
print("-"*20)
# -------------

# class Employee(object):
class Employee: # same as above, by default inherited from 'object' class

    def __init__(self, name):
        # This will automatically execute after creating object
        # This we can use it for initializing object
        # We need to pass values to this method while creating the object only
        self.name = name

    company_name = "XYZ Company"
    # if we declare any variable inside the class then it will get store in class object

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def get_employee_name(self):
        name = "abc" # This local variable, it will get cleaned up when function execution completed
        return self.name


# Create 2 object
e1 = Employee("emp-1") # __init__(e1, "emp-1")
e2 = Employee("emp-2") # __init__(e2, "emp-2")

# print
print("Company Name:", Employee.get_company_name()) # object 'Employee' will go as 1st argument
print("Employee-1 name:", e1.get_employee_name()) # object 'e1' will go as 1st argument
print("Employee-2 name:", e2.get_employee_name()) # object 'e2' will go as 1st argument

print("#"*40, end="\n\n")
#########################

print("super class is 'object' class")
print("All classes inherited from  'object' class")
print("-"*20)
# -------------

print(dir(object))

# - 'object' class is super class for all the class
# - Many methods are present inside 'object' class
#   can be access by all user defined classes
# - __new__, __init__ are 2 of them
# - when we create object of 'Employee' e1 = Employee()
#   then 1st call __new__() which is creating object and stored in e1
#   then it calls __init__()
# - Eventhoug all methods are visible in our current class (Inheritec class)
#   we can always rewrite methods present in 'object' in our current class
#   using same name (POLYMORPHISM)
# - We wrote __init__ again in our class
# - our class __init__ will override super class __init__ and execute
#   our class __init__

print("#"*40, end="\n\n")
#########################