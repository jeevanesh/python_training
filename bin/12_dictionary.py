"""
-dictionary: To keep Collection of values, like list of names, list of email-ids etc
    -- we can store duplicate values
    -- Here we can provide index to each value called KEY/VALUE PAIR
"""

print("Dictionary PART-1")
print("How to store the values")
print("-"*20)
# -------------

my_dictionary_1 = {0:"python", 1:5, 2:"online"}
# Internally it will create object of buitlin-class 'dict' and store the values
# Inside {} if we keep key:value then it will become dictionary

# We can also create using class name
my_dictionary_2 = dict({0:"python", 1:5, 2:"online"})

my_dictionary_3 = dict([(0,"python"), (1,5), (2,"online")])

# FOR KEY: We can use only IMMUTABLE VALUES like numbers, strings, tuple
my_dictionary_4 = {"course":"python", "duration":5, "mode":"online"}

# FOR VALUE: We can store any type of values (IMMUTABLE/MUTABLE)
my_dictionary_5 = {
    "duration": 5,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)
print("my_dictionary_4:", my_dictionary_4)
print("my_dictionary_5:", my_dictionary_5)

print("#"*40, end=r"\n\n")
#########################

print("Dictionary PART-2")
print("We can access each value using 'key'")
print("-"*20)
# -------------

my_dictionary = {
    "duration": 5,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n") # 5

print("course:", my_dictionary["course"]) # "Python"
print("2nd character in course name:", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("2nd Mode:", my_dictionary["mode"][1]) # "offline"
print("4th character in 2nd Mode:", my_dictionary["mode"][1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Trainer lname:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd character in Trainer lname:", my_dictionary["trainer"]["lname"][1], end="\n\n") # "y"

print("#"*40, end=r"\n\n")
#########################

print("Dictionary PART-3")
print("Methods inside 'dict' class")
print("-"*20)
# -------------

print(dir(my_dictionary))

# OR
# print(dir(dict))

print("#"*40, end=r"\n\n")
#########################


print("Dictionary PART-4")
print("Add/Remove/Update")
print("-"*20)
# -------------

my_dictionary = {"course":"python", "duration":5, "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# Add new element if key not present else Update
my_dictionary["location"] = "India"
print("my_dictionary after adding/updating location:", my_dictionary, end="\n\n")

# Add new element if key not present else Update
new_item = {"trainer": "xyz"}
my_dictionary.update(new_item)
print("my_dictionary after adding/updating trainer:", my_dictionary, end="\n\n")

removed_value = my_dictionary.popitem()
print("my_dictionary after removing last item:", my_dictionary, end="\n\n")
print("removed_value:", removed_value)

print("#"*40, end="\n\n")
#########################