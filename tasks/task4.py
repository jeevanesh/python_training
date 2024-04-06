class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def __iter__(self):
        return iter(self.emp_name)

E1 = EmployeeClass('emp-1', 100, 1000)
for c in E1:
    print("Each Char:", c)