"""
Get data from server_log.txt
then
extract info
then
write extracted info to log_report.txt and log_report.csv
"""

print("Get data from server_log.txt")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_log_file_handle = open(r"../log/server_log.txt", "r")

# Step-2: Read
# -------------
log_file_content_in_list = my_log_file_handle.readlines()
print(log_file_content_in_list)

# Step-3: Disconnect
# -------------
my_log_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Extract Info")
print("-"*20)
# -------------

extracted_info = []
for each_line in log_file_content_in_list:
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
my_txt_file_handle = open("log_report.txt", "w")
my_csv_file_handle = open("log_report.csv", "w")

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
log_report.txt
log_report.csv
""")

print("#"*40, end="\n\n")
#########################