"""
Comprehensions: We can write one line expression inside
list/tuple/dictionary/set which produce values
is called comprehensions
"""

print("Comprehensions: List")
print("-"*20)
# -------------

L = [1, 2, 3, 4]
print("L:", L)

squared_list = [i*i for i in L]
print("squared_list:", squared_list)

squared_even_list = [i*i for i in L if i%2 == 0]
print("squared_even_list:", squared_even_list)

print("#"*40, end="\n\n")
#########################

print("Comprehensions: Tuple: It is produce generator object")
print("-"*20)
# -------------

L = [1, 2, 3, 4]
print("L:", L)

squared_values = (i*i for i in L)
print("generator squared_values:", squared_values)
print("generator squared_values to list:", list(squared_values))

squared_even_values = (i*i for i in L if i%2 == 0)
print("generator squared_even_values:", squared_even_values)
print("generator squared_even_values to list:", list(squared_even_values))

print("#"*40, end="\n\n")
#########################

print("Comprehensions: Dictionary")
print("-"*20)
# -------------

L = [10, 21, 30, 41]
print("L:", L)

squared_dictionary = {k:v for k,v in enumerate(L)}
# enumerate(L) = [(0,1), (1,2), (2, 3), (3, 4)] = (index,value) pair
squared_even_no_dictionary = {k:v for k,v in enumerate(L) if v%2 ==0}

print("squared_dictionary:", squared_dictionary)
print("squared_even_no_dictionary:", squared_even_no_dictionary)

print("#"*40, end="\n\n")
#########################

print("Comprehensions: Set")
print("-"*20)
# -------------

L = [1, 2, 3, 4]
print("L:", L)

squared_set = {i*i for i in L}
print("squared_set:", squared_set)

squared_even_set = {i*i for i in L if i%2 == 0}
print("squared_even_set:", squared_even_set)

print("#"*40, end="\n\n")
#########################