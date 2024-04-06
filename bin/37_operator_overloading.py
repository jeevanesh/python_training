"""
Operator Overloading:
We can support for any operators like +, - etc. in our class

In python, for each operator there is special-name given
example:
+ = __add__
- = __sub__

for example,
If we want to support for + then we need to write __add__ in our class
"""

print("Supported + operator")
print("-"*20)
# -------------

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other_object): # self = e1, other_object = e2
        cancat_result = self.name + other_object.name
        return cancat_result

# REQUIREMENT: if we add 2 employee objects then it should concat both employee names
e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # Internally e1.__add__(e2)
print("'+' result:", result)

print("#"*40, end="\n\n")
#########################


print("Supported __str__ operator")
print("-"*20)
# -------------

# REQUIREMENT: if we print object e1 currently it is printing
# object reference now it should print employee name

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other_object): # self = e1, other_object = e2
        cancat_result = self.name + other_object.name
        return cancat_result

    def __str__(self): # return what we want to print if we print object like e1
        return self.name


e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # Internally e1.__add__(e2)
print("'+' result:", result, end="\n\n")

print("Employee-1 Name using __str__:", e1) # it calls __str__
print("Employee-2 Name using __str__:", e2, end="\n\n") # it calls __str__

print("#"*40, end="\n\n")
#########################

print("Supported len()")
print("-"*20)
# -------------

# REQUIREMENT: if we call len() it should return total no of chars in employee name

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other_object): # self = e1, other_object = e2
        cancat_result = self.name + other_object.name
        return cancat_result

    def __str__(self): # return what we want to print if we print object like e1
        return self.name

    def __len__(self):
        length = len(self.name)
        return length

e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # Internally e1.__add__(e2)
print("'+' result:", result, end="\n\n")

print("Employee-1 Name using __str__:", e1) # it calls __str__
print("Employee-2 Name using __str__:", e2, end="\n\n") # it calls __str__

print("Employee-1 Name length:", len(e1)) # it calls e1.__len__()
print("Employee-2 Name length:", len(e2), end="\n\n") # it calls e1.__len__()

print("#"*40, end="\n\n")
#########################

print("Supported iteration")
print("-"*20)
# -------------

# REQUIREMENT: if we iterate it should provide each character from emp name

# 2 Methods need to implement
# 1) __iter__
#       - 1st time it will be called
#       - If we want to initialize something before iteration
#           then we can make use of this method
#
# 2) __next__ # every iteration it will be called
#       - We can return what value we need to provide during every iteration
#
#
class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other_object): # self = e1, other_object = e2
        cancat_result = self.name + other_object.name
        return cancat_result

    def __str__(self): # return what we want to print if we print object like e1
        return self.name

    def __len__(self):
        length = len(self.name)
        return length

    def __iter__(self):
        self.start_index = 0
        return self

    def __next__(self):
        current_index = self.start_index
        if current_index < len(self.name):
            self.start_index += 1
            return self.name[current_index]
        else:
            raise StopIteration

e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # Internally e1.__add__(e2)
print("'+' result:", result, end="\n\n")

print("Employee-1 Name using __str__:", e1) # it calls __str__
print("Employee-2 Name using __str__:", e2, end="\n\n") # it calls __str__

print("Employee-1 Name length:", len(e1)) # it calls e1.__len__()
print("Employee-2 Name length:", len(e2), end="\n\n") # it calls e1.__len__()

print("Iterate using for-loop")
for each_char in e1:
    print("Emp-1 Each Char:", each_char)
for each_char in e2:
    print("Emp-2 Each Char:", each_char)
print("\n\n")

print("Iterate Manually using iter() and next()")
my_iterator = iter(e1)
print("Each Char:", next(e1))
print("Each Char:", next(e1))
print("Each Char:", next(e1))
print("Each Char:", next(e1))
print("Each Char:", next(e1), end="\n\n")
# print("Each Char:", next(e1)) # Error


print("Iterate Manually using iter() and next() using while-loop")
my_iterator = iter(e1)
while True:
    try:
        print("Each Char:", next(e1))
    except StopIteration:
        print("Iteration Completed")
        break

print("#"*40, end="\n\n")
#########################