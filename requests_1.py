import requests

url = "https://www.google.com/sdaddsds"
resp = requests.get(url)

print(f"Your request to {url} came back w/ status code {resp.status_code}")