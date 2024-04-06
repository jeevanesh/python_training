"""
Write class for log processing task
include below methods
1) get_only_ips
2) get_only_dates
3) get_only_pics
4) get_only_urls
5) get_all
6) write_to_txt
7) write_to_csv
"""

print("Log Process Class")
print("-"*20)
# -------------

class LogProcessClass:
    def __init__(self, log_file_path):
        my_file_handle = open(log_file_path, "r")
        self.log_file_content = my_file_handle.readlines()
        my_file_handle.close()

    def get_only_ips(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                ip = sp[0]
                extracted_info.append(ip)
        return extracted_info

    def get_only_dates(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
                start_index = 1
                end_index = raw_date.index(":")
                dt = raw_date[start_index:end_index]
                extracted_info.append(dt)
        return extracted_info

    def get_only_pics(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                raw_img = sp[6]  # '/pics/wpaper.gif'
                if raw_img.startswith("/pics/"):
                    img = raw_img[6:]
                else:
                    img = "No Image"
                extracted_info.append(img)
        return extracted_info

    def get_only_urls(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
                url = raw_url[1:-1]
                extracted_info.append(url)
        return extracted_info

    def get_all(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                # print("Splitted Values:", sp)

                ip = sp[0]

                raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
                start_index = 1
                end_index = raw_date.index(":")
                dt = raw_date[start_index:end_index]

                raw_img = sp[6]  # '/pics/wpaper.gif'
                if raw_img.startswith("/pics/"):
                    img = raw_img[6:]
                else:
                    img = "No Image"

                raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
                url = raw_url[1:-1]
                each_line_tuple = (ip, dt, img, url)
                extracted_info.append(each_line_tuple)
        return extracted_info

    def write_to_txt(self, out_file_path):
        my_file_handle = open(out_file_path, "w")
        print("IP", "DATE", "PICS", "URL", sep="\t", file=my_file_handle)
        extracted_data = self.get_all()
        for i, j, k, l in extracted_data:
            print(i, j, k, l, sep="\t", file=my_file_handle)
        my_file_handle.close()

    def write_to_csv(self, out_file_path):
        my_file_handle = open(out_file_path, "w")
        print("IP", "DATE", "PICS", "URL", sep=",", file=my_file_handle)
        extracted_data = self.get_all()
        for i, j, k, l in extracted_data:
            print(i, j, k, l, sep=",", file=my_file_handle)
        my_file_handle.close()


log_file_1_object = LogProcessClass(r"../log/server_log.txt")
print("IPs:", log_file_1_object.get_only_ips())
print("DATEs:", log_file_1_object.get_only_dates())
print("PICS:", log_file_1_object.get_only_pics())
print("URLs:", log_file_1_object.get_only_urls())
print("All:", log_file_1_object.get_all())
log_file_1_object.write_to_txt("class_report.txt")
log_file_1_object.write_to_csv("class_report.csv")

print("""
Created
class_report.txt
class_report.csv
Please check
""")

print("#"*40, end="\n\n")
#########################