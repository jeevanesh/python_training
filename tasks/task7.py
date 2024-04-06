class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def get_emp_salary(self):
        return self.emp_salary

class NewEmployeeClass(EmployeeClass):
    def __init__(self, emp_name, emp_id, emp_salary, tax):
        super().__init__(emp_name, emp_id, emp_salary)
        self.tax = tax

    def set_tax(self, tax):
        self.tax = tax

    def get_tax(self):
        return self.tax

    def get_emp_salary(self):
        return self.emp_salary - self.tax

    def get_old_salary(self):
        return super().get_emp_salary()

E1 = NewEmployeeClass('emp-1', 100, 1000, 200)
print(E1.get_emp_salary())  # output 800
print(E1.get_old_salary())  # output 1000