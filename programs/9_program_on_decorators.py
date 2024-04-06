print("IP Function WITHOUT DECORATOR")
print("-"*20)
# -------------
def ip_function(*, log_file_path):
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
            ip = sp[0]
            extracted_info.append(ip)
    return extracted_info
    ################

print("#"*40, end="\n\n")
#########################

print("Decorator to make use of reading log file content")
print("-"*20)
# -------------

def log_process_decorator(my_func): # my_func = ip_function
    def decorated_func(*, log_file_path):
        my_log_file_handle = open(log_file_path, "r")
        log_file_content_in_list = my_log_file_handle.readlines()
        my_log_file_handle.close()
        received_value = my_func(file_content=log_file_content_in_list)
        return received_value
    return decorated_func

print("#"*40, end="\n\n")
#########################

print("IP Function USING DECORATOR: MANUALLY")
print("-"*20)
# -------------
def ip_function(*, file_content):

    # Extract info and return
    # -------------
    extracted_info = []
    for each_line in file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            ip = sp[0]
            extracted_info.append(ip)
    return extracted_info
    ################

inner_function = log_process_decorator(ip_function)
# inner_function = decorated_func
return_value = inner_function(log_file_path=r"../log/server_log.txt")
print(return_value)

print("#"*40, end="\n\n")
#########################


print("IP Function USING DECORATOR: @log_process_decorator")
print("-"*20)
# -------------

@log_process_decorator
def ip_function(*, file_content):

    # Extract info and return
    # -------------
    extracted_info = []
    for each_line in file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            ip = sp[0]
            extracted_info.append(ip)
    return extracted_info
    ################


return_value = ip_function(log_file_path=r"../log/server_log.txt")
print(return_value)

# inner_function = log_process_decorator(ip_function)
# return_value = inner_function(log_file_path=r"../log/server_log.txt")
# print(return_value)

print("#"*40, end="\n\n")
#########################