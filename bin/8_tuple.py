"""
- tuple: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store duplicate values
    -- Here automatically index will be assigned to each values
"""

print("Tuple PART-1")
print("How to store the values")
print("-"*20)
# -------------

my_tuple_1 = (10, 12.5, "python", (100,200), ["Java", "C"])
# Internally it will create object of predefined/builtin-class 'tuple' and store the values

# OR we can use class name
my_tuple_2 = tuple((10, 12.5, "python", (100,200), ["Java", "C"]))

print(my_tuple_1, my_tuple_2, sep="\n")

print("#"*40, end=r"\n\n")
#########################

print("Tuple PART-2")
print("Indexes are similar 'string' ")
print("-"*20)
# -------------

my_tuple = (10, 12.5, "python", (100,200), ["Java", "C"])
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # "Python"
print("2nd char in Course Name:", my_tuple[2][1]) # "y"

print("#"*40, end=r"\n\n")
#########################

print("Tuple PART-3")
print("Methods inside 'tuple' class")
print("-"*20)
# -------------

print(dir(my_tuple))

# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
#########################


print("Tuple PART-4")
print("'count' & 'index' method")
print("-"*20)
# -------------

my_tuple = (10, 12.5, "python", (100,200), ("Java", "C"))
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("python")
index_of_python = my_tuple.index("python")

# Index of 'a' in 'Java'
inner_tuple = my_tuple[4] # ("Java", "C")
course_name = inner_tuple[0] # "Java"
index_of_a = course_name.index("a")

# OR, we can combine
index_of_a = my_tuple[4][0].index("a")
print("index_of_a:", index_of_a)

print("#"*40, end="\n\n")
#########################