"""
About print function
"""

print("About 'sep' : ")
print("-"*20)
# -------------

a = 100
b = 200
c = 300
d = 400

 # Default sep=" " (SPACE),
print(a, b, c, d) # In output, print each value seperated by SPACE
print(a, b, c, d, sep=",") # In output, print each value seperated by COMMA
print(a, b, c, d, sep="|") # In output, print each value seperated by |
print(a, b, c, d, sep="XYZ") # In output, print each value seperated by XYZ
print(a, b, c, d, sep="\n") # In output, print each value seperated by \n

print("#"*40, end="\n\n")
#########################

print("About 'end' : ")
print("-"*20)
# -------------

a = 100
b = 200
c = 300
d = 400

 # Default end="\n",
print(a, b, c, d) # In output, after printing all the values put '\n' at the end
print(a, b, c, d, end=".") # In output, after printing all the values put '.' at the end
print(a, b, c, d, end="XYZ\n") # In output, after printing all the values put '.' at the end

# Total 4 arguments we can pass to print function
# 1) sep 2) end 3) file 4) flush
# We will discuss 3) file 4) flush during file operations discussion

print("#"*40, end="\n\n")
#########################

