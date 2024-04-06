"""
All type of arguments in one function
"""


print("All type of arguments in one function")
print("-"*20)
# -------------

# Before *, all arguments are considered positional only arguments, no / required
# After *, all arguments are considered keyword only arguments, no seperate * required

# -----------
# positional only arguments: a, b
# variable positional arguments: c
# keyword only arguments: d, e
# variable keyword arguments: f
# -----------

# Order of the arguments
# -----------
# 1st put all positional arguments IF ANY
# then
# put variable positional arguments IF ANY
# then
# put all keyword arguments IF ANY
# then
# put variable keyword arguments IF ANY
# -----------

def add(a,b,*c,d,e,**f):
    return a + b + sum(c) + d + e + sum(f.values())

add_result_1 = add(10, 20, d=30, e=40)
# a=10, b=20, c=(), d=30, e=40, f={}

add_result_2 = add(10, 20, 30, 40, 50, d=60, e=70, x=80, y=90, z=100)
# a=10, b=20, c=(30, 40, 50), d=60, e=70, f={x:80, y:90, z:100}
print("add_result_1:", add_result_1)
print("add_result_2:", add_result_2)



# Order of the arguments
# -----------
# 1st put all positional arguments IF ANY
# then
# put variable positional arguments IF ANY
# then
# put all keyword arguments IF ANY
# then
# put variable keyword arguments IF ANY
# -----------

# Example: orders
# 1. def add(a,b,*c,d,e,**f) : ORDER IS CORRECT
# 2. def add(*c,d,e,**f) : CORRECT: variable arg then kw arg then variable kw arg
# 3. def add(*,d,e,**f) : ORDER IS CORRECT: d,e keyword arg then f is variable kw arg
# 4. def add(a,b,*,d,e) : ORDER IS CORRECT: a, b are positional, d,e are keyword

print("#"*40, end="\n\n")
#########################