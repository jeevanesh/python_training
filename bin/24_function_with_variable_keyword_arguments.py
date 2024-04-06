"""
Variable Keyword Arguments
"""


print("Variable Keyword arguments")
print("-"*20)
# -------------

def employee(*, name, company, **prev_companies):
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    print("Inside Function, Prev Companies:", prev_companies)
    return [name, company, prev_companies]

received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-1", company="comp-1", pc1="prev_comp_1", pc2="prev_comp_2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################