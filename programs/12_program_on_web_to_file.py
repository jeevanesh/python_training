"""
Web to files
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
print(soup)

print("#"*40, end="\n\n")
#########################


print("Get log data using Beautifulsoup")
print("-"*20)
# -------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
#########################


print("log data in raw format")
print("-"*20)
# -------------

log_data = soup.body.pre.text
print(repr(log_data))

print("#"*40, end="\n\n")
#########################

print("list of lines")
print("-"*20)
# -------------

list_of_lines = log_data.split("\n")
print(list_of_lines)

print("#"*40, end="\n\n")
#########################

print("Extract Info")
print("-"*20)
# -------------

extracted_info = []
for each_line in list_of_lines:
    if each_line.startswith("123"):
        sp = each_line.split()
        #print("Splitted Values:", sp)

        ip = sp[0]

        raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
        start_index = 1
        end_index = raw_date.index(":")
        dt = raw_date[start_index:end_index]

        raw_img = sp[6]  # '/pics/wpaper.gif'
        # if raw_img.endswith(".jpg") or raw_img.endswith(".png")
        # OR
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"

        raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]
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
my_txt_file_handle = open("bsoup_report.txt", "w")
my_csv_file_handle = open("bsoup_report.csv", "w")

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
bsoup_report.txt
bsoup_report.csv
""")

print("#"*40, end="\n\n")
#########################