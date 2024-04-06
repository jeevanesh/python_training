"""
How to store the values and get the values

2-way to store the values and get the values

In this section, we should get clarity on
1. CLASS Methods
2. INSTANCE Methods
"""

print("CLASS Methods and INSTANCE Methods")
print("-"*20)
# -------------

class Employee:
    @classmethod
    def store_company_name(cls, company_name):
        cls.company_name = company_name

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def store_employee_name(self, name):
        self.name = name

    def get_employee_name(self):
        return self.name


# Create 2 object
e1 = Employee()
e2 = Employee()

# Store Values
# Employee.store_company_name(Employee, "XYZ Company")
# No need to pass 'Employee' because internally it will pass
Employee.store_company_name("XYZ Company")
e1.store_employee_name("emp-1") # internally e1 will go as 1st argument
e2.store_employee_name("emp-2") # internally e2 will go as 1st argument

# print
print("Company Name:", Employee.get_company_name()) # object 'Employee' will go as 1st argument
print("Employee-1 name:", e1.get_employee_name()) # object 'e1' will go as 1st argument
print("Employee-2 name:", e2.get_employee_name()) # object 'e2' will go as 1st argument

print("#"*40, end="\n\n")
#########################

# Why @classmethod?
# -----------
# - We can access methods & variables of class object using all INSTANCE OBJECTS
# - Example: We can access store_company_name() like
#  Employee.store_company_name("ABC company") # @classmethod will make sure pass class object as 1st argument to cls
#  e1.store_company_name("ABC company") # @classmethod will make sure pass class object as 1st argument to cls
#  e2.store_company_name("ABC company") # @classmethod will make sure pass class object as 1st argument to cls
#
# -- Another Example
# Employee.get_employee_name() # ERROR: Employee object will NOT go as 1st param
# Employee.get_employee_name(e1) # CORRECT
# Employee.get_employee_name(e2) # CORRECT
#########################