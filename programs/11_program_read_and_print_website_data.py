"""
Read and print website data
https://www.jafsoft.com/searchengines/log_sample.html
"""

print("Read and print website data")
print("-"*20)
# -------------

import urllib.request as u

my_web_file_handle = u.urlopen('https://www.jafsoft.com/searchengines/log_sample.html')
web_content = my_web_file_handle.read()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
#########################

print("type of web_content")
print("-"*20)
# -------------

print(type(web_content))

print("#"*40, end="\n\n")
#########################


print("Methods inside 'bytes' class")
print("-"*20)
# -------------

print(dir(web_content))

print("#"*40, end="\n\n")
#########################


print("type after decode")
print("-"*20)
# -------------

web_content = web_content.decode()
print(type(web_content))

print("#"*40, end="\n\n")
#########################

print(web_content)
print("-"*20)
# -------------

print(web_content)

print("#"*40, end="\n\n")
#########################