"""
Conditional Statement 'if': Based on the condition we can
execute set of statements

In some languages, we will write 'if' like
if some_condition
{
s1
    s2
        s3
    s4
s5
}
s6

In python, we won't use {} to make a block instead we use INDENTATION

if some_condition
    s1
    s2
    s3
    s4
    s5
    if some_condition
        s1
        s2
        s3
        s4
        s5
s6

"""

print("Using only 'if'")
print("-"*20)
# -------------

x = 10

if x == 10: # We can group like(x == 10) and (x > 10) or (x < 10)
    print("Value of x is 10")

if x > 10:
    print("Value of x is gt 10")

if x < 10:
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
#########################

print("'if-elif'")
print("-"*20)
# -------------

x = 10

if x == 10: # We can group like(x == 10) and (x > 10) or (x < 10)
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
#########################


print("'if-elif-else'")
print("-"*20)
# -------------

x = 10

if x == 10: # We can group like(x == 10) and (x > 10) or (x < 10)
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
#########################

print("'if-with-str/list/tuple/any-other collection'")
print("-"*20)
# -------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

if my_string != "Java" or my_string != "C++":
    print("Not Java/C++")

if not my_string.startswith("Perl"):
    print("Not Perl")

if "tho" in my_string:
    print("Substring Found")

# /list/tuple/any-other collection
my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end="\n")

if "Java-1" in my_list:
    print("Value 'Java-1' found")

print("#"*40, end="\n\n")
#########################

print("'if-with-dictionary'")
print("-"*20)
# -------------

my_dictionary = {"course": "python", "duration": 5, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'mode']
if "duration" in my_dictionary.keys():
    print("Key 'duration' found")

# >>> my_dictionary.values()
# ['python', 5, 'online']
if 'online' in my_dictionary.values():
    print("Value 'online' found")

# my_dictionary.items()
# [('course', 'python'), ('duration', 5), ('mode', 'online')]
if ('duration', 5) in my_dictionary.items():
    print("Item ('duration', 5) Found")

print("#"*40, end="\n\n")
#########################