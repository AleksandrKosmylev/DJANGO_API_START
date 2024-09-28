from operator import ge
import requests

endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"

#get_response = requests.get(endpoint)  #HTTP Request
get_response = requests.get(endpoint, json = {"query" : "Hello world"})
# get_response = requests.get(endpoint, data = {"query" : "Hello world"})

### python py_client/basic.py

# print(get_response.text)
#print(get_response.json())
print(get_response.status_code)