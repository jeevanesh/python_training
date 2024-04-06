"""
Write 4th program using comprehensions
Write list comprehensions to extract IP, DATE, PICS, URL
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

ips_list = [each_line.split()[0] for each_line in log_file_content_in_list if each_line.startswith("123")]
print("ips_list:", ips_list)

dates_list = [each_line.split()[3][1:each_line.split()[3].index(":")] for each_line in log_file_content_in_list if each_line.startswith("123")]
# raw_date = each_line.split()[3]
# index_of_colon = each_line.split()[3].index(":")
print("dates_list:", dates_list)


img_list = [each_line.split()[6][6:] if each_line.split()[6].startswith("/pics/") else "No Image" for each_line in log_file_content_in_list if each_line.startswith("123")]
# raw_img = sp[6] = each_line.split()[6]
# img = raw_img[6:] = each_line.split()[6][6:]
print("img_list:", img_list)

urls_list = [each_line.split()[10][1:-1] for each_line in log_file_content_in_list if each_line.startswith("123")]
# raw_url = sp[10] = each_line.split()[10]
# url = raw_url[1:-1] = each_line.split()[10][1:-1]
print("urls_list:", urls_list)

print("#"*40, end="\n\n")
#########################

print("write to files")
print("-"*20)
# -------------
# Example-1:
#
#  >>> L = [100, 200]
# >>> M = ["A", "B"]
# >>> z = zip(L,M)
# >>> list(z)
# [(100, 'A'), (200, 'B')]
#
# Example-2
#
# z = zip(ips_list, dates_list, img_list, urls_list)
# z = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]
#
# Step-1: Connect to file
# -------------
my_txt_file_handle = open("comprehension_report.txt", "w")
my_csv_file_handle = open("comprehension_report.csv", "w")

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

# zip(ips_list, dates_list, img_list, urls_list) = [(ip, dt, img, url),(ip, dt, img, url),(ip, dt, img, url),]
for i, j, k, l in zip(ips_list, dates_list, img_list, urls_list):
    print(i, j, k, l, sep="\t", file=my_txt_file_handle)
    print(i, j, k, l, sep=",", file=my_csv_file_handle)

# Step-3: Disconnect
# -------------
my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Created below files, Pleas check
comprehension_report.txt
comprehension_report.csv
""")

print("#"*40, end="\n\n")
#########################