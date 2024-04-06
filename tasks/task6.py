class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    @staticmethod
    def average_salary(*salaries):
        if salaries:
            return sum(salaries) / len(salaries)
        else:
            return None

E1 = EmployeeClass('emp-1', 100, 1000)
E2 = EmployeeClass('emp-2', 200, 2000)
E3 = EmployeeClass('emp-3', 300, 3000)

print(EmployeeClass.average_salary(E1.emp_salary, E2.emp_salary, E3.emp_salary))  # output 2000.0