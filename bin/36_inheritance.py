"""
Inheritance: We can extend existing class to provide new features
without disturbing existing class

In this section,
1) multilevel inheritance
2) multiple inheritance
"""

print("1) multilevel inheritance")
print("-"*20)
# -------------

# Assume this is existing class
class Salary:
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# New requirement
# 1) add/view tax methods
# 2) alter get_salary method to return (salary-tax)

# We are extending Salary class
class Employee(Salary):
    # 1) add/view tax methods
    def set_tax(self, tax):
        self.tax = tax
    def get_tax(self):
        return self.tax
    # 2) alter get_salary method to return (salary-tax)
    # POLYMORPHISM: We can reuse same name as super class method
    def get_salary(self): # It will OVERRIDE super class method
        # 1-WAY:
        # return (self.salary - self.tax)
        # 2-Way calling super class method as well
        super_salary = super().get_salary()
        return super_salary - self.tax


e = Employee()
e.set_salary(20000)
e.set_tax(2000)

print("Salary:", e.get_salary())
print("Tax:", e.get_tax())

print("#"*40, end="\n\n")
#########################

# We can use class name to call super class methods
# -------------
#     def get_salary(self): # It will OVERRIDE super class method
#         # 1-WAY:
#         # return (self.salary - self.tax)
#         # 2-Way calling super class method as well
#         super_salary = super().get_salary()
#           OR
#         super_salary = Employee3.get_salary(self)
#         return super_salary - self.tax
#########################

print("2) multiple inheritance")
print("-"*20)
# -------------

# Existing Class-1
# Assume this is existing class
class Salary:
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# Existing Class-2
# Assume this is existing class
class Tax:
    def set_tax(self, tax):
        self.tax = tax
    def get_tax(self):
        return self.tax


# New Requirement
# 1) add/view salary
# 2) add/view tax
# 3) add/view name

class Employee(Salary, Tax): # MRO(Method Resolution Order) -> Left to right
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def new_get_tax(self):
        # Access using CLASS NAME instead of super() example
        result = Tax.get_tax(self)
        return result


e1 = Employee()
e1.set_name("emp-1")
e1.set_salary(20000)
e1.set_tax(2000)

print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())
print("Name:", e1.get_name())
print("New Tax:", e1.new_get_tax())

print("#"*40, end="\n\n")
#########################