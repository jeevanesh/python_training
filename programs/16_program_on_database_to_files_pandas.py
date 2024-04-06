"""
Get data from db and write to files
"""

print("Get data from database")
print("-"*20)
# -------------

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Done\n\n")

print("Create cursor")
my_db_cursor = my_db_connection.cursor()
print("Done\n\n")

print("select query")
my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
print("Done\n\n")

print("Get all records")
my_db_result = my_db_cursor.fetchall()
print("Done\n\n")

print(my_db_result)

print("#"*40, end="\n\n")
#########################


print("Create DataFrame class object with my_db_result data")
print("-"*20)
# -------------

import pandas as pd

my_db_df = pd.DataFrame(my_db_result, columns=["IP", "DATE", "PICS", "URL"])
print(my_db_df)

print("#"*40, end="\n\n")
#########################

print("Using pandas.read_sql, Get data from database")
print("-"*20)
# -------------

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Done\n\n")

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)
print(my_db_df)

print("#"*40, end="\n\n")
#########################

print("Write to files")
print("-"*20)
# -------------

my_db_df.to_csv("db_dump_1.txt", sep="\t") # We can use to_csv for txt
my_db_df.to_csv("db_dump_2.csv") # default sep=","
my_db_df.to_excel("db_dump_3.xlsx", sheet_name="my_db_data")
my_db_df.to_json("db_dump_4.json")
my_db_df.to_xml("db_dump_5.xml")
my_db_df.to_html("db_dump_6.html")

rotated_df = my_db_df.T
rotated_df.to_json("db_dump_7.json")

print("""
Below files are created please check
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
db_dump_6.html
db_dump_7.json
""")

print("#"*40, end="\n\n")
#########################