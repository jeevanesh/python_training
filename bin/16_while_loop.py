"""
While-loop: Execute the loop till the condition is True
"""

print("While Example")
print("-"*20)
# -------------

x = 0
while x < 10:
    print("Value of x is:", x)
    x = x + 1

print("#"*40, end="\n\n")
#########################

print("'while-with-str/list/tuple/any-other collection'")
print("-"*20)
# -------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

index_no = 0
while index_no < len(my_string):
    print("Each Char:", my_string[index_no])
    index_no += 1 # index_no = index_no + 1

# Syntax: for provide_some_variable in provide_any_collection
# for each_char in my_string:
#     print("Each Char:", each_char)

# /list/tuple/any-other collection
my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end="\n")

index_no = 0
while index_no < len(my_list):
    print("Each Value:", my_list[index_no])
    index_no += 1

# for each_value in my_list:
#     print("Each Value:", each_value)

print("#"*40, end="\n\n")
#########################

# -------------
# 2 Cases
###############
# Case-1: How to stop while-loop in between
# Case-2: How to skip current iteration & jump to next iteration
#########################

print("# Case-1: How to stop while-loop in between")
print("We have 'while-else' like 'if-else'")
print("-"*20)
# -------------

my_list = ["C++", "XJava-1", "Perl", "XJava-2", "Python"]
print("my_list:", my_list, end="\n")

# Requirement: Findout, are there any value starting with java
# if one value found then it is found only, no need to check for other values

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Found")
        break
    index_no = index_no + 1
else:
    print("Not Found")

# for each_value in my_list:
#     if each_value.startswith("Java"):
#         print("Found")
#         break
# else:
#     print("Not Found")

# About 'while-else'
# POINT-1: After completing while-loop, 'else' block will execute
# POINT-2: If 'while-loop' ended using 'break' then 'else' will also skipped

print("#"*40, end="\n\n")
#########################

print("# Case-2: How to skip current iteration & jump to next iteration")
print("-"*20)
# -------------

my_list = ["C++", "Java-1", "Perl", "XJava-2", "Python"]
print("my_list:", my_list, end="\n")

index_no = 0
while index_no < len(my_list):
    print("Current Value:", my_list[index_no])
    if not my_list[index_no].startswith("Java"):
        index_no += 1
        continue
    # Below code till end of the block is applicable for 'JAVA' courses only
    print("This Java course name is :", my_list[index_no])
    print("This is one version of Java")
    print("This JAVA course duration is 10 days")
    index_no += 1


# for each_value in my_list:
#     print("Current Value:", each_value)
#     # If value is not starting with java, then that value is not required for
#     # remaining block,
#     if not each_value.startswith("Java"):
#         continue
#     # Below code till end of the block is applicable for 'JAVA' courses only
#     print("This Java course name is :", each_value)
#     print("This is one version of Java")
#     print("This JAVA course duration is 10 days")

print("#"*40, end="\n\n")
#########################