"""
Write 4th program using functions

1. write function which should take log_file_path as an argument
and return extracted info in list of tuples
    :return extracted info in list of tuples

2. write function which should take txt_file_path as an argument
and it should write to txt file
    :return None

3. write function which should take csv_file_path as an argument
and it should write to csv file
    :return None
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


print("write to txt file function")
print("-"*20)
# -------------
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

print("#"*40, end="\n\n")
#########################


print("write to csv file function")
print("-"*20)
# -------------
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

print("#"*40, end="\n\n")
#########################

print("Value of __name__:", __name__)

if __name__ == "__main__":
    extracted_data = log_file_process_function(log_file_path=r"../log/server_log.txt")
    write_to_txt_file_function(data=extracted_data, txt_out_file_path="func_report.txt")
    write_to_csv_file_function(data=extracted_data, csv_out_file_path="func_report.csv")
    print("""
    Created Below files, please check
    func_report.txt
    func_report.csv
    """)

# COMMENTs on __name__
# 1. __name__ is builtin variable
# 2. If we execute current program then value of __name__ is __main__
# 3. If we import this '5_program_on_function' in another program
#    then automatically __name__ value will be file name i.e '5_program_on_function'
# 4. What is the use of it?
#   suppose '5_program_on_function' program we are using for our project/task
#   also we are planning to make-use/import this '5_program_on_function' functions
#   in another program as well then we can make __name__ block to put
#   this project specific code
# 5. How it works?
#   - If we run this program alone then __name__ value is __main__
#       so this __name__ block will execute
#   - If we import in another program then __name__ value '5_program_on_function'
#       so if condition fails, so it will not go inside 'if' block