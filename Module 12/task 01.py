import json
import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

data = response.json()

print("\nHere’s your random Chuck Norris joke:\n")
print(data["value"])