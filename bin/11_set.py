"""
- set: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store only UNIQUE values
    -- No Index to each value
    -- order of the values will be random everytime
    -- set & frozenset both can store only immutable values numbers, strings, tuples
"""

print("set PART-1")
print("How to store the values")
print("-"*20)
# -------------

my_set_1 = {10, "Python", "Java", "Python", "Java", "Python", "Java"}

my_set_2 = set([10, "Python", "Java", "Python", "Java", "Python", "Java" ])

print(my_set_1, my_set_2, sep="\n")

print("#"*40, end=r"\n\n")
#########################


# How to access individual values
# -------------
# OPTION-1: convert to list/tuple etc which is having indexes
# OPTION-2: We can iterate using loops
#########################


print("set PART-2")
print("Methods inside 'set' class")
print("-"*20)
# -------------

print(dir(my_set_1))

# OR
# print(dir(set))

print("#"*40, end=r"\n\n")
#########################


print("set PART-3")
print("'union', 'intersection', 'difference' methods")
print("-"*20)
# -------------

sb_account_customers = set(["cust-1", "cust-2", "cust-3", "cust-4"])
loan_account_customers = set(["cust-3", "cust-4", "cust-5", "cust-6"])
print("sb_account_customers:", sb_account_customers)
print("loan_account_customers:", loan_account_customers, end="\n\n")

all_customers = sb_account_customers.union(loan_account_customers)
print("all_customers:", all_customers)

customers_not_having_loan = sb_account_customers.difference(loan_account_customers)
print("customers_not_having_loan:", customers_not_having_loan)

customers_having_both = sb_account_customers.intersection(loan_account_customers)
print("customers_having_both:", customers_having_both)

print("#"*40, end="\n\n")
#########################


print("set PART-4")
print("add/remove/update")
print("-"*20)
# -------------

sb_account_customers = set(["cust-1", "cust-2", "cust-3", "cust-4"])
print("sb_account_customers:", sb_account_customers)

# add new customer
sb_account_customers.add("cust-5")
sb_account_customers.add("cust-5") # Duplicate will be removed automatically
print("sb_account_customers after adding cust-5 twice:", sb_account_customers)

# Remove customer
sb_account_customers.remove("cust-4")
print("sb_account_customers after removing cust-4:", sb_account_customers)

# Update
new_customers = {"cust-30", "cust-40", "cust-50"}
sb_account_customers.update(new_customers)
print("sb_account_customers after update:", sb_account_customers)

print("#"*40, end="\n\n")
#########################