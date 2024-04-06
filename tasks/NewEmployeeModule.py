from EmployeeModule import EmployeeClass, my_company_decorator

class NewEmployeeClass(EmployeeClass):
    def __init__(self, emp_name, emp_id, emp_salary, tax):
        super().__init__(emp_name, emp_id, emp_salary)
        self.tax = tax

    @my_company_decorator
    def get_emp_salary(self):
        return super().get_emp_salary() - self.tax

    def set_emp_tax(self, tax):
        self.tax = tax

    def get_emp_tax(self):
        return self.tax

    # def get_avg_salary(*salaries):
    #     if salaries:
    #         return sum(salaries) / len(salaries)
    #     else:
    #         return None

    def get_avg_salary(*salaries):
        total_salary = 0
        num_employees = 0
        for salary in salaries:
            if isinstance(salary, NewEmployeeClass):
                total_salary += salary.get_emp_salary()
                num_employees += 1
        if num_employees > 0:
            return total_salary / num_employees
        else:
            return None

    def __iter__(self):
        for char in self.emp_name:
            yield char

    def get_old_salary(self):
        return super().get_emp_salary()