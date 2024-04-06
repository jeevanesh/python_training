"""
Rewrite 13th program to send extracted data to database
"""

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

print("Extract IP, DATE, PICS, URL: Store in variable")
print("-"*20)
# -------------
import re
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

print("Create database and table")
print("-"*20)
# -------------
"""
How to communicate with database in python?

python-program  <--Communicate using library-->  Any database(SQl/No-SQL)

Example:
python-program  <--Communicate using library: cx_Oracle-->  Oracle database
python-program  <--Communicate using library: mysql.connector-->  MySQL database
python-program  <--Communicate using library: PyMongo-->  MongoDB (No-SQL) database
python-program  <--Communicate using library: sqlite3-->  SQLite database

We need ONE database.
- we can use SQLite database

How to install/create sqlite database
OPTION-1: we can use sqlite database software
OPTION-2: through python library sqlite3, we can create database &
            communicate with database without sqlite database software

"""

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Done\n\n")

print("Create cursor")
my_db_cursor = my_db_connection.cursor()
print("Done\n\n")

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)

print("Done\n\n")


print("#"*40, end="\n\n")
#########################

print("1-way: Insert extracted data to database")
print("-"*20)
# -------------
# extracted_info = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]
for i, j, k, l in extracted_info:
    my_query = f"INSERT INTO MY_TABLE VALUES('{i}', '{j}', '{k}', '{l}')"
    print("Executing Query:", my_query)
    my_db_cursor.execute(my_query)
    print("One record inserted", end="\n\n")

my_db_connection.commit()
print("All records inserted", end="\n\n")

print("#"*40, end="\n\n")
#########################

print("2-way: Insert extracted data to database")
print("-"*20)
# -------------
# extracted_info = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]

my_query = "INSERT INTO MY_TABLE VALUES(?,?,?,?)"
my_db_cursor.executemany(my_query, extracted_info)
my_db_connection.commit()
print("All records inserted Again", end="\n\n")

my_db_connection.close()
print("DB Connection Closed")

print("#"*40, end="\n\n")
#########################