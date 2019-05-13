import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url)
# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

# print(type(data))
print(data["joke"])
print(f"Status: {data['status']}")