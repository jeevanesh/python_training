def my_company_decorator(func):
    def wrapper(*args, **kwargs):
        print("Company Name Is: \"XYZ Company\"")
        print("Address: XYZ Address")
        return func(*args, **kwargs)
    return wrapper

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    @my_company_decorator
    def get_emp_name(self):
        return self.emp_name

    @my_company_decorator
    def get_emp_id(self):
        return self.emp_id

    @my_company_decorator
    def get_emp_salary(self):
        return self.emp_salary

E1 = EmployeeClass('emp-1', 100, 1000)
print(E1.get_emp_name())
print(E1.get_emp_id())
print(E1.get_emp_salary())