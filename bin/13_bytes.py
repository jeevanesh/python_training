"""
Bytes data
"""

print("Bytes PART-1")
print("How to store the values")
print("-"*20)
# -------------

a = b'PERSON' # shortcut
# Internally it will create object of predefined/builtin-class 'bytes' and store the values

# Or we can use class name
b = bytes(b'PERSON')

print(a, b)

print("#"*40, end="\n\n")
#########################


print("Bytes PART-2")
print("Access each value by index number")
print("-"*20)
# -------------

a = b"WEL COME"
print("a:", a, end="\n\n")

print("2nd character using +ve index no:", a[0])
print("2nd character using -ve index no:", a[-8])
print("Conver ascii 87 to character", chr(87))

print("#"*40, end="\n\n")
#########################

print("Bytes PART-3")
print("Slicing")
print("-"*20)
# -------------

a = b"WEL COME"
print("a:", a, end="\n\n")

print("from index-1 to 6:", a[1:6])

print("#"*40, end="\n\n")
#########################

print("Bytes PART-4")
print("Methods inside bytes class")
print("-"*20)
# -------------

print(dir(a))

# OR
# print(dir(bytes))

print("#"*40, end="\n\n")
#########################


print("Bytes PART-5")
print("'startswith' method")
print("-"*20)
# -------------

a = b"WEL COME"
print("a:", a, end="\n\n")

result = a.startswith(b"WEL")
print(result)

print("#"*40, end="\n\n")
#########################


print("Bytes PART-6")
print("'decode' method")
print("-"*20)
# -------------

a = b"WEL COME"
print("type of a:", type(a), end="\n\n")

a = a.decode() # bytes to string
print("type of a after decode:", type(a), end="\n\n")

a = a.encode() # string to bytes
print("type of a after encode:", type(a), end="\n\n")

print("#"*40, end="\n\n")
#########################