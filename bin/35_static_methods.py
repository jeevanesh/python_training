"""
Static Methods
"""

print("Static methods")
print("-"*20)
# -------------

# Add method to compute avg salary
# in simple, if we pass 2 nos then it should return avg of 2 nos

class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

    # OPTION-1
    # Here no where we are making use of class object 'cls'
    # other way, no need of class object reference inside method
    # @classmethod
    # def compute_avg_salary(cls, sal1, sal2):
    #     return (sal1+sal2)/2

    # OPTION-2
    # Here no where we are making use of class object 'self'
    # other way, no need of inside object reference inside method
    # def compute_avg_salary(self, sal1, sal2):
    #     return (sal1 + sal2) / 2

    # OPTION-3 (Internally NO OBJECT WILL BE PASSED AS 1st ARGUMENT)
    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2)


e1 = Salary()
e1.add_salary(20000)

e2 = Salary()
e2.add_salary(22000)

sal1 = e1.get_salary()
sal2 = e2.get_salary()

# We can access static method using either CLASS/INSTANCE

avg1 = Salary.compute_avg_salary(sal1, sal2)
avg2 = e1.compute_avg_salary(sal1, sal2)
avg3 = e2.compute_avg_salary(sal1, sal2)

print(avg1, avg2, avg3)

print("#"*40, end="\n\n")
#########################