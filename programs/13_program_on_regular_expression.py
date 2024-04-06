"""
Write 12th Program using regular expression to
extract info
"""
import re

print("Get website data")
print("-"*20)
# -------------

import urllib.request as u

my_web_file_handle = u.urlopen('https://www.jafsoft.com/searchengines/log_sample.html')
web_content = my_web_file_handle.read()
my_web_file_handle.close()
web_content = web_content.decode()
print(web_content)

print("#"*40, end="\n\n")
#########################

print("Create Beautifulsoup class object")
print("-"*20)
# -------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
log_data = soup.body.pre.text
list_of_lines = log_data.split("\n")
print(list_of_lines)


print("#"*40, end="\n\n")
#########################

print("Regular Expression: Check whether it is IP address line or not?")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT
r'''
In Regular Expression
IDENTIFIERS
------------
\d -> any ONE digit b/n 0 to 9 OR [0-9]
\D -> any ONE non-digit, except 0 to 9 or [^0-9] here ^ indicates excluding 0 to 9
. -> any ONE any character
\. -> strictly DOT
[0-9] -> any ONE digit b/n 0 to 9, here we can specify different range
[0-255] -> it can be b/n 0 to 2 OR 5. ANY ONE digit
[a-z0-9] -> it can any ONE lowercase letter OR any one digit
[a9x0] -> any ONE character in this group of characters 
        i.e it can be 'a' OR it can be '9' OR it can be 'x' OR it can be '0'
------------

QUANTIFIERS
-----------
\d{3} -> it makes \d\d\d
\d{1,3} -> it makes (\d|\d\d|\d\d\d)
-----------

MODIFIERS
-----------
* -> 0 or more times
+ -> 1 or more times
? -> 0 or one time
-----------

^ -> startswith something
$ -> endswith

'''

print("#"*40, end="\n\n")
#########################

print("Extract IP")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)


# COMMENT
# r -> raw string
r"""
put () to IP address pattern to capture IP
- this is called group
"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)


# COMMENT
# r -> raw string
r"""

26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits

\d{1,2} # Minimum 1 digit and maximum 2 digits
\d?\d # Minimum 1 digit and maximum 2 digits
[0-9]{1,2} # Minimum 1 digit and maximum 2 digits
[0-9]?[0-9] # Minimum 1 digit and maximum 2 digits
\d?[0-9] # Minimum 1 digit and maximum 2 digits
[0-9]?\d # Minimum 1 digit and maximum 2 digits
---

Apr
---
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
---
"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE, PICS: PARTIAL OUTPUT-1")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(\w+\.(jpg|gif)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)


# COMMENT
# r -> raw string
r"""

\w -> word character ie any one character in this group [a-zA-Z0-9_]
\W -> non-word character ie any one character EXCLUDING group of chars [^a-zA-Z0-9_]


"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE, PICS: PARTIAL OUTPUT-2")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(jpg|gif)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)


# COMMENT
# r -> raw string
r"""

MODIFIERS
-----------
GREEDY
* -> 0 or more times
+ -> 1 or more times
? -> 0 or one time

NON-GREEDY
*? -> 0 or more times
+? -> 1 or more times
?? -> 0 or one time

-----------

"""

print("#"*40, end="\n\n")
#########################


print("Extract IP, DATE, PICS: PARTIAL OUTPUT-3")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(jpg|gif))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)


# COMMENT
# r -> raw string
r"""
(\w+\.(jpg|gif))? 
OPTIONAL so that it will match the line which is not having PICS
"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE, PICS")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT)\s+/(pics/(\w+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img)


# COMMENT
# r -> raw string
r"""

Here we provided more information to pattern and made
(pics/\w+\.(gif|jpg))? OPTIONAL so that line which is not having image
name will be considered

\s -> ONE space
\S -> ONE non-space character. Except space any character
\s+ -> ONE or MORE space
"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE, PICS, URL")
print("-"*20)
# -------------

for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT)\s+/(pics/(\w+\.(gif|jpg)))?.*(http[s]?://[a-z./A-Z_0-9]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url)


# COMMENT
# r -> raw string
r"""

http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-z./A-Z_0-9]+

http[s]? -> s is optional
https? -> s is optional
(https)? -> https is optional
[https]? -> any ONE character in this group, that too OPTIONAL
"""

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE, PICS, URL: Store in variable")
print("-"*20)
# -------------

extracted_info = []
for each_line in list_of_lines:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT)\s+/(pics/(\w+\.(gif|jpg)))?.*(http[s]?://[a-z./A-Z_0-9]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        each_line_tuple = (ip, dt, img, url)
        extracted_info.append(each_line_tuple)

print(extracted_info)
print("#"*40, end="\n\n")
#########################


print("write to files")
print("-"*20)
# -------------

# extracted_info = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]

# Step-1: Connect to file
# -------------
my_txt_file_handle = open("regex_report.txt", "w")
my_csv_file_handle = open("regex_report.csv", "w")

# Step-2: Write
# -------------
# Write Header to txt file
# my_txt_file_handle.write("IP\tDATE\tPICS\tURL\n")
# my_txt_file_handle.writelines(["IP\t", "DATE\t", "PICS\t", "URL\n"])
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)

# Write Header to csv file
# my_csv_file_handle.write("IP,DATE,PICS,URL\n")
# my_csv_file_handle.writelines(["IP,", "DATE,", "PICS,", "URL\n"])
print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file_handle)

# extracted_info = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]
for i, j, k, l in extracted_info:
    print(i, j, k, l, sep="\t", file=my_txt_file_handle)
    print(i, j, k, l, sep=",", file=my_csv_file_handle)

# Step-3: Disconnect
# -------------
my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Created below files, Pleas check
regex_report.txt
regex_report.csv
""")

print("#"*40, end="\n\n")
#########################
