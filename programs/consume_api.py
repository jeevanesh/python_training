"""
Access API using 'requests' library

Also

we can access API using API client like POSTMAN
"""

print("GET: request")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/getdbdata'

try:
    api_response = requests.get(api_end_point)
    api_data = api_response.json()
    print("api_data:", api_data)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("POST: request")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/postdbdata'

try:
    api_response = requests.post(api_end_point, json={
 "IP": "123.123.123.126",
  "DATE": "26/Apr/2000",
   "PICS" : "wpaper.gif",
    "URL" : "http://www.jafsoft.com/asctortf/"

})
    api_data = api_response.json()
    print("api_data:", api_data)
    print("status code:", api_response.status_code)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("GET: request after POST")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/getdbdata'

try:
    api_response = requests.get(api_end_point)
    api_data = api_response.json()
    print("api_data:", api_data)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("PUT: request")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/putdbdata'

try:
    api_response = requests.put(api_end_point, json={
 "IP": "123.123.123.126",
  "DATE": "05/Apr/2024",
   "PICS" : "xyz.jpg",
    "URL" : "http://www.jafsoft.com/asctortf/"

})
    api_data = api_response.json()
    print("api_data:", api_data)
    print("status code:", api_response.status_code)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("GET: request after PUT")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/getdbdata'

try:
    api_response = requests.get(api_end_point)
    api_data = api_response.json()
    print("api_data:", api_data)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("PATCH: request")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/patchdbdata'

try:
    api_response = requests.patch(api_end_point, json={
 "IP": "123.123.123.126",
  "DATE": "20/Jan/2024",

})
    api_data = api_response.json()
    print("api_data:", api_data)
    print("status code:", api_response.status_code)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("GET: request after PATCH")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/getdbdata'

try:
    api_response = requests.get(api_end_point)
    api_data = api_response.json()
    print("api_data:", api_data)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("DELETE: request")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/deletedbdata'

try:
    api_response = requests.delete(api_end_point, json={
 "IP": "123.123.123.126"
})
    api_data = api_response.json()
    print("api_data:", api_data)
    print("status code:", api_response.status_code)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################

print("GET: request after DELETE")
print("-"*20)
# -------------
import requests

api_end_point = 'http://127.0.0.1:5000/getdbdata'

try:
    api_response = requests.get(api_end_point)
    api_data = api_response.json()
    print("api_data:", api_data)
except Exception as e:
    print("Not able to access, Reason:\n", e)
    print("Not able to access, Please check whether api program is running")
    exit()

print("#"*40, end="\n\n")
#########################