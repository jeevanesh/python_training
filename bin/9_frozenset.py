"""
- frozenset: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store only UNIQUE values
    -- No Index to each value
    -- order of the values will be random everytime
    -- set & frozenset both can store only immutable values numbers, strings, tuples
"""

print("Frozenset PART-1")
print("How to store the values")
print("-"*20)
# -------------

# No shortcut for frozenset class, so we will create using class name
fs = frozenset([10, "Python", "Java", "Python", "Java", "Python", "Java" ])
print(fs)

print("#"*40, end=r"\n\n")
#########################


# How to access individual values
# -------------
# OPTION-1: convert to list/tuple etc which is having indexes
# OPTION-2: We can iterate using loops
#########################


print("Frozenset PART-2")
print("Methods inside 'frozenset' class")
print("-"*20)
# -------------

print(dir(fs))

# OR
# print(dir(frozenset))

print("#"*40, end=r"\n\n")
#########################


print("Frozenset PART-3")
print("'union', 'intersection', 'difference' methods")
print("-"*20)
# -------------

sb_account_customers = frozenset(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_account_customers = frozenset(["cust-3", "cust-4", "cust-5", "cust-6"])
print("sb_account_customers:", sb_account_customers)
print("loan_account_customers:", loan_account_customers, end="\n\n")

all_customers = sb_account_customers.union(loan_account_customers)
print("all_customers:", all_customers)

customers_not_having_loan = sb_account_customers.difference(loan_account_customers)
print("customers_not_having_loan:", customers_not_having_loan)

customers_having_both = sb_account_customers.intersection(loan_account_customers)
print("customers_having_both:", customers_having_both)

print("#"*40, end=r"\n\n")
#########################