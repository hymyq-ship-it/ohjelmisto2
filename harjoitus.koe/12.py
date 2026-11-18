import requests
import json
vastaus= requests.get("https://jsonplaceholder.typicode.com/users/1")
data= vastaus.json()
print(data["name"])
