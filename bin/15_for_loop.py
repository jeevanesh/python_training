"""
for-loop: Iterate any collection
"""

print("'for-with-str/list/tuple/any-other collection'")
print("-"*20)
# -------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

# Syntax: for provide_some_variable in provide_any_collection
for each_char in my_string:
    print("Each Char:", each_char)

# /list/tuple/any-other collection
my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end="\n")

for each_value in my_list:
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
#########################

print("'for-with-dictionary'")
print("-"*20)
# -------------

my_dictionary = {"course": "python", "duration": 5, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'mode']
for each_key in my_dictionary.keys():
    print("Each Key using keys():", each_key)
    print("Value of that key:", my_dictionary[each_key])


# >>> my_dictionary.values()
# ['python', 5, 'online']
for each_value in my_dictionary.values():
    print("Each Value using values():", each_value)

# my_dictionary.items()
# [('course', 'python'), ('duration', 5), ('mode', 'online')]
for each_item in my_dictionary.items():
    print("each_item:", each_item)
    print("key:", each_item[0])
    print("value:", each_item[1])

# my_dictionary.items()
# [('course', 'python'), ('duration', 5), ('mode', 'online')]
for i, j in my_dictionary.items():
    print("2nd way key:", i)
    print("2nd way value:", j)

print("#"*40, end="\n\n")
#########################

# -------------
# 2 Cases
###############
# Case-1: How to stop for-loop in between
# Case-2: How to skip current iteration & jump to next iteration
#########################

print("# Case-1: How to stop for-loop in between")
print("-"*20)
# -------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end="\n")

# Requirement: Findout, are there any value starting with java
# if one value found then it is found only, no need to check for other values

for each_value in my_list:
    if each_value.startswith("Java"):
        print("Found")
        break

print("#"*40, end="\n\n")
#########################


print("print found & not-found")
print("-"*20)
# -------------

my_list = ["C++", "XJava-1", "Perl", "XJava-2", "Python"]
print("my_list:", my_list, end="\n")

# Requirement: Findout, are there any value starting with java
# if one value found then it is found only, no need to check for other values

my_flag = 0
for each_value in my_list:
    if each_value.startswith("Java"):
        my_flag = 1
        print("Found")
        break

if my_flag == 0:
    print("Not Found")

print("#"*40, end="\n\n")
#########################

print("print found & not-found using 'for-else'")
print("We have 'for-else' like 'if-else'")
print("-"*20)
# -------------

my_list = ["C++", "XJava-1", "Perl", "XJava-2", "Python"]
print("my_list:", my_list, end="\n")

# Requirement: Findout, are there any value starting with java
# if one value found then it is found only, no need to check for other values

for each_value in my_list:
    if each_value.startswith("Java"):
        print("Found")
        break
else:
    print("Not Found")

# About 'for-else'
# POINT-1: After completing for-loop, 'else' block will execute
# POINT-2: If 'for-loop' ended using 'break' then 'else' will also skipped

print("#"*40, end="\n\n")
#########################

print("# Case-2: How to skip current iteration & jump to next iteration")
print("-"*20)
# -------------

my_list = ["C++", "XJava-1", "Perl", "XJava-2", "Python"]
print("my_list:", my_list, end="\n")

for each_value in my_list:
    print("Current Value:", each_value)
    # If value is not starting with java, then that value is not required for
    # remaining block,
    if not each_value.startswith("Java"):
        continue
    # Below code till end of the block is applicable for 'JAVA' courses only
    print("This Java course name is :", each_value)
    print("This is one version of Java")
    print("This JAVA course duration is 10 days")

print("#"*40, end="\n\n")
#########################