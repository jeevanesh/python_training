"""
PACKAGES
We can organize/keep modules in folders & sub-folders
these folders & sub-folders are called PACKAGES
"""
print("1-way to import")
print("-"*20)
# -------------

import mypackage.db.mymodule

print("course:", mypackage.db.mymodule.course)

add_result = mypackage.db.mymodule.add(10,20)
print("add_result:", add_result)

e = mypackage.db.mymodule.Employee()
e.set_name("emp-1")
print("Employee Name:", e.get_name())

print("#"*40, end="\n\n")
#########################

print("2-way to import")
print("-"*20)
# -------------

import mypackage.db.mymodule as mm

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

from mypackage.db.mymodule import course, add, Employee
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

from mypackage.db.mymodule import course as c, add as a, Employee as E
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

from mypackage.db.mymodule import *
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

print("We can keep modules/packages in any directory/drive/mount-point")
print("and provide that directory path")
print("2ways to provide directory path")
print("1-way is to add in sys.path list")
print("-"*20)
# -------------

# Exmple: If we have module/package in D:\mylib
# then
import sys
sys.path.append(r"D:\mylib")
print(sys.path)
# After adding, import

print("#"*40, end="\n\n")
#########################

print("2nd way to provide directory path")
print("-"*20)
# -------------
print("""
In Environment Variable,
add new vairable & value
VARIABLE NAME=PYTHONPATH
VARIABLE VALUE="D:\mylib;E:\mylib2"
""")

print("#"*40, end="\n\n")
#########################