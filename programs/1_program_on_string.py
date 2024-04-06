"""
From the string below, extract
IP
DATE
PICS
URL

Expected Output:
-------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
-------------
"""

print("How input data looks like?")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
#########################


print("type of input data")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#"*40, end="\n\n")
#########################


print("input data in raw format")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(repr(input_data))

print("#"*40, end="\n\n")
#########################

print("Extract IP: 1-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
#########################


print("Extract IP: 2-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_1st_space = input_data.index(" ")
ip = input_data[0:index_of_1st_space]
print(ip)

print("#"*40, end="\n\n")
#########################

print("Extract IP: 3-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("splitted Values:", sp, end="\n\n")

ip = sp[0]
print("ip:", ip)

print("#"*40, end="\n\n")
#########################

print("Extract DATE: 1-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = input_data.index('[')
start_index = start_index + 1

end_index = input_data.index(":")

dt = input_data[start_index:end_index]
print(dt)

print("#"*40, end="\n\n")
#########################

print("Extract DATE: 2-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("splitted Values:", sp, end="\n\n")

raw_date = sp[3] # '[26/Apr/2000:00:23:48'

start_index = 1
end_index = raw_date.index(":")

dt = raw_date[start_index:end_index]
print(dt)

print("#"*40, end="\n\n")
#########################

print("Extract PICS: 1-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = input_data.index('/pics/') # Returns index of 1st slash
start_index = start_index + 6

# 1-way
end_index = input_data.index("HTTP") # Returns index of H
end_index = end_index - 1

# 2-way
end_index = input_data.index(" ", start_index)

img = input_data[start_index:end_index]
print(img)

print("#"*40, end="\n\n")
#########################

print("Extract PICS: 2-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("splitted Values:", sp, end="\n\n")

raw_img = sp[6] # '/pics/wpaper.gif'

# 1-way: remove '/pics/' from '/pics/wpaper.gif'
img_1 = raw_img[6:]

# 2-way: remove '/pics/' from '/pics/wpaper.gif'
raw_img_sp = raw_img.split("/")
print("raw_img_sp:", raw_img_sp) # ['', 'pics', 'wpaper.gif']
img_2 = raw_img_sp[2] # Using +ve index
img_3 = raw_img_sp[-1] # Using -ve index

# 3-way: remove '/pics/' from '/pics/wpaper.gif'
img_4 = raw_img.lstrip("/pics/")

print(img_1, img_2, img_3, img_4, sep="\n")

print("#"*40, end="\n\n")
#########################

print("Extract URL: 1-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = input_data.index("http://")
end_index = input_data.index('"', start_index)

url = input_data[start_index : end_index]
print(url)

print("#"*40, end="\n\n")
#########################

print("Extract URL: 2-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("splitted Values:", sp, end="\n\n")

raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'

# 1-way: Remove " from '"http://www.jafsoft.com/asctortf/"'
url_1 = raw_url.strip('"')

# 2-way: Remove " from '"http://www.jafsoft.com/asctortf/"'
url_2 = raw_url[1:-1]

# 3-way: Remove " from '"http://www.jafsoft.com/asctortf/"'
raw_url_sp = raw_url.split('"')
print("raw_url_sp:", raw_url_sp) # ['', 'http://www.jafsoft.com/asctortf/', '']
url_3 = raw_url_sp[1]

print(url_1, url_2, url_3, sep="\n")

print("#"*40, end="\n\n")
#########################