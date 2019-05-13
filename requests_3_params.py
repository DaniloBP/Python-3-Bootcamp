import requests

url = "https://icanhazdadjoke.com/search"

# response = requests.get(url)
# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(
						url, 
						headers = {"Accept" : "application/json"},
						params = {"term" : "cat", "limit" : 5}
						)

data = response.json()
# print(data["results"])

for joke in data["results"]:
	print(f"JOKE -->  {joke['joke']}")