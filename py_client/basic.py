import requests, json

# endpoint = "https://httpbin.org/anything"
endpoint = " http://localhost:8000/api/"


res = requests.get(endpoint, params = {"key":"1234"} ,json={"message":"Sending data to API ENdpoint"})

print(type(res.text))
print(res.json())
