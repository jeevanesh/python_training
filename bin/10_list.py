"""
- list: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store duplicate values
    -- immutable if we need then we can make use of 'tuple'
    -- Here automatically index will be assigned to each values
"""

print("list PART-1")
print("How to store the values")
print("-"*20)
# -------------

my_list_1 = [10, 12.5, "python", (100,200), ["Java", "C"]]
# Internally it will create object of predefined/builtin-class 'list' and store the values

# OR we can use class name
my_list_2 = list((10, 12.5, "python", (100,200), ["Java", "C"]))

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end=r"\n\n")
#########################

print("list PART-2")
print("Indexes are similar 'string' ")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100,200), ["Java", "C"]]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # "Python"
print("2nd char in Course Name:", my_list[2][1]) # "y"

print("#"*40, end=r"\n\n")
#########################


print("list PART-3")
print("Methods inside 'list' class")
print("-"*20)
# -------------

print(dir(my_list))

# OR
# print(dir(list))

print("#"*40, end="\n\n")
#########################


print("list PART-4")
print("'count' & 'index' method")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100,200), ("Java", "C")]
print("my_list:", my_list, end="\n\n")

count_of_python = my_list.count("python")
index_of_python = my_list.index("python")

# Index of 'a' in 'Java'
inner_list = my_list[4] # ("Java", "C")
course_name = inner_list[0] # "Java"
index_of_a = course_name.index("a")

# OR, we can combine
index_of_a = my_list[4][0].index("a")
print("index_of_a:", index_of_a)

print("#"*40, end="\n\n")
#########################

print("list PART-5")
print("add/remove/update")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100,200), ["Java", "C"]]
print("my_list:", my_list, end="\n\n")

my_list.append("Perl") # [10, 12.5, "python", (100,200), ["Java", "C"], "Perl"]
print("my_list after append perl:", my_list)

my_list[4].insert(0,"C++")
print("my_list after append c++ in inner list:", my_list)

my_list[2]="Shell"
print("my_list after updating 'python' to shell")

removed_value = my_list.pop() # Remove last element
print("my_list after removing last value:", my_list)
print("removed_value:", removed_value)

print("#"*40, end="\n\n")
#########################