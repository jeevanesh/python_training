class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def get_emp_name(self):
        return self.emp_name

    def get_emp_id(self):
        return self.emp_id

    def get_emp_salary(self):
        return self.emp_salary

E1 = EmployeeClass('emp-1', 100, 1000)
print(E1.get_emp_name())  # Output: emp-1
print(E1.get_emp_id())    # Output: 100
print(E1.get_emp_salary())# Output: 1000