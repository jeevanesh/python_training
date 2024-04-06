class EmployeeClass:
    company_head_name = None

    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    @classmethod
    def set_company_head_name(cls, name):
        cls.company_head_name = name

    @classmethod
    def get_company_head_name(cls):
        return cls.company_head_name

EmployeeClass.set_company_head_name('head-1')
print(EmployeeClass.get_company_head_name())  # output 'head-1'