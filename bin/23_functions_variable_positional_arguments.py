"""
Variable positional arguments

# OPTION-1
def some_func(all_pos_or_kw_args)

# OPTION-2
def some_func(all_only_pos_args, /)

# OPTION-3
def some_func(*, all_only_kw_args)

# OPTION-4 # for phone we can pass only values, we can't mention keyword
        because of *arg after that
def some_func(all_only_pos_args, /, phone, *var_args)

# OPTION-5
def some_func(all_only_pos_args, /, *var_args, phone)

"""

print("Variable positional arguments")
print("-"*20)
# -------------

def employee(name, company, /, *prev_companies, phone):
    print("Inside Function, Name:", name)
    print("Inside Function, Company:", company)
    print("Inside Function, Phone:", phone)
    print("Inside Function, Prev Companies:", prev_companies)
    return [name, company, phone, prev_companies]

received_value = employee("emp-1", "comp-1", phone="1233444")
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-1", "comp-1", "prev_comp_1", "prev_comp_2" ,phone="1233444")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################