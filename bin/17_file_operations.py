"""
File Operations:
Read/Write with text files like .txt, .csv, .log etc

We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect

We have functions for each step
Step-1: Connect to file
    - open() function
Step-2: Read/Write
    - For Write: 1) write 2) writelines 3) print function
    - For Read: 1) read 2) readline 3) for-loop to read line by line
            3) readlines 4) list/tuple/set/dictionary classes to read file
Step-3: Disconnect
    - flush(): Write data in buffer to file
    - close(): 1st close() will call flush() then it will close

"""
print("All write operations")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
# my_file_handle = open("provide file name or file path", "provide mode")
my_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only
# mode 'w': It will create new file
# mode 'w': IMPORTANT: It erases file content if present

# Step-2: Write
# -------------

# Our data
x = 10
y = "python\n"

# Convert other type of data to string because 'write' & 'writelines' expects string
x = str(x) + "\n"
# y -> is already a string

# 1) write: If we have data in one-string which are planning to write then
#   we can make use of 'write' because write takes one string only
my_file_handle.write(x) # Send data to buffer
my_file_handle.write(y) # Send data to buffer
my_file_handle.flush() # Write data in buffer to file

# 2) writelines: It will take any collection of values
my_data_in_list = [x, y]
my_file_handle.writelines(my_data_in_list)
my_file_handle.flush()

# 3) print function
# - no need to convert other type of data to string, print will take care
# - no need to add \n also to each value, in print we can specify in seperator
# so remove \n
x = x.strip() # remove extra spaces, \t\t etc
y = y.strip()
print(x, y, 20, "Java", sep="\n", end="", file=my_file_handle, flush=True)
# no need to convert 20 to string
# my_file_handle.flush() # Not required

# Step-3: Disconnect
# -------------
my_file_handle.close()

print("""
All write operations are completed,
please check 'my_out_file.txt'
""")

print("#"*40, end="\n\n")
#########################

print("Reading: 1) read")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_file_handle = open("my_out_file.txt", "r")
# Mode "r": Read only
# Mode "r": It will not create new file if file not present

# Step-2: Read
# -------------
file_content = my_file_handle.read() # returns complete file content in one string
print("file_content:", file_content, end="\n\n")
print("file_content in raw format:", repr(file_content), end="\n\n")

# Step-3: Disconnect
# -------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Reading: 2) readline")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_file_handle = open("my_out_file.txt", "r")
# Mode "r": Read only
# Mode "r": It will not create new file if file not present

# Step-2: Read
# -------------
file_content = my_file_handle.readline()
print("1st Line:", file_content)

file_content = my_file_handle.readline()
print("2nd Line:", file_content)

file_content = my_file_handle.readline()
print("3rd Line:", file_content)

# seek pointer: Internally file operations will make use of this pointer
# - if we open file in 'w' or 'r' then seek pointer will be pointing
#   at the BEGINNING of the file
# - if we open file in 'a' then seek pointer will be pointing
#   at the END of the file
# - We can set seek pointer to any character of the file
#   0-> 0th character which is beginning of the file

# Set seek to beginning
my_file_handle.seek(0)
file_content = my_file_handle.readline()
print("1st Line:", file_content)

# Step-3: Disconnect
# -------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Reading: 3) for-loop to read line by line")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_file_handle = open("my_out_file.txt", "r")
# Mode "r": Read only
# Mode "r": It will not create new file if file not present

# Step-2: Read
# -------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# -------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Reading: 4) readlines, list, tuple, set, dictionary")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_file_handle = open("my_out_file.txt", "r")
# Mode "r": Read only
# Mode "r": It will not create new file if file not present

# Step-2: Read
# -------------
file_content = my_file_handle.readlines() # returns in list
print("file_content using readlines():", file_content)
# seek reached EOF

# Seek already at the END, nothing to from seek pointer
file_content = my_file_handle.readlines() # returns in list
print("file_content is EMPTY because seek already at EOF:", file_content)
# seek reached EOF

# set seek to beginning
my_file_handle.seek(0)
file_content = list(my_file_handle)
print("file_content in list:", file_content)
# seek reached EOF

# set seek to beginning
my_file_handle.seek(0)
file_content = tuple(my_file_handle)
print("file_content in tuple:", file_content)
# seek reached EOF

# set seek to beginning
my_file_handle.seek(0)
file_content = set(my_file_handle)
print("file_content in set:", file_content)
# seek reached EOF

# set seek to beginning
my_file_handle.seek(0)
file_content = dict(enumerate(my_file_handle))
# enumerate will make index,value pair like [(0, line1data),(1, line2data),(2, line3data)]
print("file_content in dict:", file_content)
# seek reached EOF

# Step-3: Disconnect
# -------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################

# Different Modes
# -------------
# mode 'w': Write only, It will create new file, important is it will erase the data
# mode 'r': Read only, It will NOT create new file
# mode 'a': Append only, It will create new file only if file not present

# mode 'w+': RW, It will create new file, important is it will erase the data
# mode 'r+': RW, It will NOT create new file
# mode 'a+': RW, It will create new file only if file not present
#########################