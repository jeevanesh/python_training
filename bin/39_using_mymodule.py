"""
In this program, we are making use of
variables, functions and classes defined in mymodule.py
"""

print("about 'import' statement")
print("Inside 'mymodule' object")
print("-"*20)
# -------------

import mymodule
print(dir(mymodule))

# - import will create one brandnew object 'mymodule'
# - then import will execute mymodule.py
# - If we execute mymodule.py, 3 objects are getting created
#   1) course 2) add 3) Employee
# - 'import' will keep all 3 objects inside 'mymodule'
# - so we can access from 'mymodule object'

print("#"*40, end="\n\n")
#########################


print("1-way to import")
print("-"*20)
# -------------

import mymodule

print("course:", mymodule.course)

add_result = mymodule.add(10,20)
print("add_result:", add_result)

e = mymodule.Employee()
e.set_name("emp-1")
print("Employee Name:", e.get_name())

print("#"*40, end="\n\n")
#########################

print("2-way to import")
print("-"*20)
# -------------

import mymodule as mm

print("course:", mm.course)

add_result = mm.add(10,20)
print("add_result:", add_result)

e = mm.Employee()
e.set_name("emp-1")
print("Employee Name:", e.get_name())

print("#"*40, end="\n\n")
#########################

print("3-way to import")
print("-"*20)
# -------------

from mymodule import course, add, Employee
# all will be imported to current scope i.e current scope is global scope
# no need to prefix module name

print("course:", course)

add_result = add(10,20)
print("add_result:", add_result)

e = Employee()
e.set_name("emp-1")
print("Employee Name:", e.get_name())

print("#"*40, end="\n\n")
#########################

print("4-way to import")
print("-"*20)
# -------------

from mymodule import course as c, add as a, Employee as E
# all will be imported to current scope i.e current scope is global scope
# no need to prefix module name

print("course:", c)

add_result = a(10,20)
print("add_result:", add_result)

e = E()
e.set_name("emp-1")
print("Employee Name:", e.get_name())

print("#"*40, end="\n\n")
#########################

print("5-way to import")
print("-"*20)
# -------------

from mymodule import *
# all will be imported to current scope i.e current scope is global scope
# no need to prefix module name

print("course:", course)

add_result = add(10,20)
print("add_result:", add_result)

e = Employee()
e.set_name("emp-1")
print("Employee Name:", e.get_name())

print("#"*40, end="\n\n")
#########################