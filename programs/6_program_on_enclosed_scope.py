"""
Rewrite 5th program to print total reports generated
So
total_reports = total_txt_file_reports + total_csv_file_reports
"""

print("log file process function")
print("-"*20)
# -------------
def log_file_process_function(*, log_file_path):
    """
    function which should take log_file_path as an argument
    and return extracted info in list of tuples
    :param log_file_path:
    :return extracted_info
    """
    # Read log file
    # -------------
    my_log_file_handle = open(log_file_path, "r")
    log_file_content_in_list = my_log_file_handle.readlines()
    my_log_file_handle.close()
    ################

    # Extract info and return
    # -------------
    extracted_info = []
    for each_line in log_file_content_in_list:
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
    ################

print("#"*40, end="\n\n")
#########################


print("1-WAY: Total reports generated using GLOBAL SCOPE ")
print("-"*20)
# -------------

total_reports_created = 0

def write_to_txt_file_function(*, data, txt_out_file_path):
    """
    write function which should take txt_file_path as an argument
    and it should write to txt file
    :param txt_out_file_path:
    :return None:
    """
    my_txt_file_handle = open(txt_out_file_path, "w")
    print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)
    for i, j, k, l in data:
        print(i, j, k, l, sep="\t", file=my_txt_file_handle)
    my_txt_file_handle.close()
    global total_reports_created
    total_reports_created = total_reports_created + 1


def write_to_csv_file_function(*, data, csv_out_file_path):
    """
    write function which should take csv_file_path as an argument
    and it should write to csv file
    :param data:
    :param csv_out_file_path:
    :return None:
    """
    my_csv_file_handle = open(csv_out_file_path, "w")
    print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file_handle)
    for i, j, k, l in data:
        print(i, j, k, l, sep=",", file=my_csv_file_handle)
    my_csv_file_handle.close()
    global total_reports_created
    total_reports_created = total_reports_created + 1

# Call the function
extracted_data = log_file_process_function(log_file_path=r"../log/server_log.txt")
write_to_txt_file_function(data=extracted_data, txt_out_file_path="func_report.txt")
write_to_csv_file_function(data=extracted_data, csv_out_file_path="func_report.csv")
write_to_txt_file_function(data=extracted_data, txt_out_file_path="func_report.txt")
write_to_csv_file_function(data=extracted_data, csv_out_file_path="func_report.csv")
print("total_reports_created:", total_reports_created)

print("#"*40, end="\n\n")
#########################


print("2-WAY, BEST WAY: Total reports generated using ENCLOSED SCOPE  ")
print("-"*20)
# -------------

def write_to_file_functions():

    total_reports_created = 0

    def write_to_txt_file_function(*, data, txt_out_file_path):
        """
        write function which should take txt_file_path as an argument
        and it should write to txt file
        :param txt_out_file_path:
        :return None:
        """
        my_txt_file_handle = open(txt_out_file_path, "w")
        print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)
        for i, j, k, l in data:
            print(i, j, k, l, sep="\t", file=my_txt_file_handle)
        my_txt_file_handle.close()
        nonlocal total_reports_created
        total_reports_created = total_reports_created + 1


    def write_to_csv_file_function(*, data, csv_out_file_path):
        """
        write function which should take csv_file_path as an argument
        and it should write to csv file
        :param data:
        :param csv_out_file_path:
        :return None:
        """
        my_csv_file_handle = open(csv_out_file_path, "w")
        print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file_handle)
        for i, j, k, l in data:
            print(i, j, k, l, sep=",", file=my_csv_file_handle)
        my_csv_file_handle.close()
        nonlocal total_reports_created
        total_reports_created = total_reports_created + 1

    def get_total_count():
        return total_reports_created

    return [write_to_txt_file_function, write_to_csv_file_function, get_total_count]

received_value = write_to_file_functions()
# received_value = [write_to_txt_file_function, write_to_csv_file_function, get_total_count]
print("received_value:", received_value, end="\n\n")
txt_func = received_value[0]
csv_func = received_value[1]
get_count_func = received_value[2]

# Call the function
extracted_data = log_file_process_function(log_file_path=r"../log/server_log.txt")
txt_func(data=extracted_data, txt_out_file_path="func_report.txt")
csv_func(data=extracted_data, csv_out_file_path="func_report.csv")
txt_func(data=extracted_data, txt_out_file_path="func_report.txt")
csv_func(data=extracted_data, csv_out_file_path="func_report.csv")
total_count = get_count_func()
print("total_reports_created:", total_count)


print("#"*40, end="\n\n")
#########################