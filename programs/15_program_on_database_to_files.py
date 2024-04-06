"""
database to files
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

print("write to files")
print("-"*20)
# -------------

# extracted_info = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]

# Step-1: Connect to file
# -------------
my_txt_file_handle = open("db_report.txt", "w")
my_csv_file_handle = open("db_report.csv", "w")

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

# my_db_result = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]
for i, j, k, l in my_db_result:
    print(i, j, k, l, sep="\t", file=my_txt_file_handle)
    print(i, j, k, l, sep=",", file=my_csv_file_handle)

# Step-3: Disconnect
# -------------
my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Created below files, Pleas check
db_report.txt
db_report.csv
""")

print("#"*40, end="\n\n")
#########################