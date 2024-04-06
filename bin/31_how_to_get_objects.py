"""
How to get objects?
- Using class, we can create n number of objects

In this section, we should get clarity on
1. CLASS OBJECT
2. INSTANCE OBJECT
"""


print("CLASS object and INSTANCE OBJECT")
print("-"*20)
# -------------

class Employee:
    pass
# Use 'pass' to keep any block empty
# even though it is empty class, it is valid class

# Create 2 object
e1 = Employee()
# Employee() create brandnew object and store in 'e1'
e2 = Employee()
# Employee() create brandnew object and store in 'e2'

# Total we have 3 objects
# CLASS OBJECT: 'Employee' which is automatically getting created
# INSTANCE OBJECTS: 'e1' and 'e2' are called INSTANCE objects which we are creating

print("CLASS object 'Employee':", Employee)
print("INSTANCE object 'e1':", e1)
print("INSTANCE object 'e2':", e2)

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