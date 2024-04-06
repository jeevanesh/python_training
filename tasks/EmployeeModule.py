import functools

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    @property
    def emp_name(self):
        return self._emp_name

    @emp_name.setter
    def emp_name(self, value):
        if len(value) > 10:
            raise ValueError("Employee name cannot be longer than 10 characters")
        self._emp_name = value

    @functools.lru_cache()
    def get_emp_salary(self):
        return self.emp_salary

def my_company_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Company Name Is: \"XYZ Company\"")
        print("Address: XYZ Address")
        return func(*args, **kwargs)
    return wrapper