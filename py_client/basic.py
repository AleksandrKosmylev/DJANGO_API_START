# from operator import get
import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json = {"title": "ABC", "content" : "Hello world", "price": "ABC"})
# get_response = requests.get(endpoint, params= {"abc": 123}, json = {"query" : "Hello world"})
# get_response = requests.get(endpoint, data = {"query" : "Hello world"})


# print(get_response.text)
# print(get_response.headers)
print(get_response.json())
# print(get_response.status_code)